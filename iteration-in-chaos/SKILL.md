# Iteration Engine

Transform user feedback into a reusable iteration technique system.

**Core output:** `techs/` — reusable iteration protocols (inspection methods, design patterns, execution flows).  
**Input mechanism:** Detect patterns from user feedback → log → surface crystallized entries in `techs/`.  
**Orchestration layer:** `preferences/` — user-selected technique pipelines across dimensions (which technique per dimension, in what order).  
**Responsibility boundary:** Provide and manage iteration protocols. Problem detection (auditing) and quality verification (evaluation) are handled by other skills. Collaboration: auditing skill flags issues → iteration-engine matches corresponding iteration techniques to fix them.

## State Machine

Identify current state, execute corresponding actions, then follow the transition to the next state. Any state is a valid entry point. **When multiple states trigger simultaneously, execute in top-to-bottom priority order as listed in this table.**

| State | Trigger Condition | Action | → Next State |
|-------|-------------------|--------|--------------|
| **new-task** | Starting a new dev/iteration task | ①Identify the dimensions involved in current artifacts ②Scan `preferences/index.md` to match pipelines per dimension ③Load pipeline, prepare execution ④Check for pending logs ready for crystallization **⑤If the iteration target is iteration-engine itself, additionally load its own techs/ for dogfooding checks (use itself to iterate itself)** | → applying-tech (execute first technique in pipeline) |
| **feedback-received** | User gives correction/principle/direction | Detect whether a principle signal fires (principle statement / 3+ similar corrections / citing external standard / overriding the approach / emphasizing overall direction). Fires → write `log/{date}-{keyword}.md`, `extracted_principles` required. Doesn't fire (one-off naming / one-time fix / chat-style) → don't log | → new-task (feedback means change, apply change then continue pipeline) |
| **accumulated** | User says "organize feedback" / ≥2 logs in same direction / new-task step④ detects pending logs | Scan `log/`, identify same-direction logs → propose crystallization plan: crystallize as tech or preference? → wait for user confirmation | → crystallizing (confirmed) / → end (rejected) |
| **crystallizing** | User confirms crystallization proposal / proactively says "write it down" | tech: create `techs/{name}.md`, status: draft, fill in boundary/test cases/effect comparison. preference: create `preferences/{dimension}.md`, pipeline pointing to techs, evidence back to logs. Update log `crystallized_to`. **Immediately apply newly crystallized items to current iteration target** | → new-task (reload pipeline, new techniques enter verification loop) |
| **applying-tech** | Executing a technique within the pipeline | Execute technique workflow → check against acceptance criteria → record effectiveness result | → tech-failed (fails acceptance) / → applying-tech (continue next technique) / → new-task (pipeline complete, return to step④ to check pending logs) |
| **tech-failed** | Technique didn't pass acceptance | Analyze root cause: technique itself insufficient → update acceptance criteria / blind spots; pipeline orchestration issue → adjust preference pipeline, move old version to `archive/`. **Failure records are more valuable than success** | → applying-tech (retry same technique after fix) |
| **revalidate-preference** | User asks "is this preference still valid?" | Check effectiveness records: consistently passing → confirm valid; pattern failures → propose adjustment or archiving | → accumulated (invalid, needs replacement) / → end (valid, no change needed) |

## Core Rules

1. **Techniques must pass the verification gate before entering a pipeline.** draft → real-world testing → active/rejected (see `references/tech-template.md`). User intuition is a trigger signal, not an exemption.
2. **Preferences must point back to log evidence.** A preference without evidence is invalid.
3. **The state machine is an editing filter.** The act of placing content into the state table itself reveals what has execution value vs. what is merely reference material. Content that can't fit into the state table → goes into `references/`.
4. **Use yourself on yourself (dogfooding).** Use iteration-engine's own workflow to iterate itself. If its own workflow fails in its own context → the workflow needs adjustment.

## Quick Routing

| User says | Target state | Notes |
|-----------|-------------|-------|
| Day-to-day correction/guidance | → feedback-received | Apply improvements via new-task immediately after correction |
| "Organize recent feedback" | → accumulated | |
| Start new task / "Iterate on X" | → new-task | Load pipeline first, then check pending logs |
| "Is this preference still valid?" | → revalidate-preference | |
| "Write this down" (proactive request) | → crystallizing | Skip surfacing threshold and confirmation |
| External technique/skill found usable method | → import into `techs/`, mark `status: pending-review`, await user review | |

## External Technique Import

1. Place into `techs/`, mark `status: pending-review` and source
2. Fill in blind spots — "what can this method NOT audit?"
3. Only mark `status: active` after user review and approval, then allow entry into preference pipelines

## Red Flags

| Excuse | Reality |
|--------|---------|
| "I'll keep it in my head" | If it's not written, it doesn't exist. Next session the agent knows nothing |
| "Just log the event, don't extract principles" | `extracted_principles` is the only value of a log entry |
| "Tech files and preferences are pretty similar, merge them" | Technique = reusable method (user-independent), Preference = user's orchestration choice. Different lifecycles |
| "User-suggested techniques go straight into preferences" | Store technique independently in `techs/` first, pass verification gate before wiring into pipeline |
| "This is too simple to extract a principle" | Simple principles have the highest reuse value |
| "Wait until we have more to write together" | Write on every trigger. Accumulation is for the surfacing stage |
| "Effectiveness records aren't important" | The run that failed is more valuable than the one that passed — reveals blind spots |

## File Structure

```
iteration-engine/
  SKILL.md              ← state machine + transitions + core rules + quick routing
  techs/                ← reusable iteration protocols
    index.md
    *.md
  preferences/          ← user's technique pipeline orchestration
    index.md
    *.md
  log/                  ← feedback events + extracted principles
    *.md
  archive/              ← superseded old preferences / deprecated techniques
  references/           ← detailed templates and format specifications
    log-template.md
    tech-template.md
    preference-template.md
```
