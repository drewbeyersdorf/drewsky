---
description: Apply Chain of Verification (CoVe) to fact-check claims and reduce hallucinations by 23%
---

# Apply Chain of Verification (CoVe)

Use Meta AI's Chain of Verification methodology to validate claims and reduce hallucinations by up to 23%.

## What is CoVe?

From Meta AI Research (2024) - A 4-step systematic verification process that catches AI hallucinations before they propagate:

1. **Generate baseline response** (initial answer)
2. **Plan verification questions** (what could be wrong?)
3. **Answer independently** (verify each claim)
4. **Generate final verified response** (incorporate corrections)

## Your Task

Apply CoVe to verify factual claims, code correctness, or logical reasoning:

### Step 1: Baseline Response
- Generate the initial response to user's query
- Identify specific claims that need verification
- Tag anything you're uncertain about

### Step 2: Plan Verification
For each claim, ask:
- Can this be verified from provided files/docs?
- Is this based on assumptions vs facts?
- What would disprove this claim?
- Are there edge cases I'm missing?

### Step 3: Independent Verification
- Check files/docs directly (don't rely on memory)
- Search for counter-examples
- Test assumptions against reality
- Separate "facts" from "educated guesses"

### Step 4: Verified Response
- Present corrected response
- Clearly mark remaining uncertainties
- Provide sources/evidence for claims
- Admit gaps in knowledge honestly

## Example

**User asks:** "What's the API endpoint for user deletion?"

**You apply CoVe:**
```
🔍 Chain of Verification Active

Step 1 - Baseline Response:
"The user deletion endpoint is DELETE /api/users/:id"

Step 2 - Verification Plan:
- [ ] Check routes file for actual endpoint definition
- [ ] Verify HTTP method (DELETE vs POST)
- [ ] Check if soft delete vs hard delete
- [ ] Look for authorization requirements

Step 3 - Verification:
[Reading routes/api.js...]
Found: POST /api/users/:id/delete (line 47)
Authorization: Requires admin role (middleware:isAdmin)
Type: Soft delete (sets deletedAt timestamp)

Step 4 - Verified Response:
"The user deletion endpoint is:
- **Endpoint**: POST /api/users/:id/delete
- **Method**: POST (not DELETE)
- **Auth**: Requires admin role
- **Type**: Soft delete (doesn't remove from DB)
- **Source**: routes/api.js:47

Note: This is a soft delete that preserves data. For hard delete, see admin/purge endpoint."
```

This process catches assumptions before they become mistakes.

## When to Use
- Answering questions about code you haven't read recently
- Making architectural recommendations
- Debugging based on incomplete information
- Explaining API behavior or documentation
- Any time you feel uncertain about a claim
