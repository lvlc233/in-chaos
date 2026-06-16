---
name: deep-reading-research
description: Coordinator for deep reading, evidence research, question ledgering, subagent research, and skill distillation. Use when the user wants to read a corpus deeply, turn scattered records into a controlled workflow, or build a skill from reading logs rather than a summary.
---

# Deep Reading Research

This is the cluster coordinator, not the only worker.

Use it when the task is bigger than a single pass of reading or a keyword search. It routes work into narrower subskills so the main thread can preserve continuity while each subskill keeps a tight contract.

## What this cluster does

- `deep-reading-workflow` handles reading slices, progress tracking, restatement, and the "read then think" loop.
- `deep-question-ledger` handles questions, triggers, statuses, concept boundaries, and relation tracking.
- `deep-evidence-research` handles facts, evidence grading, hypotheses, negative evidence, and conclusion levels.
- `deep-subagent-research` handles bounded read-only research tasks for subagents.
- `deep-distillation` is optional and only used when the user explicitly asks for a reusable method, path, or task.

## Core Loop Between Artifacts

Treat the working artifacts as a closed system:

1. `reading table` produces `question table` entries.
2. `question table` chooses the next reading slice.
3. `evidence / notes` update question status and answer snapshots.
4. `reusable path / task` is produced only when the user asks to consolidate the session.
5. `distillation` is optional and never replaces the raw reading / question / evidence trail.

Hard rules:

- Do not invent an experience table as a default artifact.
- Do not let a question disappear just because a later distillation exists.
- Do not let the reading table stop at progress tracking; it must generate questions.
- Do not turn every deep session into a permanent method artifact.
- Do not close the loop unless the question state was updated from evidence or explicitly marked deferred.

If the user asks for failure-pattern review, structured audit, or terminology cleanup, use the relevant references under `references/` and apply the same shared vocabulary.

## Shared Vocabulary

Use these terms consistently across the cluster:

- `fact`
- `inference`
- `hypothesis`
- `noise`
- `trigger point`
- `current known`
- `partial`
- `resolved`
- `deferred`
- `evidence matrix`
- `negative evidence`
- `soft hypothesis`
- `competing hypotheses`
- `minimum confirmable conclusion`
- `transfer boundary`

The detailed definitions live in `references/terms.md`.

## Routing Rules

- If the user wants to understand how to read a corpus, route to `deep-reading-workflow`.
- If the user wants to know whether something is supported, route to `deep-evidence-research`.
- If the user wants to track or repair a question table, route to `deep-question-ledger`.
- If the user wants to offload a narrow uncertainty to a subagent, route to `deep-subagent-research`.
- If the user wants to turn records into a new skill or method, route to `deep-distillation`.

## Non-goals

- Do not turn field names into lifecycle explanations.
- Do not let keyword hits replace reading.
- Do not treat one example as a global rule.
- Do not hide uncertainty.
- Do not collapse `partial` into `resolved` without evidence.
- Do not force distillation when the user only asked for a deep session or research pass.

## Source Notes

This cluster is distilled from:

- `G:\work\project\game\mv_zmlt_mod\know\ok-v-mod\from-guanfan\from_github\workscope\jiaoxue-阅读记录.md`
- `G:\work\project\game\mv_zmlt_mod\know\ok-v-mod\from-guanfan\from_github\workscope\jiaoxue-问题表.md`
- The five subagent analyses of the reading-method corpus
- The installed Matt Pocock skills workflow used to separate planning, grilling, architecture, and synthesis
