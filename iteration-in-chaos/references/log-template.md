# Log 文件格式

文件名：`log/{YYYY-MM-DD}-{关键词}.md`

```markdown
## trigger: [怎么触发]
## context: [做什么事时触发的]
## method: [对话/code review/git commit/...]
## what_changed: [改了什么]

## extracted_principles:
### 1. [原则名]
  证据: [用户原话]
  原则: [一般性规则，不限于当前上下文]
### 2. ...
## tags: [...]
## crystallized_to: pending
```
crystallized_to 格式：
- pending — 尚未结晶
- 已结晶（单条）: `techs/state-machine-check.md` 或 `preferences/skill-design.md`
- 已结晶（多条）: 
  ```
  crystallized_to:
  - techs/state-machine-check.md
  - SKILL.md 规则3
  ```
```

`extracted_principles` 不能为空——只记事件不提取原则的日志没有复用价值。
