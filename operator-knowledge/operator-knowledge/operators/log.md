# 推导日志

## [2026-05-08] 知识库创建
- 以"知识是作用量"理念初始化
- 区分于 Karpathy LLM Wiki：LLM 编译 vs 自己内化
- 核心承诺：谁整理谁使用，运算即激活

## [2026-05-09] 术语统一 + 概念 Apply 验证
- "算子" → "知识单元"，术语去个人化
- 通过 Apply 验证"模型有效输出偏离"：日记 → 概念锚定 → 边界条件厘清
- 明确 skill 包三层架构：核心 skill（知识推导）、操作 skill（文档归档检索）、中间 skill（Distill 对照阅读）

## [2026-05-09] 三层 skill 架构拆分 + superpowers 审计
- 从单文件拆为 derive / capture / distill 三个 SKILL.md
- derive: 保留 Derive/Apply/Evolve 全流程，恢复 Decision Flow 流程图
- capture: 投递/检索/清理 + 元数据规范 + 软删除，补 Red Flags + 反驳表 + 异常处理
- distill: 对照阅读/筛选候选 + 输出模板，补 Common Mistakes + Red Flags + 反驳表
- 压力测试通过: derive 停在检查点 ✓, capture 写 raw 正确 ✓, distill 对照报告格式 ✓
- CSO 修复：description 改为纯触发条件 ("Use when...")，删除流程摘要
- 新增：合理化反驳表，覆盖 7 种常见绕过借口
- 压力测试：
  - RED：不带 skill 的 agent 直接给出完整 Attention Mechanism 推导 ✓
  - GREEN：带 skill 的 agent 停在检查点 1，仅追问用户当前理解 ✓
  - 绕过测试：agent 用降级方案（TODO 模板），未给完整答案 ✓

## [2026-05-09] writing-skills 审阅迭代
- 对照 writing-skills checklist 做 RED-GREEN-REFACTOR 审阅
- capture: 加 `## When to Use` 显式章节、检查点编号对齐工作流 4 步、YAML description `>` → `|`
- distill: "触发时机"移入 When to Use 附近、加 Decision Flow 决策链、"从 capture 获取"改为直接读 raw/
- derive: 拆出独立 `## When NOT to Use` 章节、重写 Decision Flow（从 4 行扩展为 6 行，覆盖全路径）、删除"为什么起效"叙事段落
- 新建顶层 `SKILL.md` 做三 skill 统一入口（快速路由表 + 数据流图）
- 交叉引用路径验证通过
