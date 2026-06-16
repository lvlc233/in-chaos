# Structured Audit Corpus

This module answers: how do we annotate source slices for later analysis?

Every slice should be tagged as one of:

- `fact`
- `inference`
- `hypothesis`
- `noise`

## Tag meanings

- `fact`: directly supported by the source
- `inference`: derived from supported facts
- `hypothesis`: candidate explanation not yet confirmed
- `noise`: useful as process context only, not as evidence

## Why this matters

The goal is not to turn the corpus into a summary.
The goal is to preserve the separation between source facts, derived structure, and speculative interpretation.

