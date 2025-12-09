# 🚀 drewsky - AI Collaboration CLI

**Research → Plan → Implement** - A CLI tool for rigorous AI-assisted software development.

[![npm version](https://img.shields.io/npm/v/drewsky.svg)](https://www.npmjs.com/package/drewsky)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 What is drewsky?

drewsky is a CLI tool that implements research-backed AI collaboration methodologies:

- **TCREI Validation** (Google AI) - Structured task intake
- **MAKER Decomposition** - Atomic step planning
- **Chain of Verification (CoVe)** (Meta AI) - 23% fewer hallucinations
- **Dual-Loop Planning** (Microsoft) - Strategic + Tactical clarity
- **96% Token Efficiency** - Optimized for cost and performance

## 📦 Installation

```bash
npm install -g drewsky
```

## ⚡ Quick Start

```bash
# Initialize drewsky in your project
drewsky init

# Start a new task with research
drewsky research "Add user authentication"

# Create an implementation plan
drewsky plan --from-research

# Check your progress
drewsky status

# Verify your claims
drewsky verify

# View productivity metrics
drewsky metrics
```

## 🔧 Commands

### `drewsky init [project-name]`

Initialize drewsky framework in your project. Creates:
- `.drewsky/` directory with templates
- `config.json` with settings
- `metrics.json` for tracking

```bash
drewsky init
drewsky init my-awesome-project
```

### `drewsky research <task>`

Create a research document with TCREI validation:
- **T**ask: What exactly needs to be done?
- **C**ontext: Why is this needed?
- **R**eference: Examples or docs to follow?
- **E**valuation: How to measure success?
- **I**nput: What files/resources to examine?

```bash
drewsky research "Implement dark mode toggle"
```

Creates `.research.md` with structured findings.

### `drewsky plan [options]`

Generate an implementation plan with Task and Progress Ledgers:

```bash
drewsky plan
drewsky plan --from-research
```

Creates `.plan.md` with:
- **Task Ledger**: Facts, guesses, decision points
- **Progress Ledger**: Atomic MAKER steps (<30 min each)
- Time estimates and confidence scores

### `drewsky status`

Show your current workflow state:

```bash
drewsky status
```

Displays:
- Current phase (Research, Plan, Implementation)
- Workflow file status
- Next recommended steps
- Project metrics

### `drewsky verify [options]`

Run Chain of Verification (CoVe) on your claims:

```bash
drewsky verify
drewsky verify --file .research.md
```

Implements Meta AI's 4-step verification:
1. Extract baseline claims
2. Generate verification questions
3. Answer independently
4. Generate verified report

Reduces hallucinations by 23%.

### `drewsky metrics`

Display productivity and efficiency metrics:

```bash
drewsky metrics
```

Shows:
- Workflow metrics (sessions, tasks completed)
- Token savings (96% efficiency gain)
- Productivity insights
- Configuration settings

## 📊 Workflow

```
┌──────────┐    ┌──────────┐    ┌──────────────┐    ┌────────────┐
│ Research │ -> │   Plan   │ -> │  Implement   │ -> │   Verify   │
└──────────┘    └──────────┘    └──────────────┘    └────────────┘
     ↓               ↓                  ↓                   ↓
 .research.md    .plan.md         (Your code)      .verification.md
```

### Example Workflow

```bash
# 1. Start with research
drewsky research "Add API rate limiting"

# Agent explores codebase, fills out TCREI
# Creates .research.md

# 2. Create implementation plan
drewsky plan --from-research

# Interactive prompts for Task/Progress Ledgers
# Creates .plan.md with atomic steps

# 3. Check status before implementing
drewsky status

# Shows: "Phase: Planning/Implementation"
# Next: "Begin implementation"

# 4. Implement your changes
# (Write code according to plan)

# 5. Verify your claims
drewsky verify

# Runs CoVe on all claims in workflow files
# Creates .verification-[timestamp].md

# 6. View metrics
drewsky metrics

# Token savings: 96%
# Tasks completed: 1
```

## 🧠 Research-Backed Methodologies

### TCREI Validation
**Source**: Google AI Research
**Impact**: Structured task intake, clearer requirements

### MAKER Decomposition
**Properties**:
- **M**anageable: <30 min per step
- **A**tomic: Single, focused action
- **K**nowable: Clear inputs/outputs
- **E**xecutable: Actionable instructions
- **R**eviewable: Verifiable completion

### Chain of Verification (CoVe)
**Source**: Meta AI ([arXiv:2309.11495](https://arxiv.org/abs/2309.11495))
**Impact**: 23% reduction in hallucinations

### Dual-Loop Planning
**Source**: Microsoft Research
**Approach**: Strategic (Task Ledger) + Tactical (Progress Ledger)

### Token Optimization
**Before**: 41,000 tokens per session
**After**: 1,500 tokens per session
**Savings**: 96%

## 🎨 Platform Support

drewsky works with multiple AI platforms:

| Platform | Support | Setup |
|----------|---------|-------|
| **Claude Code** | ✅ Full | [Guide](https://github.com/drewbeyersdorf/agent-improvement-techniques) |
| **Cursor** | ✅ Full | [Guide](https://github.com/drewbeyersdorf/agent-improvement-techniques/blob/main/CURSOR_SETUP_GUIDE.md) |
| **Windsurf** | 🔄 Planned | Coming soon |
| **VS Code (Continue)** | 🔄 Planned | Coming soon |

## 📁 File Structure

After initialization:

```
your-project/
├── .drewsky/
│   ├── config.json          # Framework settings
│   ├── metrics.json         # Productivity tracking
│   └── templates/           # Workflow templates
├── .research.md             # TCREI research (created by research command)
├── .plan.md                 # Implementation plan (created by plan command)
└── .verification-*.md       # CoVe reports (created by verify command)
```

## ⚙️ Configuration

Edit `.drewsky/config.json`:

```json
{
  "version": "0.1.0",
  "settings": {
    "confidenceThreshold": 70,
    "atomicStepDuration": 30,
    "contextWarning": 40,
    "contextEmergency": 60
  }
}
```

- **confidenceThreshold**: Minimum confidence % for steps
- **atomicStepDuration**: Max minutes per step
- **contextWarning**: Token usage warning threshold (K)
- **contextEmergency**: Token usage emergency threshold (K)

## 🤝 Contributing

We welcome contributions! See the [main repository](https://github.com/drewbeyersdorf/agent-improvement-techniques) for:
- Feature requests
- Bug reports
- Documentation improvements
- Code contributions

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Links

- **Documentation**: [GitHub Repository](https://github.com/drewbeyersdorf/agent-improvement-techniques)
- **Issues**: [Report a bug](https://github.com/drewbeyersdorf/agent-improvement-techniques/issues)
- **npm Package**: [npmjs.com/package/drewsky](https://www.npmjs.com/package/drewsky)

## 🙏 Acknowledgments

Built on research from:
- Google AI (TCREI methodology)
- Meta AI (Chain of Verification)
- Microsoft Research (Dual-Loop Planning)
- Anthropic (Claude Code platform)

---

**Made with ❤️ for rigorous AI collaboration**

*Eliminate guesswork. Verify claims. Build better software.*
