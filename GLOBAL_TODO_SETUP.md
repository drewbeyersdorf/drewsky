# ✅ Global /todo Command - Setup Complete!

**Installed:** December 8, 2025 - 1:25 AM

---

## 🎉 What Was Installed

### 1. Global `/todo` Command
**Location:** `~/.claude/commands/todo.md`

**Works:** System-wide (in any directory where you use Claude Code)

**What it does:**
- Shows all projects from your central PROJECTS.md file
- Displays git status if in a git repo
- Lists recent files in current directory
- Combines global + local view
- Suggests next actions

---

### 2. Central Projects File
**Location:** `~/PROJECTS.md` (4.4 KB)

**Contains:**
- 🔥 Active Projects (3 projects)
  - CPO Talk: "From Operator to CPO"
  - RPI Framework for Claude Code
  - Methodology Product Leadership
- 📋 Planned Projects (2 projects)
- ✅ Completed Projects (last 30 days)
- 📝 Notes & Ideas
- 🎯 Current Focus (This Week / Month / Quarter)

**Your master project tracking file!**

---

## 🚀 How to Use

### **Option 1: Use `/todo` command** (Recommended)
```bash
# In any directory, just type:
/todo

# Claude will show:
# - All projects from ~/PROJECTS.md
# - Current directory status
# - Next actions
```

### **Option 2: Edit PROJECTS.md directly**
```bash
# Open in your editor:
open ~/PROJECTS.md

# Or via terminal:
nano ~/PROJECTS.md
# vim ~/PROJECTS.md
# code ~/PROJECTS.md
```

### **Option 3: Use built-in `/todos` for session tracking**
```bash
# Shows tasks tracked during current Claude session:
/todos
```

---

## 📋 All Available Commands

You now have **10 slash commands** that work globally:

| Command | Purpose |
|---------|---------|
| `/todo` | Show all projects (global dashboard) |
| `/todos` | Show current session tasks (built-in) |
| `/tcrei` | Structure requests with TCREI validation |
| `/maker` | Break tasks into MAKER steps |
| `/verify` | Apply Chain of Verification (Meta AI) |
| `/plan` | Use Dual-Loop Planning (Microsoft) |
| `/rpi-init` | Initialize RPI Framework |
| `/rpi-help` | Show RPI command reference |
| `/rpi-status` | Check RPI Framework status |
| `/rpi-enforce` | Load full RPI protocol |

---

## 🎯 Your Current Projects (Quick View)

### Active Now:
1. **CPO Talk** - Content done, need to build slides & practice
2. **RPI Framework** - Maintenance mode, all commands working
3. **Product Leadership** - Learning via Methodology case studies

### Planned Next:
1. CPO Framework Templates (spreadsheets, calculators)
2. Product Decision Case Study Series

---

## 🔄 Workflow Recommendation

### **Daily Workflow:**

**Morning:**
```bash
# 1. Review all projects
/todo

# 2. Start Claude session, track today's work
# (I'll use TodoWrite during our conversation)

# 3. Check what needs attention today
/todos
```

**During Work:**
```bash
# Use specific commands as needed:
/tcrei   # When starting a new task
/maker   # When breaking down complex work
/verify  # When fact-checking
/plan    # When planning large changes
```

**End of Day:**
```bash
# 1. Check what was accomplished
/todos

# 2. Update PROJECTS.md with progress
open ~/PROJECTS.md

# 3. Plan tomorrow's focus
```

---

## 📝 How to Update PROJECTS.md

### Quick Edit:
```bash
# Open in your favorite editor:
code ~/PROJECTS.md        # VS Code
subl ~/PROJECTS.md        # Sublime
vim ~/PROJECTS.md         # Vim
open -a TextEdit ~/PROJECTS.md  # TextEdit
```

### What to Update:
- ✅ Mark completed tasks
- 🆕 Add new projects as they start
- 📊 Update progress on active projects
- 🗓️ Update "Last Review" date at bottom
- 💡 Capture ideas in Notes section

### Update Frequency:
- **Daily:** Quick status updates
- **Weekly:** Full review and cleanup
- **Monthly:** Archive completed, plan new projects

---

## 🎨 How `/todo` Works

When you type `/todo`, Claude will:

1. **Read ~/PROJECTS.md**
   - Parse all projects
   - Show status, progress, next steps

2. **Check current directory**
   - Git status (if git repo)
   - Recent files (last 7 days)
   - Local TODO files

3. **Combine views**
   - Global: All your projects
   - Local: Current directory details

4. **Suggest actions**
   - What to work on next
   - What needs updating
   - Quick wins available

---

## 🔍 Example Output

```markdown
# 📊 Global Project Dashboard

Last updated: December 8, 2025 - 1:30 AM
Current directory: /Users/.../RPI_Framework_Package

---

## 🌍 ALL PROJECTS

### 🔥 Active (3)
1. CPO Talk - ✅ Content done, 🎯 Build slides next
2. RPI Framework - 🟢 Maintenance mode
3. Product Leadership - 🎯 Learning & development

### 📋 Planned (2)
1. CPO Framework Templates
2. Product Decision Case Studies

---

## 📍 CURRENT PROJECT: RPI Framework

Git: Clean (1 untracked file)
Recent: 16 files modified (last 7 days)
Next: Commit todo.md changes

---

## 🚀 Quick Actions

Global:
- Set date for CPO talk delivery
- Review weekly project progress

Local:
- git add .claude/commands/todo.md
- git commit -m "Add global todo command"

---
```

---

## 🎓 Tips & Best Practices

### 1. Keep PROJECTS.md Simple
- Don't overcomplicate with too many projects
- Focus on 3-5 active projects max
- Archive completed work monthly

### 2. Use Three-Tier System
- **~/PROJECTS.md** - Master list (all projects)
- **/todo** command - Daily dashboard
- **/todos** command - Session tasks (during conversation)

### 3. Weekly Review Habit
Every Sunday (or your preferred day):
```bash
# 1. Open projects file
open ~/PROJECTS.md

# 2. Update all statuses
# 3. Move completed to "Completed" section
# 4. Update "Last Review" date
# 5. Plan next week's focus
```

### 4. Combine with Git
For code projects:
```bash
# Check project status
/todo

# Work on code
# ...

# Commit with context
git commit -m "Built slide deck outline (CPO Talk project)"
```

---

## 🛠️ Troubleshooting

### Q: `/todo` command not showing up?
**A:** Restart Claude Code to register new commands

### Q: PROJECTS.md not found?
**A:** It's at `~/PROJECTS.md` (home directory)
```bash
ls -lh ~/PROJECTS.md
# Should show 4.4K file
```

### Q: Want to reset PROJECTS.md?
**A:** Just edit it directly:
```bash
code ~/PROJECTS.md
```

### Q: How to add more commands globally?
**A:** Create new .md files in `~/.claude/commands/`
```bash
# Example:
code ~/.claude/commands/my-command.md
```

---

## 📊 System Overview

```
Your Home Directory (~/)
├── .claude/
│   └── commands/              ← Global slash commands (10 commands)
│       ├── todo.md           ← Your new global dashboard
│       ├── tcrei.md
│       ├── maker.md
│       ├── verify.md
│       ├── plan.md
│       ├── rpi-init.md
│       ├── rpi-help.md
│       ├── rpi-status.md
│       ├── rpi-enforce.md
│       └── todos.md          ← Built-in (already existed)
│
└── PROJECTS.md               ← Your master project list (4.4 KB)

Any Project Directory
└── .claude/
    └── commands/              ← Project-specific commands (optional)
        └── local-todo.md     ← Overrides global if needed
```

---

## ✅ Setup Verification

Run these commands to verify everything works:

```bash
# 1. Check global commands exist
ls -la ~/.claude/commands/

# 2. Check PROJECTS.md exists
cat ~/PROJECTS.md | head -20

# 3. Restart Claude Code

# 4. Test the command
/todo

# 5. Test built-in todos
/todos
```

---

## 🎉 You're All Set!

**What you can do now:**

1. ✅ Type `/todo` in ANY directory to see all projects
2. ✅ Edit `~/PROJECTS.md` anytime to update status
3. ✅ Use `/todos` for session-specific tasks
4. ✅ All 10 slash commands work globally

**Next steps:**

1. Restart Claude Code
2. Try `/todo` to see your dashboard
3. Update PROJECTS.md as you make progress
4. Build that CPO talk slide deck! 🎤

---

**Your productivity system is now installed!** 🚀

Questions? Just ask or type `/rpi-help` for more command info.

---

**Installation Date:** December 8, 2025 - 1:25 AM
**Version:** 1.0
**Files Created:**
- ~/.claude/commands/todo.md (2.9 KB)
- ~/PROJECTS.md (4.4 KB)
