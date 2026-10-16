"""Validate pinned benchmark images and their matching saved model answers.

Assets are checked in so publishing never depends on remote dataset access.
PTB-XL hashes match the inference records. CODE hashes identify the images
recreated with the original preprocessing and recorded dimensions.
"""
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent

def build():
    for item in json.loads((ROOT / "ecg-examples.json").read_text()):
        path = ROOT / item["image"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            raise ValueError(f"Image checksum mismatch: {path.name}")
        with Image.open(path) as im:
            im.verify()
        with Image.open(path) as im:
            if list(im.size) != item["size"]:
                raise ValueError(f"Image dimensions differ: {path.name}")
        data = json.loads((ROOT / item["outputs"]).read_text())
        if data["input_png_sha256"] != digest:
            raise ValueError("JSON is linked to another image")
        for model in ("jev", "gpt-decisions"):
            answers = data[model]["answers"]
            if set(answers) != set(data["reference_labels"]):
                raise ValueError("Missing diagnostic class")
            for answer in answers.values():
                probs = answer["probabilities"]
                if answer["choice"] not in ("YES", "NO"):
                    raise ValueError("Invalid choice")
                if not all(0 <= probs[k] <= 1 for k in ("YES", "NO")) or abs(probs["YES"]+probs["NO"]-1) > 1e-9:
                    raise ValueError("Invalid probabilities")
        print("Verified", item["image"], "and matching saved answers")

if __name__ == "__main__":
    build()
