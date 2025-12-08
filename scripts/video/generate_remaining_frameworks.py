#!/usr/bin/env python3
"""
Batch generator for remaining 6 frameworks
Generates: CIA, SOLID, MECE, AIDA, OODA, RACI
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess

W, H, FPS = 1080, 1920, 30
C = {'b': (0,0,0), 'w': (255,255,255), 'gl': (220,220,220), 'gd': (40,40,40)}
COW = ["  ((____))", "  [ x x ]", "   \\   /", "   ('  ')", "   (U)"]

def gf(s):
    for f in ["/System/Library/Fonts/Supplemental/Didot.ttc", "/System/Library/Fonts/Supplemental/Times New Roman.ttf"]:
        try: return ImageFont.truetype(f, s)
        except: pass
def gmf(s):
    try: return ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", s)
    except: return ImageFont.load_default()
def dt(d,t,y,f,c): bb=d.textbbox((0,0),t,font=f); d.text(((W-(bb[2]-bb[0]))//2,y),t,font=f,fill=c)
def dml(d,ls,y,f,c,sp=10):
    for l in ls: bb=d.textbbox((0,0),l,font=f); d.text(((W-(bb[2]-bb[0]))//2,y),l,font=f,fill=c); y+=bb[3]-bb[1]+sp
def dc(d,x,y,c,s=30):
    f=gmf(s)
    for l in COW: bb=d.textbbox((0,0),l,font=f); d.text((x-(bb[2]-bb[0])//2,y),l,font=f,fill=c); y+=bb[3]-bb[1]+5
def dw(d): dt(d,"drewbeyersdorf",H-80,gf(40),C['gl'])

# Framework definitions
FRAMEWORKS = {
    'CIA': {
        'title': 'CIA Triad',
        'subtitle': 'Security Framework',
        'letters': [
            ('C', 'Confidentiality', ['Keep information', 'private and secure', 'from unauthorized access']),
            ('I', 'Integrity', ['Maintain accuracy', 'and trustworthiness', 'of data']),
            ('A', 'Availability', ['Ensure systems', 'remain accessible', 'when needed'])
        ],
        'outro': 'Secure Your Systems'
    },
    'SOLID': {
        'title': 'SOLID',
        'subtitle': 'OOP Principles',
        'letters': [
            ('S', 'Single Responsibility', ['One class,', 'one purpose,', 'one reason to change']),
            ('O', 'Open-Closed', ['Open for extension,', 'closed for', 'modification']),
            ('L', 'Liskov Substitution', ['Subtypes must be', 'substitutable for', 'their base types']),
            ('I', 'Interface Segregation', ['Many specific interfaces', 'better than one', 'general interface']),
            ('D', 'Dependency Inversion', ['Depend on abstractions,', 'not on', 'concretions'])
        ],
        'outro': 'Write Better Code'
    },
    'MECE': {
        'title': 'MECE',
        'subtitle': 'Problem Structuring',
        'letters': [
            ('M', 'Mutually', ['Categories should', 'not overlap', 'with each other']),
            ('E', 'Exclusive', ['Each item belongs', 'in only one', 'category']),
            ('C', 'Collectively', ['Together they cover', 'the complete', 'problem space']),
            ('E', 'Exhaustive', ['Nothing is left out,', 'everything is', 'accounted for'])
        ],
        'outro': 'Structure Problems'
    },
    'AIDA': {
        'title': 'AIDA',
        'subtitle': 'Marketing Model',
        'letters': [
            ('A', 'Attention', ['Grab their attention', 'with bold hooks', 'and strong headlines']),
            ('I', 'Interest', ['Build interest by', 'showing value', 'and relevance']),
            ('D', 'Desire', ['Create desire for', 'your solution', 'and benefits']),
            ('A', 'Action', ['Drive action with', 'clear call-to-action', 'and next steps'])
        ],
        'outro': 'Convert Better'
    },
    'OODA': {
        'title': 'OODA Loop',
        'subtitle': 'Decision Making',
        'letters': [
            ('O', 'Observe', ['Gather information', 'from your', 'environment']),
            ('O', 'Orient', ['Analyze context', 'and frame', 'the situation']),
            ('D', 'Decide', ['Choose best', 'course of', 'action']),
            ('A', 'Act', ['Execute swiftly', 'and iterate', 'continuously'])
        ],
        'outro': 'Decide Faster'
    },
    'RACI': {
        'title': 'RACI',
        'subtitle': 'Responsibility Matrix',
        'letters': [
            ('R', 'Responsible', ['Who does', 'the actual', 'work?']),
            ('A', 'Accountable', ['Who has final', 'decision authority', 'and ownership?']),
            ('C', 'Consulted', ['Who provides input', 'and expertise', 'before decisions?']),
            ('I', 'Informed', ['Who needs updates', 'about progress', 'and outcomes?'])
        ],
        'outro': 'Clarify Roles'
    }
}

def gen_framework(name, data):
    print(f"\n{'='*70}\n{name} - {data['title']}\n{'='*70}\n")
    OUT = Path(f"../../output/framework_shorts/{name.lower()}_frames")
    OUT.mkdir(parents=True, exist_ok=True)
    
    # Intro scene
    def si(fn,tf):
        i=Image.new('RGB',(W,H),C['w']); d=ImageDraw.Draw(i)
        dc(d,W//2,300,C['b'],40); dt(d,data['title'],700,gf(130),C['b'])
        dt(d,data['subtitle'],850,gf(55),C['gd']); dw(d); return i
    
    # Letter scenes
    def make_scene(letter, word, lines, bg_color):
        def scene(fn,tf):
            i=Image.new('RGB',(W,H),bg_color); d=ImageDraw.Draw(i)
            txt_color = C['w'] if bg_color==C['b'] else C['b']
            sub_color = C['gl'] if bg_color==C['b'] else C['gd']
            dc(d,W//2,150,txt_color,35); dt(d,letter,450,gf(140),txt_color)
            dt(d,word,620,gf(85),txt_color); dml(d,lines,760,gf(52),sub_color); dw(d); return i
        return scene
    
    # Outro scene
    def so(fn,tf):
        i=Image.new('RGB',(W,H),C['b']); d=ImageDraw.Draw(i)
        dc(d,W//2,250,C['w'],45); dt(d,data['title'],600,gf(110),C['w'])
        dt(d,data['outro'],720,gf(55),C['gl'])
        dt(d,"github.com/drewbeyersdorf/",950,gf(45),C['w'])
        dt(d,"agent-improvement-techniques",1010,gf(45),C['w']); dw(d); return i
    
    # Build scenes
    scenes = [(si, 0, 1.5, 45)]
    num_letters = len(data['letters'])
    time_per_letter = (12 - 1.5) / num_letters
    bg_toggle = C['b']
    
    for idx, (letter, word, lines) in enumerate(data['letters']):
        start = 1.5 + idx * time_per_letter
        end = start + time_per_letter
        frames = int((end - start) * FPS)
        scenes.append((make_scene(letter, word, lines, bg_toggle), start, end, frames))
        bg_toggle = C['w'] if bg_toggle == C['b'] else C['b']
    
    scenes.append((so, 12, 15, 90))
    
    # Generate frames
    fc = 0
    for sf, st, et, nf in scenes:
        print(f"🎬 {st:.1f}-{et:.1f}s ({nf} frames)...", end="")
        for i in range(nf):
            sf(i, nf).save(OUT / f"frame_{fc:04d}.png")
            fc += 1
        print(" ✅")
    
    print(f"\n✅ {fc} frames generated\n")
    
    # Create video
    print("🎬 Creating video...")
    silent = f"../../output/framework_shorts/{name}.mp4"
    subprocess.run(['ffmpeg', '-y', '-framerate', str(FPS), '-i', str(OUT / 'frame_%04d.png'),
                   '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'slow', '-crf', '18', silent],
                   check=True, capture_output=True)
    
    # Add music
    music = "../../output/tcrei_short/classical_music.mp3"
    if Path(music).exists():
        print("🎵 Adding music...")
        final = f"../../output/framework_shorts/{name}_FINAL.mp4"
        subprocess.run(['ffmpeg', '-y', '-i', silent, '-i', music, '-t', '15',
                       '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', final],
                      check=True, capture_output=True)
        print(f"\n✅ {name} COMPLETE: {final}\n")

# Generate all
print("\n🎬 GENERATING 6 REMAINING FRAMEWORKS\n")
for name, data in FRAMEWORKS.items():
    gen_framework(name, data)

print("\n" + "="*70)
print("✅ ALL 6 FRAMEWORKS COMPLETE!")
print("="*70 + "\n")
subprocess.run(['ls', '-lh', '../../output/framework_shorts/*_FINAL.mp4'])
