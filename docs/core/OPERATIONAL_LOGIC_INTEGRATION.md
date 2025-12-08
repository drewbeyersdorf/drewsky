# 🧠 Operational Logic Integration Guide

**How "Anti-Vibe" Verification Rules Enhance the RPI Framework**

This document shows how operational logic constraints integrate with and enhance the RPI Framework's cognitive foundations.

---

## 🔄 Framework Overlap Analysis

### Core Philosophy Alignment

Both frameworks share a fundamental principle:

> **Verification over Assumption**
> - RPI Framework: "Chain of Verification (CoVe) - verify all claims with file:line references"
> - Operational Logic: "Anti-Vibe Verification Rule - execution is completion, not generation"

**Synergy:** These approaches are **complementary, not redundant**. RPI provides the *cognitive structure*, while Operational Logic provides *execution discipline*.

---

## 📊 Side-by-Side Comparison

| RPI Framework (Cognitive) | Operational Logic (Execution) | Integration Strategy |
|---------------------------|-------------------------------|---------------------|
| **TCREI Validation** - Ensure task clarity | **Context-First Pattern** - Read backend before UI | ✅ **TCREI includes reading schema/backend as Input** |
| **Chain of Verification** - Verify claims with sources | **Schema is Law** - Verify against actual schema | ✅ **CoVe verifies schema.ts as source of truth** |
| **Confidence Scoring** - Rate uncertainty 0-100% | **Recursive Debugging Loop** - Fix errors immediately | ✅ **Low confidence triggers debugging loop** |
| **MAKER Decomposition** - Break into <30min steps | **Anti-Vibe Rule** - Test each step before continuing | ✅ **Each atomic step includes test verification** |
| **Approval Gates** - Wait for user approval | **In-Distribution Tooling** - Use standard tools | ✅ **Plans specify standard tools, get approval** |

---

## 🎯 Enhanced Integration Rules

### Rule 1: Anti-Vibe Verification (ENHANCED with RPI)

**Original Operational Logic:**
```
Never mark "Done" until build/test passes
```

**RPI Enhancement:**
```
BEFORE marking task complete:
1. MUST run build/test command (Operational Logic)
2. MUST verify exit code = 0 (Operational Logic)
3. MUST document verification in .completion-snapshot.md (RPI)
4. MUST include actual test output, not assumed (CoVe)

Confidence Score: 100% only after verified test pass
```

**Implementation in ENFORCED_RPI_PROTOCOL.md:**
```markdown
### Implementation Quality Gate (ENHANCED)

BEFORE marking step complete, I verify:
✓ Followed plan exactly
✓ Tests pass (if applicable) → MUST RUN ACTUAL TESTS
✓ Exit code = 0 (verified, not assumed)
✓ No extra changes added
✓ Context still manageable
✓ Build succeeds (for code changes)

FORBIDDEN:
❌ Marking complete without running tests
❌ Assuming tests pass
❌ Hallucinating success logs
❌ "Probably works" confidence

IF tests fail → Re-decompose fix into atomic steps
```

---

### Rule 2: Schema is Law (ENHANCED with RPI)

**Original Operational Logic:**
```
Read schema.ts before writing components
```

**RPI Enhancement:**
```
TCREI Validation - Input Phase:
- Input MUST include: "Read schema.ts to verify field names"

RESEARCH PHASE:
- Create .research.md with:
  - Schema structure (verified from schema.ts:lines)
  - Field names (exact, not assumed)
  - Data types (verified)
  - Confidence: 100% (because read from source)

PLAN PHASE:
- Reference exact schema fields in code snippets
- Show schema.ts:line numbers in plan
- Verify no invented fields

Chain of Verification:
"Field 'userId' exists in schema.ts:45 where User table is defined"
```

**Implementation:**
```markdown
### RULE 10: Schema-First Development (NEW)

MANDATORY for any database/backend work:

1. **RESEARCH PHASE MUST include:**
   ```
   - Read schema.ts (or equivalent)
   - Document table structure with line numbers
   - Verify field names exist
   - Confirm data types
   - Check relationships/indexes
   ```

2. **FORBIDDEN BEHAVIORS:**
   ```
   ❌ Inventing field names not in schema
   ❌ Assuming schema structure
   ❌ Writing components without reading backend
   ❌ "Probably has a userId field"
   ```

3. **VERIFICATION FORMAT:**
   ```
   Claim: "User table has 'email' field"
   Verified: schema.ts:23 defines email: v.string()
   Confidence: 100%
   ```
```

---

### Rule 3: Recursive Debugging Loop (ENHANCED with RPI)

**Original Operational Logic:**
```
Don't ask user - read error, fix immediately
```

**RPI Enhancement:**
```
WHEN error occurs:

1. DO NOT mark step as complete (Anti-Vibe)
2. DO NOT ask user what to do (Recursive Debugging)
3. IMMEDIATELY use tools to:
   - Read error log (verify actual error)
   - Cat relevant file (verify context)
   - Apply CoVe to error message

4. CREATE .debug-plan.md with:
   - Error analysis (verified from logs)
   - Root cause (verified from code)
   - Fix steps (atomic, <30min each)
   - Confidence score for fix

5. IF confidence <70% for fix:
   - THEN ask user for input
   - ELSE proceed with fix autonomously

6. After fix:
   - Re-run tests (Anti-Vibe)
   - Verify exit code = 0
   - Update .completion-snapshot.md
```

**Implementation:**
```markdown
### RULE 11: Autonomous Error Recovery (NEW)

WHEN implementation step fails:

**PHASE 1: Error Analysis (Autonomous)**
```
→ Read error output (actual, not assumed)
→ Identify exact error message and line number
→ Cat the failing file
→ Apply CoVe: "Error states X at file.ts:Y"
→ Create .debug-plan.md
```

**PHASE 2: Confidence Check**
```
IF fix confidence ≥70%:
  → Implement fix autonomously
  → Re-run tests
  → Verify success

IF fix confidence <70%:
  → STOP and request user input
  → Show error analysis
  → Propose multiple fix options with confidence scores
```

**FORBIDDEN:**
```
❌ Asking user "What should I do?" without analysis
❌ Guessing at errors
❌ Skipping error verification
❌ Moving on without fixing
```
```

---

### Rule 4: In-Distribution Tooling (ENHANCED with RPI)

**Original Operational Logic:**
```
Use standard tools, not custom scripts
```

**RPI Enhancement:**
```
PLAN PHASE - Tool Selection:

1. Research available standard tools:
   - MCP tools (Postgres, GitHub, etc.)
   - Built-in CLI commands
   - Project-specific standard tools

2. In .plan.md, specify:
   - Which standard tool to use (verified it exists)
   - Why standard tool is preferred
   - Confidence: High (standard) vs Low (custom)

3. Quality Gate:
   ✓ Standard tool available? Use it.
   ✓ Standard tool insufficient? Document why.
   ✓ Custom script needed? Explain necessity.

Chain of Verification:
"Using `gh pr create` (verified: gh --version)"
NOT: "I'll write a script to create PRs"
```

**Implementation:**
```markdown
### RULE 12: Standard Tools First (NEW)

WHEN planning implementation:

**Tool Selection Priority:**
```
1. Standard MCP tools (highest priority)
2. Built-in CLI commands
3. Project-documented tools
4. Standard library functions
5. Custom scripts (ONLY if no alternative)
```

**PLAN PHASE MUST include:**
```
## Tool Justification

For each major operation:
- Tool chosen: [name]
- Standard/Custom: [Standard ✓]
- Verified available: [command --version output]
- Confidence: [90%+ for standard tools]

IF custom script needed:
- Justification: Why no standard tool works
- Alternatives considered: [list]
- Complexity estimate: [lines of code]
- Maintenance burden: [low/medium/high]
```

**FORBIDDEN:**
```
❌ Writing custom scripts without checking for standard tools
❌ "I'll write a script to..." (check for standard tool first!)
❌ Reinventing standard functionality
```
```

---

### Rule 5: Context-First Pattern (ENHANCED with RPI)

**Original Operational Logic:**
```
Read backend before building UI
```

**RPI Enhancement:**
```
TCREI Validation for UI tasks:

Task: "Build user profile component"

REQUIRED Input (cannot proceed without):
- Backend API endpoint (verified exists)
- Data shape from backend (verified from code)
- Schema structure (verified from schema.ts)
- Existing patterns (verified from similar components)

RESEARCH PHASE ORDER:
1. Read schema.ts (data structure)
2. Read backend API/query (data shape)
3. Read existing similar components (patterns)
4. ONLY THEN plan the UI component

Chain of Verification:
"User data has {id, name, email} from backend/api.ts:67"
NOT: "User probably has name and email fields"

Confidence: Cannot be >50% without reading backend
```

**Implementation:**
```markdown
### RULE 13: Backend-First UI Development (NEW)

FOR ANY UI/Frontend task:

**MANDATORY RESEARCH ORDER:**

```
CANNOT proceed to planning without:

1. Read schema.ts:
   - Document data structure
   - Verify field names
   - Note data types

2. Read backend logic:
   - API endpoints
   - Query structure
   - Mutation signatures
   - Response shape

3. Read existing UI patterns:
   - Similar components
   - State management approach
   - Styling conventions

4. ONLY THEN create UI plan
```

**TCREI Enhancement:**
```
Input (I): MUST include backend code references
Reference (R): MUST include similar components
Evaluation (E): MUST define how UI matches backend data

Example:
Input: Backend returns User from api/users.ts:45
Reference: Similar ProfileCard component in components/
Evaluation: UI displays all User fields from backend
```

**FORBIDDEN:**
```
❌ "I'll build the UI and we'll hook up the backend later"
❌ Assuming backend data shape
❌ Inventing API endpoints
❌ Building UI before reading backend code

MUST say:
✅ "First, let me read the backend to understand the data shape"
```
```

---

## 🔗 Complete Integration: Enhanced RPI Protocol

### Updated Workflow with Operational Logic

```
PHASE 0: TCREI VALIDATION (Enhanced)
├─ Task: Clear statement
├─ Context: Why needed
├─ Reference: Similar patterns (read existing code)
├─ Evaluation: Success = tests pass (Anti-Vibe)
├─ Input: Schema.ts + backend code (Schema is Law)
└─ Confidence check: >70% to proceed

PHASE 1: RESEARCH (Enhanced with Context-First)
├─ Read schema.ts FIRST (if data-related)
├─ Read backend logic SECOND (if UI task)
├─ Read existing patterns THIRD
├─ Verify all with file:line (CoVe)
├─ Use standard tools to explore (In-Distribution)
├─ Document in .research.md with verification
├─ Confidence scores per claim
└─ STOP for approval

PHASE 2: PLANNING (Enhanced with Standard Tools)
├─ Apply MAKER decomposition
├─ Each step specifies:
│  ├─ Standard tool to use (verified)
│  ├─ Test command to verify
│  ├─ Expected exit code
│  └─ Verification method
├─ Include schema references (exact fields)
├─ Show backend data shape in UI plans
├─ Overall confidence >70%
└─ STOP for approval

PHASE 3: IMPLEMENTATION (Enhanced with Anti-Vibe)
├─ Execute atomic steps
├─ After EACH step:
│  ├─ Run test/build command
│  ├─ Verify exit code = 0
│  ├─ Document actual output (not assumed)
│  └─ Mark complete ONLY if verified
├─ IF error occurs:
│  ├─ Read error log (Recursive Debugging)
│  ├─ Analyze root cause
│  ├─ Fix autonomously if confidence >70%
│  └─ Ask user if confidence <70%
├─ Report progress with test results
└─ Create .completion-snapshot.md with VERIFIED results
```

---

## 📋 Enhanced Enforcement Checklist

### Before EVERY task:

**Cognitive Framework Checks (RPI):**
- [ ] TCREI elements complete
- [ ] MAKER decomposition applied (if >30min)
- [ ] CoVe verification plan ready
- [ ] Confidence scored

**Operational Logic Checks (Enhanced):**
- [ ] Schema.ts will be read (if data-related)
- [ ] Backend will be read before UI
- [ ] Standard tools identified
- [ ] Test commands specified
- [ ] Exit code verification planned

### During Implementation:

**Standard RPI:**
- [ ] Following plan exactly
- [ ] Reporting progress
- [ ] Monitoring context

**Operational Enhancements:**
- [ ] Running actual tests (not assuming)
- [ ] Verifying exit codes
- [ ] Using standard tools
- [ ] Reading error logs immediately
- [ ] Fixing autonomously when possible

### Before Marking Complete:

**RPI Requirements:**
- [ ] Plan followed
- [ ] Context managed
- [ ] Snapshot created

**Operational Requirements:**
- [ ] Tests RUN and PASSED (exit code 0)
- [ ] Build succeeded (if code change)
- [ ] No invented schema fields
- [ ] Backend verified (if UI change)
- [ ] Actual output documented

---

## 🎯 Practical Integration Example

### Task: "Add user profile edit feature"

#### PHASE 0: TCREI (Enhanced)

```
Task: Add user profile edit feature
Context: Users can't update their info
Reference: Similar EditPost component exists
Evaluation: Success = user can save changes + tests pass
Input: MUST READ:
  - schema.ts for User fields
  - backend/api/users.ts for mutation
  - components/EditPost.tsx for pattern

Confidence in requirements: 90%
```

#### PHASE 1: RESEARCH (Enhanced)

```
Reading in priority order:

1. Schema verification:
   ✓ Read schema.ts:23-45
   ✓ User has: {id, name, email, avatar}
   ✓ Confidence: 100% (verified from source)

2. Backend verification:
   ✓ Read api/users.ts:67-89
   ✓ updateUser mutation exists
   ✓ Accepts: {id, name, email}
   ✓ Returns: User object
   ✓ Confidence: 100% (verified from code)

3. Pattern verification:
   ✓ Read EditPost.tsx:12-56
   ✓ Uses Formik for forms
   ✓ Validates before submit
   ✓ Shows success/error toast
   ✓ Confidence: 100% (verified pattern)

Created .research.md with all file:line references
```

#### PHASE 2: PLAN (Enhanced)

```
Atomic Steps with Operational Logic:

1. Create EditProfile component [20 min]
   - Tool: Standard React (verified: package.json:34)
   - Schema fields: name, email (verified schema.ts:25-26)
   - Pattern: Follow EditPost.tsx structure
   - Test: npm test EditProfile.test.tsx
   - Expected exit code: 0

2. Wire up updateUser mutation [15 min]
   - Backend: api/users.ts:67 updateUser function
   - Schema match: Verify fields align
   - Test: npm run test:api
   - Expected exit code: 0

3. Add form validation [15 min]
   - Tool: Formik (verified: package.json:56)
   - Validate email format
   - Test: npm test -- validation
   - Expected exit code: 0

4. Integration test [10 min]
   - Test: npm run test:integration
   - Verify: User profile updates in DB
   - Expected exit code: 0
   - Anti-Vibe: MUST see actual test pass

Confidence: 85%
```

#### PHASE 3: IMPLEMENTATION (Enhanced)

```
✓ Step 1/4: Component created
  Command run: npm test EditProfile.test.tsx
  Exit code: 0
  Output: "1 test passed"
  [VERIFIED - not assumed]

✓ Step 2/4: Mutation wired up
  Command run: npm run test:api
  Exit code: 0
  Output: "updateUser mutation works"
  [VERIFIED - not assumed]

✓ Step 3/4: Validation added
  Command run: npm test -- validation
  Exit code: 0
  Output: "Email validation passes"
  [VERIFIED - not assumed]

❌ Step 4/4: Integration test FAILED
  Command run: npm run test:integration
  Exit code: 1
  Error: "Field 'avatarUrl' does not exist on User"

RECURSIVE DEBUGGING (Autonomous):
→ Read error: Field mismatch
→ Check schema.ts:26: Field is 'avatar' not 'avatarUrl'
→ Fix: Change component to use 'avatar'
→ Re-run: npm run test:integration
→ Exit code: 0
→ Output: "Integration test passed"
✓ [VERIFIED - fixed and tested]

All steps complete - ALL TESTS VERIFIED PASSED
Created .completion-snapshot.md with actual test outputs
```

---

## 📖 Summary: Why This Integration Works

### RPI Framework Provides:
- 🧠 **Cognitive Structure** (how to think)
- 📋 **Process Discipline** (what order to do things)
- ✅ **Verification Framework** (how to confirm)

### Operational Logic Provides:
- 🔨 **Execution Standards** (what counts as done)
- 🛡️ **Error Handling** (what to do when things fail)
- 🎯 **Practical Rules** (specific best practices)

### Together They Create:
- 🚀 **Complete Workflow** (think → plan → execute → verify)
- 💯 **No Hallucinations** (everything verified)
- ⚡ **Autonomous Recovery** (fix errors immediately)
- 🎓 **Learning System** (patterns documented and reused)

---

## 🎯 Implementation in Your Repository

To add these enhancements:

1. **Update ENFORCED_RPI_PROTOCOL.md** with Rules 10-13
2. **Add this file** to explain the integration
3. **Update settings.json** with operational flags
4. **Test** with a real task to verify integration

The result: **RPI Framework with Operational Excellence** - The most rigorous AI collaboration system available.

---

**Version:** 1.1 (Enhanced with Operational Logic)
**Compatibility:** Works with existing RPI Framework
**Recommendation:** Apply all enhancements for maximum effectiveness
