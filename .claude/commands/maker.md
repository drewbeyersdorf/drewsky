---
description: Apply MAKER decomposition to break complex tasks into Manageable, Atomic, Knowable, Executable, Reviewable steps
---

# Apply MAKER Decomposition

Break down complex tasks into Manageable, Atomic, and Knowable steps using MAKER Logic - a systematic task decomposition methodology.

## What is MAKER?

From AI Engineering research - a decomposition strategy that prevents overwhelm, enables progress tracking, and identifies knowledge gaps early.

**M**anageable - Each step is small enough to complete in one focused effort
**A**tomic - Each step is indivisible and has a single purpose
**K**nowable - We can verify when each step is truly complete
**E**xecutable - Each step has clear actions (not vague)
**R**eviewable - Each step's output can be validated

## Your Task

Take the user's complex request and decompose it using MAKER:

### Step 1: Identify Complexity
- Is this task compound (multiple objectives)?
- Are there dependencies between subtasks?
- Does this require knowledge discovery first?

### Step 2: Break Down Using MAKER
For each subtask, ensure it's:
- **Manageable**: Can be done in one session
- **Atomic**: Single, indivisible purpose
- **Knowable**: Clear completion criteria
- **Executable**: Concrete actions, not vague
- **Reviewable**: Output can be validated

### Step 3: Sequence & Dependencies
- Which steps must happen first?
- Which can run in parallel?
- Where are the decision points?

### Step 4: Present for Approval
- Show the numbered step list
- Highlight any unknowns or risks
- Get user confirmation before starting

## Example

**User says:** "Implement user authentication"

**You respond with MAKER:**
```
🔨 MAKER Decomposition:

Complex task detected. Breaking down into MAKER steps:

1. [Research] Examine existing auth patterns in codebase (auth.js, user.model.js)
2. [Design] Choose auth strategy (JWT vs Session) - needs user input
3. [Setup] Install required packages (jsonwebtoken, bcrypt)
4. [Build] Create user registration endpoint with password hashing
5. [Build] Create login endpoint with token generation
6. [Build] Create auth middleware for protected routes
7. [Test] Write unit tests for auth functions
8. [Test] Write integration tests for auth flow
9. [Validate] Manual testing with Postman/curl
10. [Document] Update API documentation

Dependencies: 1 → 2 → 3 → [4,5,6] → [7,8] → 9 → 10
Unknowns: Auth strategy (need your preference)

Proceed with this breakdown?
```

This approach prevents scope creep and ensures nothing is missed.
