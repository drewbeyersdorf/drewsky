# drewsky Framework for Cursor - Setup Guide

**Transform Cursor into a 10x more effective AI coding assistant**

This guide shows you how to install the drewsky (Research-Plan-Implement) framework in Cursor.

---

## 🎯 What is drewsky?

drewsky is a research-backed AI collaboration framework that ensures:
- ✅ Research before implementing (no surprises)
- ✅ Explicit plans with approval gates (you stay in control)
- ✅ Verified claims with file:line references (no hallucinations)
- ✅ Confidence scoring (know when AI is uncertain)
- ✅ Atomic step breakdowns (manageable complexity)

**Based on research from**: Meta AI, Microsoft, Stanford, Google DeepMind

---

## ⚡ Quick Start (2 minutes)

### Option 1: Automatic Installation (Recommended)

```bash
cd your-project
curl -o .cursorrules https://raw.githubusercontent.com/drewbeyersdorf/agent-improvement-techniques/main/.cursorrules
```

Or use our installer:

```bash
cd path/to/drewsky_Framework_Package
./install-drewsky-cursor.sh
```

### Option 2: Manual Installation

1. **Download** the `.cursorrules` file from this package
2. **Copy** it to your project root:
   ```bash
   cp .cursorrules /path/to/your/project/
   ```
3. **Restart** Cursor
4. **Test** it by asking: "Add a search feature"

✅ **If Cursor asks TCREI questions (Task, Context, etc.), it's working!**

---

## 🔧 Installation Options

### Per-Project Installation (Recommended)
Install drewsky in specific projects where you need it:

```bash
# In your project directory
cp /path/to/drewsky_Framework_Package/.cursorrules .
```

**Pros:**
- Only active in projects where you want it
- Can customize per project
- Easy to remove (just delete .cursorrules)

### Global Installation (Advanced)
Install once, use everywhere:

```bash
# Copy to your home directory (Cursor reads this for all projects)
cp /path/to/drewsky_Framework_Package/.cursorrules ~/.cursorrules
```

**Pros:**
- Works in all projects automatically
- One installation for everything

**Cons:**
- Always active (no selective use)
- Harder to customize per project

---

## 📖 How It Works

### Before drewsky ❌
```
You: "Add user authentication"
Cursor: [Immediately writes code]
You: "That's not what I wanted!"
```

### After drewsky ✅
```
You: "Add user authentication"
Cursor: "I'll research this before implementing.

TCREI Validation:
- Task: What authentication method? (JWT, session, OAuth?)
- Context: Why is this needed?
- Evaluation: What defines success?"

You: [Provides clarity]
Cursor: "Research complete - here's what I found [verified]"
Cursor: "Plan created - 6 atomic steps, approve?"
You: "Approved"
Cursor: [Implements step by step with progress updates]
```

---

## 🧪 Testing Your Installation

### Test 1: TCREI Validation
```
You: "Add a search feature"
Expected: Cursor asks for Context, Evaluation criteria
```

### Test 2: Chain of Verification
```
You: "How does authentication work in this codebase?"
Expected: Cursor provides file:line references
```

### Test 3: MAKER Decomposition
```
You: "Refactor the database layer"
Expected: Cursor breaks into atomic steps, asks for approval
```

### Test 4: Confidence Scoring
```
You: "Should we use Redis or Memcached?"
Expected: Cursor provides recommendation with confidence score
```

---

## 🎓 Key Features

Once installed, Cursor will automatically:

✅ **Ask clarifying questions** when tasks are vague (TCREI)
✅ **Research before implementing** (reads actual files)
✅ **Create explicit plans** with code snippets
✅ **Wait for your approval** before making changes
✅ **Verify all claims** with file:line references
✅ **Score confidence** on recommendations (0-100%)
✅ **Break complex tasks** into atomic steps (<30 min each)
✅ **Run actual tests** (never hallucinate results)

---

## 📁 Generated Files

drewsky will create these files in your project:

| File | Purpose |
|------|---------|
| `.research.md` | Research findings with TCREI validation |
| `.plan.md` | Implementation plan with Task/Progress Ledgers |
| `.completion-snapshot.md` | Post-implementation summary |

**Tip**: Add these to `.gitignore` if you don't want to commit them:
```bash
echo ".research.md" >> .gitignore
echo ".plan.md" >> .gitignore
echo ".completion-snapshot.md" >> .gitignore
```

---

## 🔄 The Complete Workflow

### Example: "Add caching to improve API performance"

**1. Research Phase**
```
Cursor: "I'll research before implementing.

TCREI Validation:
- Task: Add caching to slow API endpoints
- Context: Which APIs? Current response times?
- Evaluation: Target performance?

Let me explore the codebase..."

[Cursor reads files, verifies claims]

Cursor: "Research complete. Findings:
✓ Product API in api/products.ts:45-67 (verified)
✓ No caching layer exists (verified)
✓ Redis in package.json (verified)

Confidence: 90%

Created .research.md for review.
Approve to proceed to planning?"
```

**2. Planning Phase**
```
You: "Approved"

Cursor: "Plan created with 5 atomic steps:

1. Install Redis client [15 min]
2. Create cache middleware [20 min]
3. Add to product endpoints [25 min]
4. Add cache invalidation [20 min]
5. Test performance [15 min]

Overall confidence: 85%

Created .plan.md with full details.
Approve to implement?"
```

**3. Implementation Phase**
```
You: "Approved"

Cursor: "Implementing...

✓ Step 1/5 complete - Redis client installed
  Tests: PASSED (exit code 0)

✓ Step 2/5 complete - Middleware created
  Tests: PASSED (exit code 0)

✓ Step 3/5 complete - Endpoints cached
  Tests: PASSED (exit code 0)

✓ Step 4/5 complete - Invalidation added
  Tests: PASSED (exit code 0)

✓ Step 5/5 complete - Performance tested
  Result: 2s → 380ms ✓
  Tests: PASSED (exit code 0)

Created .completion-snapshot.md"
```

---

## 💡 Override Commands

Need to bypass drewsky for a quick task?

```
"Skip drewsky: [your task]"
"Emergency mode: [your task]"
"No plan needed: [your task]"
```

Cursor will warn you but comply.

---

## 🚫 Uninstalling

### Per-Project
```bash
rm .cursorrules
```

### Global
```bash
rm ~/.cursorrules
```

Restart Cursor to complete uninstallation.

---

## ⚙️ Customization

You can edit `.cursorrules` to customize:

**Confidence thresholds:**
- Change `<70%` threshold for when AI should stop and ask

**Step size:**
- Change `<30 min` atomic step duration

**File names:**
- Change `.research.md`, `.plan.md` to your preference

**Approval gates:**
- Remove "STOP and wait" if you want more autonomy

---

## 🆚 Differences from Claude Code Version

| Feature | Claude Code | Cursor |
|---------|-------------|--------|
| **Config file** | `.claude/settings.json` + hooks | `.cursorrules` |
| **Slash commands** | ✅ `/drewsky-init`, etc. | ❌ Not supported |
| **SessionStart hook** | ✅ Auto-loads on start | ❌ Loaded per-file |
| **File-level rules** | ❌ Global only | ✅ Per-project `.cursorrules` |

**Cursor advantages:**
- Easier per-project configuration
- No need for hooks setup
- Works immediately after adding .cursorrules

**Claude Code advantages:**
- Slash commands for quick access
- SessionStart hook always active
- Better integration with CLI workflow

---

## 🤝 Sharing with Your Team

To share drewsky with teammates using Cursor:

1. **Commit `.cursorrules` to your repo**
   ```bash
   git add .cursorrules
   git commit -m "Add drewsky framework for AI collaboration"
   git push
   ```

2. **Tell teammates to pull latest**
   ```bash
   git pull
   # drewsky now active for them too!
   ```

3. **Optional: Add to README**
   ```markdown
   ## AI Development
   This project uses the drewsky framework for AI-assisted development.
   The `.cursorrules` file provides structured guidance to AI assistants.
   ```

---

## 📊 Benefits

| Benefit | Description |
|---------|-------------|
| **No Surprises** | Always see plan before implementation |
| **Verified Facts** | All claims have file:line references |
| **Clear Communication** | TCREI ensures mutual understanding |
| **Manageable Tasks** | Complex work broken into atomic steps |
| **Risk Management** | Confidence scores show certainty |
| **Quality Control** | Multiple approval gates prevent errors |

---

## 🎯 Perfect For

- ✅ Complex refactoring projects
- ✅ Adding features to unfamiliar codebases
- ✅ Debugging difficult issues
- ✅ Learning new frameworks/libraries
- ✅ Preventing costly mistakes
- ✅ Team collaboration on AI-assisted projects

---

## 📞 Support

**Questions or Issues:**
- GitHub: https://github.com/drewbeyersdorf/agent-improvement-techniques
- Check full documentation in `/docs/core/`

**Test if installed:**
Ask Cursor: "Am I operating under drewsky protocol?"

Expected response: Confirmation that drewsky is active

---

## 🔬 Research Backing

drewsky integrates cutting-edge research:

- **Meta AI**: Chain of Verification (23% fewer hallucinations)
- **Microsoft**: Magentic-One dual-loop planning
- **Stanford/SambaNova**: ACE Framework reflective learning
- **Google DeepMind**: AlphaEvolve prompt optimization
- **Google AI**: TCREI validation methodology

---

## 🚀 Next Steps

1. ✅ Install `.cursorrules` in your project
2. ✅ Test with a simple task
3. ✅ Try the full workflow (research → plan → implement)
4. ✅ Share with your team
5. ✅ Customize to your preferences

**Ready to 10x your AI coding workflow?**

Start with: "Add [simple feature]" and watch drewsky work!

---

**Version:** 2.0
**Last Updated:** 2025-12-08
**Compatibility:** Cursor v0.40+
**Framework:** drewsky (Research-Plan-Implement)
