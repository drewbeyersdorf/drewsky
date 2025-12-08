---
description: Apply Dual-Loop Planning with strategic (goals) and tactical (actions) coordination for complex work
---

# Apply Dual-Loop Planning

Use Microsoft's Magentic-One dual-loop planning methodology for complex, multi-phase work with strategic and tactical coordination.

## What is Dual-Loop Planning?

From Microsoft Research (Magentic-One, 2024) - A two-level planning system that separates strategic vision from tactical execution:

**Outer Loop (Strategic)** - The "what" and "why"
- High-level goals and milestones
- Success criteria and constraints
- Risk identification and mitigation
- Replanning triggers

**Inner Loop (Tactical)** - The "how" and "when"
- Concrete action steps
- Progress tracking and validation
- Stall detection and recovery
- Immediate next actions

## Your Task

Apply dual-loop planning to complex, multi-phase requests:

### Outer Loop (Strategic Planning)

1. **Define End Goal**
   - What does "done" look like?
   - What are the key milestones?
   - What constraints must be respected?

2. **Identify Risks**
   - What could go wrong?
   - What unknowns exist?
   - Where might we get stuck?

3. **Set Replanning Triggers**
   - When should we reconsider the approach?
   - What discoveries would change the plan?
   - How do we detect if we're stuck?

### Inner Loop (Tactical Execution)

1. **Current Phase** - What phase are we in?
2. **Next Actions** - What are the immediate next 3-5 steps?
3. **Progress Check** - How do we know each step worked?
4. **Stall Detection** - Are we making progress or spinning wheels?

### Coordination

- **Facts vs Guesses** - Clearly separate verified info from assumptions
- **Decision Points** - Where do we need user input?
- **Progress Ledger** - Track what's been completed vs remaining

## Example

**User says:** "Refactor our authentication system to use JWT"

**You respond with Dual-Loop Plan:**
```
🎯 Dual-Loop Planning Active

═══ OUTER LOOP (Strategic) ═══

End Goal: Replace session-based auth with stateless JWT authentication
Milestones:
1. ✓ Understand current system
2. → Design new JWT architecture
3. → Implement token generation/validation
4. → Migrate existing users
5. → Deploy with rollback plan

Constraints:
- Zero downtime requirement
- Must maintain backward compatibility during migration
- Security: JWT secret rotation strategy needed

Risks:
⚠️  Token invalidation complexity (logout, password change)
⚠️  Refresh token storage decisions
⚠️  Migration path for active sessions

Replanning Triggers:
- If current auth has custom logic we can't migrate
- If security requirements change
- If we discover breaking changes in dependencies

═══ INNER LOOP (Tactical) ═══

Current Phase: Analysis
Next Actions:
1. Read current auth implementation (auth.service.js, session.config.js)
2. Document current session lifecycle
3. List all auth-related endpoints
4. Identify custom middleware

Progress Check:
✓ For each action, I'll confirm file contents
✓ Document findings in structured format
✓ Validate understanding with you before proceeding

Stall Detection:
If after reading 5+ files I still don't understand the auth flow → ask for help
If I'm repeating the same searches → try different approach

═══ FACTS vs GUESSES ═══

Facts:
- [Will be populated as I read code]

Guesses (need verification):
- Assuming session-based auth (need to confirm)
- Assuming Express.js (need to check)

Ready to start Phase 1 (Analysis)?
```

This approach prevents getting lost in complex refactoring and ensures strategic alignment.

## When to Use
- Large refactoring tasks
- Multi-file feature implementations
- Architectural changes
- Migration projects
- Complex debugging that spans multiple systems
- Anything that takes >30 minutes
