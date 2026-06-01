---
name: evaluating-skill-output
description: Use when testing or evaluating what a skill PRODUCES when it runs — test whether a skill runs correctly and produces quality output (behavioral correctness + intermediate state quality + content/aesthetic quality). Distinct from reviewing-skills (which audits whether a skill's documentation is well-structured, static); this skill tests what the skill actually outputs (dynamic). Triggers: test a skill, evaluate skill output, does this skill run correctly, intermediate state quality, content quality, aesthetic scoring, build tests for a skill, eval skill output, test skill behavior. NOT for writing a new skill (that's writing-skills / skill-creator).
---

# evaluating-skill-output

> STATUS: evolving (v0.1, extracted from video-remix three-layer testing system). Pairs with [[reviewing-skills]].

## Core Principle

Test a skill's **output** (what it does when running + what it produces), not audit its documentation (that's [[reviewing-skills]]).

> **Structure vs Content**: reviewing-skills answers "is this skill **well-written**" (static document audit); this skill answers "does it **run correctly and produce quality output**" (dynamic output testing).
> Existing frameworks (skill-creator) can test the functional layer (L1), but **cannot systematically test intermediate state quality (L2) and content/aesthetic quality (L3)** — that is the blind spot this skill fills.

## Three Layers: What to Test

| Layer | What to Test | Judge |
|-------|-------------|-------|
| **L1 Functional / Flow** | Is the action plan correct? Are fields/branches/contracts correct? Does it fail early? | grader assertion (reuse skill-creator, **support multiple runs for variance**) |
| **L2 Intermediate State Quality** | Are each state's **intermediate artifacts** correct (if the skill is a state machine)? | grader checks state contract assertions on intermediate artifacts + records deviations; **mock single states for testing** |
| **L3 Content / Aesthetic Quality** | Is the output good? Does it resemble the target reference? | L3a: objective comparison against reference; L3b: subjective aesthetic via rubric + voting + human calibration |

> **Classify first — not every skill needs all three layers**: pure stateless tool-type may only need L1; long state-machine skills need L2; skills with content/creative output (video/copy/design) need L3.
> The Judge column lists only each layer's most characteristic method; **"record deviations + attribute root cause" applies across all three layers** (general rule #2), not just L2.

## How to Use

1. **Classify the skill under test**: Does it have a state machine? Does it have content/creative output? → Determine which layers are needed.
2. **Define standards per layer first** (standards before testing): L1 = expected assertions; L2 = state contracts; L3 = rubric anchors.
3. **Run + record deviations**: Follow methodology general rules (see `references/methodology.md`).
4. **Run multiple times to counter randomness** (reuse skill-creator variance: mean/stddev).

## Methodology General Rules (single source of truth = `references/methodology.md`)

Six rules cutting across all three layers. **Full definitions in `references/methodology.md` (authoritative source); listed here as headlines for scanning only. To change general rules, only change there — prevent dual-copy drift (this skill's own Dimension 6 warning)**:

1. Standards first, testing second;
2. **Record deviations + attribute root cause — across all three layers (L1/L2/L3), not just L2**;
3. Run multiple times against randomness;
4. Minimal context;
5. Objective / strict / skepticism-driven;
6. Judge layering, don't mix — **L1 (subdivided if skill under test is already segmented then flow/e2e) / L2 / L3a / L3b each handle their own scope**, don't score the same observation across two layers.

## L3 Aesthetic Honesty Baseline

The agent **has no reliable aesthetic judgment**. L3 breakdown:
- **L3a Objective comparison** (does it resemble the reference?) → agent can judge with evidence.
- **L3b Pure subjective aesthetic** (does it look good?) → art-exam-style rubric (dimensions + 1-5 scoring anchors) + multi-agent voting with variance + human calibration points; **dimensions with high variance / deviating from calibration → flag "requires human judgment"**.
- **Agent MUST NOT use anchorless judgments like "I think it looks good" as conclusions.**

## Self-Consistency

This skill is itself a standard → **must not double-standard**: it requires the tested skill to "record deviations / layer judges", so its own methodology doc must comply too. Use [[reviewing-skills]]'s "methodology/standard-type skill self-consistency" specialized re-audit for this skill.

## References

- `references/methodology.md` — Three-layer details (L2 mock single-state testing method / L3 honest-layering rubric template) + general rules
- `examples/video-remix.md` — First worked example (video-remix three-layer testing system)

## CHANGELOG

- **v0.1** (2026-05-29): Extracted from video-remix feedback-loop testing system. Paired with reviewing-skills to form "static structure audit + dynamic output testing".
