#!/usr/bin/env python3
"""Assemble an unchanged evaluation CSV for website publication. No model calls."""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    source = ROOT / '_xray-data'
    manifest = json.loads((source / 'manifest.json').read_text())
    output = ROOT / manifest['output']
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('wb') as destination:
        for part in manifest['parts']:
            assert Path(part['filename']).name == part['filename']
            raw = (source / part['filename']).read_bytes()
            assert len(raw) == part['size_bytes']
            assert sha256(raw).hexdigest() == part['sha256']
            destination.write(raw)
    assert output.stat().st_size == manifest['size_bytes']
    assert sha256(output.read_bytes()).hexdigest() == manifest['sha256']
    print(json.dumps({'csv_bytes': manifest['size_bytes'],
                      'csv_sha256': manifest['sha256'], 'model_calls': 0}))


if __name__ == '__main__':
    build()
