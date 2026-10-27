#!/usr/bin/env python3
"""Labeled contact sheet for visual comparisons (requires Pillow, no source changes)."""
import argparse, math, pathlib

def run(a):
    try:from PIL import Image, ImageOps, ImageDraw
    except ImportError:raise SystemExit('Requires Pillow: python3 -m pip install Pillow')
    files=[pathlib.Path(p) for p in a.images]
    if not all(f.is_file() for f in files):raise SystemExit('Missing image input')
    pictures=[]
    for f in files:
        with Image.open(f) as im:pictures.append((f.name,im.convert('RGBA').copy()))
    w,h=a.cell_width,a.cell_height
    cols=max(1,a.columns);rows=math.ceil(len(pictures)/cols)
    out=Image.new('RGB',(cols*w,rows*(h+30)),(34,36,42));draw=ImageDraw.Draw(out)
    for i,(name,img) in enumerate(pictures):
        tile=Image.new('RGBA',(w,h),(15,16,19,255))
        img.thumbnail((w,h),Image.Resampling.NEAREST)
        tile.alpha_composite(img,((w-img.width)//2,(h-img.height)//2))
        x=(i%cols)*w;y=(i//cols)*(h+30)
        out.paste(tile.convert('RGB'),(x,y));draw.text((x+7,y+h+6),name[:45],fill=(235,235,235))
    target=pathlib.Path(a.out);target.parent.mkdir(parents=True,exist_ok=True);out.save(target);print(target)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('images',nargs='+');p.add_argument('--out',required=True);p.add_argument('--columns',type=int,default=3);p.add_argument('--cell-width',type=int,default=384);p.add_argument('--cell-height',type=int,default=256);run(p.parse_args())
