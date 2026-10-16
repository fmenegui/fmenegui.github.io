"""Download the two exact ECG examples used in the published model runs.

These are illustrative examples of original benchmark inputs, not synthetic
drawings. Output stays inside the built website and never includes source
repository URLs in the published blog text.
"""
from io import BytesIO
from pathlib import Path
from urllib.request import Request,urlopen
from PIL import Image,ImageOps
import hashlib

ROOT=Path(__file__).resolve().parents[1]
EXAMPLES=[
    ("system-one-ecg","https://raw.githubusercontent.com/fmenegui/sangha-code-test-reproduce/main/data/images_sangha_style_rendering/ecg_0.png",(1568,1568),None),
    ("system-one-ptbxl","https://huggingface.co/datasets/edcci/GenECG/resolve/main/Dataset_A_ECGs_without_imperfections/00000/00001_hr_1R.png",(1568,1000),"e646a66990f233d4b8d1728bc2eeaf9e722bd4e4e8d525aa9d7536b6d500627f"),
]
def build():
    for folder,url,bounds,expected in EXAMPLES:
        req=Request(url,headers={"User-Agent":"ECG-Research-Blog/1.0"})
        with urlopen(req,timeout=120) as response:
            raw=response.read()
        with Image.open(BytesIO(raw)) as im:
            im=ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail(bounds,Image.Resampling.LANCZOS)
            buffer=BytesIO()
            im.save(buffer,format="PNG",optimize=True)
            png=buffer.getvalue()
            if im.width<256 or im.height<256:
                raise ValueError(f"Image too small for {folder}: {im.size}")
        digest=hashlib.sha256(png).hexdigest()
        if expected and digest!=expected:
            raise ValueError(f"{folder}: image differs from recorded input (sha256={digest})")
        path=ROOT/folder/"example-ecg.png"
        path.write_bytes(png)
        print(folder,im.size,digest,len(png))
if __name__=="__main__":build()
