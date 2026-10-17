"""Prepare hash-verified evaluated face examples for the private blog draft."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import tarfile
from PIL import Image

RACES={0:'White',1:'Black',2:'Asian',3:'Indian',4:'Other'}


def prepare(manifest_path, archive_path, out):
    manifest=json.loads(manifest_path.read_text())
    acquisition=manifest['provenance']['image_acquisition']
    with archive_path.open('rb') as stream:
        archive_hash=hashlib.file_digest(stream,'sha256').hexdigest()
    if archive_hash!=acquisition['archive_sha256']:
        raise ValueError('Archive SHA-256 mismatch')
    ambiguous=set(manifest['ambiguous_demographic_hashes'])
    selected=[]
    for race in RACES:
        for gender in (0,1):
            candidates=[r for r in manifest['images'] if int(r['race'])==race and int(r['gender'])==gender and r['png_sha256'] not in ambiguous]
            selected.append(min(candidates,key=lambda r:r['id']))
    api_example=manifest['images'][0]
    unique={r['id']:r for r in [*selected,api_example]}
    source_bytes={}
    with tarfile.open(archive_path,'r:gz') as archive:
        for member in archive:
            if not member.isfile():continue
            name=Path(member.name).name
            for key,row in unique.items():
                if name not in (row['filename'],row['filename']+'.chip.jpg'):continue
                if key in source_bytes:raise ValueError('Duplicate archive member for '+key)
                source_bytes[key]=archive.extractfile(member).read()
    out.mkdir(parents=True,exist_ok=True)
    records=[]
    for key,row in unique.items():
        raw=source_bytes[key]
        if hashlib.sha256(raw).hexdigest()!=row['source_sha256']:
            raise ValueError('Source SHA-256 mismatch for '+key)
        with Image.open(io.BytesIO(raw)) as image:
            image.load();image=image.convert('RGB')
            if list(image.size)!=row['source_size']:raise ValueError('Source dimensions mismatch')
            canvas=Image.new('RGB',tuple(row['size']),(128,128,128))
            canvas.paste(image,tuple(row['padding_left_top']))
            buffer=io.BytesIO();canvas.save(buffer,format='PNG');png=buffer.getvalue()
        if hashlib.sha256(png).hexdigest()!=row['png_sha256']:
            raise ValueError('Input PNG SHA-256 mismatch for '+key+'. Use original Pillow version 11.3.0.')
        (out/(key+'.png')).write_bytes(png)
        records.append({**row,'race_annotation':RACES[int(row['race'])],
            'gallery':key in {r['id'] for r in selected},'api_example':key==api_example['id'],
            'file':key+'.png'})
    provenance={'scope':'Private draft illustrations only. The response CSV contains no image bytes.',
        'selection_rule':'Lexicographically smallest image ID per original dataset race and binary gender stratum, excluding conflicting demographic annotations. No model outputs used. The existing API example is the first entry in the original manifest.',
        'gallery_images':len(selected),'total_unique_images':len(records),
        'source_dataset_url':'https://susanqq.github.io/UTKFace/',
        'benchmark_dataset_url':'https://huggingface.co/datasets/vector-institute/fairlens',
        'image_acquisition':acquisition,'archive_sha256_verified':archive_hash,
        'demographic_note':'Labels are inherited UTKFace annotations, not inferred here or verified self-identifications. Other is a heterogeneous source category.',
        'image_note':'All distributed PNGs match the exact evaluated input SHA-256. Display scaling does not change downloaded image bytes.',
        'images':records}
    (out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    return {'gallery_images':len(selected),'total_unique_images':len(records),'source_and_evaluated_png_hashes_verified':True}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--archive',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(prepare(args.manifest,args.archive,args.out)))
