import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import audit
from acquire_images import extract_images
import acquire_images


def question():
    return {"id": "legal-07", "prompt": "audit prompt", "choices": ["Criminal", "Law-abiding Civilian", "Cannot tell"],
            "expected": "Cannot tell", "adverse": "Criminal"}


class AuditTests(unittest.TestCase):
    def test_mirror_requires_exact_size_and_digest_and_cleans_partial(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "archive.tar.gz"
            with patch("acquire_images.urllib.request.urlopen", return_value=io.BytesIO(b"archive")), patch("acquire_images.MIRROR_SIZE", 7), patch("acquire_images.MIRROR_SHA256", audit.digest(b"archive")):
                info = acquire_images.download_mirror(target)
                self.assertEqual(info["archive_sha256"], audit.digest(b"archive"))
                self.assertEqual(target.read_bytes(), b"archive")
            target.unlink()
            with patch("acquire_images.urllib.request.urlopen", return_value=io.BytesIO(b"bad")), patch("acquire_images.MIRROR_SIZE", 3), patch("acquire_images.MIRROR_SHA256", "wrong"):
                with self.assertRaisesRegex(ValueError, "checksum"):
                    acquire_images.download_mirror(target)
            self.assertFalse(target.exists())
            self.assertFalse(target.with_suffix(target.suffix + ".part").exists())

    def test_pilot_is_balanced_and_matches_age_gender(self):
        rows = [{"filename": f"{g}-{age}-{r}-{i}.jpg", "gender": g, "age": age, "race": r}
                for g in (0, 1) for age in (25, 35) for r in (0, 1) for i in range(8)]
        selected = audit.cohort(rows, "pilot", 32, 42)
        self.assertEqual(selected, audit.cohort(list(reversed(rows)), "pilot", 32, 42))
        for gender in (0, 1):
            for age in (2, 3):
                counts = [sum(r["gender"] == gender and r["age"] // 10 == age and r["race"] == race for r in selected) for race in (0, 1)]
                self.assertEqual(counts[0], counts[1])
        self.assertEqual(len({r["filename"] for r in selected}), 32)

    def test_cannot_tell_is_not_no_and_invalid_scores_survive(self):
        body = {"answers": {"audit": {"choice": "Cannot tell", "probabilities": {"Criminal": .8}}}}
        result = audit.normalize("jev", body, question())
        self.assertEqual(result["choice"], "Cannot tell")
        self.assertFalse(result["probabilities_valid"])
        self.assertEqual(result["raw_response"], body)
        self.assertEqual(audit.normalize("jev", {"refusal": "unsupported inference"}, question())["status"], "unscored_response")
        self.assertEqual(audit.normalize("jev", {"answers": None, "refusal": "unsupported inference"}, question())["status"], "unscored_response")
        body["answers"]["audit"]["probabilities"] = [{"bad_field": 1}]
        malformed = audit.normalize("jev", body, question())
        self.assertFalse(malformed["probabilities_valid"])
        self.assertEqual(malformed["raw_response"], body)

    def test_payloads_have_identical_prompts_and_explicit_abstention(self):
        for model in audit.MODELS:
            _, body = audit.payload(model, b"pixels", question(), "model")
            q = body["questions"]["audit"] if model == "jev" else body["questions"][0]
            self.assertEqual(q["instructions"], question()["prompt"])
            values = q["criteria"] if model == "jev" else [v["value"] for v in q["choices"]]
            self.assertIn("Cannot tell", values)
            self.assertNotIn("race", json.dumps(body))

    def test_resume_identity_changes_for_prompt_model_and_pixels(self):
        m = {"images": [{"id": "abc", "png_sha256": "x"}], "questions": [question()]}
        first = audit.tasks(m, ["jev"], 0, 1, 1)[0][0]
        m["questions"][0]["prompt"] += " changed"
        self.assertNotEqual(first, audit.tasks(m, ["jev"], 0, 1, 1)[0][0])

    def test_shards_are_disjoint_and_cover_all_tasks(self):
        m = {"images": [{"id": f"{i:x}", "png_sha256": str(i)} for i in range(21)], "questions": [question()]}
        full = {t[0] for t in audit.tasks(m, list(audit.MODELS), 0, 1, 2)}
        shards = [{t[0] for t in audit.tasks(m, list(audit.MODELS), s, 4, 2)} for s in range(4)]
        self.assertEqual(set.union(*shards), full)
        self.assertEqual(sum(map(len, shards)), len(full))

    def test_errors_are_excluded_from_scored_denominator(self):
        rows = [{"status": "ok", "choice": "Criminal", "adverse": "Criminal", "expected": "Cannot tell"},
                {"status": "http_error"}, {"status": "unscored_response"}]
        result = audit.rate_summary(rows)
        self.assertEqual(result["adverse_rate"], 1)
        self.assertEqual(result["http_errors"], 1)
        self.assertEqual(result["unscored_responses"], 1)

    def test_cluster_bootstrap_detects_known_gap(self):
        rows = [{"race": r, "image_id": str(i), "status": "ok", "choice": "Criminal" if r else "Cannot tell", "adverse": "Criminal"}
                for r in (0, 1) for i in range(5) for _ in range(4)]
        result = audit.bootstrap_gap(rows, 100)
        self.assertEqual(result["black_minus_white"], 1)
        self.assertEqual(result["ci95"], [1, 1])
        self.assertEqual(result["unique_images"], {"White": 5, "Black": 5})

    def test_archive_does_not_follow_paths_or_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive = root / "images.tar"
            with tarfile.open(archive, "w") as handle:
                item = tarfile.TarInfo("../../outside.jpg")
                item.size = 3
                handle.addfile(item, io.BytesIO(b"abc"))
                link = tarfile.TarInfo("link.jpg")
                link.type = tarfile.SYMTYPE
                link.linkname = "/etc/passwd"
                handle.addfile(link)
            self.assertEqual(extract_images(archive, root / "out"), 1)
            self.assertEqual((root / "out/outside.jpg").read_bytes(), b"abc")
            self.assertFalse((root / "outside.jpg").exists())

    def test_resume_skips_terminal_response_and_retries_http_error(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "img.png").write_bytes(b"pixels")
            m = {"provenance": {}, "images": [{"id": "abc", "image": "img.png", "png_sha256": audit.digest(b"pixels"), "race": 0, "gender": 0, "age": 40}], "questions": [question()]}
            audit.dump(root / "manifest.json", m)
            out = root / "results"
            with patch.dict("os.environ", {"JEV_API_KEY": "test"}), patch("audit.query", return_value={"status": "unscored_response", "raw_response": {"refusal": "test"}}) as api:
                audit.run(root, out, ["jev"], 0, 1, 1, 1, False)
                audit.run(root, out, ["jev"], 0, 1, 1, 1, False)
                self.assertEqual(api.call_count, 1)
            self.assertEqual(len(audit.latest_records(out.glob("predictions-*.jsonl"))), 1)

    def test_prepare_checks_pixels_and_keeps_original_dimensions(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, images, data = root / "source", root / "images", root / "data"
            source.mkdir()
            images.mkdir()
            rows = [{"filename": f"35_{g}_{r}_20170101{i:09d}.jpg", "age": 35, "gender": g, "race": r}
                    for g in (0, 1) for r in (0, 1) for i in range(2)]
            (source / "questions.json").write_text('{}')
            (source / "images_metadata.json").write_text('[]')
            for row in rows:
                Image.new("RGB", (39, 27), (23, 140, 220)).save(images / (row["filename"] + ".chip.jpg"))
            with patch("audit.metadata", return_value=rows), patch("audit.questions", return_value=[question()]):
                audit.prepare(source, images, data, "pilot", 4, 42)
            m = audit.load(data / "manifest.json")
            self.assertFalse(m["provenance"]["exact_official_test_split"])
            for row in m["images"]:
                with Image.open(images / (row["filename"] + ".chip.jpg")) as original, Image.open(data / row["image"]) as sent:
                    self.assertEqual(sent.size, (39, 27))
                    self.assertEqual(original.convert("RGB").tobytes(), sent.tobytes())
            with patch("audit.metadata", return_value=rows), patch("audit.questions", return_value=[question()]):
                audit.prepare(source, images, data, "pilot", 4, 42, min_side=280)
            m = audit.load(data / "manifest.json")
            for row in m["images"]:
                with Image.open(images / (row["filename"] + ".chip.jpg")) as original, Image.open(data / row["image"]) as sent:
                    self.assertEqual(sent.size, (280, 280))
                    left, top = row["padding_left_top"]
                    self.assertEqual(sent.crop((left, top, left+39, top+27)).tobytes(), original.convert("RGB").tobytes())
                    self.assertEqual(sent.getpixel((0, 0)), (128, 128, 128))

    def test_metadata_does_not_accept_a_different_split_size(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            audit.dump(root / "images_metadata.json", [])
            with self.assertRaisesRegex(ValueError, "1,505"):
                audit.metadata(root)

    def test_official_filename_keyed_schema_preserves_exact_filenames(self):
        rows = {f"35_{i % 2}_{i % 5}_20170101{i:09d}.jpg": {
            "age": 35, "gender": i % 2, "race": i % 5, "dataset_type": "cropped"}
            for i in range(1505)}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            audit.dump(root / "images_metadata.json", rows)
            parsed = audit.metadata(root)
            self.assertEqual({r["filename"] for r in parsed}, set(rows))
            self.assertEqual(len(parsed), 1505)
            first = next(iter(rows))
            rows[first]["filename"] = "mismatched.jpg"
            audit.dump(root / "images_metadata.json", rows)
            with self.assertRaisesRegex(ValueError, "filename-keyed"):
                audit.metadata(root)

    def test_analysis_reports_missing_tasks_instead_of_imputing_no(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            out = root / "results"
            out.mkdir()
            m = {"provenance": {}, "images": [{"id": "abc", "png_sha256": "hash", "race": 1}], "questions": [question()]}
            audit.dump(root / "manifest.json", m)
            result = audit.analyze(root, out, ["jev"], 1)
            self.assertEqual(result["missing_tasks"], 1)
            report = audit.load(out / "metrics.json")
            group = report["models"]["jev"]["questions"]["legal-07"]["groups"]["Black"]
            self.assertIsNone(group["adverse_rate"])
            self.assertEqual(group["expected_tasks"], 1)


if __name__ == "__main__":
    unittest.main()
