# 🚀 RPI Framework for Claude Code

**Transform Claude Code into a 10x more effective AI assistant**

---

## 📦 What's in This Package?

This package contains everything you need to install the **RPI (Research → Plan → Implement) Framework with Cognitive Enhancements** for Claude Code.

### Files Included:

| File | Description |
|------|-------------|
| `install-rpi-framework.sh` | **Automatic installer script (recommended)** |
| `RPI_FRAMEWORK_SETUP_GUIDE.md` | **Complete setup guide with examples** |
| `instructions.md` | Main framework file (auto-loaded by Claude Code) |
| `ENFORCED_RPI_PROTOCOL.md` | Complete protocol rules and behaviors |
| `RPI_STATUS.md` | Status, testing, and verification guide |

---

## ⚡ Quick Start (60 seconds)

### Step 1: Download This Package

Download or clone this entire `RPI_Framework_Package` folder.

### Step 2: Run the Installer

**Option A: Global Install (Recommended)**
```bash
cd RPI_Framework_Package
./install-rpi-framework.sh
# Choose option 1 (global)
```

**Option B: Project-Specific Install**
```bash
cd RPI_Framework_Package
./install-rpi-framework.sh
# Choose option 2 (project-specific)
```

### Step 3: Restart Claude Code

```bash
# Restart Claude Code to load the framework
```

### Step 4: Test It

Start Claude Code and try:
```
"Add a search feature"
```

Expected response: Claude will ask TCREI validation questions (Context, Evaluation, etc.)

✅ **If you see TCREI questions, the framework is working!**

---

## 📖 What Does This Do?

### Before RPI ❌
```
You: "Add user authentication"
Claude: [Immediately implements something]
You: "That's not what I wanted!"
```

### After RPI ✅
```
You: "Add user authentication"
Claude: "I need to clarify:
         - What authentication method?
         - Why is this needed?
         - What defines success?"
You: [Provides clarity]
Claude: "Research complete - here's what I found [verified]"
Claude: "Plan created - 6 atomic steps, approve?"
You: "Approved"
Claude: [Implements step by step with progress updates]
```

---

## 🎯 Key Features

After installation, Claude Code will automatically:

✅ **Ask clarifying questions** when tasks are vague (TCREI)
✅ **Research before implementing** (no more assumptions)
✅ **Create explicit plans** with code snippets
✅ **Wait for your approval** before making changes
✅ **Verify all claims** with file:line references
✅ **Score confidence** on recommendations (0-100%)
✅ **Break complex tasks** into atomic steps (<30 min each)
✅ **Monitor context** and auto-compact at 40%

---

## 🧠 The 4 Cognitive Frameworks

1. **TCREI Validation** - Ensures task clarity
   - Task, Context, Reference, Evaluation, Input

2. **MAKER Decomposition** - Breaks tasks into atomic steps
   - Tasks >30 min → multiple steps <30 min each

3. **Chain of Verification (CoVe)** - Verifies all claims
   - No assumptions, only verified facts with sources

4. **Confidence Scoring** - Explicit uncertainty management
   - Every recommendation gets 0-100% confidence
   - Stops and asks questions if <80% confident

---

## 📚 Documentation

### For Quick Setup:
1. Run `install-rpi-framework.sh`
2. Test with a simple command

### For Detailed Understanding:
Read `RPI_FRAMEWORK_SETUP_GUIDE.md` for:
- Complete installation instructions
- Usage examples
- Troubleshooting
- Configuration options
- FAQ

### For Protocol Details:
Read `ENFORCED_RPI_PROTOCOL.md` for:
- Complete workflow rules
- Quality gates
- Forbidden behaviors
- Response templates

### For Testing:
Read `RPI_STATUS.md` for:
- Verification procedures
- Test scenarios
- Success indicators

---

## 🔧 Manual Installation

If you prefer manual installation:

1. **Global Install:**
   ```bash
   cp instructions.md ~/.claude/
   cp ENFORCED_RPI_PROTOCOL.md ~/.claude/
   cp RPI_STATUS.md ~/.claude/
   ```

2. **Project Install:**
   ```bash
   mkdir -p .claude
   cp instructions.md .claude/
   cp ENFORCED_RPI_PROTOCOL.md .claude/
   cp RPI_STATUS.md .claude/
   ```

3. Restart Claude Code

---

## ✅ Verification Tests

After installation, test these scenarios:

### Test 1: TCREI Validation
```
You: "Add a search feature"
Expected: Claude asks for Context, Evaluation criteria
```

### Test 2: Chain of Verification
```
You: "How does authentication work?"
Expected: Claude verifies with file:line references
```

### Test 3: MAKER Decomposition
```
You: "Refactor the database layer"
Expected: Claude breaks into atomic steps, asks for approval
```

### Test 4: Confidence Scoring
```
You: "Should we use Redis or Memcached?"
Expected: Claude provides recommendation with confidence score
```

---

## 🎓 Example Workflow

```
You: "Add caching to improve API performance"

Claude: "TCREI VALIDATION
         I need to clarify:
         - Context: Which APIs are slow? Current response times?
         - Evaluation: What's the target performance?
         - Reference: Any existing caching patterns in the codebase?"

You: "Product API is 2s, want <500ms, no caching exists yet"

Claude: "RESEARCH PHASE
         Exploring codebase...

         Findings:
         ✓ Product API in api/products.ts:45-67 (verified)
         ✓ No caching layer exists (verified)
         ✓ Redis in package.json (verified)

         Confidence: 90%

         Please review .research.md
         Approve to proceed to planning?"

You: "Approved"

Claude: "PLAN PHASE
         Created .plan.md with 5 atomic steps:

         1. Install Redis client [15 min]
         2. Create cache middleware [20 min]
         3. Add to product endpoints [25 min]
         4. Add cache invalidation [20 min]
         5. Test performance [15 min]

         Overall confidence: 85%

         Approve to implement?"

You: "Approved"

Claude: "IMPLEMENTATION
         ✓ Step 1/5 complete - Redis client installed
         ✓ Step 2/5 complete - Middleware created
         ✓ Step 3/5 complete - Endpoints cached
         ✓ Step 4/5 complete - Invalidation added
         ✓ Step 5/5 complete - Tests passing

         Performance: 2s → 380ms ✓
         Context: 35%

         Created .completion-snapshot.md"
```

---

## ⚙️ Configuration

Default settings (can be customized in `~/.claude/settings.json`):

- **Confidence thresholds:**
  - Minimum: 70% (stops below this)
  - Ask questions: 80% (asks for clarity below this)

- **Context thresholds:**
  - Warning: 40% (suggests compaction)
  - Emergency: 60% (forces compaction)

- **Quality gates:**
  - TCREI required for non-trivial tasks
  - All claims must be verified
  - Plans require atomic steps

---

## 🚫 Uninstalling

To remove the framework:

```bash
# Global uninstall
rm ~/.claude/instructions.md
rm ~/.claude/ENFORCED_RPI_PROTOCOL.md
rm ~/.claude/RPI_STATUS.md

# Project uninstall
rm .claude/instructions.md
rm .claude/ENFORCED_RPI_PROTOCOL.md
rm .claude/RPI_STATUS.md
```

---

## 💡 Override Commands

Need to bypass RPI for a quick task?

```
"Skip RPI: [your task]"
"Emergency mode: [your task]"
"No plan needed: [your task]"
```

Claude will warn you but comply.

---

## 🤝 Sharing This Package

To share with others:

1. **Send the entire `RPI_Framework_Package` folder**
2. **Tell them to run:** `./install-rpi-framework.sh`
3. **That's it!**

You can also:
- Zip the package: `zip -r RPI_Framework.zip RPI_Framework_Package/`
- Upload to GitHub/Drive/Dropbox
- Email the zip file

---

## 📊 What You Get

| Benefit | Description |
|---------|-------------|
| **No Surprises** | Always see plan before implementation |
| **Verified Facts** | All claims have file:line references |
| **Clear Communication** | TCREI ensures mutual understanding |
| **Manageable Tasks** | Complex work broken into atomic steps |
| **Risk Management** | Confidence scores show certainty |
| **Context Efficiency** | Auto-compaction keeps sessions fast |
| **Quality Control** | Multiple approval gates prevent errors |

---

## 🎯 Perfect For

- ✅ Complex refactoring projects
- ✅ Adding new features to existing codebases
- ✅ Debugging unfamiliar code
- ✅ Learning new frameworks/libraries
- ✅ Preventing costly mistakes
- ✅ Managing large, multi-step tasks
- ✅ Collaborative development

---

## 📞 Support

If you encounter issues:

1. Read the troubleshooting section in `RPI_FRAMEWORK_SETUP_GUIDE.md`
2. Check `RPI_STATUS.md` for verification tests
3. Ask Claude: "Am I operating under RPI protocol?"

---

## 🚀 Getting Started

**Ready to 10x your AI collaboration?**

```bash
./install-rpi-framework.sh
```

Choose your installation scope, restart Claude Code, and experience the difference!

---

**Version:** 1.0
**Last Updated:** 2025-12-07
**Compatibility:** Claude Code v0.2.0+

---

**Welcome to more effective, reliable, and transparent AI collaboration!** 🎉
