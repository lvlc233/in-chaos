# preference-in-chaos Design Spec

**Date:** 2026-06-01
**Status:** approved

## Overview

A lightweight skill in the in-chaos package for recording personal preferences across all dimensions of life. Personal data is stored in a separate git repo (`git@github.com:lvlc233/resource-package.git`) linked as a git submodule.

## Requirements

- Full-dimensional preference recording (tech, work, life, aesthetics, etc.)
- User-initiated recording via explicit commands ("记一下偏好: xxx")
- Free-form markdown format, organized by dimension folders
- Data in external repo via git submodule
- Independent from iteration-in-chaos (no shared state)

## Architecture

### File Structure

```
preference-in-chaos/
  SKILL.md                  # Entry: triggers + routing + write template
  resource-package/         # git submodule → personal data repo
    tech/
      index.md
      *.md
    work/
      index.md
      *.md
    life/
      index.md
      *.md
    aesthetics/
      index.md
      *.md
  references/               # Optional: format documentation
```

### SKILL.md Content

| Section | Content |
|---|---|
| Trigger | Keywords: 记一下偏好, 我的偏好, 我习惯, 我倾向于, 偏好, preference |
| Routing | Agent classifies preference text into a dimension; asks user if uncertain |
| Write template | Simple markdown template with dimension + preference + scene + timestamp |
| Dimension index | Current dimension directories and their scope |
| Quick commands | 记一下偏好, 看看偏好, 改偏好 |

### Initial Dimensions

| Dimension | Directory | Scope |
|---|---|---|
| tech | `tech/` | Code style, tools, naming, architecture |
| work | `work/` | Meeting rhythm, documentation, scheduling |
| life | `life/` | Routine, eating, shopping, habits |
| aesthetics | `aesthetics/` | Colors, layout, style preferences |

### Write Flow

1. User says "记一下: I prefer X over Y"
2. Agent identifies dimension → `{dimension}/`
3. Agent creates `resource-package/{dimension}/{slug}.md` with frontmatter
4. Agent appends entry to `resource-package/{dimension}/index.md`
5. Agent confirms "已记到 {dimension}/ 下"

### Read Flow

| User says | Agent action |
|---|---|
| 我有什么偏好 / 看看偏好 | Scan all index.md, show overview |
| 看看{维度}偏好 | Read {dimension}/index.md |
| 我关于X的偏好是什么 | grep all dimensions for keyword |

### Preference Record Template

```markdown
# {slug}

- **维度**: {dimension}
- **偏好**: {raw user preference text}
- **场景**: {context in which this was triggered}
- **记录时间**: {timestamp}
```

## Design Decisions

1. **No state machine** — Unlike iteration-in-chaos, preferences don't need lifecycle (draft/active/deprecated). Simplicity wins for now.
2. **Free-form markdown** — No enforced schema; user's raw words are the primary data.
3. **Index files as directory** — Each dimension has an `index.md` acting as a table of contents; grep is the search mechanism.
4. **No auto-detection** — Recording is always user-initiated. Agent may detect patterns but won't act without user confirmation.

## Future Considerations

- Pattern detection + proactive suggestion
- Preference lifecycle (active → outdated)
- Conflict detection between preferences
- Preference evolution tracking
