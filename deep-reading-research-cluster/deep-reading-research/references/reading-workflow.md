# Reading Workflow

This module answers: how do we read, in what order, and what do we produce after each slice?

## Core Loop

1. `Scan`
2. `Parse`
3. `Compare`
4. `Hypothesize`
5. `Verify`
6. `Ledger`
7. `Retell`

## What each step does

### Scan

- Map the corpus.
- Separate primary files, references, generated files, logs, and irrelevant files.
- Record file counts and, when useful, line counts.

### Parse

- Read the slice in context.
- Extract structure, not just keywords.
- Explain what this slice adds to the understanding.

### Compare

- Compare same-shape artifacts: template vs template, example vs example, table vs table.
- Use differences to generate sharper questions.

### Hypothesize

- Convert an unexplained name, folder, field, or pattern into a candidate explanation.
- Mark it as soft until the evidence is enough.

### Verify

- Read the next source class that can support or break the hypothesis.
- Prefer complete examples and direct documentation over intuition.

### Ledger

- Add the question to the question table.
- Preserve trigger point, current state, and answer snapshot.

### Retell

- Restate what is known, what is not, what is inferred, and what remains uncertain.
- This is a check on understanding, not a summary flourish.

## Artifact Loop

- The reading table records the slice and its status.
- The reading batch must produce new questions or update existing ones.
- Those questions become the next slice selector.
- Evidence gathered from the next slice updates question state and answer snapshots.
- A reusable path or task is only produced when the user asks to consolidate the session.
- Distillation never replaces the original trigger points or evidence trail.

## Progress Tracking

Use a compact table whenever the reading task spans more than a few files.

```text
| File | Lines read | Total lines | Status | Notes |
|---|---:|---:|---|---|
| path/to/file.md | 1-120 | 240 | partial | APIs identified; lifecycle unclear |
```

## Reading Budget

- Give each region a limited reread budget.
- Treat the budget as a guard against endless local churn.
- If the budget is exhausted, move to the next source class or ask for a targeted reread.

## Hard Rules

- Do not read file after file with no analysis.
- Do not use keyword search as a substitute for reading when the user asked for full reading.
- Do not claim a full understanding from one example.
- Do not turn names into lifecycle explanations.
- Do not hide uncertainty.
- Do not skip progress tracking when the user asked to read everything.
- Do not assume every deep session must end in a reusable method artifact.
