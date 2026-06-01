# reviewing-in-chaos 问题修复 TODO

依赖关系: A → B 表示 B 的修复建立在 A 完成后。

## 根因 A: 自举一致性 — 对自己用自己审别人的标准时，自己没做到

- [ ] **C2** 缺少 hard/soft 分层 — SKILL.md 添加 Iron Law (2-3 条必执行规则) + Red Flags 表 (3-5 条审阅者常见自欺陷阱)

## 根因 B: 文档结构性缺口

- [ ] **C1** 分类计数不一致 — SKILL.md:27 补充第 4 类"重构后复审型"
- [ ] **I5** CHANGELOG v0.3 措辞修正 — "归类加'重构后复审型'"改为"(rubric 归类加...)"
- [ ] **I1** description 混了 what — 精简 description 为纯 when 触发语
- [ ] **I3** 缺"下游消费指引" — 添加一段简短说明：审阅报告按什么优先级消费
- [ ] **I2** 缺集中式 Red Flags — 已在 C2 的 Iron Law 区域解决

## 根因 C: 运营性债务

- [ ] **I4** v0.1 遗留 3 项未完成 — 标注为"已知待办"不阻塞
- [ ] **M1** DRAFT 状态标签 — 经 6 轮真实审视后，移除或改为 STABLE
- [ ] **M2** 8 维摘要潜在漂移 — 改为一句话引用 `references/rubric.md`
- [ ] **M3** 示例表格式不一致 — video-remix 和 git-sync 格式不同，标注说明即可
