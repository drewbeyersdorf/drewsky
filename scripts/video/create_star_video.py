#!/usr/bin/env python3
"""
STAR Method - 15-Second B&W Classical
Situation, Task, Action, Result
For behavioral interviews and problem-solving

Dependencies:
pip install pillow numpy
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess
import sys

# Configuration
OUTPUT_DIR = Path("../../output/framework_shorts/star_frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

# Pure B&W
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

# ASCII Cow mascot
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
    """Scene 1: Intro (0-2s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 300, COLORS['black'], size=40)

    font_display = get_font(130)
    draw_text_centered(draw, "STAR", 700, font_display, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Method", 850, font_body, COLORS['gray_dark'], WIDTH)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_2_S(frame_num, total_frames):
    """Scene 2: S - Situation (2-4.5s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "S", 450, font_display, COLORS['white'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Situation", 620, font_title, COLORS['white'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Describe the context,",
        "background, and setting",
        "of the scenario"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_light'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_3_T(frame_num, total_frames):
    """Scene 3: T - Task (4.5-7s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['black'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "T", 450, font_display, COLORS['black'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Task", 620, font_title, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Explain the challenge,",
        "problem, or goal",
        "you needed to address"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_dark'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_4_A(frame_num, total_frames):
    """Scene 4: A - Action (7-9.5s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "A", 450, font_display, COLORS['white'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Action", 620, font_title, COLORS['white'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Detail the specific steps",
        "you took to solve",
        "the problem"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_light'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_5_R(frame_num, total_frames):
    """Scene 5: R - Result (9.5-12s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['black'], size=35)

    font_display = get_font(140)
    draw_text_centered(draw, "R", 450, font_display, COLORS['black'], WIDTH)

    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Result", 620, font_title, COLORS['black'], WIDTH)

    font_body = get_font(FONT_BODY)
    lines = [
        "Share the outcomes,",
        "measurable impact,",
        "and lessons learned"
    ]
    draw_multiline_centered(draw, lines, 750, font_body, COLORS['gray_dark'], WIDTH, spacing=10)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_6_outro(frame_num, total_frames):
    """Scene 6: Outro (12-15s)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)

    draw_cow_mascot(draw, WIDTH // 2, 250, COLORS['white'], size=45)

    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "STAR Method", 600, font_display, COLORS['white'], WIDTH)

    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Ace Your Interviews", 720, font_body, COLORS['gray_light'], WIDTH)

    font_small = get_font(FONT_SMALL)
    draw_text_centered(draw, "github.com/drewbeyersdorf/", 950, font_small, COLORS['white'], WIDTH)
    draw_text_centered(draw, "agent-improvement-techniques", 1010, font_small, COLORS['white'], WIDTH)

    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def generate_all_frames():
    """Generate all frames"""
    print("\n" + "="*70)
    print("STAR METHOD - 15-SECOND B&W CLASSICAL")
    print("Situation • Task • Action • Result")
    print("="*70 + "\n")

    scenes = [
        ("Scene 1: Intro", scene_1_intro, 0, 2, 60),
        ("Scene 2: S - Situation", scene_2_S, 2, 4.5, 75),
        ("Scene 3: T - Task", scene_3_T, 4.5, 7, 75),
        ("Scene 4: A - Action", scene_4_A, 7, 9.5, 75),
        ("Scene 5: R - Result", scene_5_R, 9.5, 12, 75),
        ("Scene 6: Outro", scene_6_outro, 12, 15, 90),
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
    print(f"✅ FRAMES GENERATED! ({frame_counter} total)")
    print("="*70 + "\n")

    return frame_counter


def combine_frames_to_video():
    """Combine frames"""
    print("🎬 Creating video...\n")

    output_path = "../../output/framework_shorts/STAR_METHOD.mp4"

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
        print(f"✅ Silent video: {output_path}\n")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def add_music_to_video(video_path, music_path):
    """Add music"""
    print("🎵 Adding classical music...\n")

    output_path = "../../output/framework_shorts/STAR_METHOD_FINAL.mp4"

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
        print("✅ STAR METHOD VIDEO COMPLETE!")
        print(f"📁 Output: {output_path}")
        print(f"⏱️  Duration: 15 seconds")
        print("🎨 Style: BLACK & WHITE")
        print("🎵 Music: Classical piano")
        print("📝 Framework: STAR Method")
        print("🎯 Use: Behavioral interviews")
        print("\n" + "="*70 + "\n")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return video_path


def main():
    """Main execution"""
    print("\n⭐ STAR METHOD VIDEO GENERATOR")
    print("Behavioral Interview Framework\n")

    generate_all_frames()
    silent_video = combine_frames_to_video()

    music_path = "../../output/tcrei_short/classical_music.mp3"

    if Path(music_path).exists():
        print(f"✅ Using classical music\n")
        final_video = add_music_to_video(silent_video, music_path)
        print(f"✨ Video ready: {final_video}")
    else:
        print(f"✅ Silent video: {silent_video}")


if __name__ == "__main__":
    main()
