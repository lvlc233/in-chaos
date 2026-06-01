# reviewing-in-chaos 修复总结

## 根因 A: 自举一致性

**SKILL.md** — 新增 Iron Law + Red Flags 节:
- Iron Law 3 条：必须读完 references、必须给 file:line 证据、先归类再定严重度
- Red Flags 表 4 条：审阅者常见自欺陷阱（"扫一眼就行""太小不配写""可以套上次结论"等）
- 新增"如何消费审阅报告"节：严重度优先级 + 根因升华是核心价值

## 根因 B: 文档结构性缺口

**SKILL.md:27** — 归类从 3 类扩展为 4 类（加"重构后复审型"），与 rubric.md 一致
**SKILL.md** description — 精简为纯 when 触发语，去掉"诊断它为何跑偏"等 what 描述
**SKILL.md:39-41** — 8 维 checklist 从每维一行详述改为纯维度名 + 引用 rubric.md，消除双副本漂移
**SKILL.md:8** — 去掉 🚧 DRAFT 标签，改为"演进中"

## 未修复 / 已知 backlog

- I4: v0.1 遗留 3 项（重构型 worked example / 正面范例 / D8 跨平台展开）→ 留待后续真实审视中自然回填
- M3: 示例表格式不一致 → 刻意保留（短链路用轻量表合理）

## 变更文件清单

- `SKILL.md` — description + classification + 8-dim inline summaries + DRAFT status + Iron Law + Red Flags + 消费指引
