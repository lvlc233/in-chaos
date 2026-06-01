---
name: evaluating-skill-output
description: Use when testing or evaluating what a skill PRODUCES when it runs — 测一个 skill 跑起来对不对、做得好不好(行为正确性 + 状态流中间质量 + 内容/审美质量)。区别于 reviewing-skills(那个审 skill 文档写得合不合理,静态);本 skill 测 skill 跑出来的东西(动态)。Triggers 测试 skill、评估 skill 产出、skill 跑得对吗、中间状态质量、内容质量、审美评分、给 skill 建测试、eval skill output、test skill behavior。NOT 写新 skill(那是 writing-skills / skill-creator)。
---

# evaluating-skill-output

> 🚧 STATUS: 演进中(v0.1,从 video-remix 三层测试体系提炼)。与 [[reviewing-skills]] 配对。

## 核心原则

测一个 skill 的**产出**(它跑起来做的事 + 做出来的东西),不是审它的文档(那是 [[reviewing-skills]])。

> **结构 vs 内容**:reviewing-skills 答"这 skill **写得**合不合理"(静态读文档);本 skill 答"它**跑得**对不对、做得好不好"(动态看产出)。
> 现成框架(skill-creator)能测功能层(L1),但**系统性测不了状态流中间质量(L2)和内容/审美质量(L3)**——那是本 skill 补的盲区。

## 三层:测什么

| 层 | 测什么 | 裁判 |
|---|---|---|
| **L1 功能 / flow** | 行动计划对吗、字段/分支/契约对吗、早 fail 吗 | grader assertion(复用 skill-creator,**支持多跑取方差**) |
| **L2 状态流中间质量** | 每个状态的**中间产物**对吗(若 skill 是状态流) | grader 对照状态契约 assert 中间产物 + 记偏离;**mock 单状态测** |
| **L3 内容 / 审美质量** | 产出好不好、像不像目标参照 | L3a 对照参照物客观判;L3b 主观审美用 rubric + 投票 + 人类校准 |

> **先归类,不是每个 skill 都要三层**:纯无状态工具型可能只要 L1;长状态流 skill 要 L2;有内容/创意产出(视频/文案/设计)的才要 L3。
> 裁判列只标各层最特征的判法;**「记偏离 + 归因」是三层通用**(总则 #2),别只在 L2 记。

## 怎么用

1. **归类被测 skill**:有状态流吗?有内容/创意产出吗?→ 定要哪几层。
2. **每层先定标准**(先有标准后测):L1 = expected assertion;L2 = 状态契约;L3 = rubric 锚点。
3. **跑 + 记偏离**:按方法论总则(详见 `references/methodology.md`)。
4. **多次跑抗随机**(复用 skill-creator variance:mean/stddev)。

## 方法论总则(单一源头 = `references/methodology.md`)

六条横切三层。**完整定义在 `references/methodology.md`(权威源);本处只列标题供扫读,要改总则只改那里——避免双副本漂移(本 skill 维度 6 自己警告过的病)**:

1. 先有标准后测;
2. **记偏离 + 归因 —— 三层(L1/L2/L3)都记,不只 L2**;
3. 多次跑抗随机;
4. 最小上下文;
5. 客观 / 严厉 / 怀疑驱动;
6. 裁判分层别混用 —— **L1(被测若已细分则 flow/e2e)/ L2 / L3a / L3b 各管各**,同一观测量别两层重复打分。

## L3 审美的诚实底线

agent **没有可靠审美**。L3 分层:
- **L3a 客观对标**(像不像参照物)→ agent 能带证据判。
- **L3b 纯主观审美**(好不好看)→ 艺考式 rubric(维度 + 1-5 评分锚点)+ 多 agent 投票取方差 + 人类校准点;**方差大 / 偏离校准的维度标「需人类裁决」**。
- **禁止 agent 用"我觉得不错"这类无锚点判断当结论。**

## 自举一致性

本 skill 自己就是一套标准 → **必须无双标**:它要求被测"记偏离 / 裁判分层",自己的方法论文档也得遵守。用 [[reviewing-skills]] 的"方法论 / 标准型 skill 自举一致性"专项复审本 skill。

## References

- `references/methodology.md` — 三层详细(L2 mock 单状态测法 / L3 诚实分层 rubric 模板)+ 总则
- `examples/video-remix.md` — 第一个 worked example(video-remix 三层测试体系)

## CHANGELOG

- **v0.1**(2026-05-29):从 video-remix 反馈环测试体系提炼。与 reviewing-skills 配对成「静态审结构 + 动态测产出」。
