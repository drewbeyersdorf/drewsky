#!/usr/bin/env python3
"""RICE Framework - Reach, Impact, Confidence, Effort"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess, sys

OUT = Path("../../output/framework_shorts/rice_frames")
OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
C = {'black': (0,0,0), 'white': (255,255,255), 'gl': (220,220,220), 'gd': (40,40,40)}
COW = ["  ((____))", "  [ x x ]", "   \\   /", "   ('  ')", "   (U)"]

def gf(s):
    for f in ["/System/Library/Fonts/Supplemental/Didot.ttc", "/System/Library/Fonts/Supplemental/Times New Roman.ttf"]:
        try: return ImageFont.truetype(f, s)
        except: pass
    return ImageFont.load_default()

def gmf(s):
    try: return ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", s)
    except: return ImageFont.load_default()

def dt(d, t, y, f, c, w):
    bb = d.textbbox((0,0), t, font=f)
    d.text(((w-(bb[2]-bb[0]))//2, y), t, font=f, fill=c)

def dml(d, ls, y, f, c, w, sp=10):
    for l in ls:
        bb = d.textbbox((0,0), l, font=f)
        d.text(((w-(bb[2]-bb[0]))//2, y), l, font=f, fill=c)
        y += bb[3]-bb[1]+sp

def dc(d, x, y, c, s=30):
    f = gmf(s)
    for l in COW:
        bb = d.textbbox((0,0), l, font=f)
        d.text((x-(bb[2]-bb[0])//2, y), l, font=f, fill=c)
        y += bb[3]-bb[1]+5

def dw(d, w, h):
    f = gf(40)
    t = "drewbeyersdorf"
    bb = d.textbbox((0,0), t, font=f)
    d.text((w-bb[2]+bb[0]-40, h-80), t, font=f, fill=C['gl'])

def si(fn, tf):
    i = Image.new('RGB', (W,H), C['white'])
    d = ImageDraw.Draw(i)
    dc(d, W//2, 300, C['black'], 40)
    dt(d, "RICE", 700, gf(130), C['black'], W)
    dt(d, "Framework", 850, gf(55), C['gd'], W)
    dw(d, W, H)
    return i

def sR(fn, tf):
    i = Image.new('RGB', (W,H), C['black'])
    d = ImageDraw.Draw(i)
    dc(d, W//2, 150, C['white'], 35)
    dt(d, "R", 450, gf(140), C['white'], W)
    dt(d, "Reach", 620, gf(85), C['white'], W)
    dml(d, ["How many people", "will this impact?", "Estimate users affected"], 760, gf(52), C['gl'], W)
    dw(d, W, H)
    return i

def sI(fn, tf):
    i = Image.new('RGB', (W,H), C['white'])
    d = ImageDraw.Draw(i)
    dc(d, W//2, 150, C['black'], 35)
    dt(d, "I", 450, gf(140), C['black'], W)
    dt(d, "Impact", 620, gf(85), C['black'], W)
    dml(d, ["What's the effect", "on each person?", "Rate the improvement"], 760, gf(52), C['gd'], W)
    dw(d, W, H)
    return i

def sC(fn, tf):
    i = Image.new('RGB', (W,H), C['black'])
    d = ImageDraw.Draw(i)
    dc(d, W//2, 150, C['white'], 35)
    dt(d, "C", 450, gf(140), C['white'], W)
    dt(d, "Confidence", 620, gf(85), C['white'], W)
    dml(d, ["How sure are we", "about estimates?", "Assess uncertainty"], 760, gf(52), C['gl'], W)
    dw(d, W, H)
    return i

def sE(fn, tf):
    i = Image.new('RGB', (W,H), C['white'])
    d = ImageDraw.Draw(i)
    dc(d, W//2, 150, C['black'], 35)
    dt(d, "E", 450, gf(140), C['black'], W)
    dt(d, "Effort", 620, gf(85), C['black'], W)
    dml(d, ["How much work", "is required?", "Count person-months"], 760, gf(52), C['gd'], W)
    dw(d, W, H)
    return i

def so(fn, tf):
    i = Image.new('RGB', (W,H), C['black'])
    d = ImageDraw.Draw(i)
    dc(d, W//2, 250, C['white'], 45)
    dt(d, "RICE", 600, gf(110), C['white'], W)
    dt(d, "Prioritize Better", 720, gf(55), C['gl'], W)
    dt(d, "github.com/drewbeyersdorf/", 950, gf(45), C['white'], W)
    dt(d, "agent-improvement-techniques", 1010, gf(45), C['white'], W)
    dw(d, W, H)
    return i

print("\n"+"="*70+"\nRICE FRAMEWORK\n"+"="*70+"\n")
scenes = [(si,0,1.5,45),(sR,1.5,4,75),(sI,4,6.5,75),(sC,6.5,9,75),(sE,9,12,90),(so,12,15,90)]
fc = 0
for sf,st,et,nf in scenes:
    print(f"🎬 {st}-{et}s ({nf} frames)...", end="")
    for i in range(nf):
        sf(i,nf).save(OUT/f"frame_{fc:04d}.png")
        fc += 1
    print(" ✅")

print(f"\n✅ {fc} frames\n\n🎬 Creating video...")
subprocess.run(['ffmpeg','-y','-framerate',str(FPS),'-i',str(OUT/'frame_%04d.png'),'-c:v','libx264','-pix_fmt','yuv420p','-preset','slow','-crf','18','../../output/framework_shorts/RICE.mp4'], check=True, capture_output=True)
print("✅ Silent video\n🎵 Adding music...")
mp = "../../output/tcrei_short/classical_music.mp3"
if Path(mp).exists():
    subprocess.run(['ffmpeg','-y','-i','../../output/framework_shorts/RICE.mp4','-i',mp,'-t','15','-c:v','copy','-c:a','aac','-b:a','192k','-shortest','../../output/framework_shorts/RICE_FINAL.mp4'], check=True, capture_output=True)
    print("\n"+"="*70+"\n✅ RICE FRAMEWORK COMPLETE!\n📁 framework_shorts/RICE_FINAL.mp4\n"+"="*70+"\n")
