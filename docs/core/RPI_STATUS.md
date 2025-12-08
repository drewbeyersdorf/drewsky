# RPI Framework Status

## ✅ ENFORCED RPI MODE + 10x COGNITIVE FRAMEWORKS: ACTIVE

The Research → Plan → Implement workflow with **Cognitive Enhancement** is now **MANDATORY** for all non-trivial tasks.

---

## What This Means

### For You (The User)
- You will **always** see research before implementation
- You will **always** approve plans before code changes
- You will **always** get approval gates
- You will **always** see verified claims (not assumptions)
- You will **always** get confidence scores on recommendations
- You will **never** see surprise implementations
- You will **never** see unverified "probably" statements

### For Claude (The Agent)
**RPI Core Requirements:**
- **MUST** research before implementing
- **MUST** create explicit plans with code snippets
- **MUST** stop at approval gates
- **MUST** monitor context window
- **CANNOT** implement without approval
- **CANNOT** skip research for complex tasks

**Cognitive Framework Requirements:**
- **MUST** validate TCREI (Task, Context, Reference, Evaluation, Input)
- **MUST** use MAKER decomposition for tasks >30 minutes
- **MUST** verify all claims with Chain of Verification (CoVe)
- **MUST** assign confidence scores to recommendations
- **MUST** stop and ask questions when confidence <80%
- **CANNOT** proceed with vague requirements
- **CANNOT** make unverified claims
- **CANNOT** assume when can verify

---

## How to Verify It's Working

### Test 1: TCREI Validation (Cognitive Framework)
```
You: "Add a new feature to the system"

Expected Behavior:
✓ Claude asks for missing TCREI elements:
  - "What's the context? Why is this needed?"
  - "What does success look like?"
  - "Are there examples to follow?"
✓ Claude STOPS until TCREI is complete
✓ Claude documents TCREI in .research.md

If Claude proceeds without asking → Cognitive Framework NOT active
```

### Test 2: Chain of Verification (CoVe)
```
You: "How does authentication work?"

Expected Behavior:
✓ Claude verifies claims with file:line references
✓ You see: "Verified by reading auth.ts:45-67..."
✓ Claude assigns confidence scores to claims
✓ Assumptions are marked with ⚠️ and low confidence

If you see "probably" or unverified claims → CoVe NOT active
```

### Test 3: MAKER Decomposition
```
You: "Refactor the authentication system"

Expected Behavior:
✓ Claude estimates >30 minutes
✓ Claude decomposes into atomic steps
✓ Each step has input/output/verification
✓ Claude presents decomposition for approval
✓ Claude STOPS before executing

If Claude skips decomposition → MAKER NOT active
```

### Test 4: Confidence Scoring
```
You: "Should we use Redis or Memcached?"

Expected Behavior:
✓ Claude provides recommendation with confidence score
✓ If confidence <80%, Claude asks clarifying questions
✓ You see confidence breakdown by factor
✓ Uncertainties are explicitly listed

If no confidence score → Confidence Scoring NOT active
```

### Test 5: Standard RPI Approval Gates
```
You should see these STOP points:
1. TCREI validation: "Please provide missing context..."
2. After research: "Waiting for your approval to proceed to planning"
3. After plan: "I will NOT implement until you approve"
4. Low confidence: "My confidence is X%, need clarification on..."

If you don't see these → Framework NOT active
```

---

## Current Settings

```json
{
  "enforced_rpi": true,
  "context_threshold_warning": 40,
  "context_threshold_emergency": 60,
  "require_plan_approval": true,
  "require_research_approval": true,
  "auto_compact_enabled": true,
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

### What Each Cognitive Framework Does

**TCREI Validation** (Input Clarity):
- Ensures Task, Context, Reference, Evaluation, and Input are clear
- Stops and asks questions if requirements are vague
- Documents understanding before starting work

**MAKER Decomposition** (Task Management):
- Breaks tasks >30 min into atomic steps (<30 min each)
- Each step has clear input, output, and verification
- Prevents large, unmanageable tasks

**Chain of Verification (CoVe)** (Factuality):
- All claims verified with sources (file:line references)
- No "probably" or "should" statements
- Assumptions marked with confidence scores

**Confidence Scoring** (Uncertainty Management):
- Every recommendation gets 0-100% confidence score
- <70% confidence → STOP and ask questions
- <80% confidence → Request clarification
- Uncertainties explicitly listed

---

## Files Created

| File | Purpose |
|------|---------|
| `ENFORCED_RPI_PROTOCOL.md` | The rules Claude follows |
| `settings.json` | Configuration settings |
| `RPI_STATUS.md` | This status file |
| `USER_GUIDE_context_engineering.md` | Your complete guide |
| `QUICK_REFERENCE.md` | Your cheat sheet |
| `agent_context_engineering.md` | Technical protocol |

---

## What Changed

### BEFORE (Optional RPI)
```
You: "Add feature X"
Claude: [Immediately implements]
You: "Wait, that's not what I wanted!"
```

### AFTER (Enforced RPI)
```
You: "Add feature X"
Claude: "Starting RESEARCH phase..."
Claude: "Created .research.md - please review"
You: [Reviews] "Good, plan it"
Claude: "Created .plan.md - please approve"
You: [Reviews] "Approved"
Claude: "Implementing..."
```

---

## Override Commands (If Needed)

If you need to bypass RPI for a specific task:

```
"Skip research, implement directly: [task]"
"Emergency mode: [task]"
"No RPI: [task]"
```

⚠️ Claude will warn you about bypassing safety checks but will comply.

---

## Troubleshooting

### Claude isn't stopping at approval gates
→ Say: "You must stop and wait for my approval at each phase"

### Claude is implementing without a plan
→ Say: "Stop. Create .plan.md first and wait for approval"

### Context is growing too large
→ Say: "Compact the context now"

### Claude isn't using sub-agents
→ Say: "Use sub-agents for this research to keep context clean"

---

## Next Steps

1. **Test it**: Give Claude a complex task and watch the RPI workflow activate
2. **Review outputs**: Look for `.research.md` and `.plan.md` files
3. **Use approval gates**: Take control at each STOP point
4. **Monitor context**: Claude will report context % automatically

---

## Success Indicators

✅ You're seeing `.research.md` files before implementation
✅ You're seeing `.plan.md` files with code snippets
✅ Claude is asking for approval at each gate
✅ Context stays <40% most of the time
✅ You're reviewing plans, not watching Claude search

---

## Framework is Active and Enforced

**Status**: ✅ ACTIVE (RPI + Cognitive Frameworks)
**Mode**: ENFORCED
**Bypass**: Available via override commands
**Monitoring**: Automatic context tracking + cognitive quality gates enabled

**You now have mandatory RPI workflow enhanced with 10x Cognitive Frameworks:**
- ✅ TCREI Validation - Input clarity enforced
- ✅ MAKER Decomposition - Complex tasks broken into atomic steps
- ✅ Chain of Verification - All claims verified with sources
- ✅ Confidence Scoring - Uncertainty explicitly managed

Ready to test? Give Claude any complex task and watch:
1. TCREI validation (asks clarifying questions if needed)
2. Research phase with verified claims
3. MAKER decomposition for complex tasks
4. Confidence-scored recommendations
5. Approval gates at each phase
