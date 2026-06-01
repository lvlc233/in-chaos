# 维度偏好索引

## 维度定义表

| dimension | 定义 | 匹配关键词 | 排除场景 |
|-----------|------|-----------|----------|
| skill-design | skill/SKILL.md 的结构设计、状态机、规则分层 | skill, SKILL.md, 状态机, 规则, 结构 | 外部审核方法论 (→ review-methodology) |
| review-methodology | 审核/评测方法论的迭代改进 | 审核, 评测, rubric, 方法论, 盲区 | skill 结构设计 (→ skill-design) |

> 匹配规则：agent 根据当前迭代对象的产出物类型和用户意图，用关键词匹配选择维度。匹配失败时回退到语义推断并询问用户。

## 管线索引

| dimension | 管线 | 适用上下文 |
|-----------|------|-----------|
| skill-design | state-machine-check → responsibility-boundary-check | 编写或迭代 skill 时 |
| review-methodology | structure-audit → blind-spot-driven-design | 外部审核暴露技术盲区时 |
