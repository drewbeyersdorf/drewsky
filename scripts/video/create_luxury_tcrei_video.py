#!/usr/bin/env python3
"""
TCREI Short - Luxury European Fashion House Style
Elegant, minimalist, high-end aesthetic with ASCII cow mascot
British tech wealth meets luxury design

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
OUTPUT_DIR = Path("../../output/tcrei_short/luxury_frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

# LUXURY COLOR PALETTE - European Fashion House
COLORS = {
    'cream': (250, 248, 245),        # Elegant cream background
    'charcoal': (45, 45, 45),        # Sophisticated dark gray
    'gold': (212, 175, 55),          # Luxury gold accent
    'sage': (169, 176, 148),         # Muted sage green
    'navy': (25, 40, 60),            # Deep navy blue
    'white': (255, 255, 255),        # Pure white
    'black': (0, 0, 0),              # Pure black
    'warm_gray': (120, 115, 110),    # Warm neutral
}

# Elegant serif fonts for luxury feel
FONT_DISPLAY = 100   # Large elegant display
FONT_TITLE = 80      # Section titles
FONT_BODY = 55       # Body text
FONT_SMALL = 35      # Small details

# ASCII Cow mascot (from the image)
COW_ASCII = [
    "  ((____))",
    "  [ x x ]",
    "   \\   /",
    "   ('  ')",
    "   (U)"
]


def get_font(size, bold=False):
    """Get elegant serif font for luxury aesthetic"""
    try:
        # Try Didot (classic luxury serif on macOS)
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Didot.ttc", size)
    except:
        try:
            # Fallback to Times New Roman (elegant serif)
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", size)
        except:
            try:
                # Fallback to Georgia
                return ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", size)
            except:
                # Last resort
                return ImageFont.load_default()


def get_mono_font(size):
    """Get monospace font for ASCII cow"""
    try:
        # Monaco for clean ASCII rendering
        return ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", size)
    except:
        try:
            # Fallback to Courier
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", size)
        except:
            return ImageFont.load_default()


def draw_text_centered(draw, text, y_position, font, color, img_width):
    """Draw text centered horizontally"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img_width - text_width) // 2
    draw.text((x, y_position), text, font=font, fill=color)
    return bbox[3] - bbox[1]  # Return text height


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
    """Draw drewbeyersdorf watermark in bottom right corner"""
    font = get_font(FONT_SMALL)
    text = "drewbeyersdorf"

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = img_width - text_width - 40
    y = img_height - 80

    # Draw with subtle gold color
    draw.text((x, y), text, font=font, fill=COLORS['gold'])


def create_luxury_gradient(width, height, color1, color2):
    """Create subtle luxury gradient"""
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        for x in range(width):
            pixels[x, y] = (r, g, b)

    return img


def scene_1_intro(frame_num, total_frames):
    """Scene 1: Elegant Introduction (0-5s, 150 frames)"""
    # Cream to warm gradient
    img = create_luxury_gradient(WIDTH, HEIGHT, COLORS['cream'], COLORS['warm_gray'])
    draw = ImageDraw.Draw(img)

    # Cow mascot at top
    draw_cow_mascot(draw, WIDTH // 2, 250, COLORS['charcoal'], size=35)

    # Elegant title
    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "TCREI", 600, font_display, COLORS['charcoal'], WIDTH)

    # Subtitle
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Perfect AI Alignment", 730, font_body, COLORS['gold'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_2_T(frame_num, total_frames):
    """Scene 2: T - Task (5-10s, 150 frames)"""
    # Navy background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['navy'])
    draw = ImageDraw.Draw(img)

    # Cow mascot talking
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['gold'], size=40)

    # Letter T
    font_display = get_font(140)
    draw_text_centered(draw, "T", 500, font_display, COLORS['gold'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Task", 680, font_title, COLORS['cream'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "What exactly", 800, font_body, COLORS['sage'], WIDTH)
    draw_text_centered(draw, "do you need?", 870, font_body, COLORS['sage'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_3_C(frame_num, total_frames):
    """Scene 3: C - Context (10-15s, 150 frames)"""
    # Cream background
    img = create_luxury_gradient(WIDTH, HEIGHT, COLORS['cream'], (240, 238, 235))
    draw = ImageDraw.Draw(img)

    # Cow mascot talking
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['charcoal'], size=40)

    # Letter C
    font_display = get_font(140)
    draw_text_centered(draw, "C", 500, font_display, COLORS['charcoal'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Context", 680, font_title, COLORS['navy'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Why is this", 800, font_body, COLORS['warm_gray'], WIDTH)
    draw_text_centered(draw, "necessary?", 870, font_body, COLORS['warm_gray'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_4_R(frame_num, total_frames):
    """Scene 4: R - Reference (15-20s, 150 frames)"""
    # Navy background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['navy'])
    draw = ImageDraw.Draw(img)

    # Cow mascot talking
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['gold'], size=40)

    # Letter R
    font_display = get_font(140)
    draw_text_centered(draw, "R", 500, font_display, COLORS['gold'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Reference", 680, font_title, COLORS['cream'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Any existing", 800, font_body, COLORS['sage'], WIDTH)
    draw_text_centered(draw, "examples?", 870, font_body, COLORS['sage'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_5_E(frame_num, total_frames):
    """Scene 5: E - Evaluation (20-25s, 150 frames)"""
    # Cream background
    img = create_luxury_gradient(WIDTH, HEIGHT, COLORS['cream'], (240, 238, 235))
    draw = ImageDraw.Draw(img)

    # Cow mascot talking
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['charcoal'], size=40)

    # Letter E
    font_display = get_font(140)
    draw_text_centered(draw, "E", 500, font_display, COLORS['charcoal'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Evaluation", 680, font_title, COLORS['navy'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "How to measure", 800, font_body, COLORS['warm_gray'], WIDTH)
    draw_text_centered(draw, "success?", 870, font_body, COLORS['warm_gray'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_6_I(frame_num, total_frames):
    """Scene 6: I - Input (25-28s, 90 frames)"""
    # Navy background
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['navy'])
    draw = ImageDraw.Draw(img)

    # Cow mascot talking
    draw_cow_mascot(draw, WIDTH // 2, 200, COLORS['gold'], size=40)

    # Letter I
    font_display = get_font(140)
    draw_text_centered(draw, "I", 500, font_display, COLORS['gold'], WIDTH)

    # Word
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Input", 680, font_title, COLORS['cream'], WIDTH)

    # Description
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Read the schema", 800, font_body, COLORS['sage'], WIDTH)
    draw_text_centered(draw, "first?", 870, font_body, COLORS['sage'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def scene_7_outro(frame_num, total_frames):
    """Scene 7: Elegant Outro (28-30s, 60 frames)"""
    # Luxury gradient
    img = create_luxury_gradient(WIDTH, HEIGHT, COLORS['cream'], COLORS['warm_gray'])
    draw = ImageDraw.Draw(img)

    # Cow mascot
    draw_cow_mascot(draw, WIDTH // 2, 300, COLORS['charcoal'], size=45)

    # TCREI
    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "TCREI", 650, font_display, COLORS['charcoal'], WIDTH)

    # Tagline
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Perfect Alignment", 770, font_body, COLORS['gold'], WIDTH)

    # CTA
    font_small = get_font(FONT_SMALL + 10)
    draw_text_centered(draw, "drewbeyersdorf", 1000, font_small, COLORS['navy'], WIDTH)

    # Watermark
    draw_watermark(draw, WIDTH, HEIGHT)

    return img


def generate_all_frames():
    """Generate all frames for the luxury video"""
    print("\n" + "="*70)
    print("TCREI SHORT - LUXURY EUROPEAN FASHION HOUSE STYLE")
    print("Elegant • Minimalist • British Tech Wealth")
    print("="*70 + "\n")

    scenes = [
        ("Scene 1: Introduction", scene_1_intro, 0, 5, 150),
        ("Scene 2: T - Task", scene_2_T, 5, 10, 150),
        ("Scene 3: C - Context", scene_3_C, 10, 15, 150),
        ("Scene 4: R - Reference", scene_4_R, 15, 20, 150),
        ("Scene 5: E - Evaluation", scene_5_E, 20, 25, 150),
        ("Scene 6: I - Input", scene_6_I, 25, 28, 90),
        ("Scene 7: Outro", scene_7_outro, 28, 30, 60),
    ]

    frame_counter = 0

    for scene_name, scene_func, start_time, end_time, num_frames in scenes:
        print(f"🎨 Generating {scene_name} ({start_time}-{end_time}s, {num_frames} frames)...")

        for i in range(num_frames):
            # Generate frame
            img = scene_func(i, num_frames)

            # Save frame
            frame_path = OUTPUT_DIR / f"frame_{frame_counter:04d}.png"
            img.save(frame_path)

            frame_counter += 1

            # Progress indicator
            if (i + 1) % 50 == 0 or i == num_frames - 1:
                print(f"  {i+1}/{num_frames} frames...", end="")

        print(f" ✅ Complete!")

    print("\n" + "="*70)
    print("✅ ALL FRAMES GENERATED!")
    print(f"📁 Location: {OUTPUT_DIR}")
    print(f"📊 Total frames: {frame_counter}")
    print("="*70 + "\n")

    return frame_counter


def combine_frames_to_video():
    """Use ffmpeg to combine frames into luxury video"""
    print("🎬 Combining frames into video...\n")

    output_path = "../../output/tcrei_short/TCREI_LUXURY.mp4"

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

    print(f"Running ffmpeg...\n")

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("\n" + "="*70)
        print("✅ LUXURY VIDEO CREATED!")
        print(f"📁 Output: {output_path}")
        print(f"📐 Format: {WIDTH}x{HEIGHT} (9:16 vertical)")
        print(f"🎞️  FPS: {FPS}")
        print(f"⏱️  Duration: 30 seconds")
        print("🎨 Style: EUROPEAN FASHION HOUSE")
        print("🐄 Mascot: ASCII Cow throughout")
        print("✍️  Watermark: drewbeyersdorf")
        print("\n" + "="*70)
        print("\n🎉 LUXURY TCREI SHORT COMPLETE!")
        print("="*70)
        print("\n✨ Elegant • Sophisticated • British Tech Wealth")
        print("="*70 + "\n")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error combining frames: {e}")
        print("Make sure ffmpeg is installed: brew install ffmpeg")
        sys.exit(1)


def main():
    """Main execution"""
    print("\n💎 LUXURY TCREI SHORT GENERATOR")
    print("European Fashion House Aesthetic\n")

    # Generate frames
    total_frames = generate_all_frames()

    # Combine into video
    combine_frames_to_video()


if __name__ == "__main__":
    main()
