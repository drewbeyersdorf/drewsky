#!/bin/bash
# Quick Start Script for Knowledge Shorts Production Pipeline

set -e  # Exit on error

echo "=================================================="
echo "Knowledge Shorts Production Pipeline - Quick Start"
echo "=================================================="
echo ""

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    echo "Error: Please run this script from the framework_shorts directory"
    exit 1
fi

# Check Python
echo "→ Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "✗ Python not found. Please install Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$($PYTHON --version 2>&1 | awk '{print $2}')
echo "  ✓ Found Python $PYTHON_VERSION"

# Check FFmpeg
echo ""
echo "→ Checking FFmpeg..."
if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version 2>&1 | head -n1 | awk '{print $3}')
    echo "  ✓ Found FFmpeg $FFMPEG_VERSION"
else
    echo "  ✗ FFmpeg not found"
    echo ""
    echo "  Please install FFmpeg:"
    echo "    macOS:   brew install ffmpeg"
    echo "    Linux:   sudo apt install ffmpeg"
    echo ""
    exit 1
fi

# Install Python dependencies
echo ""
echo "→ Installing Python dependencies..."
$PYTHON -m pip install -r requirements.txt --quiet
echo "  ✓ Dependencies installed"

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "→ Creating .env file..."
    cp .env.example .env
    echo "  ✓ Created .env"
    echo ""
    echo "  IMPORTANT: Edit .env and add your OPENAI_API_KEY"
    echo "  Or change tts_provider to 'gtts' in pipeline/config/settings.yaml for free TTS"
fi

# Check dependencies
echo ""
echo "→ Running dependency check..."
$PYTHON pipeline/main.py check-dependencies

# List available terms
echo ""
echo "→ Available terms:"
$PYTHON pipeline/main.py list-terms

# Suggest next steps
echo ""
echo "=================================================="
echo "Setup Complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Configure API key (if using OpenAI TTS):"
echo "   export OPENAI_API_KEY='your-key-here'"
echo ""
echo "2. Generate your first video:"
echo "   python pipeline/main.py generate --term idempotency"
echo ""
echo "3. Preview without compilation (faster):"
echo "   python pipeline/main.py preview --term technical_debt"
echo ""
echo "4. Generate all computing fundamentals:"
echo "   python pipeline/main.py batch --category computing_fundamentals --parallel 2"
echo ""
echo "For more help:"
echo "   python pipeline/main.py --help"
echo "   cat PIPELINE_README.md"
echo ""
