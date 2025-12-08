#!/usr/bin/env python3
"""
SMART Goals - 15-Second B&W Classical
Specific, Measurable, Achievable, Relevant, Time-bound
For effective goal setting

Dependencies:
pip install pillow numpy
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess
import sys

OUTPUT_DIR = Path("../../output/framework_shorts/smart_frames")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray_light': (220, 220, 220),
    'gray_dark': (40, 40, 40),
}

FONT_DISPLAY = 110
FONT_TITLE = 85
FONT_BODY = 52
FONT_SMALL = 45

COW_ASCII = [
    "  ((____))",
    "  [ x x ]",
    "   \\   /",
    "   ('  ')",
    "   (U)"
]


def get_font(size):
    try:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Didot.ttc", size)
    except:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", size)
        except:
            return ImageFont.load_default()


def get_mono_font(size):
    try:
        return ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", size)
    except:
        return ImageFont.load_default()


def draw_text_centered(draw, text, y_position, font, color, img_width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img_width - text_width) // 2
    draw.text((x, y_position), text, font=font, fill=color)


def draw_multiline_centered(draw, lines, start_y, font, color, img_width, spacing=10):
    current_y = start_y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (img_width - text_width) // 2
        draw.text((x, current_y), line, font=font, fill=color)
        current_y += text_height + spacing


def draw_cow_mascot(draw, x_pos, y_pos, color, size=30):
    font = get_mono_font(size)
    current_y = y_pos
    for line in COW_ASCII:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        line_x = x_pos - (text_width // 2)
        draw.text((line_x, current_y), line, font=font, fill=color)
        current_y += bbox[3] - bbox[1] + 5


def draw_watermark(draw, img_width, img_height):
    font = get_font(40)
    text = "drewbeyersdorf"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = img_width - text_width - 40
    y = img_height - 80
    draw.text((x, y), text, font=font, fill=COLORS['gray_light'])


def scene_intro(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 300, COLORS['black'], size=40)
    font_display = get_font(130)
    draw_text_centered(draw, "SMART", 700, font_display, COLORS['black'], WIDTH)
    font_body = get_font(FONT_BODY + 3)
    draw_text_centered(draw, "Goals", 850, font_body, COLORS['gray_dark'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_S(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)
    font_display = get_font(140)
    draw_text_centered(draw, "S", 450, font_display, COLORS['white'], WIDTH)
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Specific", 620, font_title, COLORS['white'], WIDTH)
    font_body = get_font(FONT_BODY)
    lines = ["Clear and well-defined", "objectives with", "precise outcomes"]
    draw_multiline_centered(draw, lines, 760, font_body, COLORS['gray_light'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_M(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['black'], size=35)
    font_display = get_font(140)
    draw_text_centered(draw, "M", 450, font_display, COLORS['black'], WIDTH)
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Measurable", 620, font_title, COLORS['black'], WIDTH)
    font_body = get_font(FONT_BODY)
    lines = ["Track progress with", "quantifiable metrics", "and milestones"]
    draw_multiline_centered(draw, lines, 760, font_body, COLORS['gray_dark'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_A(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)
    font_display = get_font(140)
    draw_text_centered(draw, "A", 450, font_display, COLORS['white'], WIDTH)
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Achievable", 620, font_title, COLORS['white'], WIDTH)
    font_body = get_font(FONT_BODY)
    lines = ["Realistic within your", "resources, time,", "and constraints"]
    draw_multiline_centered(draw, lines, 760, font_body, COLORS['gray_light'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_R(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['black'], size=35)
    font_display = get_font(140)
    draw_text_centered(draw, "R", 450, font_display, COLORS['black'], WIDTH)
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Relevant", 620, font_title, COLORS['black'], WIDTH)
    font_body = get_font(FONT_BODY)
    lines = ["Aligned with broader", "vision, values,", "and priorities"]
    draw_multiline_centered(draw, lines, 760, font_body, COLORS['gray_dark'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_T(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['black'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 150, COLORS['white'], size=35)
    font_display = get_font(140)
    draw_text_centered(draw, "T", 450, font_display, COLORS['white'], WIDTH)
    font_title = get_font(FONT_TITLE)
    draw_text_centered(draw, "Time-bound", 620, font_title, COLORS['white'], WIDTH)
    font_body = get_font(FONT_BODY)
    lines = ["Set clear deadlines", "and target dates", "for completion"]
    draw_multiline_centered(draw, lines, 760, font_body, COLORS['gray_light'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def scene_outro(frame_num, total_frames):
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['white'])
    draw = ImageDraw.Draw(img)
    draw_cow_mascot(draw, WIDTH // 2, 250, COLORS['black'], size=45)
    font_display = get_font(FONT_DISPLAY)
    draw_text_centered(draw, "SMART Goals", 600, font_display, COLORS['black'], WIDTH)
    font_body = get_font(FONT_BODY)
    draw_text_centered(draw, "Set Better Goals", 720, font_body, COLORS['gray_dark'], WIDTH)
    font_small = get_font(FONT_SMALL)
    draw_text_centered(draw, "github.com/drewbeyersdorf/", 950, font_small, COLORS['black'], WIDTH)
    draw_text_centered(draw, "agent-improvement-techniques", 1010, font_small, COLORS['black'], WIDTH)
    draw_watermark(draw, WIDTH, HEIGHT)
    return img


def generate_all_frames():
    print("\n" + "="*70)
    print("SMART GOALS - 15-SECOND B&W CLASSICAL")
    print("="*70 + "\n")

    scenes = [
        ("Intro", scene_intro, 0, 1.5, 45),
        ("S - Specific", scene_S, 1.5, 3.5, 60),
        ("M - Measurable", scene_M, 3.5, 5.5, 60),
        ("A - Achievable", scene_A, 5.5, 7.5, 60),
        ("R - Relevant", scene_R, 7.5, 9.5, 60),
        ("T - Time-bound", scene_T, 9.5, 12, 75),
        ("Outro", scene_outro, 12, 15, 90),
    ]

    frame_counter = 0
    for scene_name, scene_func, start_time, end_time, num_frames in scenes:
        print(f"🎬 {scene_name} ({start_time}-{end_time}s, {num_frames} frames)...", end="")
        for i in range(num_frames):
            img = scene_func(i, num_frames)
            frame_path = OUTPUT_DIR / f"frame_{frame_counter:04d}.png"
            img.save(frame_path)
            frame_counter += 1
        print(f" ✅")

    print("\n" + "="*70)
    print(f"✅ {frame_counter} frames generated!")
    print("="*70 + "\n")
    return frame_counter


def combine_frames_to_video():
    print("🎬 Creating video...\n")
    output_path = "../../output/framework_shorts/SMART_GOALS.mp4"
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
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"✅ Silent video: {output_path}\n")
    return output_path


def add_music_to_video(video_path, music_path):
    print("🎵 Adding music...\n")
    output_path = "../../output/framework_shorts/SMART_GOALS_FINAL.mp4"
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
    subprocess.run(cmd, check=True, capture_output=True)
    print("\n" + "="*70)
    print("✅ SMART GOALS VIDEO COMPLETE!")
    print(f"📁 {output_path}")
    print("="*70 + "\n")
    return output_path


def main():
    print("\n🎯 SMART GOALS VIDEO GENERATOR\n")
    generate_all_frames()
    silent_video = combine_frames_to_video()
    music_path = "../../output/tcrei_short/classical_music.mp3"
    if Path(music_path).exists():
        final_video = add_music_to_video(silent_video, music_path)
        print(f"✨ Video ready: {final_video}")


if __name__ == "__main__":
    main()
