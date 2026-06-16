# Terms

This file defines the shared vocabulary for the cluster. Each term has two parts:

- `What it is`
- `How to use it`

## Reading terms

### Gradual reading

What it is: read from broad structure to narrow detail.
How to use it: start with directory layout, then README, then templates, then examples, then tables and code slices.

### Full reading

What it is: read the relevant corpus completely when the task demands it.
How to use it: do not replace full reading with keyword search unless the user explicitly narrows the task.

### Problem-driven reading

What it is: reading as question discovery, not summary writing.
How to use it: every new concept, field, or structural difference should generate a question.

### Explicit thinking

What it is: each reading slice must produce visible analysis.
How to use it: state what was read, what it means, what it raises, and what should be read next.

### Reading progress

What it is: track how much of each file has been read.
How to use it: keep file, range, status, and next step in the output.

### Reading state table

What it is: a structured progress ledger.
How to use it: mark files as `pending`, `partial`, `read`, `reviewed`, or `skipped`.

### No backtracking budget

What it is: each region has a limited reread budget.
How to use it: after the budget is spent, rely on recorded evidence unless the user explicitly asks for another pass.

### Restatement

What it is: reconstruct understanding in your own words.
How to use it: after each meaningful batch, say what the source says, what it does not say, what is inferred, and what remains uncertain.

### Live notes

What it is: raw reading-time thinking.
How to use it: preserve the original thought first; do not force it into final conclusions immediately.

## Question terms

### Trigger point

What it is: the source that caused the question.
How to use it: record the file, field, line, example, or observation that created the question.

### Question state

What it is: current resolution level.
How to use it: use `unresolved`, `partial`, `resolved`, or `deferred`.

### Current known

What it is: the bounded set of facts already supported by the corpus.
How to use it: answer only from what is already present in the notes and evidence.

### Relation table

What it is: a compact map of how concepts connect.
How to use it: record dependency, reference, source, and scope.

### Concept boundary

What it is: what a concept can and cannot explain.
How to use it: attach explicit limits to every important concept.

## Evidence terms

### First fact

What it is: the most direct source class.
How to use it: prefer official templates, official examples, library/source files, and runtime observations.

### Evidence level

What it is: a way to rank evidence sources.
How to use it: label evidence as first fact, 1.5 fact, second fact, or external reference.

### Evidence matrix

What it is: a table that binds claims to evidence.
How to use it: include evidence, source, support, limits, and what cannot be proved.

### Negative evidence

What it is: missing docs, absent fields, unused examples, or unsupported lifecycle claims.
How to use it: record it explicitly; it lowers confidence but does not prove absence.

### Soft hypothesis

What it is: a candidate explanation that is not yet confirmed.
How to use it: use it for names, folders, headers, and partial examples.

### Competing hypotheses

What it is: multiple plausible explanations kept alive at once.
How to use it: keep them when the mechanism is not yet separated by evidence.

### Minimum confirmable conclusion

What it is: the smallest safe statement the evidence supports.
How to use it: do not expand the claim beyond what the evidence can carry.

### Transfer boundary

What it is: where a conclusion can and cannot be generalized.
How to use it: state whether the claim is only an example, a template rule, or a reusable pattern.

## Execution terms

### User clues

What it is: the user-provided files, guesses, symptoms, constraints, and prior answers.
How to use it: route them into hypotheses or research paths; never treat them as background noise.

### Subagent deep research

What it is: bounded, evidence-heavy delegated research.
How to use it: give the subagent a path, question, search directions, output format, and constraints.

### Task sheet

What it is: the exact contract for a subagent.
How to use it: include ownership, search scope, questions, and required evidence shape.

### Async research

What it is: parallel research while the main thread keeps synthesizing.
How to use it: delegate only separable uncertainties.

### Experience data

What it is: debugging or reading outcomes that are useful but not yet permanent truth.
How to use it: keep failures, fixes, and verification; do not over-explain unstable conclusions.

### Problem clustering

What it is: grouping related problems for review.
How to use it: cluster by target relevance, root cause, or repeated symptom.

### No intermediate attempt log

What it is: do not preserve noisy chronology by default.
How to use it: keep the final useful fix and the problem clusters, not every false start.

### Downstream interface

What it is: what each consumer gets from the workflow.
How to use it: deliver different outputs to API, case guide, builder, and user.

### Skill distillation

What it is: turning records and questions into reusable rules.
How to use it: extract behavior, not prose; do not copy the original records into the skill.

### Structured audit corpus

What it is: source slices tagged as `fact`, `inference`, `hypothesis`, or `noise`.
How to use it: keep the layers separate so later analysis can stay controlled.

