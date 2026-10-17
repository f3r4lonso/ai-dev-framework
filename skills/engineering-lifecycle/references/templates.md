# Templates

## Requirement and acceptance criteria

```markdown
## <Feature or change>
Goal: <outcome for the user, one sentence>
Users / callers: <who>
In scope: <bullets>
Out of scope: <bullets>
Constraints: <performance, security, compatibility, budget, deadlines>
Acceptance criteria (each testable):
- Given <context>, when <action>, then <observable result>
Open questions: <only those that change scope, risk or architecture>
```

## Task plan

```markdown
| # | Step | Files / areas | Verification | Rollback |
|---|---|---|---|---|
| 1 | ... | ... | test or command that proves it | how to undo |
Risks: <what could break, who is affected>
```

## Architecture decision record (ADR)

Store as `docs/adr/NNNN-short-title.md` in the project that owns the decision. Never edit an accepted ADR;
supersede it with a new one.

```markdown
# NNNN. <Decision title>
Status: proposed | accepted | superseded by NNNN
Date: YYYY-MM-DD
## Context
<forces, constraints, evidence>
## Options considered
1. <option> — pros / cons / cost
2. ...
## Decision
<what and why>
## Consequences
<positive, negative, follow-up work, how to reverse>
```

## Work report (output contract)

```markdown
Outcome: <done / partly done / blocked> — <one sentence>
Changed: <paths and why>
Verified: <checks that ran, with result>
Not verified: <checks not run and why>
Risks / open decisions: <bullets>
Next step: <the single most valuable follow-up>
```
