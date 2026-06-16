# Subagent Research

This module answers: how do we delegate without losing the thread?

## When to use

Use a subagent when the uncertainty is:

- separable
- evidence-heavy
- narrow enough to own
- not better handled by the main thread directly

## Task Sheet

Every subagent task should include:

- ownership
- search path
- search keywords or files
- exact questions
- required evidence format
- read-only or editable scope
- what not to touch

## Required Output

Ask the subagent to return:

1. direct evidence with paths
2. negative evidence
3. conclusion level
4. remaining uncertainty

## Anti-Pattern

- Do not let subagents re-plan the whole task.
- Do not ask a subagent to explain the world.
- Do not use a subagent as a bypass for scope limits.

