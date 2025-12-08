---
description: Check drewsky Framework installation status and verify all components are present
---

# drewsky Framework Status Check

Verify drewsky Framework installation and report current configuration status.

## Task

Check that all framework components are properly installed and ready to use.

## Verification Steps

### 1. Directory Structure
Check these directories exist:
```
✓ docs/core/          - Core drewsky documentation
✓ docs/tutorials/     - Tutorial guides
✓ docs/sessions/      - Session files
✓ scripts/            - Utility scripts
✓ output/             - Generated content
```

### 2. Core Documentation Files
Verify critical files are present:
```
✓ README.md                           - Main documentation
✓ docs/core/ENFORCED_drewsky_PROTOCOL.md  - Core protocol rules
✓ docs/core/drewsky_FRAMEWORK_SETUP_GUIDE.md - Setup guide
✓ docs/core/OPERATIONAL_LOGIC_INTEGRATION.md - Logic integration
✓ docs/core/V2_INTEGRATION_SUMMARY.md - Research enhancements
```

### 3. Command Files
Check that all CLI commands are available:
```
✓ .claude/commands/drewsky-init.md    - Framework initialization
✓ .claude/commands/tcrei.md       - TCREI validation
✓ .claude/commands/maker.md       - MAKER decomposition
✓ .claude/commands/verify.md      - Chain of Verification
✓ .claude/commands/plan.md        - Dual-loop planning
✓ .claude/commands/drewsky-help.md    - Command reference
✓ .claude/commands/drewsky-status.md  - This file
✓ .claude/commands/drewsky-enforce.md - Protocol enforcement
```

### 4. Framework Version
Check and report:
- Current version (v2.0 with research enhancements)
- Research integrations active (Meta AI, Microsoft, Stanford, Google DeepMind)

### 5. Git Status (if applicable)
If in a git repository:
- Current branch
- Any uncommitted changes
- Sync status with remote

## Output Format

Present results as:

```
📊 drewsky Framework Status Report

Installation:
✅ Directory structure: Complete (5/5)
✅ Core documentation: Complete (5/5)
✅ CLI commands: Complete (8/8)

Framework Version: v2.0
Research Enhancements Active:
  ✅ Meta AI - Chain of Verification (CoVe)
  ✅ Microsoft - Magentic-One Dual-Loop Planning
  ✅ Stanford/SambaNova - Reflective Learning
  ✅ Google DeepMind - AlphaEvolve Optimization

Git Repository: [status if applicable]

Status: ✅ Ready to use

Available Commands:
  • /drewsky-init - Initialize framework
  • /tcrei - Apply TCREI validation
  • /maker - Apply MAKER decomposition
  • /verify - Apply Chain of Verification
  • /plan - Apply Dual-Loop Planning
  • /drewsky-help - Show all commands

Next Steps:
  → Run /drewsky-init to activate framework for this session
  → Run /drewsky-help to see command reference
  → See README.md for complete documentation
```

## Troubleshooting

If components are missing:
1. Verify you're in the correct directory: `pwd`
2. Check README.md for setup instructions
3. Review docs/core/drewsky_FRAMEWORK_SETUP_GUIDE.md
4. Ensure .claude/commands/ directory exists
