"""Insert verified PNG bytes into one CSV request template. Never sends it."""
import argparse
import base64
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path


def reconstruct(csv_path,task_id,image_path,source_image=False):
    csv.field_size_limit(32*1024*1024)
    opener=gzip.open if csv_path.suffix=='.gz' else open
    with opener(csv_path,'rt',encoding='utf-8',newline='') as f:
        row=next((r for r in csv.DictReader(f) if r['task_id']==task_id),None)
    if row is None:raise ValueError('Task ID not found')
    raw=image_path.read_bytes()
    if source_image:
        from PIL import Image
        assert hashlib.sha256(raw).hexdigest()==row['source_image_sha256'],'Source hash mismatch'
        with Image.open(io.BytesIO(raw)) as source:
            source.load();source=source.convert('RGB')
            canvas=Image.new('RGB',(int(row['input_width']),int(row['input_height'])),tuple(json.loads(row['padding_rgb_json'])))
            canvas.paste(source,(int(row['padding_left']),int(row['padding_top'])))
            b=io.BytesIO();canvas.save(b,format='PNG');raw=b.getvalue()
    assert hashlib.sha256(raw).hexdigest()==row['input_image_sha256'],'Input PNG hash mismatch. Source conversion uses Pillow 11.3.0 in the original protocol. Supply the prepared PNG or use that pinned version.'
    call=json.loads(row['api_call_json'])
    placeholder='<BASE64_PNG_SHA256:'+row['input_image_sha256']+'>'
    def fill(obj):
        if isinstance(obj,str):return obj.replace(placeholder,base64.b64encode(raw).decode())
        if isinstance(obj,list):return [fill(v) for v in obj]
        if isinstance(obj,dict):return {k:fill(v) for k,v in obj.items()}
        return obj
    return fill(call)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv',type=Path,required=True);p.add_argument('--task-id',required=True)
    p.add_argument('--image',type=Path,required=True);p.add_argument('--source-image',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();call=reconstruct(a.csv,a.task_id,a.image,a.source_image)
    a.out.write_text(json.dumps(call,ensure_ascii=False,indent=2)+'\n')
    print('Verified request written locally. No model call was made. Authentication must be supplied separately.')
