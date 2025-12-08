---
description: Apply TCREI validation (Task, Context, Reference, Evaluation, Input) to structure requests
---

# Apply TCREI Validation

Apply the TCREI (Task, Context, Reference, Evaluation, Input) framework to structure and validate your request for optimal AI collaboration.

## What is TCREI?

From Google's AI research - a 5-point validation that reduces ambiguity and improves AI output quality by ensuring complete task specification.

## Your Task

Take the user's request and help them structure it using TCREI:

### T - Task (What exactly?)
- What specific outcome or deliverable is needed?
- What is the core objective?
- What should NOT be included?

### C - Context (Why needed?)
- What problem does this solve?
- Who will use this?
- What constraints or requirements exist?

### R - Reference (Any examples?)
- Are there existing examples to follow?
- What patterns or standards should be matched?
- Any anti-patterns to avoid?

### E - Evaluation (Measure success?)
- How will we know this is complete?
- What are the acceptance criteria?
- What edge cases should be tested?

### I - Input (Read schema first?)
- What existing code/files should be examined first?
- What data structures or APIs are involved?
- What dependencies exist?

## Process

1. **Analyze the user's request** - Understand what they want
2. **Ask clarifying questions** - For any missing TCREI components
3. **Present structured version** - Show the request in TCREI format
4. **Get confirmation** - Ensure alignment before proceeding
5. **Execute with precision** - Use the validated structure

## Example

**User says:** "Fix the authentication bug"

**You respond with TCREI:**
```
📋 TCREI Validation:

T - Task: Debug and fix the authentication failure that prevents user login
C - Context: Users report they can't log in since yesterday's deployment
R - Reference: Should follow OAuth 2.0 standard, see auth.js:45-120
E - Evaluation: Users can successfully log in, tests pass, no console errors
I - Input: Need to examine: auth.js, login.component.ts, error logs

Should I proceed with this understanding?
```

This reduces hallucinations by ensuring complete specifications.
