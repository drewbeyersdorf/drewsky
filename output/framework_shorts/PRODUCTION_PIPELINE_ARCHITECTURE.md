# Knowledge Shorts Production Pipeline
## Automated Video Generation System for Educational Content

---

## Overview

**Goal:** Automatically generate educational short-form videos (15-30s) from term definitions with ASCII cow aesthetic.

**Input:** Term name, definition, examples, complexity level
**Output:** Complete video file ready for upload (MP4, 1080x1920, 15-30s)

---

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   PRODUCTION PIPELINE                        │
└─────────────────────────────────────────────────────────────┘

    INPUT: Term Config (JSON/YAML)
      │
      ├─► [1] SCRIPT GENERATOR
      │       │
      │       ├─► Template Engine
      │       ├─► AI Enhancement (optional)
      │       └─► Script Validation
      │
      ├─► [2] VISUAL GENERATOR
      │       │
      │       ├─► ASCII Scene Creator
      │       ├─► Animation Builder
      │       ├─► Scene Sequencer
      │       └─► Image Export (PNG sequence)
      │
      ├─► [3] AUDIO GENERATOR
      │       │
      │       ├─► Text-to-Speech Engine
      │       ├─► Background Music (optional)
      │       ├─► Sound Effects (optional)
      │       └─► Audio Mix
      │
      ├─► [4] TEXT OVERLAY GENERATOR
      │       │
      │       ├─► Key Term Extraction
      │       ├─► Timing Calculation
      │       └─► Subtitle Format
      │
      └─► [5] VIDEO COMPILER
              │
              ├─► Scene Assembly
              ├─► Audio Sync
              ├─► Text Overlay
              ├─► Transitions
              └─► Final Export (MP4)

    OUTPUT: Ready-to-upload video file
```

---

## Component Details

### 1. Script Generator

**Purpose:** Generate structured scripts from term definitions

**Input:**
```json
{
  "term": "Idempotency",
  "category": "computing_fundamentals",
  "complexity": "medium",
  "duration_target": 25,
  "definition": "Operation that produces same result if repeated",
  "examples": ["light switch", "API requests", "payment buttons"],
  "why_matters": "Prevents duplicate charges, safe retries"
}
```

**Output:**
```json
{
  "script": {
    "hook": "Press a button once, twice, 100 times...",
    "definition": "Idempotency means you can do something...",
    "example": "Like a light switch - flip it to 'on' 100 times...",
    "application": "If your payment button isn't idempotent...",
    "cta": "Follow for more computing concepts"
  },
  "timing": {
    "hook": 3,
    "definition": 7,
    "example": 10,
    "application": 4,
    "cta": 1
  },
  "visuals": [
    "ascii_cow_pressing_button",
    "result_diagram",
    "payment_example"
  ]
}
```

**Technology:**
- Jinja2 templates for script structure
- Optional: Claude API for enhancement/variation
- JSON schema validation

---

### 2. Visual Generator

**Purpose:** Create ASCII art scenes and animations

**Components:**

#### A. ASCII Scene Library
Pre-built components:
- `cow_neutral.txt` - Default ASCII cow
- `cow_thinking.txt` - Cow with thought bubble
- `cow_teaching.txt` - Cow pointing at board
- `cow_confused.txt` - Cow with question marks
- `diagrams/` - Common diagrams (before/after, flowcharts)

#### B. Animation Engine
- Frame-by-frame ASCII animation
- Transition effects (fade, slide)
- Highlighting/emphasis
- Text reveals

#### C. Scene Templates
```python
scenes = {
    "comparison": {
        "layout": "split_screen",
        "elements": ["left_example", "vs_separator", "right_example"]
    },
    "process": {
        "layout": "sequential",
        "elements": ["step1", "arrow", "step2", "arrow", "step3"]
    },
    "demonstration": {
        "layout": "centered",
        "elements": ["ascii_cow", "action", "result"]
    }
}
```

**Output:** PNG image sequence (1080x1920 per frame)

**Technology:**
- Pillow (PIL) for image generation
- Custom ASCII renderer
- Monospace font (JetBrains Mono, Fira Code)
- Color palette for emphasis

---

### 3. Audio Generator

**Purpose:** Generate narration and background audio

**Components:**

#### A. Text-to-Speech
Options:
1. **OpenAI TTS API** (recommended)
   - Voices: alloy, echo, fable, onyx, nova, shimmer
   - High quality, natural
   - Cost: ~$15 per 1M characters

2. **ElevenLabs** (alternative)
   - Very natural voices
   - Voice cloning possible
   - Cost: ~$22 per 100k characters

3. **gTTS** (free fallback)
   - Google Text-to-Speech
   - Lower quality
   - No cost

#### B. Background Music (optional)
- Low-volume ambient music
- Royalty-free tracks
- Loopable segments
- Duck under narration

#### C. Sound Effects (optional)
- Subtle UI sounds for transitions
- "Pop" for key terms appearing
- Keep minimal to avoid distraction

**Output:** WAV/MP3 audio file

**Technology:**
- `openai` Python library
- `pydub` for audio processing
- FFmpeg for mixing

---

### 4. Text Overlay Generator

**Purpose:** Create on-screen text overlays for key terms

**Types:**
1. **Key Term Definition** (bottom third)
   - Appears at end of explanation
   - Format: "Term = Definition"
   - Bold, high contrast

2. **Subtitle Track** (optional)
   - Full narration text
   - Word-by-word or phrase-by-phrase
   - Improves accessibility

3. **Emphasis Text** (mid-screen)
   - Single words for emphasis
   - Synced to narration
   - Fade in/out

**Output:** SRT subtitle file + overlay specs

**Technology:**
- `srt` Python library
- Timing based on TTS duration
- Position/style specs for FFmpeg

---

### 5. Video Compiler

**Purpose:** Assemble all components into final video

**Process:**
1. Load PNG sequence (visuals)
2. Calculate frame rate from timing
3. Overlay text at specified timestamps
4. Sync audio track
5. Add transitions between scenes
6. Export final video

**Output Specs:**
- Format: MP4 (H.264)
- Resolution: 1080x1920 (9:16 portrait)
- Frame rate: 30fps
- Audio: AAC, 44.1kHz
- Bitrate: 5-8 Mbps

**Technology:**
- FFmpeg (primary engine)
- `moviepy` (Python wrapper, optional)
- Hardware acceleration (if available)

---

## File Structure

```
framework_shorts/
├── pipeline/
│   ├── config/
│   │   ├── terms/
│   │   │   ├── computing_fundamentals.json
│   │   │   ├── design_systems.json
│   │   │   └── data_statistics.json
│   │   ├── templates/
│   │   │   ├── script_templates.json
│   │   │   └── scene_templates.json
│   │   └── settings.yaml
│   │
│   ├── generators/
│   │   ├── script_generator.py
│   │   ├── visual_generator.py
│   │   ├── audio_generator.py
│   │   ├── text_overlay_generator.py
│   │   └── video_compiler.py
│   │
│   ├── assets/
│   │   ├── ascii/
│   │   │   ├── cows/
│   │   │   ├── diagrams/
│   │   │   └── decorations/
│   │   ├── fonts/
│   │   │   └── JetBrainsMono-Regular.ttf
│   │   ├── music/
│   │   │   └── ambient_loop.mp3
│   │   └── sfx/
│   │       └── pop.wav
│   │
│   ├── output/
│   │   ├── scripts/
│   │   ├── visuals/
│   │   ├── audio/
│   │   └── videos/
│   │
│   └── main.py  # Orchestrator
│
├── COMPUTING_FUNDAMENTALS_SCRIPTS.md
├── PRODUCTION_PIPELINE_ARCHITECTURE.md
└── requirements.txt
```

---

## Configuration System

### Global Settings (`settings.yaml`)

```yaml
# Production Settings
video:
  resolution: [1080, 1920]  # width x height
  fps: 30
  format: "mp4"
  quality: "high"  # low, medium, high

audio:
  tts_provider: "openai"  # openai, elevenlabs, gtts
  voice: "nova"
  background_music: true
  music_volume: 0.15

visual:
  font: "JetBrainsMono-Regular.ttf"
  font_size: 48
  background_color: "#0a0a0a"
  text_color: "#00ff00"
  accent_color: "#ff6b35"

timing:
  fade_duration: 0.5
  scene_transition: 0.3
  text_delay: 0.2

branding:
  show_cow: true
  show_watermark: false
  end_cta: "Follow for more tech concepts"
```

### Term Configuration (`terms/computing_fundamentals.json`)

```json
{
  "terms": [
    {
      "id": "compaction",
      "name": "Compaction",
      "category": "computing_fundamentals",
      "complexity": "simple",
      "duration": 20,
      "definition": "Reorganizing data to eliminate fragmentation",
      "examples": [
        "hard drive defragmentation",
        "database compaction",
        "memory cleanup"
      ],
      "analogies": [
        "organizing a messy desk",
        "Marie Kondo for data"
      ],
      "why_matters": "Faster access, less wasted space",
      "related_terms": ["bit_rot", "caching"],
      "visual_style": "before_after_comparison",
      "ascii_scenes": [
        "scattered_files",
        "arrow_transition",
        "organized_files"
      ]
    }
  ]
}
```

---

## CLI Usage

### Single Video Generation

```bash
python pipeline/main.py generate \
  --term idempotency \
  --category computing_fundamentals \
  --output output/videos/
```

### Batch Generation

```bash
# Generate all computing fundamentals
python pipeline/main.py batch \
  --category computing_fundamentals \
  --output output/videos/

# Generate specific terms
python pipeline/main.py batch \
  --terms compaction,idempotency,race_condition \
  --output output/videos/
```

### Custom Configuration

```bash
python pipeline/main.py generate \
  --term technical_debt \
  --config custom_config.yaml \
  --voice alloy \
  --duration 30
```

### Preview Mode (Skip video compilation)

```bash
python pipeline/main.py preview \
  --term cache_invalidation
# Opens browser with script, visuals, estimated timing
```

---

## Workflow Examples

### Example 1: Quick Single Video

```bash
# 1. Edit term config if needed
vim pipeline/config/terms/computing_fundamentals.json

# 2. Generate video
python pipeline/main.py generate --term idempotency

# 3. Review output
open output/videos/idempotency.mp4

# 4. Upload to platforms
```

### Example 2: Batch Production

```bash
# Generate all 13 computing fundamentals
python pipeline/main.py batch \
  --category computing_fundamentals \
  --parallel 4

# Videos appear in output/videos/
# computing_fundamentals_compaction.mp4
# computing_fundamentals_idempotency.mp4
# ... (11 more)
```

### Example 3: Custom Iteration

```bash
# Generate with different voices to compare
for voice in alloy echo fable onyx nova shimmer; do
  python pipeline/main.py generate \
    --term race_condition \
    --voice $voice \
    --output "output/voice_tests/${voice}/"
done
```

---

## Quality Assurance

### Automated Checks

1. **Script Validation**
   - Duration within 15-30s range
   - All required sections present
   - No placeholder text

2. **Visual Validation**
   - All frames generated
   - Proper resolution
   - No corrupted images

3. **Audio Validation**
   - File exists and playable
   - Duration matches script
   - No clipping/distortion

4. **Video Validation**
   - Duration correct
   - Audio/video in sync
   - Text overlays visible
   - Proper encoding

### Manual Review Checklist

- [ ] Script is accurate and clear
- [ ] Examples are relatable
- [ ] ASCII visuals support explanation
- [ ] Narration pacing is natural
- [ ] Key term overlay is readable
- [ ] No technical errors
- [ ] Appropriate for target audience

---

## Optimization Strategies

### Cost Optimization

1. **TTS Caching**
   - Cache generated audio by script hash
   - Reuse if script unchanged
   - Saves on API calls

2. **Parallel Processing**
   - Generate multiple videos concurrently
   - Limit based on API rate limits
   - Use queue system for batches

3. **Incremental Generation**
   - Only regenerate changed components
   - Track modification timestamps
   - Skip unchanged assets

### Performance Optimization

1. **Pre-render Assets**
   - Generate ASCII cow variations once
   - Cache common diagrams
   - Reuse background patterns

2. **Hardware Acceleration**
   - Use GPU for video encoding (NVENC)
   - Parallel frame rendering
   - SSD for temporary files

3. **Lazy Loading**
   - Load assets only when needed
   - Stream video compilation
   - Clean up temp files immediately

---

## Extension Points

### Future Enhancements

1. **AI Script Generation**
   - Use Claude API for script writing
   - Generate variations automatically
   - A/B test different approaches

2. **Interactive Previews**
   - Web UI for reviewing scripts
   - Real-time visual preview
   - Edit and regenerate quickly

3. **Analytics Integration**
   - Track which terms perform best
   - Optimize duration based on engagement
   - Iterate on successful patterns

4. **Multi-Language Support**
   - Translate scripts automatically
   - TTS in different languages
   - Expand audience reach

5. **Style Variations**
   - Multiple visual themes
   - Different cow personalities
   - Seasonal/event-based aesthetics

6. **Social Media Integration**
   - Auto-upload to YouTube/TikTok/Instagram
   - Generate platform-specific metadata
   - Schedule posting times

---

## Dependencies

### Python Packages

```txt
# Core
pillow>=10.0.0          # Image generation
pydub>=0.25.1           # Audio processing
python-dotenv>=1.0.0    # Environment config

# Script Generation
jinja2>=3.1.2           # Template engine
pyyaml>=6.0             # Config parsing
jsonschema>=4.17.0      # Validation

# AI/TTS (optional)
openai>=1.0.0           # OpenAI TTS
elevenlabs>=0.2.0       # Alternative TTS

# Video Compilation
moviepy>=1.0.3          # Video editing (optional)
srt>=3.5.0              # Subtitle generation

# Utilities
tqdm>=4.65.0            # Progress bars
click>=8.1.0            # CLI framework
```

### System Dependencies

```bash
# FFmpeg (required)
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Ubuntu

# ImageMagick (optional, for advanced effects)
brew install imagemagick  # macOS
sudo apt install imagemagick  # Ubuntu
```

---

## Next Steps

1. **Build MVP Pipeline**
   - Script generator (template-based)
   - Basic ASCII visual generator
   - OpenAI TTS integration
   - FFmpeg video compiler

2. **Test with 3 Terms**
   - Idempotency (medium complexity)
   - Technical Debt (high engagement)
   - Compaction (simple, visual)

3. **Iterate Based on Output**
   - Adjust timing
   - Refine visual style
   - Optimize audio quality

4. **Scale to Full Batch**
   - Generate all 13 computing fundamentals
   - Review and refine
   - Prepare for upload

5. **Expand Pipeline**
   - Add Design & Systems
   - Add Data & Statistics
   - Build library of 50+ videos

---

*Production Pipeline Architecture v1.0*
*Designed for automated educational content generation*
