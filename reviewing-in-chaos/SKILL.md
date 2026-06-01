---
name: reviewing-skills
description: Use when auditing or reviewing an EXISTING skill's architecture for defects — examine a skill's structural flaws, diagnose why it goes off-course under context compression or across sessions, compare against well-established quality baselines. Triggers: audit a skill, what's wrong with this skill, skill defects, skill architecture review, review a skill. NOT for writing a brand-new skill (use writing-skills / skill-creator instead).
---

# reviewing-skills

> STATUS: evolving (DRAFT — current version controlled by CHANGELOG.md)
> This rubric is still iterating. After each real skill review, backfill newly learned dimensions / bad smells into
> `references/rubric.md` and `CHANGELOG.md`. **Iteration is a side path, don't block the main review.**

## Core Principle

Review a skill's **architecture** — not nitpick syntax — assess whether its **organization** enables an LLM to perform correctly under real constraints:
**context will be compressed, sessions will switch, tasks will be dispatched asynchronously**.

> A skill's robustness should not depend on runtime assumptions it can't control (e.g. "the runtime won't compress context").

## When to Use / Not Use

**Use:** auditing an existing skill; diagnosing why a skill fails in production; benchmarking against a rubric; preparing to restructure a skill.
**Not use:** writing a new skill (→ `writing-skills` / `skill-creator`); modifying application code.

## Review Process

1. **Read fully** — target skill's SKILL.md + all references, line by line (not skimming). Measure volume first (`wc -l`).
2. **Classify first + run each rubric dimension** — determine skill type (long-chain stateful / short-chain tool / pure guidance), then evaluate against `references/rubric.md` 8 dimensions, recording each.
3. **Mark defects + evidence** — each defect gets `file:line` + baseline comparison (what it should look like).
4. **Assign severity** — Architectural / Structural / Robustness / Minor.
5. **Find root cause** — most defects share the same underlying issue; crystallize into one sentence.
6. **Provide improvement direction** — one actionable direction per defect.
7. **Acknowledge strengths** — list what it does right, avoid one-sidedness (diagnosis is only credible when balanced).
8. **(Side path) Backfill** — if new dimensions / bad smells not in rubric are discovered, update rubric + CHANGELOG. Don't block the main review.

Output format reference: `examples/video-remix.md` (root cause → volume clarification → defect table → strengths → root cause crystallized → improvement directions).

## 8-Dimension Checklist (see references/rubric.md for details)

1. **Volume & attention budget** — How large is SKILL.md? What must be present vs. read on demand? (count self-written vs vendor separately)
2. **Single responsibility vs. kitchen sink** — How many responsibilities? Is there a "what it does NOT do" boundary declaration?
3. **State persistence across context compression / step transitions** — Relies on writing to disk (robust) or memory (fragile)? Critical for long-chain stateful skills
4. **Explicit control flow** — Is the decision skeleton (flowchart) separated from execution details? (bidirectional: too much crammed in vs. purely prose where structure is needed)
5. **Enforcement layering + centralized anti-hallucination** — Hard rules vs soft rules clearly separated? Anti-hallucination guardrails concentrated in one red-flag zone or scattered?
6. **Composability & downstream awareness** — Cross-reference or copy? Existing skills in same repo reused? Downstream notification mechanism in place?
7. **Description = trigger condition** — Only describes *when*, not mixed with *what* / capability list / workflow?
8. **Execution-layer correctness / failure modes** — (Tool-type especially) Command semantics correct? Cross-platform? Silent-fail? Critical for tool-type skills

> **Classify the skill first** to determine the main battleground: **Long-chain stateful** → Dimension 3 as litmus test ("after step K with compression, does earlier state still exist?");
> **Short-chain tool** → Dimension 8 as litmus test ("is the core command semantics of the signature feature actually correct?"). Don't force Dimension 3 onto short-chain tools.

## Baseline Anchors (living references)

- **superpowers / writing-skills** — Good-skill scorecard: Iron Law, Red Flags table, Rigid/Flexible labeling,
  progressive disclosure, CSO (description only states trigger conditions).
- **video-use** — Long-process paradigm: **never trust memory, persist everything to disk** (project.md / edl.json / takes_packed.md, read on startup),
  `ask→confirm→execute→iterate→persist`, hard rules vs artistic freedom, self-eval capped at top (Cap at 3).

## Sibling Skill

- **`evaluating-skill-output`** — This skill statically audits "is it **well-written**"; once the structure review is done, to **dynamically test the output** (behavioral correctness / intermediate state quality / content aesthetic quality), switch to that skill. The two form a pair: "audit + test" — incomplete without both.

## References

- `references/rubric.md` — 8-dimension details (inspection questions / good patterns / bad smells / severity)
- `examples/video-remix.md` — First worked example (monolithic version review)
- `CHANGELOG.md` — Iteration log
