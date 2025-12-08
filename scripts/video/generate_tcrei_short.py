#!/usr/bin/env python3
"""
TCREI Explainer Short - Automated Production Script
Uses Google Gemini 2.0 Flash API
Creates: 30-second vertical video for YouTube Shorts/TikTok/Reels

Setup:
1. Get free API key: https://aistudio.google.com/
2. pip install google-generativeai
3. Set GEMINI_API_KEY environment variable
4. Run: python generate_tcrei_short.py
"""

import google.generativeai as genai
import os
import json
from pathlib import Path

# ===== CONFIGURATION =====
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
OUTPUT_DIR = Path("tcrei_short")
OUTPUT_DIR.mkdir(exist_ok=True)

# ===== SCRIPT =====
SCRIPT = """[0:00] STOP letting AI guess what you want!

[0:03] Most developers just say "add authentication"
and wonder why AI builds the wrong thing.

[0:08] There's a better way: T-C-R-E-I

[0:11] T - Task: What exactly do you need?

[0:14] C - Context: Why is it needed?

[0:16] R - Reference: Any existing patterns?

[0:19] E - Evaluation: How do you measure success?

[0:22] I - Input: Should AI read your schema first?

[0:25] Result? You and AI are perfectly aligned
before ANY code is written.

[0:28] Try the RPI Framework. Link in bio!"""

# ===== SCENES =====
SCENES = {
    "scene_1_hook": {
        "duration": "0:00-0:03",
        "text": "STOP letting AI guess what you want!",
        "visual_focus": "Attention-grabbing hook with split screen",
        "style": "Urgent, bold, red warning colors"
    },
    "scene_2_problem": {
        "duration": "0:03-0:08",
        "text": 'Most developers just say "add authentication" and wonder why AI builds the wrong thing.',
        "visual_focus": "Frustrated developer, speech bubble",
        "style": "Relatable problem visualization"
    },
    "scene_3_solution": {
        "duration": "0:08-0:11",
        "text": "There's a better way: T-C-R-E-I",
        "visual_focus": "TCREI logo reveal with impact",
        "style": "Confident, solution introduction"
    },
    "scene_4_breakdown": {
        "duration": "0:11-0:25",
        "text": """T - Task: What exactly do you need?
C - Context: Why is it needed?
R - Reference: Any existing patterns?
E - Evaluation: How do you measure success?
I - Input: Should AI read your schema first?""",
        "visual_focus": "Each TCREI letter with icon and description",
        "style": "Educational, clear breakdown"
    },
    "scene_5_result": {
        "duration": "0:25-0:28",
        "text": "Result? You and AI are perfectly aligned before ANY code is written.",
        "visual_focus": "Before/after comparison, success visualization",
        "style": "Triumphant, transformation"
    },
    "scene_6_cta": {
        "duration": "0:28-0:30",
        "text": "Try the RPI Framework. Link in bio!",
        "visual_focus": "RPI logo, GitHub CTA",
        "style": "Friendly call-to-action"
    }
}


def generate_voice_script():
    """Generate optimized voice narration using Gemini"""
    print("\n📝 Generating voice narration...")

    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        prompt = f"""You are an expert voice-over script writer for viral YouTube Shorts.

**Original script:**
{SCRIPT}

**Requirements:**
- 30 seconds exactly
- Vertical video (9:16)
- Fast-paced, energetic
- Hook in first 3 seconds
- Clear pronunciation guides for TTS

**Your task:**
Review this script and provide:
1. Optimized version (if any improvements needed)
2. Pronunciation guide for technical terms (TCREI, etc.)
3. Emphasis suggestions (which words to stress)
4. Pacing notes (where to pause, speed up)

Make it perfect for text-to-speech generation."""

        response = model.generate_content(
            prompt,
            generation_config={'temperature': 0.7, 'max_output_tokens': 1024}
        )

        # Save optimized script
        output_file = OUTPUT_DIR / "voice_script_optimized.txt"
        with open(output_file, 'w') as f:
            f.write("# TCREI Short - Voice Narration\n\n")
            f.write("## Original Script\n")
            f.write(SCRIPT)
            f.write("\n\n## Optimized by Gemini 2.0 Flash\n")
            f.write(response.text if response else "Error generating")

        print(f"✓ Saved to {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        # Fallback: save original script
        output_file = OUTPUT_DIR / "voice_script.txt"
        with open(output_file, 'w') as f:
            f.write(SCRIPT)
        print(f"✓ Saved original script to {output_file}")
        return output_file


def generate_scene_visuals():
    """Generate detailed visual descriptions for each scene"""
    print("\n🎨 Generating scene visual descriptions...")

    for scene_id, scene_data in SCENES.items():
        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')

            prompt = f"""You are a professional video designer creating visuals for a 30-second vertical video (9:16 aspect ratio).

**Scene:** {scene_id}
**Duration:** {scene_data['duration']}
**Narration:** {scene_data['text']}
**Visual Focus:** {scene_data['visual_focus']}
**Style:** {scene_data['style']}

**Platform:** YouTube Shorts / TikTok / Instagram Reels
**Tool:** Canva Free (drag-and-drop editor)

**Your task:**
Create a detailed visual specification for this scene that includes:

1. **Background**
   - Color/gradient (hex codes)
   - Mood and atmosphere

2. **Main Elements**
   - Text overlays (exact wording, size, position)
   - Characters/icons (specific from Canva library)
   - Graphics (shapes, lines, etc.)

3. **Layout**
   - Element positioning (top third, center, bottom)
   - Visual hierarchy (what draws the eye first)

4. **Animations**
   - Entry effect (fade in, slide in, pop)
   - During-scene animation (pulse, shake, highlight)
   - Timing (when each element appears)

5. **Typography**
   - Font recommendations (available in Canva)
   - Sizes (large enough for mobile viewing)
   - Colors and contrast

Make it:
- Bold and eye-catching
- Mobile-optimized (readable on small screens)
- Easy to create in Canva
- Aligned with vertical video best practices

Generate the visual description now:"""

            response = model.generate_content(
                prompt,
                generation_config={'temperature': 0.8, 'max_output_tokens': 1536}
            )

            # Save scene description
            output_file = OUTPUT_DIR / f"{scene_id}_visual.md"
            with open(output_file, 'w') as f:
                f.write(f"# {scene_id.replace('_', ' ').title()}\n\n")
                f.write(f"**Duration:** {scene_data['duration']}\n")
                f.write(f"**Narration:** {scene_data['text']}\n\n")
                f.write("---\n\n")
                f.write(response.text if response else "Error generating")

            print(f"✓ {scene_id}")

        except Exception as e:
            print(f"❌ Error on {scene_id}: {e}")


def generate_canva_guide():
    """Generate step-by-step Canva implementation guide"""
    print("\n📐 Generating Canva quick-start guide...")

    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        prompt = """You are a Canva expert creating a beginner-friendly guide for making a 30-second vertical video.

**Project Specs:**
- Format: Vertical (1080x1920, 9:16 aspect ratio)
- Duration: 30 seconds
- Platform: YouTube Shorts / TikTok / Reels
- Tool: Canva Free (no watermark)
- Scenes: 6 total

**Your task:**
Create a step-by-step Canva guide that includes:

1. **Initial Setup**
   - How to create vertical video project in Canva
   - Exact dimensions and settings
   - Page structure (6 pages for 6 scenes)

2. **Design Tips for Vertical Video**
   - Safe zones (avoid top/bottom cutoff)
   - Text sizing for mobile readability
   - Element positioning

3. **Creating Common Elements**
   - Text overlays (large, bold)
   - Speech bubbles
   - Split screen effect
   - Icon placement
   - Background gradients

4. **Animations**
   - Best animation presets for Shorts
   - Timing suggestions
   - Transitions between pages

5. **Adding Audio**
   - How to upload voiceover
   - Syncing voice to pages
   - Adding background music (optional)

6. **Export Settings**
   - Exact settings for 1080x1920
   - Quality recommendations
   - Confirming no watermark

Make it:
- Step-by-step (numbered)
- Screenshot-worthy (clear instructions)
- Beginner-friendly (assume no Canva experience)
- Optimized for YouTube Shorts success

Generate the guide now:"""

        response = model.generate_content(
            prompt,
            generation_config={'temperature': 0.7, 'max_output_tokens': 2048}
        )

        # Save Canva guide
        output_file = OUTPUT_DIR / "CANVA_QUICK_START.md"
        with open(output_file, 'w') as f:
            f.write("# Canva Quick-Start Guide - TCREI Short\n\n")
            f.write("**Format:** Vertical (1080x1920)\n")
            f.write("**Duration:** 30 seconds\n")
            f.write("**Scenes:** 6\n\n")
            f.write("---\n\n")
            f.write(response.text if response else "Error generating")

        print(f"✓ Saved to {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def create_checklist():
    """Create production checklist"""
    print("\n✅ Creating production checklist...")

    checklist = """# TCREI Short - Production Checklist

## Pre-Production
- [ ] Gemini API key configured
- [ ] Scripts generated
- [ ] Visual descriptions reviewed
- [ ] Canva account ready (free tier)

## Voice Generation
- [ ] Copy voice script to SPEECHMA
- [ ] Voice: US English Professional
- [ ] Speed: 1.1x (energetic, fast-paced)
- [ ] Download MP3 (30 seconds)

## Video Creation (Canva)
- [ ] New project created (1080x1920)
- [ ] 6 pages added (one per scene)
- [ ] Scene 1: Hook (3s) - Red, bold, "STOP"
- [ ] Scene 2: Problem (5s) - Developer, speech bubble
- [ ] Scene 3: Logo (3s) - TCREI reveal
- [ ] Scene 4: Breakdown (14s) - 5 letters with icons
- [ ] Scene 5: Result (3s) - Before/after comparison
- [ ] Scene 6: CTA (2s) - "Link in bio"
- [ ] Voiceover added and synced
- [ ] Animations applied (slide in, pop, pulse)
- [ ] Background music added (optional, -20dB)

## Quality Check
- [ ] Duration: Exactly 30 seconds ✓
- [ ] Format: 1080x1920 (vertical) ✓
- [ ] Text readable on mobile ✓
- [ ] Hook grabs attention (first 3s) ✓
- [ ] Audio clear and synced ✓
- [ ] No watermark ✓

## Export & Publish
- [ ] Exported as MP4 (1080x1920)
- [ ] Uploaded to YouTube Shorts
- [ ] Title: "TCREI: Stop AI from Guessing! #ai #programming"
- [ ] Description with GitHub link
- [ ] Cross-posted to TikTok
- [ ] Cross-posted to Instagram Reels
- [ ] Bio link updated with GitHub

## Post-Launch
- [ ] Monitor views (first 48 hours critical)
- [ ] Respond to comments
- [ ] Track link clicks from bio
- [ ] Analyze performance (watch time, engagement)

---

**Production Time Estimate:**
- Voice generation: 5 minutes
- Canva design: 30-45 minutes
- Review & adjustments: 15 minutes
- Export & upload: 10 minutes
**Total: ~1 hour**

**Cost: $0** (100% free)
"""

    output_file = OUTPUT_DIR / "PRODUCTION_CHECKLIST.md"
    with open(output_file, 'w') as f:
        f.write(checklist)

    print(f"✓ Saved to {output_file}")
    return output_file


def main():
    """Generate all assets for TCREI short"""
    print("=" * 60)
    print("  TCREI Explainer Short - Asset Generator")
    print("  Using Google Gemini 2.0 Flash API (FREE)")
    print("  Duration: 30 seconds | Format: Vertical (9:16)")
    print("=" * 60)

    # Check API key
    if API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("\n❌ ERROR: Please set your Gemini API key!")
        print("\nOptions:")
        print("1. Set environment variable: export GEMINI_API_KEY='your-key'")
        print("2. Edit script: API_KEY = 'your-key'")
        print("\nGet free key: https://aistudio.google.com/")
        return 1

    # Configure API
    try:
        genai.configure(api_key=API_KEY)
        print("\n✓ Gemini API configured")
    except Exception as e:
        print(f"\n❌ Error configuring API: {e}")
        return 1

    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}\n")
    print("Generating assets...\n")

    # Generate all assets
    generate_voice_script()
    generate_scene_visuals()
    generate_canva_guide()
    create_checklist()

    print("\n" + "=" * 60)
    print("✓ Asset generation complete!")
    print(f"Check {OUTPUT_DIR.absolute()}")
    print("\nFiles created:")
    print("- voice_script_optimized.txt (narration)")
    print("- scene_1_hook_visual.md")
    print("- scene_2_problem_visual.md")
    print("- scene_3_solution_visual.md")
    print("- scene_4_breakdown_visual.md")
    print("- scene_5_result_visual.md")
    print("- scene_6_cta_visual.md")
    print("- CANVA_QUICK_START.md")
    print("- PRODUCTION_CHECKLIST.md")
    print("\nNext steps:")
    print("1. Copy voice script to SPEECHMA → generate audio")
    print("2. Open Canva → create 1080x1920 video")
    print("3. Follow CANVA_QUICK_START.md guide")
    print("4. Use scene visual descriptions")
    print("5. Export & upload to YouTube Shorts/TikTok/Reels")
    print("\nEstimated production time: ~1 hour")
    print("Total cost: $0")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
