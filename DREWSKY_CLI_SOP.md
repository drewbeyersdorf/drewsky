# drewsky CLI - Standard Operating Procedure (SOP)

**Version**: 1.0
**Last Updated**: December 8, 2025
**Purpose**: Complete walkthrough of drewsky CLI workflow for AI-assisted development

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Workflow Phases](#workflow-phases)
4. [Step-by-Step Guide](#step-by-step-guide)
5. [Command Reference](#command-reference)
6. [Troubleshooting](#troubleshooting)
7. [Best Practices](#best-practices)

---

## Overview

The drewsky CLI implements a **Research → Plan → Implement** workflow with research-backed validation methodologies:

- **TCREI Validation** (Google AI) - Structured task intake
- **MAKER Decomposition** - Atomic step planning
- **Chain of Verification (CoVe)** (Meta AI) - 23% hallucination reduction
- **Dual-Loop Planning** (Microsoft) - Strategic + Tactical clarity

**Expected outcome**: Rigorous, verifiable software development with 96% token efficiency.

---

## Prerequisites

### Installation

```bash
npm install -g drewsky
```

### Verify Installation

```bash
drewsky --version
# Expected output: 0.1.0 (or current version)
```

### Required Knowledge

- Basic command line usage
- Understanding of your project requirements
- Familiarity with your codebase structure

---

## Workflow Phases

```
┌──────────────┐    ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│   Research   │ -> │     Plan     │ -> │   Implement      │ -> │    Verify    │
└──────────────┘    └──────────────┘    └──────────────────┘    └──────────────┘
      ↓                   ↓                      ↓                     ↓
 .research.md         .plan.md              (Your code)      .verification.md
```

**Phase 1: Research** - Validate requirements with TCREI
**Phase 2: Plan** - Create atomic steps with Task/Progress Ledgers
**Phase 3: Implement** - Execute plan with verification checkpoints
**Phase 4: Verify** - Run Chain of Verification on claims

---

## Step-by-Step Guide

### Example Task: "Add dark mode toggle to application"

---

### STEP 1: Initialize drewsky in Your Project

**Command:**
```bash
drewsky init [project-name]
```

**Example:**
```bash
cd ~/projects/my-app
drewsky init my-app
```

**Expected Output:**
```
🚀 drewsky Framework Initialization

   ╭──────────────────────────────────────────╮
   │                                          │
   │   ✅ drewsky initialized successfully!   │
   │                                          │
   │   Created:                               │
   │     .drewsky/                            │
   │       ├── templates/                     │
   │       │   ├── research.template.md       │
   │       │   ├── plan.template.md           │
   │       │   └── completion.template.md     │
   │       ├── config.json                    │
   │       └── metrics.json                   │
   │                                          │
   │   Next steps:                            │
   │     1. drewsky research "your task"      │
   │     2. drewsky plan                      │
   │     3. drewsky status                    │
   │                                          │
   ╰──────────────────────────────────────────╯

💡 Tip: Run drewsky --help to see all commands
```

**What Happened:**
- Created `.drewsky/` directory with configuration
- Set up metrics tracking (token savings, productivity)
- Created workflow templates for research, plan, and completion docs

**Files Created:**
```
.drewsky/
├── config.json          # Framework settings
├── metrics.json         # Productivity tracking
└── templates/           # Workflow templates
    ├── research.template.md
    ├── plan.template.md
    └── completion.template.md
```

**Config Contents** (`.drewsky/config.json`):
```json
{
  "version": "0.1.0",
  "created": "2025-12-08T05:00:49.820Z",
  "settings": {
    "confidenceThreshold": 70,
    "atomicStepDuration": 30,
    "contextWarning": 40,
    "contextEmergency": 60
  }
}
```

---

### STEP 2: Create Research Document (TCREI Validation)

**Command:**
```bash
drewsky research "Add dark mode toggle to application"
```

**Interactive Prompts:**

The CLI will ask you 5 questions to validate your task using TCREI methodology:

1. **Task**: What exactly needs to be done?
2. **Context**: Why is this needed? What problem does it solve?
3. **Reference**: Are there examples, docs, or patterns to follow?
4. **Evaluation**: How will success be measured? What defines "done"?
5. **Input**: What files/data/resources need to be examined first?

**Example Answers:**

**Task:**
```
Add a dark mode toggle that allows users to switch between light
and dark themes. The toggle should persist the user's preference
across sessions and apply globally to all components.
```

**Context:**
```
Users have requested a dark mode option to reduce eye strain during
night-time usage. This is a common accessibility feature that improves
user experience and meets modern UI expectations. Current application
only supports light theme.
```

**Reference:**
```
- Material UI dark mode implementation patterns
- CSS custom properties for theming
- localStorage API for persistence
- React Context API for global state
```

**Evaluation:**
```
Success criteria:
- Toggle button visible in header/navigation
- Theme switches immediately without page reload
- Preference persists after browser close/reopen
- All components properly styled in both themes
- No flash of wrong theme on page load
```

**Input:**
```
Need to examine:
- Current component structure (likely in src/components/)
- Existing CSS/styling approach (CSS modules, styled-components, etc.)
- State management setup (Context, Redux, etc.)
- Root App component for theme provider
```

**Output File:** `.research.md`

**Snapshot of Generated File:**
```markdown
# Research: Add dark mode toggle to application

**Created**: December 8, 2025
**Status**: In Progress

---

## TCREI Validation

### Task
Add a dark mode toggle that allows users to switch between light
and dark themes. The toggle should persist the user's preference
across sessions and apply globally to all components.

### Context
Users have requested a dark mode option to reduce eye strain during
night-time usage. This is a common accessibility feature that improves
user experience and meets modern UI expectations.

### Reference
- Material UI dark mode implementation patterns
- CSS custom properties for theming
- localStorage API for persistence
- React Context API for global state

### Evaluation
Success criteria:
- Toggle button visible in header/navigation
- Theme switches immediately without page reload
- Preference persists after browser close/reopen
- All components properly styled in both themes

### Input
Need to examine:
- Current component structure (src/components/)
- Existing CSS/styling approach
- State management setup
- Root App component for theme provider

---

## Research Findings

- [ ] Read relevant files
- [x] Identified theming approach needed
- [x] Listed requirements for persistence
- [ ] Document current styling patterns

---

## Verified Claims

- ✓ Dark mode requires global state management
- ✓ localStorage is standard for theme persistence
- ? Current app structure unknown - needs investigation

---

## Confidence Assessment

**Overall Confidence**: 75%

**Breakdown:**
- Task understanding: 90%
- Technical approach: 80%
- Resource availability: 60%
- Time estimation: 70%
```

**Next Action:**
Review `.research.md` and fill in the "Research Findings" section by exploring your codebase.

---

### STEP 3: Check Workflow Status

**Command:**
```bash
drewsky status
```

**Expected Output:**
```
📊 drewsky Workflow Status

Current Phase: 🔍 Research

Workflow Files:

  ✓ .research.md (exists)
  ○ .plan.md (not found)
  ○ .completion-snapshot.md (not found)

Project Metrics:

  Sessions: 0
  Research phases: 0
  Plans created: 0
  Tasks completed: 0
  Token savings: 96%

📌 Next Steps:

  1. Review .research.md findings
  2. Run: drewsky plan --from-research
  3. Or manually create .plan.md
```

**Interpretation:**
- **Current Phase**: Research - you have research doc but no plan yet
- **Workflow Files**: Shows which workflow files exist
- **Next Steps**: System suggests creating a plan next

---

### STEP 4: Create Implementation Plan

**Command:**
```bash
drewsky plan --from-research
```

**Interactive Prompts:**

The CLI will guide you through creating:
1. **Task Ledger (Strategic)**: Facts, guesses, decision points
2. **Progress Ledger (Tactical)**: Atomic MAKER steps

**Example Input Flow:**

**Task Ledger - Facts:**
```
1. ✓ Dark mode requires theme switching mechanism
2. ✓ localStorage persists data across browser sessions
3. ✓ CSS custom properties enable dynamic theming
4. ✓ React Context provides global state management
(Press Enter to finish)
```

**Task Ledger - Guesses:**
```
1. ? Application uses React (assumption)
2. ? CSS modules or styled-components for styling
3. ? No existing theme infrastructure
(Press Enter to finish)
```

**Task Ledger - Decision Points:**
```
1. [ ] Use Context API vs Redux for theme state
2. [ ] CSS custom properties vs CSS-in-JS
3. [ ] Toggle placement (header, settings, floating button)
(Press Enter to finish)
```

**Progress Ledger - Steps:**

For each step, the CLI prompts for:
- **Step name**: Descriptive name
- **Input**: What's needed to start
- **Action**: Exact steps to take
- **Output**: What will be created/changed
- **Verification**: How to confirm it worked
- **Confidence**: 0-100%
- **Time**: Estimate in minutes

**Example Step 1:**
```
Step name: Create theme context and provider
Input: Current codebase structure
Action: Create ThemeContext.js with React Context API, implement
        useTheme hook, add light/dark theme objects
Output: src/context/ThemeContext.js file with theme provider component
Verification: Import and test context in App.js
Confidence: 90
Time: 20
```

**Example Step 2:**
```
Step name: Add theme CSS custom properties
Input: Theme context from Step 1
Action: Define CSS variables for colors (--bg-primary, --text-primary),
        create theme.css with light and dark variations
Output: src/styles/theme.css with complete variable set
Verification: Apply variables to root element and verify color changes
Confidence: 85
Time: 25
```

**Output File:** `.plan.md`

**Snapshot of Generated File:**
```markdown
# Implementation Plan: Add dark mode toggle to application

**Created**: December 8, 2025
**Status**: Draft

---

## Task Ledger (Strategic)

### Facts (Verified)
- ✓ Dark mode requires theme switching mechanism
- ✓ localStorage persists data across browser sessions
- ✓ CSS custom properties enable dynamic theming
- ✓ React Context provides global state management

### Guesses (Need Validation)
- ? Application uses React (assumption based on modern web app)
- ? CSS modules or styled-components for styling
- ? No existing theme infrastructure

### Decision Points
- [ ] Use Context API vs Redux for theme state
- [ ] CSS custom properties vs CSS-in-JS
- [ ] Toggle placement (header, settings, floating button)

---

## Progress Ledger (Tactical)

### Step 1: Create theme context and provider
- **Input**: Current codebase structure
- **Action**: Create ThemeContext.js with React Context API,
             implement useTheme hook, add light/dark theme objects
- **Output**: src/context/ThemeContext.js file with theme provider
- **Verification**: Import and test context in App.js
- **Confidence**: 90%
- **Time**: 20 minutes

### Step 2: Add theme CSS custom properties
- **Input**: Theme context from Step 1
- **Action**: Define CSS variables for colors, create theme.css
             with light and dark variations
- **Output**: src/styles/theme.css with complete variable set
- **Verification**: Apply variables to root, verify color changes
- **Confidence**: 85%
- **Time**: 25 minutes

### Step 3: Implement localStorage persistence
- **Input**: Theme context from Step 1
- **Action**: Add useEffect to save theme, read initial theme
             from localStorage on mount
- **Output**: Updated ThemeContext.js with persistence logic
- **Verification**: Toggle theme, refresh, verify persists
- **Confidence**: 90%
- **Time**: 15 minutes

### Step 4: Create toggle button component
- **Input**: Theme context and styling from previous steps
- **Action**: Build ToggleSwitch component with sun/moon icons,
             wire up to theme context
- **Output**: src/components/ThemeToggle.js component
- **Verification**: Click toggle and see theme switch
- **Confidence**: 85%
- **Time**: 20 minutes

### Step 5: Update existing components with theme variables
- **Input**: All components in src/components/
- **Action**: Replace hardcoded colors with CSS custom properties
- **Output**: Updated component stylesheets
- **Verification**: Switch themes, verify all components respond
- **Confidence**: 70%
- **Time**: 30 minutes

### Step 6: Prevent flash of unstyled content (FOUC)
- **Input**: Persistence logic from Step 3
- **Action**: Add inline script to check localStorage before
             React hydration
- **Output**: Updated index.html with inline script
- **Verification**: Hard refresh page, verify no flash
- **Confidence**: 75%
- **Time**: 25 minutes

---

## Overall Assessment

**Total Steps**: 6
**Estimated Time**: 135 minutes (2.25 hours)
**Overall Confidence**: 82%

---

## Approval

- [ ] Plan reviewed
- [ ] Steps are atomic (<30 min each)
- [ ] Test commands defined
- [ ] Ready to implement
```

**Expected Output After Generation:**
```
✔ Plan created successfully

   ╭──────────────────────────────────────╮
   │                                      │
   │   ✓ Plan Generated                   │
   │                                      │
   │   File: .plan.md                     │
   │   Steps: 6                           │
   │   Time: 135 minutes                  │
   │   Confidence: 82%                    │
   │                                      │
   │   Review the plan and get approval   │
   │   before implementing.               │
   │                                      │
   ╰──────────────────────────────────────╯

📌 Next Steps:
  1. Review .plan.md
  2. Get stakeholder approval
  3. Begin implementation
  4. Use drewsky status to track progress
```

---

### STEP 5: Review Status Again

**Command:**
```bash
drewsky status
```

**Expected Output:**
```
📊 drewsky Workflow Status

Current Phase: ⚙️ Planning / Implementation

Workflow Files:

  ✓ .research.md (exists)
  ✓ .plan.md (exists)
  ○ .completion-snapshot.md (not found)

Project Metrics:

  Sessions: 0
  Research phases: 0
  Plans created: 0
  Tasks completed: 0
  Token savings: 96%

📌 Next Steps:

  1. Review .plan.md steps
  2. Get stakeholder approval
  3. Begin implementation
  4. Run: drewsky verify to check claims
```

**Notice:** Phase changed to "Planning / Implementation"

---

### STEP 6: Verify Claims with Chain of Verification (CoVe)

**Command:**
```bash
drewsky verify
```

**What It Does:**
1. Scans `.research.md` and `.plan.md` for verifiable claims
2. Extracts claims with file:line references
3. Generates verification questions for each claim
4. Prompts you to verify each claim manually
5. Creates verification report

**Interactive Flow:**

```
🔍 drewsky Chain of Verification (CoVe)

Verifying: .plan.md

Found 4 claim(s) to verify:

1. Dark mode requires theme switching mechanism
   Source: Line 11

   Verification questions:
   1) What evidence supports this assertion?
   2) Are there any contradicting sources?
   3) Has this been independently verified?

   Verification status:
   > ✓ Verified - Claim is accurate

2. localStorage persists data across browser sessions
   Source: Line 12

   [... similar flow ...]
```

**Output File:** `.verification-[timestamp].md`

**Snapshot:**
```markdown
# Verification Report: .plan.md

**Date**: December 8, 2025, 9:05 PM
**Method**: Chain of Verification (CoVe)

---

## Summary

**Total claims**: 4
**Verified**: 3
**Uncertain**: 1
**False**: 0

---

## Detailed Results

### 1. ✓ Dark mode requires theme switching mechanism
**Status**: verified

### 2. ✓ localStorage persists data across browser sessions
**Status**: verified

### 3. ✓ CSS custom properties enable dynamic theming
**Status**: verified

### 4. ? Application uses React (assumption)
**Status**: uncertain
**Notes**: Need to verify actual framework used in codebase

---

## Recommendations

⚠️  1 claim(s) need attention:

- [ ] Review: Application uses React (Line 20)
```

**Expected Output:**
```
   ╭──────────────────────────────────────╮
   │                                      │
   │   Verification Complete              │
   │                                      │
   │   Report saved: .verification.md     │
   │                                      │
   │   Verified: 3/4                      │
   │                                      │
   │   ⚠️  1 claim(s) need attention      │
   │                                      │
   ╰──────────────────────────────────────╯

For more on CoVe: https://arxiv.org/abs/2309.11495
```

---

### STEP 7: View Productivity Metrics

**Command:**
```bash
drewsky metrics
```

**Expected Output:**
```
📈 drewsky Metrics Dashboard

Project initialized: December 8, 2025
Last updated: Never

   ╭────────────────────────╮
   │                        │
   │   Workflow Metrics     │
   │                        │
   │   Sessions: 0          │
   │   Research phases: 0   │
   │   Plans created: 0     │
   │   Tasks completed: 0   │
   │                        │
   ╰────────────────────────╯

   ╭────────────────────────────────────────╮
   │                                        │
   │   Token Efficiency                     │
   │                                        │
   │   Before optimization: 41,000 tokens   │
   │   After optimization: 1,500 tokens     │
   │   Tokens saved: 39,500                 │
   │   Efficiency gain: 96%                 │
   │                                        │
   ╰────────────────────────────────────────╯

   ╭────────────────────────────────────────────╮
   │                                            │
   │   Productivity Insights                    │
   │                                            │
   │   Tasks per session: 0                     │
   │   Completion rate: 0% (of started tasks)   │
   │                                            │
   ╰────────────────────────────────────────────╯

   ╭───────────────────────────────────╮
   │                                   │
   │   Configuration                   │
   │                                   │
   │   Confidence threshold: 70%       │
   │   Atomic step duration: 30 min    │
   │   Context warning: 40K tokens     │
   │   Context emergency: 60K tokens   │
   │                                   │
   ╰───────────────────────────────────╯

🧠 Methodology Impact:

  ✓ TCREI validation - Structured task intake
  ✓ MAKER decomposition - Atomic step planning
  ✓ Chain of Verification - 23% fewer hallucinations
  ✓ Dual-Loop Planning - Strategic + Tactical clarity
```

---

### STEP 8: Implement Your Plan

Now execute each step from `.plan.md`:

1. Create theme context → Verify
2. Add CSS variables → Verify
3. Implement persistence → Verify
4. Build toggle component → Verify
5. Update components → Verify
6. Prevent FOUC → Verify

**Use AI Agent (Claude, Cursor, etc.) to help implement each step while following your plan.**

---

### STEP 9: Create Completion Snapshot (Optional)

After finishing implementation, document what was accomplished:

**File:** `.completion-snapshot.md`

```markdown
# Completion Snapshot: Add dark mode toggle

**Completed**: December 8, 2025
**Duration**: 2.5 hours

---

## Summary

Successfully implemented dark mode toggle with theme persistence
and zero flash on page load. All 6 steps completed as planned.

---

## Steps Completed

- ✓ Step 1: Theme context - ThemeContext.js created
- ✓ Step 2: CSS variables - theme.css with 12 variables
- ✓ Step 3: Persistence - localStorage integration working
- ✓ Step 4: Toggle component - Animated sun/moon toggle
- ✓ Step 5: Component updates - 15 components themed
- ✓ Step 6: FOUC prevention - Inline script added

---

## Test Results

```
npm test
✓ ThemeContext tests (3/3)
✓ ThemeToggle tests (2/2)
✓ Integration tests (4/4)

Exit code: 0
```

---

## Files Modified

- `src/context/ThemeContext.js` - Created theme provider
- `src/styles/theme.css` - Created CSS variables
- `src/components/ThemeToggle.js` - Created toggle component
- `public/index.html` - Added FOUC prevention script
- 15 component files - Applied theme variables
```

---

## Command Reference

### drewsky init [project-name]
Initialize drewsky framework in a project

**Options:**
- `[project-name]` - Optional name for project directory

**Example:**
```bash
drewsky init my-app
```

---

### drewsky research <task>
Create research document with TCREI validation

**Arguments:**
- `<task>` - Required task description

**Example:**
```bash
drewsky research "Add user authentication"
```

**Output:** `.research.md`

---

### drewsky plan [options]
Generate implementation plan with Task/Progress Ledgers

**Options:**
- `--from-research` - Use existing `.research.md` to pre-fill task name

**Example:**
```bash
drewsky plan --from-research
```

**Output:** `.plan.md`

---

### drewsky status
Show current workflow state

**Example:**
```bash
drewsky status
```

**Shows:**
- Current phase (Research, Planning, Implementation, Complete)
- Which workflow files exist
- Project metrics
- Next recommended steps

---

### drewsky verify [options]
Run Chain of Verification on file claims

**Options:**
- `--file <path>` - Specific file to verify (default: auto-detect)

**Example:**
```bash
drewsky verify
drewsky verify --file .plan.md
```

**Output:** `.verification-[timestamp].md`

---

### drewsky metrics
Show productivity and token savings stats

**Example:**
```bash
drewsky metrics
```

**Shows:**
- Workflow metrics (sessions, tasks completed)
- Token efficiency (96% savings)
- Productivity insights
- Configuration settings

---

## Troubleshooting

### Issue: "Not Initialized" Error

**Problem:**
```
⚠️  Not Initialized

This project has not been initialized with drewsky.
```

**Solution:**
```bash
drewsky init
```

---

### Issue: Interactive Prompts Not Working

**Problem:** Questions don't appear or freeze

**Solutions:**
1. Ensure terminal supports interactive input
2. Check Node.js version (requires >=18.0.0)
3. Try running with `node` explicitly:
   ```bash
   node $(which drewsky) research "task"
   ```

---

### Issue: Verification Finds No Claims

**Problem:** `drewsky verify` says "No claims found"

**Cause:** Claims need file:line references or specific patterns

**Solution:** Add verifiable claims to your files:
```markdown
- ✓ User model defined in `src/models/user.ts:15-42`
- ✓ Authentication uses JWT tokens (verified in `auth.ts:89`)
```

---

### Issue: Metrics Show Zero

**Problem:** All metrics show 0 even after using commands

**Cause:** Metrics update after workflow completion, not during

**Solution:** This is expected. Metrics will update when you complete full workflows.

---

## Best Practices

### 1. Always Start with Research

Don't skip the research phase. TCREI validation:
- Clarifies requirements
- Identifies unknowns early
- Reduces rework later

**Bad:**
```bash
# Skipping research ❌
drewsky plan
```

**Good:**
```bash
# Proper workflow ✅
drewsky research "Add feature X"
# ... fill in research findings ...
drewsky plan --from-research
```

---

### 2. Keep Steps Atomic (<30 min)

**Bad Step:**
```
Step: Implement entire authentication system
Time: 180 minutes ❌
```

**Good Steps:**
```
Step 1: Create User model
Time: 20 minutes ✅

Step 2: Set up JWT library
Time: 15 minutes ✅

Step 3: Implement login endpoint
Time: 25 minutes ✅
```

---

### 3. Include File References in Claims

**Bad:**
```
- The app uses React ❌
```

**Good:**
```
- ✓ App uses React (verified in `package.json:12`) ✅
```

---

### 4. Use Verify Before Final Implementation

Run verification **after planning, before implementing**:

```bash
drewsky plan
drewsky verify    # Check claims before coding
# ... implement ...
drewsky verify    # Check again after coding
```

---

### 5. Track Progress with Status

Check status regularly:
```bash
drewsky status  # Before starting
# ... work on Step 1 ...
drewsky status  # After each step
```

---

### 6. Update Metrics Manually

If CLI metrics aren't updating, manually update `.drewsky/metrics.json`:

```json
{
  "sessions": 5,
  "researchPhases": 5,
  "plansCreated": 4,
  "tasksCompleted": 3,
  "tokenSavings": {
    "before": 41000,
    "after": 1500,
    "savingsPercent": 96
  }
}
```

---

### 7. Commit Workflow Files to Git

**Recommended .gitignore:**
```gitignore
# Keep workflow files
!.research.md
!.plan.md
!.completion-snapshot.md
!.verification-*.md

# Keep drewsky config
!.drewsky/config.json

# Ignore node_modules in .drewsky
.drewsky/node_modules/
```

Benefits:
- Team visibility into planning
- Historical record of decisions
- Easy onboarding for new developers

---

## Summary Checklist

For every new task:

- [ ] 1. Initialize project: `drewsky init`
- [ ] 2. Create research: `drewsky research "task"`
- [ ] 3. Fill in research findings
- [ ] 4. Create plan: `drewsky plan --from-research`
- [ ] 5. Review plan carefully
- [ ] 6. Verify claims: `drewsky verify`
- [ ] 7. Get stakeholder approval
- [ ] 8. Implement step-by-step
- [ ] 9. Verify after implementation
- [ ] 10. Check metrics: `drewsky metrics`
- [ ] 11. Create completion snapshot
- [ ] 12. Commit workflow files to git

---

## Additional Resources

- **drewsky Repository**: https://github.com/drewbeyersdorf/agent-improvement-techniques
- **npm Package**: https://www.npmjs.com/package/drewsky
- **Chain of Verification Paper**: https://arxiv.org/abs/2309.11495
- **TCREI Methodology**: Google AI Research
- **Dual-Loop Planning**: Microsoft Research

---

**Last Updated**: December 8, 2025
**Document Version**: 1.0
**Maintained By**: drewsky CLI Team

---

*Generated with drewsky CLI - Rigorous AI collaboration for modern software development*
