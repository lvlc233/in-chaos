# iteration-in-chaos 问题修复 TODO

> 依赖关系: A → B 表示 A 完成后 B 的修改基础才成立。

## P0 — 状态机入口点声明修复 [C1] → 解锁后续所有状态机问题

- [ ] **C1-1** 去掉 `SKILL.md:12` "任何状态都是合法入口点" 声明
- [ ] **C1-2** 标注每个状态是 `入口级` 还是 `内部级`
- [ ] **C1-3** 给 3 个内部级状态 (applying-tech / tech-failed / crystallizing) 补一句"缺少前置状态上下文时，先回到 new-task 重载"

## P1 — 职责边界行消歧 [C2] ← 与状态机无关，独立修复

- [ ] **C2-1** 将 `SKILL.md:8` 的歧义行改为不倒读的明确表述

## P2 — tech rejection 路径 [C3] ← 依赖 P0 状态表结构稳定后新增

- [ ] **C3-1** 新增 `tech-rejected` 状态或扩展 `tech-failed` 支持结构性失败 → archive
- [ ] **C3-2** 同步更新 Quick Routing 加入 rejection 入口

## P3 — 结束态定义 [I4] ← 依赖 P0 状态表结构稳定

- [ ] **I4-1** 定义 "→ 结束" 的具体含义，统一为 → idle 或新增 idle 状态

## P4 — Quick Routing 补全 [I2] ← 依赖 P0/P2/P3 状态表变化

- [ ] **I2-1** 新增路由: "看一下当前管线" → 加载 preferences/index.md
- [ ] **I2-2** 新增路由: "有哪些反馈还没整理" → 扫 log/ crystallized_to: pending
- [ ] **I2-3** 新增路由: "评估 X 这个技术" → 加载对应 tech 文件

## P5 — action 粒度 [M2] ← 独立修复，不依赖其他

- [ ] **M2-1** 将 tech-failed action 拆为 ①分析根因 ②修改对应文件 ③重试

## P6 — applying-tech 进度追踪 [M3] ← 依赖 P0 状态表结构稳定

- [ ] **M3-1** applying-tech action 加入 pipeline index 追踪（如 "2/5"）

## P7 — crystallized_to 格式统一 [I3] ← 独立修复

- [ ] **I3-1** 在 log-template 里补充 resolved 阶段的格式示例

## P8 — preference-template 示例同步 [M1 + M4] ← 独立修复

- [ ] **M8-1** 将 template 示例 tech 名换为实际存在的 techs
- [ ] **M8-2** 将 template 示例管线换为实际管线
