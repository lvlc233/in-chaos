---
name: evaluating-in-chaos
description: Use when testing or evaluating what a skill produces when it runs. Triggers 测试 skill、评估 skill 产出、skill 跑得对吗、中间状态质量、内容质量、审美评分、给 skill 建测试、eval skill output、test skill behavior。NOT 写新 skill(那是 writing-skills / skill-creator)。
---

# evaluating-in-chaos

> 🚧 STATUS: 演进中(v0.6.2,自举一致性 13/13 ✅, checklist 行号引用全量更新)。

## 核心原则

测一个 skill 的**产物**(它跑起来做的事 + 做出来的东西),不审文档结构。三层: 行为正确性 (L1) + 状态流中间质量 (L2) + 内容/审美质量 (L3)。

> **文档审计 vs 产出测试**:审计答"这 skill **写得**合不合理"(静态);本 skill 答"它**跑得**对不对、做得好不好"(动态)。
> 现成框架(skill-creator)能测功能层(L1),但**系统性测不了状态流中间质量(L2)和内容/审美质量(L3)**——那是本 skill 补的盲区。

## 三层:测什么

| 层 | 测什么 | 裁判 |
|---|---|---|
| **L1 功能 / flow** | 行动计划对吗、字段/分支/契约对吗、早 fail 吗 | grader assertion(复用 skill-creator,**支持多跑取方差**) |
| **L2 状态流中间质量** | 每个状态的**中间产物**对吗(若 skill 是状态流) | grader 对照状态契约 assert 中间产物 + 记偏离。**mock 单状态测** |
| **L3 内容 / 审美质量** | 产物好不好、像不像目标参照 | L3a 对照参照物客观判;L3b 主观审美用 rubric + 投票 + 人类校准 |

> **先归类,不是每个 skill 都要三层**:纯无状态工具型可能只要 L1;长状态流 skill 要 L2;有内容/创意产出(视频/文案/设计)的才要 L3。
> 裁判列只标各层最特征的判法;**「记偏离 + 归因」是三层通用**(总则 #2),别只在 L2 记。

## 怎么用

1. **归类被测 skill**:有状态流吗?有内容/创意产出吗?→ 定要哪几层。
2. **每层先定标准**(先有标准后测):L1 = expected assertion;L2 = 状态契约;L3 = rubric 锚点。
3. **跑 + 记偏离**:按方法论总则(详见 `references/methodology.md`)。
4. **多次跑抗随机**(复用 skill-creator variance:mean/stddev)。

## 方法论总则(单一源头 = `references/methodology.md`)

六条横切三层。完整定义和细节均在 `references/methodology.md`(权威源)。此处仅列标题供快速索引：

1. 先有标准后测
2. 记偏离 + 归因
3. 多次跑抗随机
4. 最小上下文
5. 客观 / 严厉 / 怀疑驱动
6. 裁判分层别混用

## L3 审美的诚实底线

> 完整细节见 `references/methodology.md` §L3。

agent **没有可靠审美**。L3 分层:
- **L3a 客观对标**(像不像参照物)→ agent 能带证据判。
- **L3b 纯主观审美**(好不好看)→ 艺考式 rubric(维度 + 1-5 评分锚点)+ 多 agent 投票取方差 + 人类校准点;**方差大 / 偏离校准的维度标「需人类裁决」**。
- **禁止 agent 用"我觉得不错"这类无锚点判断当结论。**

## 自举一致性

本 skill 自己就是一套标准 → **必须无双标**:它要求被测"记偏离 / 裁判分层",自己的方法论文档也得遵守。

对照检查: 详见 `references/self-consistency-checklist.md`（13 项逐条验证）。**每次修改 methodology.md 总则或 L3 规则后，跑一遍该表**——不是"有空再查"，是改完即查。

## References

- `references/methodology.md` — 三层详细(L2 mock 单状态测法 / L3 诚实分层 rubric 模板)+ 总则
- `references/self-consistency-checklist.md` — 自举一致性 13 项对照表
- `examples/video-remix.md` — 第一个 worked example(video-remix 三层测试体系)

## CHANGELOG

- **v0.6.2**(2026-06-01):lazy-in-chaos Round 2 审计 → 2 项修复：description 去能力描述 (CSO)、自举 evals/ 特例显式声明 (methodology.md + checklist)。
- **v0.6.1**(2026-06-01):reviewing+iteration 二次验收暴露 checklist 行级证据过时 (#12 仍引 v0.3, #2/#3/#5/#6/#13 行号偏移) → 全量重跑：13 项行号引用更新至当前版本、#13 ⚠️→✅、#12 证据从 v0.3 更新为 v0.6、补 events/v0.6...md、structure-audit 盲区扩展 (配对契约)。
- **v0.6**(2026-06-01):reviewing-in-chaos 外部审计发现 7 项抛光层缺陷 → 7 项修复：methodology.md 总则 hard/best-practice 分层、L3 段补 methodology.md 指针、References 补 checklist、Limitations 加 reviewing-in-chaos 配对回链、video-remix example 统一 "why" 分隔符 + 母体版本锚点、checklist "最近检查"更新。
- **v0.5**(2026-06-01):自测发现 checklist #2 设计缺陷（events/ 用途错配为测试偏离记录）→ 修正为两步验证 + methodology.md 回填存放约定。首跑 11/13 → 修正后 13/13 ✅。
- **v0.4**(2026-06-01):自举一致性首跑——13 项 checklist 实测，11/13 ✅，2 ⚠️。发现 checklist 自身设计缺陷：#2 将 events/ 错当测试偏离记录目录（events/ 实际是迭代事件日志），暴露"checklist 自己也需要被自举"的二阶自举问题。
- **v0.3**(2026-06-01):操作化自举一致性——将"重跑对照检查"从一句宣言变为 13 项可执行 checklist (`references/self-consistency-checklist.md`)，SKILL.md 自举段引用之。
- **v0.2**(2026-05-29):消除双副本漂移（总则收归 methodology.md 单一源头）、三层表补 L1/L3 记偏离、L2 加 mock prompt 模板、L3 投票参数具体化、新增 Limitations 章节。
- **v0.1**(2026-05-29):从 video-remix 反馈环测试体系提炼。

## Limitations

- **不能代替人类验收测试**:L3b 审美分是近似值,方差大时需人类裁决。
- **依赖被测 skill 的状态契约准确性**:若被测 skill 自身未定义状态契约,L2 测试无法进行。
- **L1 功能层依赖 skill-creator**:若无 skill-creator,退化为手工 assertion checklist,覆盖粒度下降。
- **不测创造性质(creativity quality)**:框架只能测"像不像参照物",测不了"有没有创新价值"。
- **不做架构审计**:skill 架构/文档组织 → `reviewing-in-chaos`。本 skill 只测产出物动态质量。
