"""Download the official aligned/cropped UTKFace release for research."""
from pathlib import Path
import argparse
import hashlib
import json
import tarfile
import urllib.request
import zipfile

FOLDER = "https://drive.google.com/drive/folders/0BxYys69jI14kU0I1YUQyY1ZDRUE"
MIRROR = "https://huggingface.co/datasets/py97/UTKFace-Cropped/resolve/e80f21fb21fa3631380c3cb634b79be3ac2f4cba/UTKFace.tar.gz"
MIRROR_SHA256 = "2c0655397b498e81b82d685ee74bee8c2e4364a5897caf3afec6ea48929024a7"
MIRROR_SIZE = 106634631


def download_mirror(target):
    """Explicit mirror choice, immutable revision and verified archive bytes."""
    tmp = target.with_suffix(target.suffix + ".part")
    try:
        hasher = hashlib.sha256()
        total = 0
        with urllib.request.urlopen(MIRROR, timeout=60) as response, tmp.open("wb") as file:
            while chunk := response.read(1024 * 1024):
                total += len(chunk)
                if total > MIRROR_SIZE:
                    raise ValueError("Mirror archive exceeds pinned size")
                hasher.update(chunk)
                file.write(chunk)
        if total != MIRROR_SIZE or hasher.hexdigest() != MIRROR_SHA256:
            raise ValueError("Mirror archive checksum or size mismatch")
        tmp.replace(target)
        return {"source": "hf-mirror", "url": MIRROR, "archive_sha256": hasher.hexdigest(), "bytes": total,
                "original_source": "https://susanqq.github.io/UTKFace/", "terms": "Original non-commercial research restriction applies",
                "limitation": "Mirror bytes pinned. Byte equality with unavailable original Drive archive is not independently verified"}
    finally:
        tmp.unlink(missing_ok=True)


def extract_images(archive, destination):
    """Flatten only regular image entries. Never extract paths or symlinks."""
    destination.mkdir(parents=True, exist_ok=True)
    count = 0
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as handle:
            for item in handle.infolist():
                name = Path(item.filename).name
                if item.is_dir() or not name.lower().endswith((".jpg", ".jpeg", ".png")):
                    continue
                if item.file_size > 20_000_000:
                    raise ValueError("Oversized image archive entry")
                raw = handle.read(item)
                target = destination / name
                if target.exists() and target.read_bytes() != raw:
                    raise ValueError("Conflicting image filenames")
                target.write_bytes(raw)
                count += 1
    else:
        with tarfile.open(archive) as handle:
            for item in handle:
                name = Path(item.name).name
                if not item.isfile() or not name.lower().endswith((".jpg", ".jpeg", ".png")):
                    continue
                if item.size > 20_000_000:
                    raise ValueError("Oversized image archive entry")
                raw = handle.extractfile(item).read()
                target = destination / name
                if target.exists() and target.read_bytes() != raw:
                    raise ValueError("Conflicting image filenames")
                target.write_bytes(raw)
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=("official", "hf-mirror"), default="official")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent / "utkface"
    downloads = root / "archives"
    downloads.mkdir(parents=True, exist_ok=True)
    if args.source == "hf-mirror":
        target = downloads / "UTKFace.tar.gz"
        provenance = download_mirror(target)
        paths = [str(target)]
    else:
        import gdown
        target = downloads / "UTKFace.tar.gz"
        name = gdown.download(id="0BxYys69jI14kYVM3aVhKS1VhRUk", output=str(target), quiet=True, use_cookies=False)
        paths = [name] if name else gdown.download_folder(FOLDER, output=str(downloads), quiet=True, use_cookies=False)
        provenance = {"source": "official", "url": FOLDER}
    if not paths:
        raise RuntimeError("Official UTKFace download unavailable. Supply the original cropped release manually")
    count = 0
    for name in paths:
        path = Path(name)
        if path.name.endswith((".zip", ".tar", ".tar.gz", ".tgz")):
            count += extract_images(path, root / "images")
    if count == 0:
        raise RuntimeError("Official folder returned no supported image archive")
    provenance["extracted_images"] = count
    (root / "acquisition.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print("Extracted", count, "images using", args.source)


if __name__ == "__main__":
    main()
