#!/usr/bin/env python3
"""
TCREI Short - RETRO ATARI STYLE Video Generator
Hermes on the Atari aesthetic - chunky pixels, limited colors, 8-bit vibes

Dependencies:
pip install pillow numpy

Generates frames, then use ffmpeg to combine into video
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import subprocess
import sys

# Configuration
OUTPUT_DIR = Path("../../output/tcrei_short/retro_frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 6  # Lower FPS = more retro feel

# ATARI COLOR PALETTE (Classic Atari 2600 colors)
ATARI_COLORS = {
    'black': (0, 0, 0),
    'red': (200, 60, 60),          # Atari red
    'orange': (255, 127, 39),      # Atari orange
    'yellow': (255, 255, 102),     # Atari yellow
    'green': (80, 220, 100),       # Atari green
    'blue': (100, 176, 255),       # Atari blue
    'cyan': (120, 240, 240),       # Atari cyan
    'white': (255, 255, 255),
    'gray': (128, 128, 128),
    'dark_gray': (64, 64, 64),
}

# Retro fonts - using basic PIL, will make it chunky
FONT_SIZE_HUGE = 140
FONT_SIZE_LARGE = 100
FONT_SIZE_MEDIUM = 70
FONT_SIZE_SMALL = 50


def create_pixelated_background(width, height, color1, color2, pattern='gradient'):
    """Create retro pixelated background"""
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    if pattern == 'gradient':
        for y in range(height):
            ratio = y / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            for x in range(width):
                pixels[x, y] = (r, g, b)
    elif pattern == 'scanlines':
        for y in range(height):
            color = color1 if y % 4 < 2 else color2
            for x in range(width):
                pixels[x, y] = color
    elif pattern == 'checkerboard':
        block_size = 40
        for y in range(height):
            for x in range(width):
                if ((x // block_size) + (y // block_size)) % 2 == 0:
                    pixels[x, y] = color1
                else:
                    pixels[x, y] = color2

    return img


def add_crt_effect(img):
    """Add CRT scanline effect"""
    draw = ImageDraw.Draw(img, 'RGBA')
    width, height = img.size

    # Horizontal scanlines
    for y in range(0, height, 3):
        draw.line([(0, y), (width, y)], fill=(0, 0, 0, 40), width=1)

    # Slight vignette
    for i in range(50):
        opacity = int(i * 1.5)
        draw.rectangle([i, i, width-i, height-i], outline=(0, 0, 0, opacity))

    return img


def create_retro_text(text, font_size, color, outline_color=None):
    """Create blocky retro text with outline"""
    # Calculate text size
    temp_img = Image.new('RGB', (WIDTH, HEIGHT))
    temp_draw = ImageDraw.Draw(temp_img)

    try:
        # Try to use a monospace font
        font = ImageFont.truetype("/System/Library/Fonts/Monaco.dfont", font_size)
    except:
        font = ImageFont.load_default()

    # Get text bounding box
    bbox = temp_draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Create image for text
    text_img = Image.new('RGBA', (text_width + 20, text_height + 20), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_img)

    # Draw outline (chunky retro style)
    if outline_color:
        for offset_x in [-4, -2, 0, 2, 4]:
            for offset_y in [-4, -2, 0, 2, 4]:
                if offset_x != 0 or offset_y != 0:
                    text_draw.text(
                        (10 + offset_x, 10 + offset_y),
                        text,
                        font=font,
                        fill=outline_color
                    )

    # Draw main text
    text_draw.text((10, 10), text, font=font, fill=color)

    return text_img


def scene_1_hook(frame_num, total_frames):
    """Scene 1: STOP! - Atari warning screen style (0-3s = 18 frames)"""
    # Red alert background with scanlines
    bg = create_pixelated_background(
        WIDTH, HEIGHT,
        ATARI_COLORS['red'],
        ATARI_COLORS['black'],
        'scanlines'
    )

    draw = ImageDraw.Draw(bg)

    # Flashing border effect (Atari style)
    if frame_num % 4 < 2:
        border_color = ATARI_COLORS['yellow']
    else:
        border_color = ATARI_COLORS['red']

    for i in range(20):
        draw.rectangle([i, i, WIDTH-i, HEIGHT-i], outline=border_color, width=3)

    # STOP text (appears with pixel animation)
    if frame_num >= 0:
        stop_text = create_retro_text(
            "STOP!",
            FONT_SIZE_HUGE,
            ATARI_COLORS['yellow'],
            ATARI_COLORS['black']
        )
        x = (WIDTH - stop_text.width) // 2
        y = 250
        bg.paste(stop_text, (x, y), stop_text)

    # Secondary text
    if frame_num >= 6:
        letting_text = create_retro_text(
            "LETTING AI",
            FONT_SIZE_MEDIUM,
            ATARI_COLORS['cyan'],
            ATARI_COLORS['black']
        )
        x = (WIDTH - letting_text.width) // 2
        y = 700
        bg.paste(letting_text, (x, y), letting_text)

    if frame_num >= 10:
        guess_text = create_retro_text(
            "GUESS WHAT\nYOU WANT!",
            FONT_SIZE_MEDIUM,
            ATARI_COLORS['white'],
            ATARI_COLORS['black']
        )
        x = (WIDTH - guess_text.width) // 2
        y = 1200
        bg.paste(guess_text, (x, y), guess_text)

    # Add CRT effect
    bg = add_crt_effect(bg)

    return bg


def scene_2_problem(frame_num, total_frames):
    """Scene 2: Problem screen (3-8s = 30 frames)"""
    # Dark blue background with grid pattern
    bg = create_pixelated_background(
        WIDTH, HEIGHT,
        ATARI_COLORS['black'],
        ATARI_COLORS['dark_gray'],
        'checkerboard'
    )

    draw = ImageDraw.Draw(bg)

    # Retro computer terminal aesthetic
    # Draw grid lines
    for i in range(0, HEIGHT, 80):
        draw.line([(0, i), (WIDTH, i)], fill=ATARI_COLORS['dark_gray'], width=2)

    # Speech bubble (retro style)
    if frame_num >= 24:  # Appears at ~4s
        bubble_y = 500
        draw.rectangle(
            [150, bubble_y, 930, bubble_y + 200],
            fill=ATARI_COLORS['white'],
            outline=ATARI_COLORS['cyan'],
            width=6
        )

        # Triangle pointer
        draw.polygon(
            [(540, bubble_y + 200), (480, bubble_y + 280), (600, bubble_y + 280)],
            fill=ATARI_COLORS['white'],
            outline=ATARI_COLORS['cyan']
        )

        auth_text = create_retro_text(
            '"ADD AUTH"',
            FONT_SIZE_LARGE,
            ATARI_COLORS['black'],
            None
        )
        x = (WIDTH - auth_text.width) // 2
        bg.paste(auth_text, (x, bubble_y + 50), auth_text)

    # Error message (Atari style)
    if frame_num >= 30:
        error_text = create_retro_text(
            "AI BUILDS THE",
            FONT_SIZE_MEDIUM,
            ATARI_COLORS['orange'],
            ATARI_COLORS['black']
        )
        x = (WIDTH - error_text.width) // 2
        bg.paste(error_text, (x, 1200), error_text)

        wrong_text = create_retro_text(
            "WRONG THING!",
            FONT_SIZE_LARGE,
            ATARI_COLORS['red'],
            ATARI_COLORS['black']
        )
        x = (WIDTH - wrong_text.width) // 2
        bg.paste(wrong_text, (x, 1350), wrong_text)

        # Flashing X
        if frame_num % 4 < 2:
            draw.text((WIDTH//2 - 30, 1500), "X",
                     fill=ATARI_COLORS['red'], font=None)

    bg = add_crt_effect(bg)
    return bg


def scene_3_solution(frame_num, total_frames):
    """Scene 3: TCREI Logo reveal (8-11s = 18 frames)"""
    # Blue gradient background
    bg = create_pixelated_background(
        WIDTH, HEIGHT,
        ATARI_COLORS['blue'],
        ATARI_COLORS['black'],
        'gradient'
    )

    draw = ImageDraw.Draw(bg)

    # Retro star field effect
    import random
    random.seed(42)  # Consistent stars
    for _ in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(2, 6)
        if frame_num % 6 < 3:
            draw.ellipse([x, y, x+size, y+size], fill=ATARI_COLORS['white'])

    # TCREI logo (pixelated reveal)
    scale = min(1.0, frame_num / 6)  # Zoom in effect
    if scale > 0:
        tcrei_text = create_retro_text(
            "TCREI",
            int(FONT_SIZE_HUGE * 1.2),
            ATARI_COLORS['yellow'],
            ATARI_COLORS['blue']
        )

        # Center with scale
        scaled_width = int(tcrei_text.width * scale)
        scaled_height = int(tcrei_text.height * scale)
        tcrei_scaled = tcrei_text.resize((scaled_width, scaled_height), Image.NEAREST)

        x = (WIDTH - scaled_width) // 2
        y = 600
        bg.paste(tcrei_scaled, (x, y), tcrei_scaled)

    # Subtitle
    if frame_num >= 10:
        subtitle = create_retro_text(
            "PERFECT AI ALIGNMENT",
            FONT_SIZE_SMALL,
            ATARI_COLORS['cyan'],
            ATARI_COLORS['black']
        )
        x = (WIDTH - subtitle.width) // 2
        bg.paste(subtitle, (x, 1100), subtitle)

    bg = add_crt_effect(bg)
    return bg


def scene_4_breakdown(frame_num, total_frames):
    """Scene 4: TCREI Breakdown - Terminal style (11-25s = 84 frames)"""
    # Black terminal background
    bg = Image.new('RGB', (WIDTH, HEIGHT), ATARI_COLORS['black'])
    draw = ImageDraw.Draw(bg)

    # Green terminal scanlines
    for i in range(0, HEIGHT, 2):
        draw.line([(0, i), (WIDTH, i)], fill=(0, 40, 0), width=1)

    # Terminal border
    draw.rectangle([40, 40, WIDTH-40, HEIGHT-40],
                   outline=ATARI_COLORS['green'], width=8)

    # Each letter appears sequentially
    letters = [
        ("T", "TASK", "WHAT EXACTLY?", 200, 0),
        ("C", "CONTEXT", "WHY NEEDED?", 450, 14),
        ("R", "REFERENCE", "ANY EXAMPLES?", 700, 28),
        ("E", "EVALUATION", "MEASURE SUCCESS?", 950, 42),
        ("I", "INPUT", "READ SCHEMA FIRST?", 1200, 56),
    ]

    for letter, word, desc, y_pos, start_frame in letters:
        if frame_num >= start_frame:
            # Letter with emoji-style icon
            icon_map = {"T": "[]", "C": "()", "R": "<>", "E": "++", "I": "##"}
            icon = icon_map.get(letter, "**")

            letter_text = create_retro_text(
                f"{letter} {icon}",
                FONT_SIZE_LARGE,
                ATARI_COLORS['yellow'],
                ATARI_COLORS['green']
            )
            bg.paste(letter_text, (150, y_pos), letter_text)

            # Word
            if frame_num >= start_frame + 4:
                word_text = create_retro_text(
                    word,
                    FONT_SIZE_MEDIUM,
                    ATARI_COLORS['cyan'],
                    ATARI_COLORS['black']
                )
                bg.paste(word_text, (450, y_pos + 10), word_text)

            # Description
            if frame_num >= start_frame + 8:
                desc_text = create_retro_text(
                    desc,
                    FONT_SIZE_SMALL,
                    ATARI_COLORS['white'],
                    None
                )
                bg.paste(desc_text, (150, y_pos + 90), desc_text)

    bg = add_crt_effect(bg)
    return bg


def scene_5_result(frame_num, total_frames):
    """Scene 5: Before/After (25-28s = 18 frames)"""
    bg = Image.new('RGB', (WIDTH, HEIGHT), ATARI_COLORS['black'])
    draw = ImageDraw.Draw(bg)

    # Split screen with retro dividing line
    # Top half - BEFORE (red/chaotic)
    for y in range(0, HEIGHT//2):
        for x in range(0, WIDTH, 40):
            if (x + y) % 80 < 40:
                color = ATARI_COLORS['red']
            else:
                color = ATARI_COLORS['dark_gray']
            draw.rectangle([x, y, x+40, y+40], fill=color)

    before_text = create_retro_text(
        "BEFORE",
        FONT_SIZE_LARGE,
        ATARI_COLORS['yellow'],
        ATARI_COLORS['black']
    )
    x = (WIDTH - before_text.width) // 2
    bg.paste(before_text, (x, 200), before_text)

    chaos_text = create_retro_text(
        "CHAOTIC!",
        FONT_SIZE_MEDIUM,
        ATARI_COLORS['orange'],
        ATARI_COLORS['black']
    )
    x = (WIDTH - chaos_text.width) // 2
    bg.paste(chaos_text, (x, 350), chaos_text)

    # Bottom half - AFTER (green/organized)
    for y in range(HEIGHT//2, HEIGHT):
        for x in range(0, WIDTH, 40):
            if (x // 40) % 2 == 0:
                color = ATARI_COLORS['green']
            else:
                color = ATARI_COLORS['black']
            draw.rectangle([x, y, x+40, y+40], fill=color)

    after_text = create_retro_text(
        "AFTER",
        FONT_SIZE_LARGE,
        ATARI_COLORS['yellow'],
        ATARI_COLORS['black']
    )
    x = (WIDTH - after_text.width) // 2
    bg.paste(after_text, (x, 1100), after_text)

    aligned_text = create_retro_text(
        "PERFECT\nALIGNMENT!",
        FONT_SIZE_MEDIUM,
        ATARI_COLORS['cyan'],
        ATARI_COLORS['black']
    )
    x = (WIDTH - aligned_text.width) // 2
    bg.paste(aligned_text, (x, 1300), aligned_text)

    # Dividing line with animation
    line_y = HEIGHT // 2
    for i in range(0, WIDTH, 20):
        if (i + frame_num * 40) % 40 < 20:
            draw.rectangle([i, line_y-10, i+20, line_y+10],
                          fill=ATARI_COLORS['yellow'])

    bg = add_crt_effect(bg)
    return bg


def scene_6_cta(frame_num, total_frames):
    """Scene 6: Call to Action (28-30s = 12 frames)"""
    # Blue background with retro pattern
    bg = create_pixelated_background(
        WIDTH, HEIGHT,
        ATARI_COLORS['blue'],
        ATARI_COLORS['black'],
        'gradient'
    )

    draw = ImageDraw.Draw(bg)

    # Flashing border
    if frame_num % 4 < 2:
        for i in range(30):
            draw.rectangle([i*2, i*2, WIDTH-i*2, HEIGHT-i*2],
                          outline=ATARI_COLORS['cyan'], width=2)

    # Main text
    rpi_text = create_retro_text(
        "RPI FRAMEWORK",
        FONT_SIZE_LARGE,
        ATARI_COLORS['yellow'],
        ATARI_COLORS['blue']
    )
    x = (WIDTH - rpi_text.width) // 2
    bg.paste(rpi_text, (x, 600), rpi_text)

    # Link text with retro cursor
    link_text = create_retro_text(
        "LINK IN BIO",
        FONT_SIZE_MEDIUM,
        ATARI_COLORS['white'],
        ATARI_COLORS['black']
    )
    x = (WIDTH - link_text.width) // 2
    bg.paste(link_text, (x, 1000), link_text)

    # Animated down arrow (old-school style)
    arrow_y = 1200 + (frame_num % 8) * 10
    draw.polygon(
        [(WIDTH//2, arrow_y), (WIDTH//2 - 80, arrow_y - 80), (WIDTH//2 + 80, arrow_y - 80)],
        fill=ATARI_COLORS['cyan'],
        outline=ATARI_COLORS['yellow']
    )

    bg = add_crt_effect(bg)
    return bg


def generate_all_frames():
    """Generate all frames for the 30-second video"""
    print("=" * 70)
    print("TCREI SHORT - RETRO ATARI STYLE GENERATOR")
    print("Hermes on the Atari aesthetic - chunky pixels, 8-bit vibes")
    print("=" * 70)
    print()

    scenes = [
        ("Scene 1: STOP Hook", scene_1_hook, 0, 3, 18),
        ("Scene 2: Problem", scene_2_problem, 3, 8, 30),
        ("Scene 3: TCREI Logo", scene_3_solution, 8, 11, 18),
        ("Scene 4: Breakdown", scene_4_breakdown, 11, 25, 84),
        ("Scene 5: Before/After", scene_5_result, 25, 28, 18),
        ("Scene 6: Call to Action", scene_6_cta, 28, 30, 12),
    ]

    frame_number = 0

    for scene_name, scene_func, start_sec, end_sec, total_frames in scenes:
        print(f"\n🎬 Generating {scene_name} ({start_sec}-{end_sec}s, {total_frames} frames)...")

        for i in range(total_frames):
            frame = scene_func(i, total_frames)

            # Save frame
            frame_path = OUTPUT_DIR / f"frame_{frame_number:04d}.png"
            frame.save(frame_path)

            # Progress
            if (i + 1) % 6 == 0:
                print(f"  Generated {i+1}/{total_frames} frames...", end='\r')

            frame_number += 1

        print(f"  ✅ {scene_name} complete! ({total_frames} frames)")

    print(f"\n{'=' * 70}")
    print(f"✅ ALL FRAMES GENERATED!")
    print(f"📁 Location: {OUTPUT_DIR}")
    print(f"📊 Total frames: {frame_number}")
    print(f"{'=' * 70}")

    return frame_number


def combine_frames_to_video():
    """Use ffmpeg to combine frames into video"""
    print("\n🎥 Combining frames into video...")

    output_video = "../../output/tcrei_short/TCREI_SHORT_RETRO_ATARI.mp4"

    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except:
        print("\n❌ ffmpeg not found!")
        print("Install with: brew install ffmpeg")
        print(f"\nOR manually combine frames from: {OUTPUT_DIR}")
        print(f"Command: ffmpeg -framerate {FPS} -i {OUTPUT_DIR}/frame_%04d.png -c:v libx264 -pix_fmt yuv420p {output_video}")
        return None

    # FFmpeg command
    cmd = [
        'ffmpeg',
        '-y',  # Overwrite output
        '-framerate', str(FPS),
        '-i', str(OUTPUT_DIR / 'frame_%04d.png'),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'slow',
        '-crf', '18',  # High quality
        output_video
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"\n✅ VIDEO CREATED SUCCESSFULLY!")
        print(f"📁 Output: {output_video}")
        print(f"📐 Format: {WIDTH}x{HEIGHT} (9:16 vertical)")
        print(f"🎞️  FPS: {FPS} (retro low framerate)")
        print(f"⏱️  Duration: ~30 seconds")
        print(f"🎨 Style: RETRO ATARI (Hermes aesthetic)")
        return output_video
    else:
        print(f"\n❌ Error creating video: {result.stderr}")
        return None


if __name__ == "__main__":
    print("\n🕹️  RETRO ATARI TCREI SHORT GENERATOR")
    print("Chunky pixels, limited colors, 8-bit aesthetic\n")

    # Generate frames
    total_frames = generate_all_frames()

    # Combine into video
    video_path = combine_frames_to_video()

    if video_path:
        print("\n" + "=" * 70)
        print("🎉 RETRO TCREI SHORT COMPLETE!")
        print("=" * 70)
        print("\n📤 Next steps:")
        print("1. Review the video")
        print("2. Add voice narration (optional)")
        print("3. Upload to YouTube Shorts, TikTok, Instagram Reels")
        print("\n🎨 ATARI AESTHETIC: Chunky pixels, scanlines, limited palette")
        print("=" * 70)

    print("\n✨ Generation complete! Hermes would be proud. 🕹️")
