---
name: reviewing-in-chaos
description: Use when auditing or reviewing an EXISTING skill's architecture for defects. Triggers: 审视 skill、这个 skill 哪里不好、skill 缺陷、复审 skill、skill 架构、review a skill、audit a skill、skill architecture review. NOT for writing a brand-new skill (use writing-skills / skill-creator instead).
---

# reviewing-in-chaos

> STATUS: 演进中 (当前版本以 CHANGELOG.md 为准)
> 本 rubric 仍在迭代。每完成一次真实 skill 审视,把新学到的维度 / 坏味道回填进
> `references/rubric.md` 与 `CHANGELOG.md`。**迭代是旁路的,不阻塞当前主审视工作。**

## 核心原则

审一个 skill 的**架构**,不是抠它语法对不对,而是看它的**组织方式**能否让一个 LLM 在真实约束下
——**上下文会被压缩、会换 session、会被异步派发**——稳定地把活干对。

> 一个 skill 的健壮性,不应依赖它无法控制的运行时假设(例如"runtime 不会压缩上下文")。

## 何时用 / 不用

**用**:复审已有 skill;诊断 skill 为何在生产跑偏;对照标尺评估质量;为重构 skill 做准备。
**不用**:写新 skill(→ `writing-skills` / `skill-creator`);改业务代码。

> **本 skill 自身归类: 纯指导型。** 无脚本/命令，D8 对其为 N/A。8 步流程是方法论指引，中间产物依赖上下文窗口——因此 D3 落盘要求对自身不适用（坦诚声明，非双标逃避）。

## 审视流程

1. **读全** — 目标 skill 的 SKILL.md + 所有 references,逐行读(不看大概)。先量体量(`wc -l`)。
2. **先归类 + 逐维度过 rubric** — 先判断 skill 类型（长链路有状态 / 短链路工具 / 纯指导 / 重构后复审型），再对照 `references/rubric.md` 的 8 维逐条记录。
3. **标缺陷 + 证据** — 每个缺陷给 `file:line` + 对照标尺(它本该长什么样)。
4. **排严重度** — 🔴架构级 / 🟠结构级 / 🟡健壮性 / ⚪轻微。
5. **找根因** — 多数缺陷常是同一病灶的并发症,升华成一句话。
6. **给改进方向** — 每缺陷一条可执行方向。
7. **肯定优点** — 列它做对的地方,避免一边倒(诊断才可信)。
8. **(旁路)回填** — 若学到 rubric 没有的新维度 / 坏味道,更新 rubric + CHANGELOG。不阻塞主流程。

输出形态参考 `examples/video-remix.md`(根因 → 体量澄清 → 缺陷表 → 优点 → 根因升华 → 改进方向)。短链路工具型可省略"根因升华"独立段、保留"归类"段在前，两个范例的差异是 skill 类型不同导致的合法变体，非格式缺陷。

## 8 维 checklist

详见 `references/rubric.md`（每维含检查问题 / 好的样子 / 坏味道 / 严重度）。此处只列维度名供快速扫读：

1. 体量与注意力预算 | 2. 单一职责 vs 大杂烩 | 3. 状态跨上下文压缩传递 | 4. 控制流是否显式 | 5. 强制力分层 + 防幻觉 | 6. 可组合性与下游感知 | 7. Description = 触发条件 | 8. 执行层正确性 / 失败模式

> **先给 skill 归类**,决定主战场:**长链路有状态型** → 维度 3 试金"第 K 步压缩了前面还在吗?";
> **短链路工具型** → 维度 8 试金"招牌功能的核心命令语义真的对吗?"(短链路别硬给维度 3 扣 🔴)。

## Iron Law (Rigid — 不可跳过)

1. **必须读完所有 references 再下判断。** 只读 SKILL.md 不读 rubric → 审不完整。
2. **每个缺陷必须给出 `file:line` 证据。** 没证据的"感觉不好"不是有效反馈。
3. **先归类再定严重度。** 长链路型打维度 8 的 🔴 或工具型打维度 3 的 🔴，一律降级。**例外**: 若长链路型 skill 同时具备工具特征 (含脚本/命令)，D8 的 🔴 不降级——因为功能地基有洞优先于架构归类。

## Red Flags (Flexible — 审阅者自欺信号)

| 你在想 | 现实 |
|--------|------|
| "这个 skill 很短，扫一眼就行" | 短不等于没问题。必须逐行读。 |
| "这个问题在维度 X 和维度 Y 都提过了，不重复了" | 同一问题在不同维度视角下不同。各维独立记录。 |
| "这个问题太小，不配写进 review" | 小问题是大问题的症状。照记不误。 |
| "这个 skill 我审过类似的，可以套上次结论" | 每个 skill 有独立上下文。复用判断，不复用结论。 |
| "核心问题我理解了，不用逐维过了" | 代替系统性检查等于放弃方法论。各维独立记录是 Iron Law 的前置约束。 |
| "这是 workflow 级的问题，rubric 管不了" | 用 scope 理由跳维，是"太小不配写"的变体但更隐蔽。先记录，再由严重度决定。 |

## 如何消费审阅报告

审阅报告按严重度优先级消费：🔴架构级 → 立即修，阻塞合并；🟠结构级 → 本次迭代内修；🟡健壮性 → 下个迭代修；⚪轻微 → P3 backlog。**根因升华是报告的核心价值**——多数缺陷是同一病灶的并发症，看懂根因比逐一修缺陷更高效。审阅报告可作为 `iteration-in-chaos` 迭代引擎的输入源（反馈 → 暴露盲区 → 更新技术 → 闭环），生态内 skill 相互驱动。

## 标尺锚点(活参考)

- **superpowers / writing-skills** — 好 skill 评分卡:Iron Law、Red Flags 表、Rigid/Flexible 标注、
  progressive disclosure、CSO(description 只写触发条件)。
- **video-use** — 长流程范式:**永不信任记忆,一切落盘**(project.md / edl.json / takes_packed.md,启动先读)、
  `ask→confirm→execute→iterate→persist`、hard rules vs artistic freedom、self-eval 集中封顶(Cap at 3)。

## References

- `references/rubric.md` — 8 维详细(检查问题 / 好的样子 / 坏味道 / 严重度)
- `examples/video-remix.md` — 第一个 worked example(单体版审视)
- `CHANGELOG.md` — 迭代日志
