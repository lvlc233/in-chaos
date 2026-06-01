# reviewing-in-chaos 问题追踪

> 状态: 持续收敛中。每项缺陷必须有 `file:line` 证据 (Iron Law #2 自举)。

## 已修复 ✅

- [x] **🔴 C1** 分类计数不一致 — `SKILL.md:27` 补充第 4 类"重构后复审型"，与 `rubric.md:11` 一致。证据: `events/C1-I1-M1-M2-multi.md`
- [x] **🔴 C2** 缺少 hard/soft 分层 — `SKILL.md:46-59` 新增 Iron Law (3 条) + Red Flags 表 (4 条)。证据: `events/C2-ironlaw.md`
- [x] **🟠 I1** description 混了 what — `SKILL.md:3` 精简为纯 when 触发语。证据: `events/C1-I1-M1-M2-multi.md`
- [x] **🟠 I2** 缺集中式 Red Flags — 被 C2 覆盖。证据: `events/C2-ironlaw.md`
- [x] **🟠 I3** 缺"下游消费指引" — `SKILL.md:62-63` 已添加"如何消费审阅报告"节。证据: `events/I3-I4-I5-M3-docs.md`
- [x] **🟠 I5** CHANGELOG v0.3 措辞 — `CHANGELOG.md:33` 经 C1 修复后双向落定。证据: `events/I3-I4-I5-M3-docs.md`
- [x] **🟡 M1** DRAFT 状态标签 — `SKILL.md:8` 改为"演进中 (当前版本以 CHANGELOG.md 为准)"。证据: `events/C1-I1-M1-M2-multi.md`
- [x] **🟡 M2** 8 维摘要潜在漂移 — `SKILL.md:39` 改为一句话引用 `references/rubric.md`。证据: `events/C1-I1-M1-M2-multi.md`
- [x] **🟡 M3** 示例表格式不一致 — `SKILL.md:37` 保留差异，短链路轻量表 vs 长链路全表。证据: `events/I3-I4-I5-M3-docs.md`
- [x] **🟡 自归类声明** — `SKILL.md:24` 审视流程段前已加 "本 skill 自身归类: 纯指导型" + D3/D8 坦诚声明。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **🟡 Red Flags 未饱和** — `SKILL.md:54-63` Red Flags 已从 4 条扩充到 6 条。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **🟡 Iron Law #3 边缘** — `SKILL.md:52` 已加例外子句 (长链路+有脚本时 D8 🔴 不降级)。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **🟡 范例结构漂移** — `SKILL.md:37` 输出模板已加注短链路合法变体说明。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **⚪ 与 iteration-in-chaos 双向引用** — `SKILL.md:67` 下游消费段已 cross-ref iteration-in-chaos。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **🟡 Rigid/Flexible 标签缺失** — `SKILL.md:48,54` 已加 `(Rigid)`/`(Flexible)` 标签。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **⚪ iteration-in-chaos 未回链** — `iteration-in-chaos/SKILL.md:6` 已 cross-ref reviewing-in-chaos。证据: CHANGELOG v0.7 `2026-06-01`
- [x] **⚪ CHANGELOG line 不准** — `CHANGELOG.md:10-14` 5 处行号已校核。证据: CHANGELOG v0.7 `2026-06-01`

## 待修复

当前为零——全部已修复 ✅

## 已知 backlog (不阻塞)

- [ ] `CHANGELOG.md:53` — 补第三个 worked example (重构后复审型 + 方法论/标准型)
- [ ] `CHANGELOG.md:54` — 补纯正面范例
- [ ] `CHANGELOG.md:55` — 维度 8 跨平台清单扩充
