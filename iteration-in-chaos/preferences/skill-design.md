# skill-design
## 管线
1. [state-machine-check](../techs/state-machine-check.md) → 2. [responsibility-boundary-check](../techs/responsibility-boundary-check.md)
## 理由
先检查结构是否状态驱动（执行效率），再检查职责边界是否清晰（协作效率）。状态机解决"agent 怎么快速定位动作"，边界检查解决"这个 skill 该不该做这件事"。两者互补：状态机管内部组织，边界管对外接口。
## 适用上下文
编写或迭代 skill 时
## 证据
- log/2026-05-29-state-driven-execution.md §1
- log/2026-05-29-identity-is-iteration-schemes.md §2
## 生效记录
| 日期 | 项目 | 管线走了吗 | 结果 | 调整 |
|------|------|-----------|------|------|
| 2026-05-29 | iteration-engine | 通过 | state-machine-check 通过（线性→状态表），responsibility-boundary-check 通过（明确职责边界） | - |
| 2026-05-29 | iteration-engine | 通过 | 第二轮：state-machine-check 通过（增加 transitions + 多状态并发），responsibility-boundary-check 通过（增加协作协议） | - |
