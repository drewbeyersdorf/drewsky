# Knowledge Shorts Production Pipeline

Automated system for generating educational short-form videos with ASCII cow aesthetic.

## Quick Start

### 1. Installation

```bash
# Install Python dependencies
cd framework_shorts
pip install -r requirements.txt

# Install system dependencies
# macOS:
brew install ffmpeg

# Linux (Ubuntu/Debian):
sudo apt install ffmpeg

# Check all dependencies
python pipeline/main.py check-dependencies
```

### 2. Configuration

```bash
# Set up API keys (if using OpenAI TTS)
export OPENAI_API_KEY="your-api-key-here"

# Or use free Google TTS by editing pipeline/config/settings.yaml:
# Change: tts_provider: "gtts"
```

### 3. Generate Your First Video

```bash
# Generate a single video
python pipeline/main.py generate --term idempotency

# Preview without full compilation
python pipeline/main.py preview --term idempotency

# List all available terms
python pipeline/main.py list-terms
```

## Usage

### Generate Single Video

```bash
python pipeline/main.py generate \
  --term <term_id> \
  --category computing_fundamentals \
  --output output/videos/
```

**Example:**
```bash
python pipeline/main.py generate --term technical_debt
```

### Generate Multiple Videos (Batch)

```bash
# Generate all terms in a category
python pipeline/main.py batch --category computing_fundamentals

# Generate specific terms
python pipeline/main.py batch \
  --category computing_fundamentals \
  --terms compaction,idempotency,race_condition

# Use parallel processing (faster)
python pipeline/main.py batch \
  --category computing_fundamentals \
  --parallel 4
```

### Preview Mode (Faster Testing)

```bash
# Generate script and visuals only (no video compilation)
python pipeline/main.py preview --term cache_invalidation
```

This creates:
- Script markdown file
- Visual scene images
- HTML preview page

### List All Terms

```bash
python pipeline/main.py list-terms
```

## Configuration

### Global Settings

Edit `pipeline/config/settings.yaml` to customize:

#### Video Settings
```yaml
video:
  resolution:
    width: 1080
    height: 1920  # 9:16 vertical
  fps: 30
  format: "mp4"
```

#### Audio Settings
```yaml
audio:
  tts_provider: "openai"  # or "gtts" for free alternative
  voice: "nova"  # OpenAI voices: alloy, echo, fable, onyx, nova, shimmer
```

#### Visual Settings
```yaml
visual:
  colors:
    background: "#0a0a0a"  # Near black
    text_primary: "#00ff00"  # Matrix green
    accent: "#ff6b35"  # Orange
```

### Term Configuration

Terms are defined in `pipeline/config/terms/computing_fundamentals.json`:

```json
{
  "id": "idempotency",
  "name": "Idempotency",
  "complexity": "medium",
  "duration": 25,
  "definition": "Operation that produces same result if repeated",
  "hook": "Press a button once, twice, 100 times...",
  "explanation": "Like a light switch - always the same result",
  "example": "If your payment button isn't idempotent, clicking twice charges you twice",
  "why_matters": "Idempotent systems are safe to retry",
  "on_screen_text": "Idempotency = Same action, same result, every time"
}
```

## Output Structure

```
output/
├── scripts/           # Generated scripts (MD + JSON)
│   ├── idempotency_script.md
│   └── idempotency_script.json
├── visuals/           # Scene images
│   └── idempotency/
│       ├── scene_01_title.png
│       ├── scene_02_hook.png
│       ├── scene_03_main.png
│       ├── scene_04_definition.png
│       └── preview.html
├── audio/            # Generated narration
│   ├── idempotency_narration.mp3
│   └── cache/        # Cached TTS audio
└── videos/           # Final videos
    └── computing_fundamentals_idempotency.mp4
```

## Available Commands

### Main Commands

| Command | Description |
|---------|-------------|
| `generate` | Generate a single video |
| `batch` | Generate multiple videos |
| `preview` | Generate preview (no compilation) |
| `list-terms` | List all available terms |
| `check-dependencies` | Verify installations |

### Generate Options

```
--term TEXT        Term ID to generate [required]
--category TEXT    Term category [default: computing_fundamentals]
--output PATH      Output directory
--config PATH      Custom config file
```

### Batch Options

```
--category TEXT    Term category [required]
--terms TEXT       Comma-separated term IDs (or all if omitted)
--output PATH      Output directory
--parallel INT     Number of parallel jobs [default: 1]
--config PATH      Custom config file
```

## Complete Computing Fundamentals Example

Generate all 13 computing fundamentals videos:

```bash
# Sequential (slower, but safer)
python pipeline/main.py batch --category computing_fundamentals

# Parallel (faster, uses more resources)
python pipeline/main.py batch \
  --category computing_fundamentals \
  --parallel 4
```

Generate specific high-priority terms:

```bash
python pipeline/main.py batch \
  --category computing_fundamentals \
  --terms technical_debt,race_condition,idempotency,cache_invalidation \
  --parallel 2
```

## Customization

### Using Different TTS Voices

```bash
# Edit settings.yaml to change voice
audio:
  voice: "alloy"  # Options: alloy, echo, fable, onyx, nova, shimmer
```

Or use free Google TTS:

```bash
audio:
  tts_provider: "gtts"  # No API key needed
```

### Custom Video Style

```bash
# Edit settings.yaml
visual:
  colors:
    background: "#000000"  # Pure black
    text_primary: "#ffffff"  # White text
    accent: "#00ffff"  # Cyan accent
```

### Adding New Terms

1. Edit `pipeline/config/terms/computing_fundamentals.json`
2. Add new term object:

```json
{
  "id": "your_term",
  "name": "Your Term",
  "complexity": "simple",
  "duration": 20,
  "definition": "Clear definition",
  "hook": "Attention-grabbing opening",
  "explanation": "Detailed explanation",
  "example": "Concrete example",
  "why_matters": "Why it's important",
  "on_screen_text": "Your Term = Definition"
}
```

3. Generate:

```bash
python pipeline/main.py generate --term your_term
```

## Performance Tips

### Speed Optimization

1. **Use parallel processing for batches:**
   ```bash
   python pipeline/main.py batch --category computing_fundamentals --parallel 4
   ```

2. **Enable TTS caching (on by default):**
   - Reuses audio for unchanged scripts
   - Saves API costs and time

3. **Use preview mode during development:**
   ```bash
   python pipeline/main.py preview --term test_term
   ```

### Cost Optimization (OpenAI TTS)

- **Caching:** First generation costs $, subsequent are free
- **Batch processing:** More efficient than one-by-one
- **Free alternative:** Use `tts_provider: "gtts"` (lower quality)

**Estimated costs:**
- 25-second video script ≈ 150 words ≈ $0.002 per generation
- 13 videos (first time) ≈ $0.026
- Regenerating cached videos ≈ $0

## Troubleshooting

### "FFmpeg not found"

```bash
# Install FFmpeg
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
```

### "OpenAI API key not found"

```bash
export OPENAI_API_KEY="your-key-here"

# Or switch to free Google TTS in settings.yaml:
audio:
  tts_provider: "gtts"
```

### "Permission denied" when running main.py

```bash
chmod +x pipeline/main.py
```

### Videos are too slow to generate

```bash
# Use parallel processing
python pipeline/main.py batch --category computing_fundamentals --parallel 4

# Or reduce video quality in settings.yaml:
video:
  quality: "medium"  # Instead of "high"
```

### Audio doesn't sync with video

This usually means the script timing doesn't match audio duration. The pipeline automatically adjusts, but you can manually tune:

```yaml
timing:
  # Adjust section proportions
```

## Architecture

The pipeline consists of 5 main components:

1. **Script Generator** (`script_generator.py`)
   - Loads term config
   - Generates structured scripts
   - Calculates timing

2. **Visual Generator** (`visual_generator.py`)
   - Creates ASCII art scenes
   - Generates PNG image sequence
   - Builds preview HTML

3. **Audio Generator** (`audio_generator.py`)
   - Generates TTS narration
   - Caches audio for reuse
   - Optional background music

4. **Video Compiler** (`video_compiler.py`)
   - Assembles scenes into video
   - Syncs audio
   - Adds text overlays

5. **Main Orchestrator** (`main.py`)
   - CLI interface
   - Coordinates all components
   - Handles batch processing

## Next Steps

1. **Generate sample videos:**
   ```bash
   python pipeline/main.py generate --term idempotency
   python pipeline/main.py generate --term technical_debt
   python pipeline/main.py generate --term race_condition
   ```

2. **Review and iterate:**
   - Check `output/videos/` for generated videos
   - Adjust settings in `pipeline/config/settings.yaml`
   - Modify term configs in `pipeline/config/terms/`

3. **Generate full batch:**
   ```bash
   python pipeline/main.py batch --category computing_fundamentals --parallel 4
   ```

4. **Upload to platforms:**
   - Videos are ready for TikTok, YouTube Shorts, Instagram Reels
   - 9:16 aspect ratio, 15-30s duration
   - Include hashtags: #ComputerScience #TechEducation #LearnToCode

## Support

For issues or questions:
- Check `PRODUCTION_PIPELINE_ARCHITECTURE.md` for detailed technical docs
- Review `pipeline/config/settings.yaml` for all options
- Run `python pipeline/main.py --help` for CLI help

---

**Current Status:** Production-ready pipeline for Computing Fundamentals (13 terms)

**Next:** Design & Systems, Data & Statistics (25 more terms each)
