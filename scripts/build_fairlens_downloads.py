#!/usr/bin/env python3
"""Package the saved FairLens results for offline reproduction. No API calls."""
from hashlib import sha256
import json
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "blog/system-one-fairlens"
ARCHIVE = POST / "data/fairlens-reproducibility.zip"
EXPECTED_CSV = "595db4c2563eac7f2f75df059dbe0c6a2111a235dccf8884b3641984988baf94"


def build():
    csv_path = POST / "data/fairlens-responses.csv.gz"
    source = ROOT / "_fairlens-data"
    manifest = json.loads((source / "manifest.json").read_text())
    assert manifest["sha256"] == EXPECTED_CSV
    with csv_path.open("wb") as destination:
        for part in manifest["parts"]:
            assert Path(part["filename"]).name == part["filename"]
            raw = (source / part["filename"]).read_bytes()
            assert len(raw) == part["size_bytes"]
            assert sha256(raw).hexdigest() == part["sha256"]
            destination.write(raw)
    assert sha256(csv_path.read_bytes()).hexdigest() == EXPECTED_CSV
    paths = sorted(
        path for path in POST.rglob("*")
        if path.is_file()
        and path != ARCHIVE
        and path.name != "checksums.json"
        and "__pycache__" not in path.parts
    )
    checksums = {
        path.relative_to(POST).as_posix(): sha256(path.read_bytes()).hexdigest()
        for path in paths
    }
    checksum_path = POST / "checksums.json"
    checksum_path.write_text(json.dumps(checksums, indent=2) + "\n")
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in paths + [checksum_path]:
            entry = zipfile.ZipInfo(path.relative_to(POST).as_posix(), (2026, 10, 17, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_STORED if path.suffix == ".gz" else zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            archive.writestr(entry, path.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
        assert json.loads(archive.read("checksums.json")) == checksums
    print(json.dumps({"download_files": len(checksums), "archive_bytes": ARCHIVE.stat().st_size,
                      "csv_sha256": EXPECTED_CSV, "model_calls": 0}))


if __name__ == "__main__":
    build()
