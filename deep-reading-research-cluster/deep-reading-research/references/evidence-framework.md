# Evidence Framework

This module answers: how do we judge claims?

## Evidence Order

Prefer evidence in this order:

1. Complete context
2. Official or primary explicit rule
3. Complete example
4. Header or field name
5. Folder or file name
6. Keyword hit

## Claim Types

- `fact`: directly supported
- `inference`: derived from facts
- `hypothesis`: candidate explanation
- `noise`: not useful for the current claim

## Conclusion Levels

- `confirmed`
- `partially confirmed`
- `unconfirmed`
- `disproved`

## Evidence Matrix

Always record:

- claim or hypothesis
- evidence
- source class
- what it supports
- what it limits
- what it cannot prove

## Negative Evidence

Negative evidence is required when it changes confidence.

Examples:

- missing documentation
- absent field
- unused example
- unsupported lifecycle claim

Negative evidence does not prove absence. It only narrows the claim.

## Soft Hypothesis

Use a soft hypothesis when:

- a name looks meaningful
- a folder suggests a role
- a table header implies a field relation
- an example looks representative but is not yet sufficient

## Competing Hypotheses

Keep multiple explanations alive when the mechanism is not yet separated.

## Minimum Confirmable Conclusion

Every deep research pass should finish with the smallest statement the evidence can safely carry.

## Transfer Boundary

For every important conclusion, state whether it is:

- a single example
- a template rule
- a reusable pattern
- a version-limited observation

