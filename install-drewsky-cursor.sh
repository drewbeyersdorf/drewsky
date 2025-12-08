#!/bin/bash

# drewsky Framework Installer for Cursor
# This script installs the drewsky (Research-Plan-Implement) framework for Cursor

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════╗"
echo "║                                                       ║"
echo "║         drewsky Framework Installer for Cursor       ║"
echo "║                                                       ║"
echo "║   Research → Plan → Implement with AI assistance     ║"
echo "║                                                       ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Check if .cursorrules exists in current directory
CURSORRULES_SOURCE=".cursorrules"

if [ ! -f "$CURSORRULES_SOURCE" ]; then
    echo -e "${RED}Error: .cursorrules file not found in current directory${NC}"
    echo "Please run this script from the drewsky_Framework_Package directory"
    exit 1
fi

echo -e "${BLUE}drewsky Framework Installation Options:${NC}"
echo ""
echo "1) Install in current project (recommended)"
echo "   - Installs .cursorrules in current directory"
echo "   - Only active in this project"
echo ""
echo "2) Install globally for all projects"
echo "   - Installs .cursorrules in home directory"
echo "   - Active in all Cursor projects"
echo ""
echo "3) Install in specific project directory"
echo "   - You specify the path"
echo "   - Only active in that project"
echo ""
echo "4) Exit"
echo ""

read -p "Choose installation type (1-4): " choice

case $choice in
    1)
        echo ""
        echo -e "${BLUE}Installing in current project...${NC}"

        # Get current directory (where user ran the script from)
        INSTALL_DIR="$(pwd)"

        # Don't install if we're in the package directory itself
        if [ -f "$INSTALL_DIR/.cursorrules" ] && [ "$(basename $INSTALL_DIR)" = "drewsky_Framework_Package" ]; then
            echo -e "${YELLOW}Warning: You're in the package directory. Installing in parent directory.${NC}"
            INSTALL_DIR="$(dirname $INSTALL_DIR)"
        fi

        # Copy .cursorrules
        cp "$CURSORRULES_SOURCE" "$INSTALL_DIR/.cursorrules"

        echo ""
        echo -e "${GREEN}✓ Installation complete!${NC}"
        echo ""
        echo "drewsky framework installed at:"
        echo "  $INSTALL_DIR/.cursorrules"
        echo ""
        echo -e "${BLUE}Next steps:${NC}"
        echo "1. Open this project in Cursor"
        echo "2. Test by asking: 'Add a search feature'"
        echo "3. If Cursor asks TCREI questions, it's working!"
        ;;

    2)
        echo ""
        echo -e "${BLUE}Installing globally...${NC}"

        # Install in home directory
        cp "$CURSORRULES_SOURCE" "$HOME/.cursorrules"

        echo ""
        echo -e "${GREEN}✓ Global installation complete!${NC}"
        echo ""
        echo "drewsky framework installed at:"
        echo "  $HOME/.cursorrules"
        echo ""
        echo -e "${YELLOW}Note: This will apply to ALL Cursor projects${NC}"
        echo ""
        echo -e "${BLUE}Next steps:${NC}"
        echo "1. Restart Cursor"
        echo "2. Open any project"
        echo "3. Test by asking: 'Add a search feature'"
        ;;

    3)
        echo ""
        read -p "Enter project directory path: " project_path

        # Expand ~ to home directory
        project_path="${project_path/#\~/$HOME}"

        # Check if directory exists
        if [ ! -d "$project_path" ]; then
            echo -e "${RED}Error: Directory does not exist: $project_path${NC}"
            exit 1
        fi

        echo ""
        echo -e "${BLUE}Installing in specified project...${NC}"

        # Copy .cursorrules
        cp "$CURSORRULES_SOURCE" "$project_path/.cursorrules"

        echo ""
        echo -e "${GREEN}✓ Installation complete!${NC}"
        echo ""
        echo "drewsky framework installed at:"
        echo "  $project_path/.cursorrules"
        echo ""
        echo -e "${BLUE}Next steps:${NC}"
        echo "1. Open $project_path in Cursor"
        echo "2. Test by asking: 'Add a search feature'"
        ;;

    4)
        echo ""
        echo "Installation cancelled."
        exit 0
        ;;

    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}drewsky framework is now installed!${NC}"
echo ""
echo "📖 Read CURSOR_SETUP_GUIDE.md for detailed usage"
echo "🧪 Test with these scenarios:"
echo "   - 'Add a search feature' (tests TCREI)"
echo "   - 'How does auth work?' (tests verification)"
echo "   - 'Refactor database layer' (tests MAKER)"
echo ""
echo "💡 Override with: 'Skip drewsky: [task]'"
echo ""
echo "📊 What drewsky provides:"
echo "   ✓ Research before implementing"
echo "   ✓ Explicit plans with approval gates"
echo "   ✓ Verified claims (file:line references)"
echo "   ✓ Confidence scoring (0-100%)"
echo "   ✓ Atomic step breakdowns"
echo ""
echo "🔗 Full docs: https://github.com/drewbeyersdorf/agent-improvement-techniques"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════${NC}"
echo ""
