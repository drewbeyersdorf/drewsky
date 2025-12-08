---
description: Show all current projects, tasks, and progress tracking for drewsky Framework and active work
---

# Project & Task Overview

Display a comprehensive overview of all current projects, active tasks, and work in progress.

## What to Show

### 1. Active Projects
Scan the following locations and summarize active work:
- `/output/` directory - Recent deliverables and work products
- Root directory - Any TODO.md, TASKS.md, or PROJECT.md files
- Git status - Uncommitted changes and untracked files
- Recent files - Files modified in last 7 days

### 2. Project Categories

Organize findings into:

**🎯 In Progress**
- What's actively being worked on
- Current status and blockers
- Next immediate steps

**📋 Planned**
- Queued work not yet started
- Dependencies or prerequisites
- Estimated effort (if known)

**✅ Completed Recently**
- Finished in last 7 days
- Key deliverables produced
- What was accomplished

**🚧 Blocked/Waiting**
- Work that's paused
- What's blocking it
- Action needed to unblock

### 3. Quick Stats
Provide at-a-glance metrics:
- Total active projects
- Files modified recently
- Git status (clean, ahead, uncommitted changes)
- Output files created this week

### 4. Suggested Next Actions
Based on the project state, suggest:
- What to work on next
- What needs attention
- What can be closed/archived

## Output Format

Use this structure:

```markdown
# 📊 Project Dashboard

Last updated: [Current date/time]

## 🎯 Active Projects (X)

### [Project Name]
**Status:** [In Progress/Blocked/Planning]
**Location:** [Path to main files]
**Progress:** [Brief status]
**Next Step:** [Immediate next action]

## 📋 Project List

| Project | Status | Progress | Last Updated |
|---------|--------|----------|--------------|
| ...     | ...    | ...      | ...          |

## 📈 Quick Stats

- Active projects: X
- Files modified (7d): X
- Git status: [Clean/Changes/Ahead]
- Recent outputs: X files

## 🚀 Suggested Next Actions

1. [Action based on analysis]
2. [Action based on analysis]
3. [Action based on analysis]

## 📁 Recent Activity

[List of recently modified files with context]

## 💡 Notes

[Any observations about the project state, patterns, or recommendations]
```

## Special Considerations

- If output/ directory has many files, group by type/date
- If git shows uncommitted work, highlight it
- If there are old branches or stale work, suggest cleanup
- Provide actionable next steps, not just status

## Make It Actionable

For each project, include:
- ✅ Clear status indicator
- 📅 When last updated
- 🎯 What's the next concrete step
- 🚦 Any blockers or dependencies
- 📊 Progress estimate (if determinable)

Generate this overview now.
