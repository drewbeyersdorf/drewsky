# 🚀 RPI Framework Setup Guide for Claude Code

**Transform Claude Code into a 10x more effective AI assistant**

This guide will help you install the **RPI (Research → Plan → Implement) Framework with Cognitive Enhancements** for Claude Code.

---

## 📖 Table of Contents

1. [What is RPI Framework?](#what-is-rpi-framework)
2. [Why Use It?](#why-use-it)
3. [What You'll Get](#what-youll-get)
4. [Prerequisites](#prerequisites)
5. [Installation Methods](#installation-methods)
   - [Method 1: Quick Install (Recommended)](#method-1-quick-install-recommended)
   - [Method 2: Manual Install](#method-2-manual-install)
6. [Verification](#verification)
7. [Usage Examples](#usage-examples)
8. [Troubleshooting](#troubleshooting)

---

## What is RPI Framework?

The RPI Framework is a structured workflow that forces Claude Code to:

1. **Research** - Explore and understand before coding
2. **Plan** - Create explicit plans with approval gates
3. **Implement** - Execute only after approval

**Plus 4 Cognitive Frameworks:**
- **TCREI** - Validates task clarity (Task, Context, Reference, Evaluation, Input)
- **MAKER** - Decomposes complex tasks into atomic steps
- **CoVe** - Chain of Verification for all claims
- **Confidence Scoring** - Explicit uncertainty management

---

## Why Use It?

### Without RPI Framework ❌
```
You: "Add user authentication"
Claude: [Immediately starts coding]
Claude: [Makes assumptions]
Claude: [Implements something you didn't want]
You: "Wait, that's not what I meant!"
```

### With RPI Framework ✅
```
You: "Add user authentication"
Claude: "TCREI VALIDATION - I need to clarify:
         - What authentication method? (OAuth, JWT, etc.)
         - What's the context? (Why needed now?)
         - What does success look like?"
You: "JWT tokens, because we need API auth, success = secure endpoints"
Claude: "RESEARCH PHASE - Exploring codebase..."
Claude: "Created .research.md - Found auth.ts, verified current setup"
Claude: "PLAN PHASE - Created .plan.md with 6 atomic steps"
You: [Review plan] "Looks good, proceed"
Claude: "IMPLEMENTATION - Step 1/6 complete... Step 2/6 complete..."
```

**Benefits:**
- ✅ No surprise implementations
- ✅ Always get approval before changes
- ✅ Verified claims (no assumptions)
- ✅ Clear confidence scores
- ✅ Atomic, manageable tasks
- ✅ Context window managed automatically

---

## What You'll Get

After installation, Claude Code will:

| Feature | Description |
|---------|-------------|
| **Approval Gates** | Must approve research AND plan before implementation |
| **TCREI Validation** | Asks clarifying questions for vague tasks |
| **Verified Claims** | All statements have file:line references |
| **Confidence Scores** | Every recommendation scored 0-100% |
| **Atomic Steps** | Tasks >30min broken into <30min chunks |
| **Context Monitoring** | Auto-compacts at 40% to stay efficient |
| **No Assumptions** | Verifies by reading actual code |

---

## Prerequisites

- Claude Code CLI installed ([Installation Guide](https://github.com/anthropics/claude-code))
- Basic terminal/command line knowledge
- 5 minutes of your time

---

## Installation Methods

### Method 1: Quick Install (Recommended)

**Step 1: Download the RPI Framework Files**

You need 3 files (your friend will provide these):
- `instructions.md`
- `ENFORCED_RPI_PROTOCOL.md`
- `RPI_STATUS.md`

**Step 2: Choose Installation Scope**

**Option A: Global (All Projects)**
```bash
# Create .claude directory if it doesn't exist
mkdir -p ~/.claude

# Copy the 3 files
cp instructions.md ~/.claude/
cp ENFORCED_RPI_PROTOCOL.md ~/.claude/
cp RPI_STATUS.md ~/.claude/
```

**Option B: Project-Specific (Single Project Only)**
```bash
# Navigate to your project
cd /path/to/your/project

# Create .claude directory
mkdir -p .claude

# Copy the 3 files
cp instructions.md .claude/
cp ENFORCED_RPI_PROTOCOL.md .claude/
cp RPI_STATUS.md .claude/
```

**Step 3: Update Settings (Optional but Recommended)**

Edit `~/.claude/settings.json` (create if doesn't exist):

```json
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
```

**Step 4: Restart Claude Code**

```bash
# If Claude Code is running, restart it
# The framework will auto-load on next session
```

---

### Method 2: Manual Install

**Step 1: Create Directory Structure**

```bash
# For global install
mkdir -p ~/.claude

# OR for project-specific
cd /path/to/project && mkdir -p .claude
```

**Step 2: Create the Files**

The 3 required files will be provided separately:
1. `instructions.md` - Main entry point (auto-loaded by Claude Code)
2. `ENFORCED_RPI_PROTOCOL.md` - Complete protocol rules
3. `RPI_STATUS.md` - Status and testing guide

Place them in your `.claude/` directory (global or project-specific).

**Step 3: Configure Settings**

Add RPI configuration to `~/.claude/settings.json` (see settings above).

---

## Verification

### Test 1: Check Files Installed

```bash
# For global install
ls -l ~/.claude/instructions.md
ls -l ~/.claude/ENFORCED_RPI_PROTOCOL.md
ls -l ~/.claude/RPI_STATUS.md

# For project install
ls -l .claude/instructions.md
ls -l .claude/ENFORCED_RPI_PROTOCOL.md
ls -l .claude/RPI_STATUS.md
```

You should see all 3 files.

### Test 2: Verify Auto-Loading

Start a new Claude Code session:

```bash
claude
```

Give it a vague task:
```
"Add a search feature"
```

**Expected Response:**
```
⚠️ TCREI VALIDATION FAILED

I need the following information to proceed effectively:

Missing Context (Why):
- Why is search needed?
- What problem does this solve?

Missing Evaluation (Success Criteria):
- How will we know this is complete?
- What should the search cover?
...
```

If you see TCREI validation → ✅ **Framework is working!**

### Test 3: Verify Chain of Verification

Ask:
```
"How does the authentication system work?"
```

**Expected Response:**
```
I'm using the RPI workflow for this task.

RESEARCH PHASE:
Launching sub-agents to explore authentication system...
Created .research.md with verified findings.

[Shows file:line references like "Verified by reading auth.ts:45-67"]
```

If you see file:line references → ✅ **CoVe is working!**

---

## Usage Examples

### Example 1: Simple Task (No RPI Needed)

```
You: "What's in this file?"
Claude: [Reads and tells you - RPI skipped for trivial tasks]
```

### Example 2: Feature Request (Full RPI)

```
You: "Add caching to the API"

Claude: "TCREI VALIDATION
         Missing:
         - Context: Why add caching?
         - Evaluation: What's success?
         - Reference: Which APIs should be cached?"

You: "APIs are slow (>2s), success = <500ms, cache product endpoints"

Claude: "RESEARCH PHASE
         Launching sub-agents...
         Created .research.md

         Key findings:
         ✓ Current API in api/products.ts:23-45 (verified)
         ✓ No caching layer exists (verified)
         ✓ Redis already in tech stack (verified package.json:34)

         Confidence: 90%

         Please approve to proceed to planning."

You: "Approved"

Claude: "PLAN PHASE
         Created .plan.md with 5 atomic steps:

         1. Install Redis client [15 min]
         2. Create cache middleware [20 min]
         3. Add cache to product endpoints [25 min]
         4. Add cache invalidation [20 min]
         5. Test cache hit/miss [15 min]

         Confidence: 85%

         Please approve to implement."

You: "Approved"

Claude: "IMPLEMENTATION
         ✓ Step 1/5 complete - Redis client installed
         ✓ Step 2/5 complete - Middleware created
         ..."
```

### Example 3: Low Confidence Scenario

```
You: "Optimize the database queries"

Claude: "⚠️ UNCERTAINTY DETECTED

         Confidence: 45%

         Uncertainties:
         ❓ Which queries are slow? (Need profiling data)
         ❓ What's the performance target?
         ❓ Are there existing indexes?

         Questions:
         1. Have you run query analysis?
         2. What's the current vs target performance?
         3. Which specific endpoints are slow?

         Need these answers to proceed with >70% confidence."
```

---

## Understanding the Workflow

### Phase 0: TCREI Validation
```
IF task is vague:
  → STOP and request clarity
  → Document TCREI elements
```

### Phase 1: Research
```
→ Use sub-agents for exploration
→ Read actual code (verify claims)
→ Create .research.md with:
  - TCREI documentation
  - Verified findings (file:line)
  - Confidence scores
→ STOP for approval
```

### Phase 2: Plan
```
→ Apply MAKER (if >30min task)
→ Create .plan.md with:
  - Atomic steps
  - Code snippets (before/after)
  - Confidence assessment
→ STOP for approval
```

### Phase 3: Implement
```
→ Execute approved plan
→ Report progress per step
→ Monitor context window
→ Create completion snapshot
```

---

## File Outputs You'll See

When working with RPI, Claude creates these files:

| File | When Created | Purpose |
|------|--------------|---------|
| `.research.md` | After research phase | TCREI + verified findings |
| `.plan.md` | After planning phase | Atomic steps + code snippets |
| `.context-snapshot.md` | When context >40% | Context compaction |
| `.completion-snapshot.md` | After implementation | Final summary |

---

## Configuration Options

### Adjusting Thresholds

Edit `~/.claude/settings.json`:

```json
{
  "cognitive_frameworks": {
    "minimum_confidence_threshold": 70,  // Stop if below this
    "stop_and_ask_threshold": 80         // Ask questions if below this
  },
  "context_threshold_warning": 40,       // Warn at 40% context
  "context_threshold_emergency": 60      // Force compact at 60%
}
```

### Override Commands

You can bypass RPI for specific tasks:

```
"Skip research, implement directly: [task]"
"Emergency mode: [task]"
"No RPI: [task]"
```

Claude will warn you but comply.

---

## Troubleshooting

### Issue: Framework Not Loading

**Problem:** Claude doesn't show TCREI validation or approval gates.

**Solutions:**
1. Check files exist:
   ```bash
   ls ~/.claude/instructions.md
   ```
2. Restart Claude Code completely
3. Verify file permissions:
   ```bash
   chmod 644 ~/.claude/instructions.md
   ```

### Issue: Claude Skipping Approval Gates

**Problem:** Claude implements without waiting for approval.

**Solution:**
Say: "Stop. You must wait for my approval after each phase per RPI protocol."

### Issue: Too Many Questions

**Problem:** Claude asks too many TCREI questions for simple tasks.

**Solution:**
Provide more context upfront:
```
Instead of: "Fix the bug"
Say: "Fix the authentication bug in auth.ts that's causing 401 errors on /login endpoint. Success = users can log in."
```

### Issue: Files Not Found

**Problem:** Claude says it can't find `ENFORCED_RPI_PROTOCOL.md`.

**Solution:**
Ensure all 3 files are in the same directory:
```bash
ls ~/.claude/*.md
```

---

## Advanced: Project-Specific Overrides

You can have different RPI settings per project:

1. **Global settings** in `~/.claude/` (default for all projects)
2. **Project settings** in `/your/project/.claude/` (overrides global)

Claude Code loads in this order:
1. Global `~/.claude/instructions.md`
2. Project `.claude/instructions.md` (if exists, overrides global)

---

## Uninstalling

To remove the RPI framework:

```bash
# Global uninstall
rm ~/.claude/instructions.md
rm ~/.claude/ENFORCED_RPI_PROTOCOL.md
rm ~/.claude/RPI_STATUS.md

# Optionally remove RPI settings from ~/.claude/settings.json
```

---

## FAQ

**Q: Does this slow down Claude?**
A: For trivial tasks (like "read this file"), RPI is automatically skipped. For complex tasks, the upfront research/planning saves time by preventing mistakes.

**Q: Can I disable it temporarily?**
A: Yes, use override commands: "Skip RPI: [your task]"

**Q: What if I just want to experiment?**
A: Say "Emergency mode" and Claude will skip RPI with a warning.

**Q: Does this work with all Claude Code versions?**
A: Yes, as long as your Claude Code supports `.claude/instructions.md` auto-loading (v0.2.0+).

**Q: Can I customize the protocol?**
A: Yes! Edit `ENFORCED_RPI_PROTOCOL.md` to adjust rules, thresholds, or add your own requirements.

---

## Support & Questions

If you run into issues:

1. Read the `RPI_STATUS.md` file for verification tests
2. Check the `ENFORCED_RPI_PROTOCOL.md` for detailed rules
3. Ask Claude: "Am I operating under RPI protocol?"

---

## Credits

Created by: [Your Name]
Version: 1.0
Last Updated: 2025-12-07

---

## What's Next?

After installation:

1. ✅ Test with the verification steps above
2. ✅ Try a real task and experience the workflow
3. ✅ Adjust confidence thresholds if needed
4. ✅ Share with other developers!

**Welcome to 10x more effective AI collaboration!** 🚀
