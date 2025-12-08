#!/usr/bin/env python3
"""
TCREI Short - Clean, Readable Video Generator
Human-friendly with consistent colors and large readable text

Dependencies:
pip install pillow numpy

Generates frames, then uses ffmpeg to combine into video
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import subprocess
import sys

# Configuration
OUTPUT_DIR = Path("../../output/tcrei_short/frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30  # Smooth modern framerate

# CLEAN COLOR PALETTE (Consistent, high contrast)
COLORS = {
    'red': (220, 53, 69),        # Bootstrap red - for warnings
    'blue': (13, 110, 253),      # Bootstrap blue - for trust
    'green': (25, 135, 84),      # Bootstrap green - for success
    'dark': (33, 37, 41),        # Dark background
    'white': (255, 255, 255),    # White text
    'light_gray': (248, 249, 250),  # Light backgrounds
}

# Font sizes - LARGE for readability
FONT_HUGE = 120
FONT_LARGE = 90
FONT_MEDIUM = 70
FONT_SMALL = 50


def get_font(size):
    """Get system font that's readable"""
    try:
        # Try to use Arial Bold (available on macOS)
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", size)
    except:
        try:
            # Fallback to Helvetica
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
        except:
            # Last resort - default font
            return ImageFont.load_default()


def create_solid_background(width, height, color):
    """Create solid color background"""
    img = Image.new('RGB', (width, height), color)
    return img


def draw_text_centered(draw, text, y_position, font, color, img_width):
    """Draw text centered horizontally"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img_width - text_width) // 2
    draw.text((x, y_position), text, font=font, fill=color)


def draw_multiline_text_centered(draw, text, y_position, font, color, img_width, line_spacing=20):
    """Draw multiline text centered"""
    lines = text.split('\n')
    current_y = y_position
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (img_width - text_width) // 2
        draw.text((x, current_y), line, font=font, fill=color)
        current_y += bbox[3] - bbox[1] + line_spacing


def scene_1_hook(frame_num, total_frames):
    """Scene 1: STOP! - Red warning (0-3s, 90 frames)"""
    # Solid red background - consistent throughout
    img = create_solid_background(WIDTH, HEIGHT, COLORS['red'])
    draw = ImageDraw.Draw(img)

    # Large STOP text
    font_huge = get_font(FONT_HUGE)
    draw_text_centered(draw, "STOP!", 400, font_huge, COLORS['white'], WIDTH)

    # Subtitle
    font_large = get_font(FONT_LARGE)
    draw_text_centered(draw, "letting AI guess", 600, font_large, COLORS['white'], WIDTH)
    draw_text_centered(draw, "what you want!", 720, font_large, COLORS['white'], WIDTH)

    return img


def scene_2_problem(frame_num, total_frames):
    """Scene 2: Problem (3-8s, 150 frames)"""
    # Dark background - consistent
    img = create_solid_background(WIDTH, HEIGHT, COLORS['dark'])
    draw = ImageDraw.Draw(img)

    # Speech bubble text
    font_large = get_font(FONT_LARGE)
    draw_text_centered(draw, '"Add auth"', 500, font_large, COLORS['white'], WIDTH)

    # Problem statement
    font_medium = get_font(FONT_MEDIUM)
    draw_text_centered(draw, "AI builds the", 900, font_medium, COLORS['white'], WIDTH)
    draw_text_centered(draw, "WRONG thing ❌", 1000, font_medium, COLORS['red'], WIDTH)

    return img


def scene_3_solution(frame_num, total_frames):
    """Scene 3: TCREI Logo (8-11s, 90 frames)"""
    # Blue background - consistent
    img = create_solid_background(WIDTH, HEIGHT, COLORS['blue'])
    draw = ImageDraw.Draw(img)

    # TCREI logo
    font_huge = get_font(160)
    draw_text_centered(draw, "TCREI", 700, font_huge, COLORS['white'], WIDTH)

    # Tagline
    font_medium = get_font(FONT_MEDIUM)
    draw_text_centered(draw, "Perfect AI Alignment ✨", 950, font_medium, COLORS['white'], WIDTH)

    return img


def scene_4_breakdown(frame_num, total_frames):
    """Scene 4: TCREI Breakdown (11-25s, 420 frames)"""
    # Dark background - consistent
    img = create_solid_background(WIDTH, HEIGHT, COLORS['dark'])
    draw = ImageDraw.Draw(img)

    font_large = get_font(FONT_LARGE)
    font_medium = get_font(FONT_MEDIUM)
    font_small = get_font(FONT_SMALL)

    # Title
    draw_text_centered(draw, "TCREI Framework:", 150, font_large, COLORS['white'], WIDTH)

    # Show items progressively
    items = [
        ("T 📋", "Task", "What exactly?", 300),
        ("C 🎯", "Context", "Why needed?", 540),
        ("R 🔍", "Reference", "Any examples?", 780),
        ("E ✅", "Evaluation", "Measure success?", 1020),
        ("I 📊", "Input", "Read schema first?", 1260),
    ]

    # Determine how many items to show based on frame
    progress = frame_num / total_frames
    items_to_show = min(len(items), int(progress * len(items)) + 1)

    for i in range(items_to_show):
        letter, word, question, y_pos = items[i]
        draw_text_centered(draw, letter, y_pos, font_large, COLORS['blue'], WIDTH)
        draw_text_centered(draw, word, y_pos + 80, font_medium, COLORS['white'], WIDTH)
        draw_text_centered(draw, question, y_pos + 160, font_small, COLORS['light_gray'], WIDTH)

    return img


def scene_5_result(frame_num, total_frames):
    """Scene 5: Before/After (25-28s, 90 frames)"""
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    # Top half - RED (before)
    draw.rectangle([(0, 0), (WIDTH, HEIGHT//2)], fill=COLORS['red'])

    # Bottom half - GREEN (after)
    draw.rectangle([(0, HEIGHT//2), (WIDTH, HEIGHT)], fill=COLORS['green'])

    font_large = get_font(FONT_LARGE)
    font_medium = get_font(FONT_MEDIUM)

    # Before text
    draw_text_centered(draw, "BEFORE ❌", 350, font_large, COLORS['white'], WIDTH)
    draw_text_centered(draw, "Chaotic", 480, font_medium, COLORS['white'], WIDTH)

    # After text
    draw_text_centered(draw, "AFTER ✅", 1200, font_large, COLORS['white'], WIDTH)
    draw_text_centered(draw, "Perfect Alignment!", 1330, font_medium, COLORS['white'], WIDTH)

    return img


def scene_6_cta(frame_num, total_frames):
    """Scene 6: Call to Action (28-30s, 60 frames)"""
    # Blue background - consistent
    img = create_solid_background(WIDTH, HEIGHT, COLORS['blue'])
    draw = ImageDraw.Draw(img)

    font_huge = get_font(FONT_HUGE)
    font_large = get_font(FONT_LARGE)

    # Main CTA
    draw_text_centered(draw, "RPI Framework", 700, font_huge, COLORS['white'], WIDTH)

    # Link
    draw_text_centered(draw, "Link in bio ⬇️", 900, font_large, COLORS['white'], WIDTH)

    return img


def generate_all_frames():
    """Generate all frames for the video"""
    print("\n" + "="*70)
    print("TCREI SHORT - CLEAN & READABLE VERSION")
    print("Large text, consistent colors, human-friendly")
    print("="*70 + "\n")

    scenes = [
        ("Scene 1: STOP Hook", scene_1_hook, 0, 3, 90),
        ("Scene 2: Problem", scene_2_problem, 3, 8, 150),
        ("Scene 3: TCREI Logo", scene_3_solution, 8, 11, 90),
        ("Scene 4: Breakdown", scene_4_breakdown, 11, 25, 420),
        ("Scene 5: Before/After", scene_5_result, 25, 28, 90),
        ("Scene 6: Call to Action", scene_6_cta, 28, 30, 60),
    ]

    frame_counter = 0

    for scene_name, scene_func, start_time, end_time, num_frames in scenes:
        print(f"🎬 Generating {scene_name} ({start_time}-{end_time}s, {num_frames} frames)...")

        for i in range(num_frames):
            # Generate frame
            img = scene_func(i, num_frames)

            # Save frame
            frame_path = OUTPUT_DIR / f"frame_{frame_counter:04d}.png"
            img.save(frame_path)

            frame_counter += 1

            # Progress indicator
            if (i + 1) % 30 == 0 or i == num_frames - 1:
                print(f"  Generated {i+1}/{num_frames} frames...", end="")

        print(f"  ✅ {scene_name} complete! ({num_frames} frames)")

    print("\n" + "="*70)
    print("✅ ALL FRAMES GENERATED!")
    print(f"📁 Location: {OUTPUT_DIR}")
    print(f"📊 Total frames: {frame_counter}")
    print("="*70 + "\n")

    return frame_counter


def combine_frames_to_video():
    """Use ffmpeg to combine frames into video"""
    print("🎥 Combining frames into video...\n")

    output_path = "../../output/tcrei_short/TCREI_SHORT_CLEAN.mp4"

    # ffmpeg command
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

    print(f"Running: {' '.join(cmd)}\n")

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("\n" + "="*70)
        print("✅ VIDEO CREATED SUCCESSFULLY!")
        print(f"📁 Output: {output_path}")
        print(f"📐 Format: {WIDTH}x{HEIGHT} (9:16 vertical)")
        print(f"🎞️  FPS: {FPS}")
        print(f"⏱️  Duration: ~30 seconds")
        print("🎨 Style: CLEAN & READABLE")
        print("\n" + "="*70)
        print("\n🎉 CLEAN TCREI SHORT COMPLETE!")
        print("="*70)
        print("\n📤 Next steps:")
        print("1. Review the video")
        print("2. Add voice narration (optional)")
        print("3. Upload to YouTube Shorts, TikTok, Instagram Reels")
        print("\n✨ Large text, consistent colors, easy to read! 📱")
        print("="*70 + "\n")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error combining frames: {e}")
        print("Make sure ffmpeg is installed: brew install ffmpeg")
        sys.exit(1)


def main():
    """Main execution"""
    print("\n🎬 CLEAN TCREI SHORT GENERATOR")
    print("Readable text, consistent colors, human-friendly\n")

    # Generate frames
    total_frames = generate_all_frames()

    # Combine into video
    combine_frames_to_video()


if __name__ == "__main__":
    main()
