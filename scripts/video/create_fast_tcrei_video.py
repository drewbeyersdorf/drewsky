#!/usr/bin/env python3
"""
TCREI Short - Fast 15-Second B&W Classical
Pure B&W, R = Resources, longer descriptive text
Classical music, 15 seconds total

Dependencies:
pip install pillow numpy
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import subprocess
import sys

# Configuration
OUTPUT_DIR = Path("../../output/tcrei_short/fast_frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

# PURE BLACK & WHITE
COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray_light': (220, 220, 220),
    'gray_dark': (40, 40, 40),
}

# Fonts
FONT_DISPLAY = 110
FONT_TITLE = 85
FONT_BODY = 55
FONT_SMALL = 45

# ASCII Cow
COW_ASCII = [
    "  ((____))",
    "  [ x x ]",
    "   \\   /",
    "   ('  ')",
    "   (U)"
]

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
    """Get monospace font"""
    try:
        return ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", size)
    except:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", size)
        except:
            return ImageFont.load_default()


def draw_text_centered(draw, text, y_position, font, color, img_width):
    """Draw centered text"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img_width - text_width) // 2
    draw.text((x, y_position), text, font=font, fill=color)


def draw_multiline_centered(draw, lines, start_y, font, color, img_width, spacing=15):
    """Draw multiple lines centered"""
    current_y = start_y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (img_width - text_width) // 2
        draw.text((x, current_y), line, font=font, fill=color)
        current_y += text_height + spacing


def draw_cow_mascot(draw, x_pos, y_pos, color, size=30):
    """Draw ASCII cow"""
    font = get_mono_font(size)
    current_y = y_pos
    for line in COW_ASCII:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        line_x = x_pos - (text_width // 2)
        draw.text((line_x, current_y), line, font=font, fill=color)
        current_y += bbox[3] - bbox[1] + 5


def draw_watermark(draw, img_width, img_height):
    """Draw watermark"""
    font = get_font(FONT_SMALL - 5)
    text = "drewbeyersdorf"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = img_width - text_width - 40
    y = img_height - 80
    draw.text((x, y), text, font=font, fill=COLORS['gray_light'])


def scene_1_intro(frame_num, total_frames):
    """Scene 1: Quick Intro (0-2s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 300, COLORS['black'], size=40)

    font_display = get_font(130)
    draw_text_centered(draw, "TCREI", 700, font_display, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Perfect AI Alignment", 850, font_body, COLORS['gray_dark'], WIDTH)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_2_T(frame_num, total_frames):
    """Scene 2: T - Task (2-4s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "T", 450, font_display, COLORS['white'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Task", 620, font_title, COLORS['white'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Define the specific goal,",
        "desired outcome,",
        "and success criteria"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_light'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_3_C(frame_num, total_frames):
    """Scene 3: C - Context (4-6s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['black'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "C", 450, font_display, COLORS['black'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Context", 620, font_title, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Share why this matters,",
        "relevant background,",
        "and business constraints"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_dark'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_4_R(frame_num, total_frames):
    """Scene 4: R - Resources (6-8s) - CORRECTED"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "R", 450, font_display, COLORS['white'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Resources", 620, font_title, COLORS['white'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Provide code examples,",
        "documentation links,",
        "and existing patterns"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_light'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_5_E(frame_num, total_frames):
    """Scene 5: E - Evaluation (8-10s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['black'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "E", 450, font_display, COLORS['black'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Evaluation", 620, font_title, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Define how to measure",
        "success with specific",
        "metrics and tests"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_dark'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_6_I(frame_num, total_frames):
    """Scene 6: I - Iteration (10-12s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "I", 450, font_display, COLORS['white'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Iteration", 620, font_title, COLORS['white'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Refine through cycles,",
        "incorporate feedback,",
        "and continuously improve"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_light'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_7_outro(frame_num, total_frames):
    """Scene 7: Outro (12-15s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 250, COLORS['black'], size=45)

    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "TCREI", 600, font_display, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Perfect Alignment", 720, font_body, COLORS['gray_dark'], WIDTH)

    font_small = get_font(FONT_SMALL)
    draw_text_centered(draw, "github.com/drewbeyersdorf/", 950, font_small, COLORS['black'], WIDTH)
    draw_text_centered(draw, "agent-improvement-techniques", 1010, font_small, COLORS['black'], WIDTH)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def generate_all_frames():
    """Generate all frames - 15 seconds total"""
    print("\n" + "="*70)
    print("TCREI SHORT - FAST 15-SECOND B&W")
    print("R = Resources • Longer Descriptive Text")
    print("="*70 + "\n")

    scenes = [
        ("Scene 1: Intro", scene_1_intro, 0, 2, 60),
        ("Scene 2: T - Task", scene_2_T, 2, 4, 60),
        ("Scene 3: C - Context", scene_3_C, 4, 6, 60),
        ("Scene 4: R - Resources", scene_4_R, 6, 8, 60),
        ("Scene 5: E - Evaluation", scene_5_E, 8, 10, 60),
        ("Scene 6: I - Iteration", scene_6_I, 10, 12, 60),
        ("Scene 7: Outro", scene_7_outro, 12, 15, 90),
    ]

    frame_counter = 0

    for scene_name, scene_func, start_time, end_time, num_frames in scenes:
        print(f"🎬 {scene_name} ({start_time}-{end_time}s, {num_frames} frames)...")

        for i in range(num_frames):
            img = scene_func(i, num_frames)
            frame_path = OUTPUT_DIR / f"frame_{frame_counter:04d}.png"
            img.save(frame_path)
            frame_counter += 1

            if (i + 1) % 30 == 0 or i == num_frames - 1:
                print(f"  {i+1}/{num_frames}...", end="")

        print(f" ✅")

    print("\n" + "="*70)
    print(f"✅ ALL FRAMES GENERATED! ({frame_counter} total)")
    print("="*70 + "\n")

    return frame_counter


def combine_frames_to_video():
    """Combine frames into video"""
    print("🎬 Creating silent video...\n")

    output_path = "../../output/tcrei_short/TCREI_FAST_SILENT.mp4"

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


def add_music_to_video(video_path, music_path):
    """Add classical music to video"""
    print("🎵 Adding classical music...\n")

    output_path = "../../output/tcrei_short/TCREI_FAST_FINAL.mp4"

    # Trim music to 15 seconds
    cmd = [
        'ffmpeg', '-y',
        '-i', video_path,
        '-i', music_path,
        '-t', '15',
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        output_path
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("\n" + "="*70)
        print("✅ FINAL 15-SECOND VIDEO COMPLETE!")
        print(f"📁 Output: {output_path}")
        print(f"📐 Format: {WIDTH}x{HEIGHT} (9:16 vertical)")
        print(f"🎞️  FPS: {FPS}")
        print(f"⏱️  Duration: 15 seconds (FAST!)")
        print("🎨 Style: BLACK & WHITE")
        print("🎵 Music: Classical piano")
        print("🐄 Mascot: ASCII Cow")
        print("✍️  Watermark: drewbeyersdorf")
        print(f"🔗 GitHub: {GITHUB_LINK}")
        print("📝 R = Resources (corrected)")
        print("📖 Longer descriptive text for each letter")
        print("\n" + "="*70)
        print("\n🎉 FAST B&W TCREI SHORT COMPLETE!")
        print("="*70 + "\n")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ Error adding music: {e}")
        print(f"\n✅ Silent video available: {video_path}")
        return video_path


def main():
    """Main execution"""
    print("\n⚡ FAST 15-SECOND TCREI GENERATOR")
    print("B&W • Classical • Longer Text\n")

    # Generate frames
    generate_all_frames()

    # Create silent video
    silent_video = combine_frames_to_video()

    # Check if music exists from previous run
    music_path = "../../output/tcrei_short/classical_music.mp3"

    if Path(music_path).exists():
        print(f"✅ Using existing classical music: {music_path}\n")
        final_video = add_music_to_video(silent_video, music_path)
        print(f"✨ Open final video: {final_video}")
    else:
        print(f"⚠️  No music file found at: {music_path}")
        print(f"✅ Silent video ready: {silent_video}")
        print("\nTo add music:")
        print("1. Download royalty-free classical music")
        print(f"2. Save as: {music_path}")
        print("3. Run script again")


if __name__ == "__main__":
    main()
