---
name: deep-reading-workflow
description: Read a corpus in slices, maintain progress, restate after each batch, and preserve the reading loop. Use when the user wants full reading, reading progress tracking, or stepwise understanding instead of a keyword search.
---

# Deep Reading Workflow

Use this skill when the task is: "read this corpus deeply and keep track of what happened while reading."

## What this skill does

- maps the corpus
- reads in slices
- maintains reading status
- restates before concluding
- keeps the read-think-read loop active
- treats each deep session as an isolated pass unless the user asks to continue the same task

## Required Output

Every batch should include:

- file or slice
- read range
- current understanding
- new questions
- next slice

If the corpus is large, include a progress table.

## Hard Rules

- Do not read file after file with no analysis.
- Do not turn keyword hits into full understanding.
- Do not skip progress tracking when the user asked for full reading.
- Do not hide uncertainty.
- Do not promote raw reading notes into a permanent reusable method unless the user asked for distillation.

## References

See `../deep-reading-research/references/reading-workflow.md` and `../deep-reading-research/references/terms.md`.
