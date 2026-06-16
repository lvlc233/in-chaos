# Question Ledger

This module answers: how do we turn reading into a stable question system?

## Ledger Shape

Each question should carry:

- `questionId`
- `text`
- `status`
- `answerSnapshot`
- `triggerPoint`
- `evidenceRecordIds`
- `theme`

## Status Model

- `unresolved`
- `partial`
- `resolved`
- `deferred`

## Trigger Point Rules

- A question must be tied to the file, field, line, example, or observation that raised it.
- If the trigger point is weak, keep the question in a waiting bucket rather than promoting it too early.

## Relation Table

Use a relation table when the question is really about how concepts connect.

```text
| Concept A | Relation | Concept B | Evidence | Notes |
|---|---|---|---|---|
```

## Concept Boundary

For any important concept, record:

- what it explains
- what it does not explain
- what evidence is still missing

## Answer Snapshot

- Store the current known answer as a snapshot.
- Keep it overwritable.
- The point is to preserve how understanding changed over time.

## Upgrade Rule

- `partial` can become `resolved` only when evidence is concrete enough to support the stronger claim.
- Do not promote a question simply because the wording sounds plausible.

