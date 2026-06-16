---
name: deep-question-ledger
description: Turn reading into an explicit question ledger with trigger points, states, answer snapshots, and relation tables. Use when the task is to track unresolved items, preserve concept boundaries, or maintain a question-driven reading record.
---

# Deep Question Ledger

Use this skill when the important artifact is the question table, not the prose summary.

## What this skill does

- records each question separately
- binds each question to a trigger point
- tracks unresolved / partial / resolved / deferred states
- preserves answer snapshots over time
- records concept boundaries and relation tables
- feeds the next reading slice selection

## Hard Rules

- Every question needs a trigger point.
- Do not merge unresolved questions too early.
- Do not promote `partial` to `resolved` without evidence.
- Do not answer from memory when the corpus has not said it yet.
- Do not let a later summary erase the original question state or trigger point.
- Do not turn the ledger into a permanent knowledge base by default.

## Required Output

For each question, include:

- trigger point
- state
- answer snapshot
- evidence links
- concept boundary

## Loop Role

- The ledger is the handoff point between reading and the next reading pass.
- Unresolved and partial items should stay visible because they select the next slice.
- When later evidence arrives, update the snapshot first, then decide whether the state can move forward.
- If the item is still not supported, keep it in the ledger instead of burying it in distillation.
- The ledger is session-scoped unless the user explicitly asks to export it as a reusable artifact.

## References

See `../deep-reading-research/references/question-ledger.md` and `../deep-reading-research/references/terms.md`.
