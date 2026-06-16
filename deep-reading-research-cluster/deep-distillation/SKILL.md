---
name: deep-distillation
description: Distill reading logs, question tables, and debugging records into reusable rules, clusters, and downstream interfaces. Use when the goal is to turn raw notes into a transferable skill or method.
---

# Deep Distillation

Use this skill when the task is: "turn the raw records into a reusable method or path" and the user explicitly asked for that output.

## What this skill does

- clusters repeated problems
- keeps the final fix and verification
- extracts behavior rules
- strips noisy chronology
- states transfer boundaries
- preserves downstream interfaces
- is optional, not automatic

## Hard Rules

- Do not copy raw logs into the final skill.
- Do not turn domain content into a general rule unless the corpus supports it.
- Do not preserve intermediate attempts unless they explain the final fix.
- Do not erase uncertainty; mark unstable conclusions as experience data.
- Do not produce a reusable artifact unless the user asked to extract one.

## Required Output

Include:

- reusable rules
- what should not be carried forward
- transfer boundary
- downstream target

## References

See `../deep-reading-research/references/experience-distillation.md`, `../deep-reading-research/references/downstream-interfaces.md`, and `../deep-reading-research/references/terms.md`.
