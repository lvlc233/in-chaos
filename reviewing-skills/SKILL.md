---
name: reviewing-skills
description: Use when auditing or reviewing an EXISTING skill's architecture for defects — 复审 / 审视一个已有 skill 的结构缺陷、诊断它为何在上下文压缩或跨会话下跑偏、对照公认好用的 skill 找差距。Triggers 审视 skill、这个 skill 哪里不好、skill 缺陷、复审 skill、skill 架构、review a skill、audit a skill、skill architecture review。NOT for writing a brand-new skill (use writing-skills / skill-creator instead).
---

# reviewing-skills

> 🚧 STATUS: 演进中 (DRAFT — 当前版本以 CHANGELOG.md 为准)
> 本 rubric 仍在迭代。每完成一次真实 skill 审视,把新学到的维度 / 坏味道回填进
> `references/rubric.md` 与 `CHANGELOG.md`。**迭代是旁路的,不阻塞当前主审视工作。**

## 核心原则

审一个 skill 的**架构**,不是抠它语法对不对,而是看它的**组织方式**能否让一个 LLM 在真实约束下
——**上下文会被压缩、会换 session、会被异步派发**——稳定地把活干对。

> 一个 skill 的健壮性,不应依赖它无法控制的运行时假设(例如"runtime 不会压缩上下文")。

## 何时用 / 不用

**用**:复审已有 skill;诊断 skill 为何在生产跑偏;对照标尺评估质量;为重构 skill 做准备。
**不用**:写新 skill(→ `writing-skills` / `skill-creator`);改业务代码。

## 审视流程

1. **读全** — 目标 skill 的 SKILL.md + 所有 references,逐行读(不看大概)。先量体量(`wc -l`)。
2. **先归类 + 逐维度过 rubric** — 先判断 skill 类型(长链路有状态 / 短链路工具 / 纯指导),再对照 `references/rubric.md` 的 8 维逐条记录。
3. **标缺陷 + 证据** — 每个缺陷给 `file:line` + 对照标尺(它本该长什么样)。
4. **排严重度** — 🔴架构级 / 🟠结构级 / 🟡健壮性 / ⚪轻微。
5. **找根因** — 多数缺陷常是同一病灶的并发症,升华成一句话。
6. **给改进方向** — 每缺陷一条可执行方向。
7. **肯定优点** — 列它做对的地方,避免一边倒(诊断才可信)。
8. **(旁路)回填** — 若学到 rubric 没有的新维度 / 坏味道,更新 rubric + CHANGELOG。不阻塞主流程。

输出形态参考 `examples/video-remix.md`(根因 → 体量澄清 → 缺陷表 → 优点 → 根因升华 → 改进方向)。

## 8 维 checklist(详见 references/rubric.md)

1. **体量与注意力预算** — SKILL.md 多大?哪些必须在场 vs 按需读?(自写 vs vendor 分开数)
2. **单一职责 vs 大杂烩** — 负责几件事?有没有"不做什么"边界声明?
3. **状态如何跨上下文压缩 / 跨步骤传递** — 靠落盘(健壮)还是靠记忆(脆弱)?⭐长链路有状态型最致命
4. **控制流是否显式** — 决策骨架(flowchart)与执行细节分离了吗?(双向:塞太多 / 该有却全散文)
5. **强制力分层 + 防幻觉集中** — hard rule vs soft 分清?防幻觉是集中红旗区还是散落?
6. **可组合性与下游感知** — cross-reference 还是拷贝?同仓有现成 skill 没复用?喂下游告知机制了吗?
7. **Description = 触发条件** — 只写 when,没混 what / 能力清单 / 流程?
8. **执行层正确性 / 失败模式** — (工具型尤其)命令语义对吗?跨平台?silent-fail?⭐工具型最致命

> **先给 skill 归类**,决定主战场:**长链路有状态型** → 维度 3 试金"第 K 步压缩了前面还在吗?";
> **短链路工具型** → 维度 8 试金"招牌功能的核心命令语义真的对吗?"(短链路别硬给维度 3 扣 🔴)。

## 标尺锚点(活参考)

- **superpowers / writing-skills** — 好 skill 评分卡:Iron Law、Red Flags 表、Rigid/Flexible 标注、
  progressive disclosure、CSO(description 只写触发条件)。
- **video-use** — 长流程范式:**永不信任记忆,一切落盘**(project.md / edl.json / takes_packed.md,启动先读)、
  `ask→confirm→execute→iterate→persist`、hard rules vs artistic freedom、self-eval 集中封顶(Cap at 3)。

## 姊妹 skill

- **`evaluating-skill-output`** — 本 skill 静态审"**写得**合不合理";审完结构、要**动态测产出**(行为正确性 / 状态流中间质量 / 内容审美质量)就转它。两者配对成「审 + 测」,缺一不全。

## References

- `references/rubric.md` — 8 维详细(检查问题 / 好的样子 / 坏味道 / 严重度)
- `examples/video-remix.md` — 第一个 worked example(单体版审视)
- `CHANGELOG.md` — 迭代日志
