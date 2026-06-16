---
name: deep-subagent-research
description: Delegate narrow, evidence-heavy uncertainties to read-only subagents with exact ownership, search paths, keywords, and evidence requirements. Use when the main thread should keep synthesizing while a bounded research task runs in parallel.
---

# Deep Subagent Research

Use this skill when the task should be delegated instead of explored only in the main thread.

## What this skill does

- writes bounded task sheets
- assigns exact ownership
- keeps the research read-only unless the user asked otherwise
- requires direct evidence and negative evidence
- merges subagent results back into the main thread

## Task Sheet Requirements

Every task sheet should include:

- ownership
- search path
- search keywords or files
- exact questions
- output format
- read-only or editable scope
- what not to touch

## Required Output

Ask for:

- direct evidence with paths
- negative evidence
- conclusion level
- remaining uncertainty

## Hard Rules

- Do not let a subagent re-plan the whole task.
- Do not use a subagent to bypass scope limits.
- Do not delegate an unclear task without bounding it first.

## References

See `../deep-reading-research/references/subagent-research.md` and `../deep-reading-research/references/terms.md`.

