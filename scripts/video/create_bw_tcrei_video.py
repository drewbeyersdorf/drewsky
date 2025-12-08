#!/usr/bin/env python3
"""
TCREI Short - Black & White Classical Style
Pure B&W, elegant serif fonts, classical music aesthetic
I = Iteration (corrected)

Dependencies:
pip install pillow numpy

Generates frames, then uses ffmpeg to combine with classical music
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import subprocess
import sys

# Configuration
OUTPUT_DIR = Path("../../output/tcrei_short/bw_frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

# PURE BLACK & WHITE - No grays, pure contrast
COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray_light': (220, 220, 220),    # Only for subtle accents
    'gray_dark': (40, 40, 40),        # Only for subtle accents
}

# Elegant fonts
FONT_DISPLAY = 110
FONT_TITLE = 85
FONT_BODY = 60
FONT_SMALL = 40

# ASCII Cow mascot
COW_ASCII = [
    "  ((____))",
    "  [ x x ]",
    "   \\   /",
    "   ('  ')",
    "   (U)"
]

# GitHub link
GITHUB_LINK = "github.com/drewbeyersdorf/agent-improvement-techniques"


def get_font(size):
    """Get elegant serif font"""
    try:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Didot.ttc", size)
    except:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", size)
        except:
            try:
                return ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", size)
            except:
                return ImageFont.load_default()


def get_mono_font(size):
    """Get monospace font for ASCII cow"""
    try:
        return ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", size)
    except:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", size)
        except:
            return ImageFont.load_default()


def draw_text_centered(draw, text, y_position, font, color, img_width):
    """Draw text centered horizontally"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img_width - text_width) // 2
    draw.text((x, y_position), text, font=font, fill=color)
    return bbox[3] - bbox[1]


def draw_cow_mascot(draw, x_pos, y_pos, color, size=30):
    """Draw the ASCII cow mascot"""
    font = get_mono_font(size)
    current_y = y_pos

    for line in COW_ASCII:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        line_x = x_pos - (text_width // 2)
        draw.text((line_x, current_y), line, font=font, fill=color)
        current_y += bbox[3] - bbox[1] + 5


def draw_watermark(draw, img_width, img_height):
    """Draw drewbeyersdorf watermark in corner"""
    font = get_font(FONT_SMALL)
    text = "drewbeyersdorf"

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = img_width - text_width - 40
    y = img_height - 80

    draw.text((x, y), text, font=font, fill=COLORS['gray_light'])


def scene_1_intro(frame_num, total_frames):
    """Scene 1: Introduction (0-5s)"""
    # White background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 250, COLORS['black'], size=35)

    # Title
    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "TCREI", 600, font_display, COLORS['black'], WIDTH)

    # Subtitle
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Perfect AI Alignment", 730, font_body, COLORS['gray_dark'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_2_T(frame_num, total_frames):
    """Scene 2: T - Task (5-10s)"""
    # Black background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['white'], size=40)

    # Letter T
    font_display = get_font(150)
    draw_text_centered(draw, "T", 500, font_display, COLORS['white'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Task", 700, font_title, COLORS['white'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "What exactly", 820, font_body, COLORS['gray_light'], WIDTH)
    draw_text_centered(draw, "do you need?", 900, font_body, COLORS['gray_light'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_3_C(frame_num, total_frames):
    """Scene 3: C - Context (10-15s)"""
    # White background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['black'], size=40)

    # Letter C
    font_display = get_font(150)
    draw_text_centered(draw, "C", 500, font_display, COLORS['black'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Context", 700, font_title, COLORS['black'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Why is this", 820, font_body, COLORS['gray_dark'], WIDTH)
    draw_text_centered(draw, "necessary?", 900, font_body, COLORS['gray_dark'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_4_R(frame_num, total_frames):
    """Scene 4: R - Reference (15-20s)"""
    # Black background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['white'], size=40)

    # Letter R
    font_display = get_font(150)
    draw_text_centered(draw, "R", 500, font_display, COLORS['white'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Reference", 700, font_title, COLORS['white'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Any existing", 820, font_body, COLORS['gray_light'], WIDTH)
    draw_text_centered(draw, "examples?", 900, font_body, COLORS['gray_light'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_5_E(frame_num, total_frames):
    """Scene 5: E - Evaluation (20-25s)"""
    # White background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['black'], size=40)

    # Letter E
    font_display = get_font(150)
    draw_text_centered(draw, "E", 500, font_display, COLORS['black'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Evaluation", 700, font_title, COLORS['black'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "How to measure", 820, font_body, COLORS['gray_dark'], WIDTH)
    draw_text_centered(draw, "success?", 900, font_body, COLORS['gray_dark'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_6_I(frame_num, total_frames):
    """Scene 6: I - Iteration (25-28s) - CORRECTED"""
    # Black background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['white'], size=40)

    # Letter I
    font_display = get_font(150)
    draw_text_centered(draw, "I", 500, font_display, COLORS['white'], WIDTH)

    # Word - CORRECTED TO ITERATION
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Iteration", 700, font_title, COLORS['white'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Refine through", 820, font_body, COLORS['gray_light'], WIDTH)
    draw_text_centered(draw, "feedback loops", 900, font_body, COLORS['gray_light'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_7_outro(frame_num, total_frames):
    """Scene 7: Outro with GitHub link (28-30s)"""
    # White background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 300, COLORS['black'], size=45)

    # TCREI
    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "TCREI", 650, font_display, COLORS['black'], WIDTH)

    # Tagline
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Perfect Alignment", 770, font_body, COLORS['gray_dark'], WIDTH)

    # GitHub link - ADDED
    font_small = get_font(FONT_SMALL)
    draw_text_centered(draw, "github.com/drewbeyersdorf/", 1000, font_small, COLORS['black'], WIDTH)
    draw_text_centered(draw, "agent-improvement-techniques", 1055, font_small, COLORS['black'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def generate_all_frames():
    """Generate all frames"""
    print("\n" + "="*70)
    print("TCREI SHORT - BLACK & WHITE CLASSICAL STYLE")
    print("Pure B&W • I = Iteration • Classical Music")
    print("="*70 + "\n")

    scenes = [
        ("Scene 1: Introduction", scene_1_intro, 0, 5, 150),
        ("Scene 2: T - Task", scene_2_T, 5, 10, 150),
        ("Scene 3: C - Context", scene_3_C, 10, 15, 150),
        ("Scene 4: R - Reference", scene_4_R, 15, 20, 150),
        ("Scene 5: E - Evaluation", scene_5_E, 20, 25, 150),
        ("Scene 6: I - Iteration", scene_6_I, 25, 28, 90),
        ("Scene 7: Outro + GitHub", scene_7_outro, 28, 30, 60),
    ]

    frame_counter = 0

    for scene_name, scene_func, start_time, end_time, num_frames in scenes:
        print(f"🎬 {scene_name} ({start_time}-{end_time}s, {num_frames} frames)...")

        for i in range(num_frames):
            img = scene_func(i, num_frames)
            frame_path = OUTPUT_DIR / f"frame_{frame_counter:04d}.png"
            img.save(frame_path)
            frame_counter += 1

            if (i + 1) % 50 == 0 or i == num_frames - 1:
                print(f"  {i+1}/{num_frames} frames...", end="")

        print(f" ✅")

    print("\n" + "="*70)
    print(f"✅ ALL FRAMES GENERATED! ({frame_counter} total)")
    print("="*70 + "\n")

    return frame_counter


def combine_frames_to_video():
    """Combine frames into video (without audio first)"""
    print("🎬 Combining frames into video...\n")

    output_path = "../../output/tcrei_short/TCREI_BW_SILENT.mp4"

    cmd = [
        'ffmpeg', '-y',
        '-framerate', str(FPS),
        '-i', str(OUTPUT_DIR / 'frame_%04d.png'),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'slow',
        '-crf', '18',
        output_path
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Silent video created: {output_path}\n")
        return output_path

    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def download_classical_music():
    """Download royalty-free classical music"""
    print("🎵 Downloading classical music (royalty-free)...\n")

    music_url = "https://www.bensound.com/bensound-music/bensound-pianomoment.mp3"
    output_path = "../../output/tcrei_short/classical_music.mp3"

    cmd = [
        'curl', '-L',
        '-o', output_path,
        music_url
    ]

    try:
        print(f"Downloading from bensound.com (royalty-free classical)...")
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Music downloaded: {output_path}\n")
        return output_path

    except subprocess.CalledProcessError as e:
        print(f"⚠️  Could not download music automatically.")
        print(f"\nManual option: Download classical music and save as:")
        print(f"  {output_path}")
        print(f"\nFree classical music sources:")
        print(f"  - https://www.bensound.com (royalty-free)")
        print(f"  - https://incompetech.com (Kevin MacLeod)")
        print(f"  - YouTube Audio Library (search 'classical piano')")
        return None


def add_music_to_video(video_path, music_path):
    """Add classical music to video"""
    print("🎵 Adding classical music to video...\n")

    output_path = "../../output/tcrei_short/TCREI_BW_FINAL.mp4"

    cmd = [
        'ffmpeg', '-y',
        '-i', video_path,
        '-i', music_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        output_path
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("\n" + "="*70)
        print("✅ FINAL VIDEO WITH CLASSICAL MUSIC CREATED!")
        print(f"📁 Output: {output_path}")
        print(f"📐 Format: {WIDTH}x{HEIGHT} (9:16 vertical)")
        print(f"🎞️  FPS: {FPS}")
        print(f"⏱️  Duration: 30 seconds")
        print("🎨 Style: BLACK & WHITE")
        print("🎵 Music: Classical")
        print("🐄 Mascot: ASCII Cow")
        print("✍️  Watermark: drewbeyersdorf")
        print(f"🔗 GitHub: {GITHUB_LINK}")
        print("📝 I = Iteration (corrected)")
        print("\n" + "="*70)
        print("\n🎉 BLACK & WHITE TCREI SHORT COMPLETE!")
        print("="*70 + "\n")

        return output_path

    except subprocess.CalledProcessError as e:
        print(f"❌ Error adding music: {e}")
        print(f"\n✅ Silent video is available at: {video_path}")
        print("You can add music manually using a video editor.")
        return video_path


def main():
    """Main execution"""
    print("\n🎹 BLACK & WHITE TCREI SHORT GENERATOR")
    print("Classical • Elegant • Pure B&W\n")

    # Generate frames
    generate_all_frames()

    # Combine into silent video
    silent_video = combine_frames_to_video()

    # Try to download and add classical music
    music_path = download_classical_music()

    if music_path and Path(music_path).exists():
        # Add music to video
        final_video = add_music_to_video(silent_video, music_path)
        print(f"✨ Open the final video: {final_video}")
    else:
        print(f"\n✅ Silent B&W video ready: {silent_video}")
        print("\nTo add classical music:")
        print("1. Download royalty-free classical music")
        print(f"2. Save as: tcrei_short/classical_music.mp3")
        print("3. Run this script again to combine")


if __name__ == "__main__":
    main()
