#!/usr/bin/env python3
"""Prepare the verified public FairLens CSV. No analysis code is distributed."""
from hashlib import sha256
import json
from pathlib import Path


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
    ARCHIVE.unlink(missing_ok=True)
    (POST / "checksums.json").unlink(missing_ok=True)
    print(json.dumps({"csv_bytes": csv_path.stat().st_size,
                      "csv_sha256": EXPECTED_CSV, "model_calls": 0}))



if __name__ == "__main__":
    build()
