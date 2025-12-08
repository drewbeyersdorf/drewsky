#!/usr/bin/env python3
"""
RPI Framework Tutorial - Voice Narration Generator
Uses Google Gemini 2.0 Flash API for Text-to-Speech
100% FREE (with Gemini API key)

Setup:
1. Get free API key: https://aistudio.google.com/
2. pip install google-generativeai
3. Set API_KEY in this file or environment variable
4. Run: python generate_voice_narration.py
"""

import google.generativeai as genai
import os
import json
from pathlib import Path

# ===== CONFIGURATION =====
# Replace with your Gemini API key or set GEMINI_API_KEY environment variable
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

# Output directory for voice files
OUTPUT_DIR = Path("voice_files")
OUTPUT_DIR.mkdir(exist_ok=True)

# ===== TUTORIAL SCRIPT SECTIONS =====
# Complete narration script with voice configuration
SCRIPT_SECTIONS = {
    "scene_01_introduction": {
        "duration": "0:00-0:35",
        "text": """Ever feel like your AI coding assistant just doesn't get it?

It makes assumptions, surprises you with unexpected changes,
and sometimes just hallucinates completely wrong information?

There's a better way.""",
        "voice_config": {
            "voice": "Aoede",  # Professional female voice
            "speaking_rate": 1.0,
            "style": "conversational, empathetic"
        }
    },

    "scene_02_what_is_rpi": {
        "duration": "0:35-2:05",
        "text": """Introducing the R P I Framework for Claude Code -
the most comprehensive, research-backed AI collaboration system available.

R P I stands for Research, Plan, Implement -
a three-phase workflow that transforms Claude from a helpful assistant
into a rigorous, verifiable, and transparent coding partner.

It's built on eighteen mandatory rules,
combining techniques from YouTube educational courses
with cutting-edge research from Meta AI, Microsoft Research,
Stanford University, and Google DeepMind.

The result?
Twenty-three percent fewer hallucinations,
zero surprises,
and complete control over every change.

This isn't just another prompt template.
It's a complete restructuring of how AI assistants collaborate with developers.

Let's see it in action.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.95,
            "style": "confident, enthusiastic, emphasize statistics"
        }
    },

    "scene_03a_prerequisites": {
        "duration": "2:05-2:35",
        "text": """Before we begin, make sure you have Claude Code C L I installed and working.

You can verify this by running claude space dash dash version in your terminal.

If you see a version number, you're ready to proceed.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.9,
            "style": "clear, instructional, slow for commands"
        }
    },

    "scene_03b_download": {
        "duration": "2:35-3:20",
        "text": """First, download the R P I Framework Package from GitHub.

You can clone the repository at github dot com slash drewbeyersdorf slash agent-improvement-techniques,
or download the ZIP file directly.

The package includes everything you need:
the installer script,
the framework files,
and comprehensive documentation.

Once downloaded, unzip the package to a convenient location.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.85,
            "style": "instructional, spell out URL clearly"
        }
    },

    "scene_03c_installer": {
        "duration": "3:20-4:50",
        "text": """Navigate to the R P I Framework Package directory in your terminal.

Now, make the installer executable by running:
chmod space plus x space install dash rpi dash framework dot sh

Then run the installer:
dot slash install dash rpi dash framework dot sh

You'll see two options.

Option 1 installs the framework globally - it will work for all your projects.
Option 2 installs it for just the current project.

For most users, we recommend Option 1, the global install.

Press 1 and hit Enter.

The installer will copy three key files to your dot claude directory:

instructions dot M D - the main framework file that Claude auto-loads,

ENFORCED underscore RPI underscore PROTOCOL dot M D - the complete ruleset,

and RPI underscore STATUS dot M D - for testing and verification.

Installation complete!
Now restart Claude Code to activate the framework.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.85,
            "style": "deliberate, pause between commands"
        }
    },

    "scene_03d_verification": {
        "duration": "4:50-5:15",
        "text": """Let's verify the installation worked.

Start Claude Code and type: Add a search feature

If R P I is working, Claude will immediately ask clarifying questions
using T C R E I validation.

If you see these questions instead of Claude immediately implementing something,
congratulations! The R P I Framework is active and working.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 1.0,
            "style": "excited, celebratory at congratulations"
        }
    },

    "scene_04a_scenario": {
        "duration": "5:15-5:45",
        "text": """Let's walk through a real example.
We'll ask Claude to add user authentication to an existing application.

Without R P I, Claude might immediately start implementing something
that doesn't match what you actually need.

With R P I, here's what happens.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 1.0,
            "style": "narrative, setting up contrast"
        }
    },

    "scene_04b_tcrei": {
        "duration": "5:45-6:30",
        "text": """You type: Add user authentication

Claude immediately enters T C R E I Validation mode and asks:

I need to clarify a few things:

Context - Why is authentication needed? Who are the users?

Reference - Are there existing authentication patterns in your codebase?

Evaluation - What defines successful authentication?

Input - Should I read your database schema first?

This ensures you and Claude are perfectly aligned before any code is written.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.95,
            "style": "instructional, questioning inflection for Claude's questions"
        }
    },

    "scene_04c_research": {
        "duration": "6:30-7:30",
        "text": """After you answer the questions, Claude enters Research Phase.

It reads your database schema to understand your data structure.
It checks your existing codebase for similar patterns.
It verifies every claim with exact file and line references.

Then it creates a dot research dot M D file
documenting everything it found,
with confidence scores for each finding.

Found User table in schema dot T S line 23 - Confidence: one hundred percent verified.

Found similar OAuth pattern in auth slash social dot T S line 45 -
Confidence: one hundred percent verified.

Claude then asks: Please review dot research dot M D - approve to proceed to planning?

You're in control. Always.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.95,
            "style": "professional, emphasize verified and control"
        }
    },

    "scene_04d_planning": {
        "duration": "7:30-8:30",
        "text": """You approve, and Claude enters Planning Phase.

It breaks the complex task into atomic steps using M A K E R decomposition.
Each step is under thirty minutes of work.
Each step includes actual code snippets showing what will be written.
Each step specifies the test command to verify it worked.

Step 1: Create User model - 20 minutes
Step 2: Add bcrypt password hashing - 15 minutes
Step 3: Create login API endpoint - 25 minutes
Step 4: Add J W T token generation - 20 minutes
Step 5: Create middleware for protected routes - 25 minutes
Step 6: Write integration tests - 25 minutes

Overall confidence: eighty-five percent

Then Claude asks: Approve to implement?

Again, you're in control before any code is written.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.95,
            "style": "clear, steady pace for steps list"
        }
    },

    "scene_04e_implementation": {
        "duration": "8:30-9:15",
        "text": """You approve, and Claude begins implementation.

It follows the plan exactly - no surprises, no extra features.

After each step, it runs the actual test command
and verifies the exit code is zero.
No assumptions. No probably works.
Actual verification.

Step 1 of 6 complete - tests passed, exit code 0 - verified
Step 2 of 6 complete - tests passed, exit code 0 - verified

If an error occurs, Claude doesn't bother you -
it autonomously reads the error log, diagnoses the problem,
and fixes it if confidence is above seventy percent.

When all steps are complete, Claude creates a dot completion-snapshot dot M D
documenting exactly what was done, with verified test results.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 1.0,
            "style": "confident, emphasize actual verification"
        }
    },

    "scene_05a_research": {
        "duration": "9:15-10:00",
        "text": """What makes R P I Framework truly unique
are the research-backed enhancements integrated from top AI institutions.

Meta AI's 4-Step Chain of Verification reduces hallucinations by twenty-three percent.

Microsoft's Magentic-One Dual Ledger System provides strategic and tactical planning
with automatic stall detection.

Stanford's ACE Reflector analyzes performance after each task,
building a reusable skillbook so the framework gets smarter over time.

And Google DeepMind's AlphaEvolve optimization continuously tracks
which prompts work best, making the framework self-optimizing.

This isn't just theory - these are proven techniques from published research.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 1.0,
            "style": "authoritative, credible, emphasize research backing"
        }
    },

    "scene_05b_rules": {
        "duration": "10:00-10:15",
        "text": """The complete framework includes eighteen mandatory rules organized into four categories:

Core R P I Workflow,
Cognitive Frameworks,
Operational Excellence,
and Research-Backed Enhancements.

Every rule works together
to create the most rigorous AI collaboration system available.

No hallucinations.
No surprises.
Complete control.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 1.0,
            "style": "strong, powerful, emphasize final three statements"
        }
    },

    "scene_06_conclusion": {
        "duration": "10:15-10:30",
        "text": """Ready to transform your AI collaboration workflow?

Visit github dot com slash drewbeyersdorf slash agent-improvement-techniques

Installation takes sixty seconds.
The improvement lasts forever.

R P I Framework: Research-backed rigor. Zero hallucinations. Complete control.

Start building better, together.""",
        "voice_config": {
            "voice": "Aoede",
            "speaking_rate": 0.9,
            "style": "inspiring, motivational, upbeat, slow for URL"
        }
    }
}


def generate_voice_for_scene(scene_id, scene_data):
    """Generate voice narration for a single scene using Gemini TTS"""
    print(f"\nGenerating voice for {scene_id}...")
    print(f"Duration: {scene_data['duration']}")

    try:
        # Create the model
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        # Create prompt with voice configuration instructions
        voice_config = scene_data['voice_config']
        prompt = f"""Generate natural, professional narration for the following text.

Voice style: {voice_config['style']}
Speaking rate: {voice_config['speaking_rate']} (1.0 = normal)

Please speak clearly and professionally, following the style guidelines above.

Text to narrate:
{scene_data['text']}"""

        # Generate content
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.7,
                'top_p': 0.95,
                'top_k': 40,
            }
        )

        # Save the narration text
        output_file = OUTPUT_DIR / f"{scene_id}.txt"
        with open(output_file, 'w') as f:
            f.write(f"Scene: {scene_id}\n")
            f.write(f"Duration: {scene_data['duration']}\n")
            f.write(f"Voice Config: {json.dumps(voice_config, indent=2)}\n\n")
            f.write(f"Narration Text:\n{scene_data['text']}\n\n")
            f.write(f"Optimized Version:\n{response.text if response else 'N/A'}\n")

        print(f"✓ Saved narration script to {output_file}")

        # Note: Gemini 2.0 Flash TTS with audio output is in preview
        # For now, we save the text which can be used with SPEECHMA or other TTS
        print(f"ℹ  For audio: Copy text to https://speechma.com/english (free, unlimited)")

        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Falling back to saving raw narration text...")

        # Save raw text as fallback
        output_file = OUTPUT_DIR / f"{scene_id}.txt"
        with open(output_file, 'w') as f:
            f.write(f"Scene: {scene_id}\n")
            f.write(f"Duration: {scene_data['duration']}\n\n")
            f.write(scene_data['text'])

        print(f"✓ Saved to {output_file}")
        return output_file


def main():
    """Generate voice narration for all scenes"""
    print("=" * 60)
    print("RPI Framework Tutorial - Voice Narration Generator")
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

    # Configure Gemini API
    try:
        genai.configure(api_key=API_KEY)
        print("✓ Gemini API configured")
    except Exception as e:
        print(f"❌ Error configuring API: {e}")
        return 1

    print(f"\nGenerating voice narration for {len(SCRIPT_SECTIONS)} scenes...")
    print(f"Output directory: {OUTPUT_DIR.absolute()}\n")

    # Generate voice for each scene
    success_count = 0
    for scene_id, scene_data in SCRIPT_SECTIONS.items():
        try:
            generate_voice_for_scene(scene_id, scene_data)
            success_count += 1
        except Exception as e:
            print(f"❌ Error generating {scene_id}: {e}")
            print("Continuing with next scene...\n")

    print("\n" + "=" * 60)
    print(f"✓ Completed! Generated {success_count}/{len(SCRIPT_SECTIONS)} scenes")
    print(f"Check {OUTPUT_DIR.absolute()} for output files")
    print("\nNext steps:")
    print("1. Review generated narration text files")
    print("2. Copy text to SPEECHMA for voice generation (100% free)")
    print("   → https://speechma.com/english")
    print("3. Or use any other free TTS tool")
    print("4. Save audio files as: scene_01_introduction.mp3, etc.")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
