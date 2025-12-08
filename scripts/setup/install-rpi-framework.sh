#!/bin/bash

# RPI Framework Installer for Claude Code
# Version 1.0

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                            ║${NC}"
echo -e "${BLUE}║       RPI Framework Installer for Claude Code             ║${NC}"
echo -e "${BLUE}║       Research → Plan → Implement + Cognitive Frameworks  ║${NC}"
echo -e "${BLUE}║                                                            ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if running from the correct directory
if [ ! -f "instructions.md" ] || [ ! -f "ENFORCED_RPI_PROTOCOL.md" ]; then
    echo -e "${RED}❌ Error: Required files not found!${NC}"
    echo ""
    echo "Please run this script from the directory containing:"
    echo "  - instructions.md"
    echo "  - ENFORCED_RPI_PROTOCOL.md"
    echo "  - RPI_STATUS.md"
    echo ""
    exit 1
fi

# Ask installation type
echo -e "${YELLOW}Choose installation scope:${NC}"
echo ""
echo "  1) Global (all Claude Code sessions everywhere)"
echo "  2) Project-specific (current directory only)"
echo ""
read -p "Enter choice [1 or 2]: " choice

case $choice in
    1)
        INSTALL_DIR="$HOME/.claude"
        SCOPE="global"
        echo ""
        echo -e "${GREEN}Installing globally to: $INSTALL_DIR${NC}"
        ;;
    2)
        INSTALL_DIR="$(pwd)/.claude"
        SCOPE="project"
        echo ""
        echo -e "${GREEN}Installing to current project: $INSTALL_DIR${NC}"
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

# Create directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

echo ""
echo -e "${BLUE}📦 Installing RPI Framework files...${NC}"
echo ""

# Copy files
echo "  → Copying instructions.md..."
cp instructions.md "$INSTALL_DIR/"

echo "  → Copying ENFORCED_RPI_PROTOCOL.md..."
cp ENFORCED_RPI_PROTOCOL.md "$INSTALL_DIR/"

echo "  → Copying RPI_STATUS.md..."
cp RPI_STATUS.md "$INSTALL_DIR/"

# Check if settings.json exists
SETTINGS_FILE="$INSTALL_DIR/settings.json"

if [ -f "$SETTINGS_FILE" ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Existing settings.json found.${NC}"
    echo ""
    read -p "Do you want to backup and update it? [y/N]: " backup_choice

    if [[ $backup_choice =~ ^[Yy]$ ]]; then
        BACKUP_FILE="$SETTINGS_FILE.backup.$(date +%Y%m%d_%H%M%S)"
        echo "  → Backing up to: $BACKUP_FILE"
        cp "$SETTINGS_FILE" "$BACKUP_FILE"

        # Create updated settings (you may want to merge instead)
        echo "  → Adding RPI configuration to settings.json..."
        cat > "$SETTINGS_FILE" << 'EOF'
{
  "enforced_rpi": true,
  "context_threshold_warning": 40,
  "context_threshold_emergency": 60,
  "require_plan_approval": true,
  "require_research_approval": true,
  "auto_compact_enabled": true,
  "sub_agent_for_exploration": true,
  "cognitive_frameworks": {
    "tcrei_validation": true,
    "maker_decomposition": true,
    "chain_of_verification": true,
    "confidence_scoring": true,
    "minimum_confidence_threshold": 70,
    "stop_and_ask_threshold": 80
  },
  "minimum_plan_quality": {
    "code_snippets_required": true,
    "testing_procedure_required": true,
    "file_line_references_required": true,
    "tcrei_documentation_required": true,
    "verification_statements_required": true,
    "confidence_assessment_required": true,
    "atomic_steps_required_for_30min_tasks": true
  },
  "forbidden_behaviors": [
    "implement_without_plan",
    "skip_research_for_complex_tasks",
    "add_unrequested_features",
    "assume_without_reading_code",
    "proceed_with_missing_tcrei",
    "make_unverified_claims",
    "skip_confidence_scoring",
    "proceed_below_confidence_threshold"
  ],
  "output_files": {
    "research": ".research.md",
    "plan": ".plan.md",
    "context_snapshot": ".context-snapshot.md",
    "completion": ".completion-snapshot.md"
  },
  "quality_gates": {
    "research": {
      "tcrei_complete": true,
      "all_claims_verified": true,
      "confidence_scores_assigned": true,
      "no_unverified_assumptions": true
    },
    "plan": {
      "maker_decomposition_applied": true,
      "atomic_steps_only": true,
      "confidence_assessment_included": true,
      "minimum_confidence": 70
    }
  }
}
EOF
        echo -e "${GREEN}  ✓ Settings updated${NC}"
        echo -e "${YELLOW}  Note: Manual merge may be needed if you had custom settings${NC}"
    else
        echo "  → Skipping settings.json update"
    fi
else
    echo "  → Creating settings.json..."
    cat > "$SETTINGS_FILE" << 'EOF'
{
  "enforced_rpi": true,
  "context_threshold_warning": 40,
  "context_threshold_emergency": 60,
  "require_plan_approval": true,
  "require_research_approval": true,
  "auto_compact_enabled": true,
  "sub_agent_for_exploration": true,
  "cognitive_frameworks": {
    "tcrei_validation": true,
    "maker_decomposition": true,
    "chain_of_verification": true,
    "confidence_scoring": true,
    "minimum_confidence_threshold": 70,
    "stop_and_ask_threshold": 80
  }
}
EOF
    echo -e "${GREEN}  ✓ Settings created${NC}"
fi

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                            ║${NC}"
echo -e "${GREEN}║       ✅ RPI Framework Installed Successfully!             ║${NC}"
echo -e "${GREEN}║                                                            ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Installation summary
echo -e "${BLUE}📋 Installation Summary:${NC}"
echo ""
echo -e "  Scope:     ${GREEN}$SCOPE${NC}"
echo -e "  Location:  ${GREEN}$INSTALL_DIR${NC}"
echo ""
echo "  Files installed:"
echo "    ✓ instructions.md"
echo "    ✓ ENFORCED_RPI_PROTOCOL.md"
echo "    ✓ RPI_STATUS.md"
echo "    ✓ settings.json"
echo ""

# Verification
echo -e "${BLUE}🧪 Quick Verification:${NC}"
echo ""
echo "  Run these commands to verify:"
echo "    ls -l $INSTALL_DIR/*.md"
echo ""

# Next steps
echo -e "${YELLOW}📚 Next Steps:${NC}"
echo ""
echo "  1. Restart Claude Code (if currently running)"
echo "  2. Start a new session and test with:"
echo "     → 'Add a search feature' (should ask TCREI questions)"
echo "  3. Read RPI_STATUS.md for testing procedures:"
echo "     → cat $INSTALL_DIR/RPI_STATUS.md"
echo ""

if [ "$SCOPE" == "global" ]; then
    echo -e "${GREEN}The RPI Framework will now activate in ALL Claude Code sessions!${NC}"
else
    echo -e "${GREEN}The RPI Framework will activate when working in this project directory.${NC}"
fi

echo ""
echo -e "${BLUE}For help and documentation:${NC}"
echo "  → Read RPI_FRAMEWORK_SETUP_GUIDE.md"
echo "  → Ask Claude: 'Am I operating under RPI protocol?'"
echo ""
echo -e "${GREEN}Happy coding with enhanced AI collaboration! 🚀${NC}"
echo ""
