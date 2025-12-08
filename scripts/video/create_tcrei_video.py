#!/usr/bin/env python3
"""
TCREI Short - Fully Automated Video Generator
Creates the complete 30-second vertical video using MoviePy

Dependencies:
pip install moviepy pillow numpy

This script generates the ENTIRE video - no manual work needed!
"""

from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
from pathlib import Path

# Configuration
OUTPUT_DIR = Path("../../output/tcrei_short/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

# Colors (from AI recommendations)
RED = (255, 65, 54)
BLUE = (74, 144, 226)
GREEN = (80, 200, 120)
DARK = (34, 34, 34)
WHITE = (255, 255, 255)
GRAY = (204, 204, 204)


def create_text_clip(text, fontsize, color, position, duration, font_path=None):
    """Create a text clip with specified properties"""
    return TextClip(
        text,
        fontsize=fontsize,
        color=color,
        font=font_path or 'Arial-Bold',
        size=(WIDTH-100, None),
        method='caption',
        align='center'
    ).set_position(position).set_duration(duration)


def create_gradient_background(color1, color2, width, height):
    """Create a gradient background image"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return np.array(img)


def scene_1_hook():
    """Scene 1: STOP - Hook (0-3s)"""
    print("Creating Scene 1: Hook...")

    # Red gradient background
    bg_array = create_gradient_background((255, 65, 54), (220, 20, 60), WIDTH, HEIGHT)
    bg = ImageClip(bg_array).set_duration(3)

    # Main text: STOP
    stop_text = create_text_clip(
        "STOP!",
        fontsize=140,
        color='white',
        position=('center', 300),
        duration=3
    ).crossfadein(0.3)

    # Secondary text
    letting_text = create_text_clip(
        "letting AI",
        fontsize=70,
        color='red',
        position=('center', 800),
        duration=3
    ).crossfadein(0.5)

    guess_text = create_text_clip(
        "guess what you want!",
        fontsize=60,
        color='white',
        position=('center', 1400),
        duration=3
    ).crossfadein(0.8)

    return CompositeVideoClip([bg, stop_text, letting_text, guess_text])


def scene_2_problem():
    """Scene 2: Problem (3-8s)"""
    print("Creating Scene 2: Problem...")

    # Dark background
    bg = ColorClip(size=(WIDTH, HEIGHT), color=DARK).set_duration(5)

    # Speech bubble text
    speech = create_text_clip(
        '"Add auth"',
        fontsize=60,
        color='white',
        position=('center', 600),
        duration=5
    ).crossfadein(0.3)

    # Problem text
    problem = create_text_clip(
        "AI builds the\nWRONG thing ❌",
        fontsize=70,
        color='white',
        position=('center', 1200),
        duration=5
    ).crossfadein(0.6)

    return CompositeVideoClip([bg, speech, problem])


def scene_3_solution():
    """Scene 3: TCREI Logo (8-11s)"""
    print("Creating Scene 3: Solution...")

    # Blue gradient background
    bg_array = create_gradient_background(BLUE, (46, 92, 138), WIDTH, HEIGHT)
    bg = ImageClip(bg_array).set_duration(3)

    # TCREI logo
    logo = create_text_clip(
        "TCREI",
        fontsize=160,
        color='white',
        position=('center', 700),
        duration=3
    ).resize(lambda t: 1 + 0.3 * np.sin(t * 3))  # Pulse effect

    # Tagline
    tagline = create_text_clip(
        "Perfect AI Alignment ✨",
        fontsize=45,
        color='lightblue',
        position=('center', 1100),
        duration=3
    ).crossfadein(0.5)

    return CompositeVideoClip([bg, logo, tagline])


def scene_4_breakdown():
    """Scene 4: TCREI Breakdown (11-25s)"""
    print("Creating Scene 4: Breakdown...")

    # Dark background
    bg = ColorClip(size=(WIDTH, HEIGHT), color=DARK).set_duration(14)

    sections = [
        ("T 📋\nTask\nWhat exactly?", 200, 0),
        ("C 🎯\nContext\nWhy needed?", 500, 2),
        ("R 🔍\nReference\nAny examples?", 800, 4),
        ("E ✅\nEvaluation\nMeasure success?", 1100, 6),
        ("I 📊\nInput\nRead schema first?", 1400, 8),
    ]

    clips = [bg]
    for text, y_pos, start_time in sections:
        clip = create_text_clip(
            text,
            fontsize=50,
            color='white',
            position=('center', y_pos),
            duration=14-start_time
        ).set_start(start_time).crossfadein(0.5)
        clips.append(clip)

    return CompositeVideoClip(clips)


def scene_5_result():
    """Scene 5: Result (25-28s)"""
    print("Creating Scene 5: Result...")

    # Split background
    top_half = ColorClip(size=(WIDTH, HEIGHT//2), color=RED).set_position((0, 0)).set_duration(3)
    bottom_half = ColorClip(size=(WIDTH, HEIGHT//2), color=GREEN).set_position((0, HEIGHT//2)).set_duration(3)

    # Before text
    before = create_text_clip(
        "BEFORE ❌\nChaotic",
        fontsize=60,
        color='white',
        position=('center', 400),
        duration=3
    )

    # After text
    after = create_text_clip(
        "AFTER ✅\nPerfect Alignment!",
        fontsize=60,
        color='white',
        position=('center', 1200),
        duration=3
    )

    return CompositeVideoClip([top_half, bottom_half, before, after])


def scene_6_cta():
    """Scene 6: Call to Action (28-30s)"""
    print("Creating Scene 6: CTA...")

    # Blue gradient background
    bg_array = create_gradient_background(BLUE, (46, 92, 138), WIDTH, HEIGHT)
    bg = ImageClip(bg_array).set_duration(2)

    # Main CTA
    main = create_text_clip(
        "RPI Framework",
        fontsize=80,
        color='white',
        position=('center', 700),
        duration=2
    )

    # Link text
    link = create_text_clip(
        "Link in bio ⬇️",
        fontsize=60,
        color='white',
        position=('center', 1100),
        duration=2
    )

    return CompositeVideoClip([bg, main, link])


def create_full_video():
    """Combine all scenes into final video"""
    print("=" * 60)
    print("TCREI Short - Automated Video Generation")
    print("=" * 60)

    # Create all scenes
    scenes = [
        scene_1_hook(),      # 0-3s
        scene_2_problem(),   # 3-8s
        scene_3_solution(),  # 8-11s
        scene_4_breakdown(), # 11-25s
        scene_5_result(),    # 25-28s
        scene_6_cta(),       # 28-30s
    ]

    # Concatenate scenes
    print("\nCombining scenes...")
    final_video = concatenate_videoclips(scenes, method="compose")

    # Add fade transitions
    print("Adding transitions...")
    final_video = final_video.crossfadein(0.5).crossfadeout(0.5)

    # Output path
    output_path = OUTPUT_DIR / "tcrei_short_FINAL.mp4"

    # Write video
    print(f"\nExporting video to: {output_path}")
    print("This may take a few minutes...")
    final_video.write_videofile(
        str(output_path),
        fps=FPS,
        codec='libx264',
        audio=False,  # Add voice separately
        preset='medium',
        threads=4
    )

    print("\n" + "=" * 60)
    print("✅ VIDEO GENERATION COMPLETE!")
    print(f"📁 Output: {output_path}")
    print(f"📐 Format: {WIDTH}x{HEIGHT} (9:16 vertical)")
    print(f"⏱️  Duration: ~30 seconds")
    print("\n" + "=" * 60)
    print("\nNext steps:")
    print("1. Add voiceover using video editor (optional)")
    print("2. Upload to YouTube Shorts, TikTok, Instagram Reels")
    print("=" * 60)

    return output_path


if __name__ == "__main__":
    try:
        create_full_video()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have installed dependencies:")
        print("  pip install moviepy pillow numpy")
