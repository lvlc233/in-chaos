---
name: deep-evidence-research
description: Judge claims with evidence levels, matrices, negative evidence, competing hypotheses, and minimum confirmable conclusions. Use when the task is to decide what the corpus supports rather than to restate what it says.
---

# Deep Evidence Research

Use this skill when the question is: "what can we safely conclude?"

## What this skill does

- ranks evidence
- keeps competing hypotheses alive
- records negative evidence
- assigns conclusion levels
- preserves transfer boundaries
- gives minimum confirmable conclusions

## Hard Rules

- Names and headers only produce candidate explanations.
- Example code is not a global rule unless the evidence says so.
- Negative evidence must be recorded when it changes confidence.
- Do not flatten `unconfirmed` into `confirmed`.

## Required Output

Include:

- claim or hypothesis
- evidence matrix
- negative evidence
- conclusion level
- transfer boundary
- minimum confirmable conclusion

## References

See `../deep-reading-research/references/evidence-framework.md`, `../deep-reading-research/references/structured-audit-corpus.md`, and `../deep-reading-research/references/terms.md`.

