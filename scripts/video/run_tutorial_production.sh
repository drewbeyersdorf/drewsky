#!/bin/bash
# RPI Framework Tutorial - Master Production Script
# Runs complete FREE production workflow using Gemini 2.0 Flash API
# Total cost: $0

set -e  # Exit on error

echo "============================================================"
echo "  RPI Framework Tutorial - FREE Production Workflow"
echo "  Using: Gemini 2.0 Flash API + Free Tools"
echo "============================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Gemini API key is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo -e "${RED}❌ ERROR: GEMINI_API_KEY environment variable not set!${NC}"
    echo ""
    echo "Get your free API key at: https://aistudio.google.com/"
    echo ""
    echo "Then set it:"
    echo "  export GEMINI_API_KEY='your-key-here'"
    echo ""
    echo "Or add to your ~/.bashrc or ~/.zshrc"
    exit 1
fi

echo -e "${GREEN}✓ Gemini API key found${NC}"
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ ERROR: python3 not found!${NC}"
    echo "Install Python 3: https://www.python.org/downloads/"
    exit 1
fi

echo -e "${GREEN}✓ Python 3 found${NC}"
echo ""

# Check for google-generativeai package
echo "Checking for required Python packages..."
if ! python3 -c "import google.generativeai" &> /dev/null; then
    echo -e "${YELLOW}⚠ google-generativeai not installed${NC}"
    echo "Installing now..."
    pip3 install google-generativeai
    echo -e "${GREEN}✓ Installed google-generativeai${NC}"
else
    echo -e "${GREEN}✓ google-generativeai already installed${NC}"
fi

echo ""
echo "============================================================"
echo "  Step 1: Generate Voice Narration"
echo "============================================================"
echo ""
echo "Running: python3 generate_voice_narration.py"
echo ""

python3 generate_voice_narration.py

echo ""
echo "============================================================"
echo "  Step 2: Generate Scene Descriptions"
echo "============================================================"
echo ""
echo "Running: python3 generate_scene_descriptions.py"
echo ""

python3 generate_scene_descriptions.py

echo ""
echo "============================================================"
echo "  ✓ Automation Complete!"
echo "============================================================"
echo ""
echo -e "${GREEN}Generated files:${NC}"
echo "  📁 voice_files/ - Narration text (copy to SPEECHMA for voice)"
echo "  📁 scene_descriptions/ - Visual descriptions for Canva"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo ""
echo "1. Voice Generation (Choose one):"
echo "   a) Copy narration text to SPEECHMA (100% free)"
echo "      → https://speechma.com/english"
echo "   OR"
echo "   b) Use any other free TTS tool"
echo ""
echo "2. Video Animation:"
echo "   → Open Canva: https://www.canva.com/create/animated-videos/"
echo "   → Follow: scene_descriptions/CANVA_IMPLEMENTATION_GUIDE.md"
echo "   → Use visual descriptions from scene_descriptions/*.md"
echo ""
echo "3. Review full guides:"
echo "   → FREE_PRODUCTION_GUIDE.md (complete workflow)"
echo "   → TUTORIAL_QUICK_START.md (fast track)"
echo ""
echo "============================================================"
echo "  🎥 Ready to create your tutorial video!"
echo "  Total cost: \$0 | Time estimate: 4-5 hours"
echo "============================================================"
echo ""
