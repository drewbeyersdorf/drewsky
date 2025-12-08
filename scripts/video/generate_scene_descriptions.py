#!/usr/bin/env python3
"""
RPI Framework Tutorial - Scene Description Generator
Uses Google Gemini 2.0 Flash API to generate detailed visual descriptions
for creating animations in Canva, CapCut, or other free video tools

Setup:
1. Get free API key: https://aistudio.google.com/
2. pip install google-generativeai
3. Set API_KEY in this file or environment variable
4. Run: python generate_scene_descriptions.py
"""

import google.generativeai as genai
import os
import json
from pathlib import Path

# ===== CONFIGURATION =====
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
OUTPUT_DIR = Path("scene_descriptions")
OUTPUT_DIR.mkdir(exist_ok=True)

# ===== SCENE OUTLINES =====
SCENES = {
    "scene_01_introduction": {
        "duration": "0:00-0:35",
        "title": "Introduction - Frustrated Developer",
        "narration": "Ever feel like your AI coding assistant just doesn't get it? It makes assumptions, surprises you...",
        "key_elements": [
            "Developer character at desk",
            "Laptop with code errors",
            "Frustrated expression",
            "Thought bubbles with problems",
            "Transition to RPI logo reveal"
        ]
    },

    "scene_02_what_is_rpi": {
        "duration": "0:35-2:05",
        "title": "What is RPI Framework",
        "narration": "Introducing the RPI Framework - Research, Plan, Implement...",
        "key_elements": [
            "RPI workflow diagram (R→P→I)",
            "18 Rules badge",
            "Research institution logos (Meta, Microsoft, Stanford, DeepMind)",
            "Statistics: 23% reduction",
            "Benefits visualization"
        ]
    },

    "scene_03_installation": {
        "duration": "2:05-5:15",
        "title": "Installation Guide",
        "narration": "Before we begin... terminal commands... installer steps...",
        "key_elements": [
            "Terminal window mock-up",
            "Command sequences with output",
            "File copying visualization",
            "Progress indicators",
            "Success confirmation"
        ]
    },

    "scene_04_usage_example": {
        "duration": "5:15-9:15",
        "title": "First Usage Example",
        "narration": "Let's walk through adding user authentication... TCREI validation... research phase...",
        "key_elements": [
            "Chat interface (user and Claude messages)",
            "TCREI questions highlighted",
            ".research.md document visualization",
            ".plan.md with code snippets",
            "Test execution with verified results"
        ]
    },

    "scene_05_advanced_features": {
        "duration": "9:15-10:15",
        "title": "Advanced Features & Research",
        "narration": "Research-backed enhancements from Meta, Microsoft, Stanford, DeepMind...",
        "key_elements": [
            "Research institution logos with features",
            "4-step CoVe diagram",
            "Dual ledger visualization",
            "18 rules organized in 4 categories",
            "Interlocking system graphic"
        ]
    },

    "scene_06_conclusion": {
        "duration": "10:15-10:30",
        "title": "Conclusion & Call to Action",
        "narration": "Ready to transform your workflow? Visit GitHub...",
        "key_elements": [
            "GitHub URL prominent",
            "QR code for mobile",
            "Key stats: 60 seconds install, forever improved",
            "RPI logo with tagline",
            "Social media links"
        ]
    }
}


def generate_scene_description(scene_id, scene_data):
    """Generate detailed visual description for a scene using Gemini"""
    print(f"\nGenerating description for {scene_id}...")
    print(f"Title: {scene_data['title']}")

    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        prompt = f"""You are a professional video production designer creating detailed visual descriptions for an animated tutorial video.

**Scene Information:**
- Scene: {scene_data['title']}
- Duration: {scene_data['duration']}
- Narration summary: {scene_data['narration']}
- Key elements: {', '.join(scene_data['key_elements'])}

**Target Tools:** Canva, CapCut, or similar free video editing tools

**Your Task:**
Generate a comprehensive visual scene description that includes:

1. **Background Design**
   - Colors, gradients, patterns
   - Overall mood and atmosphere

2. **Foreground Elements**
   - Character design and poses (if applicable)
   - UI elements (terminal windows, chat bubbles, documents, etc.)
   - Icons, badges, logos
   - Specific placement (left, right, center, top, bottom)

3. **Text Overlays**
   - Main title text
   - Subtitles, callouts, labels
   - Font suggestions (sans-serif, monospace, etc.)
   - Text size and placement

4. **Animation Suggestions**
   - Entry animations (fade in, slide in, pop in)
   - During-scene animations (pulse, highlight, progress bars)
   - Exit animations (fade out, slide out)
   - Timing suggestions (when each element appears)

5. **Color Palette**
   - Primary colors (hex codes if possible)
   - Accent colors
   - How colors create visual hierarchy

6. **Asset Requirements**
   - Specific illustrations needed (developer character, icons, etc.)
   - Where to find free assets (Canva library, Unsplash, etc.)
   - Custom elements to create

**Important:**
- Keep it implementable in FREE tools (Canva, CapCut)
- Be specific about sizes, positions, colors
- Suggest free asset sources
- Make it professional but achievable

Generate the visual description now:"""

        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.8,
                'top_p': 0.95,
                'max_output_tokens': 2048,
            }
        )

        # Save the description
        output_file = OUTPUT_DIR / f"{scene_id}.md"
        with open(output_file, 'w') as f:
            f.write(f"# {scene_data['title']}\n\n")
            f.write(f"**Duration:** {scene_data['duration']}\n\n")
            f.write(f"**Narration:** {scene_data['narration']}\n\n")
            f.write(f"**Key Elements:** {', '.join(scene_data['key_elements'])}\n\n")
            f.write("---\n\n")
            f.write("## Visual Description (Generated by Gemini 2.0 Flash)\n\n")
            f.write(response.text if response else "Error generating description")

        print(f"✓ Saved to {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def generate_canva_instructions():
    """Generate specific Canva implementation guide"""
    print("\nGenerating Canva implementation guide...")

    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        prompt = """You are a Canva expert creating a step-by-step guide for implementing the RPI Framework tutorial video.

**Context:**
- Video: RPI Framework Tutorial (10:30 duration)
- Tool: Canva Free (no watermark)
- Output: 1920x1080 MP4
- 6 main scenes (introduction, overview, installation, example, features, conclusion)

**Your Task:**
Create a detailed, step-by-step Canva workflow guide that includes:

1. **Initial Setup**
   - How to create the project (exact dimensions, settings)
   - Template selection (if any)
   - Page/slide structure

2. **For Each Scene Type:**
   - Terminal window: How to create mock-up
   - Chat interface: How to create user/Claude bubbles
   - Diagrams: How to build workflow visualizations
   - Stats/numbers: How to create engaging data displays

3. **Canva-Specific Tips:**
   - Which Canva elements to use (shapes, text boxes, etc.)
   - How to find free assets in Canva library
   - Animation preset recommendations
   - Text styling (fonts, sizes, colors)

4. **Timeline & Audio:**
   - How to add voiceover files
   - How to sync animations to audio
   - Page duration setup

5. **Export Settings:**
   - Exact export configuration for 1080p
   - How to avoid watermark (confirm it's free tier)

Make it beginner-friendly with clear, actionable steps."""

        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.7,
                'max_output_tokens': 3000,
            }
        )

        output_file = OUTPUT_DIR / "CANVA_IMPLEMENTATION_GUIDE.md"
        with open(output_file, 'w') as f:
            f.write("# Canva Implementation Guide\n\n")
            f.write("**Generated by Gemini 2.0 Flash API**\n\n")
            f.write(response.text if response else "Error generating guide")

        print(f"✓ Saved Canva guide to {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def main():
    """Generate scene descriptions and implementation guide"""
    print("=" * 60)
    print("RPI Framework Tutorial - Scene Description Generator")
    print("Using Google Gemini 2.0 Flash API (FREE)")
    print("=" * 60)

    # Check API key
    if API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("\n❌ ERROR: Please set your Gemini API key!")
        print("\nOptions:")
        print("1. Set in script: API_KEY = 'your-key-here'")
        print("2. Set environment variable: export GEMINI_API_KEY='your-key-here'")
        print("\nGet your free key at: https://aistudio.google.com/")
        return 1

    # Configure API
    try:
        genai.configure(api_key=API_KEY)
        print("✓ Gemini API configured")
    except Exception as e:
        print(f"❌ Error configuring API: {e}")
        return 1

    print(f"\nGenerating detailed scene descriptions...")
    print(f"Output directory: {OUTPUT_DIR.absolute()}\n")

    # Generate descriptions for each scene
    success_count = 0
    for scene_id, scene_data in SCENES.items():
        if generate_scene_description(scene_id, scene_data):
            success_count += 1

    # Generate Canva implementation guide
    print("\n" + "-" * 60)
    generate_canva_instructions()

    print("\n" + "=" * 60)
    print(f"✓ Completed! Generated {success_count}/{len(SCENES)} scene descriptions")
    print(f"✓ Check {OUTPUT_DIR.absolute()} for output files")
    print("\nFiles created:")
    print("- scene_01_introduction.md")
    print("- scene_02_what_is_rpi.md")
    print("- ... (all 6 scenes)")
    print("- CANVA_IMPLEMENTATION_GUIDE.md")
    print("\nNext steps:")
    print("1. Review scene descriptions")
    print("2. Follow Canva implementation guide")
    print("3. Create animations using the detailed visual specs")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
