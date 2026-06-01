---
name: lazy-in-chaos
description: Use when running the 3-skill mutual-iteration cycle (reviewing + evaluating → iteration → rotate). Triggers: 互驱迭代 / 三轮互驱 / lazy iterate / 懒人迭代 / 跑一轮互驱 / 懒人版. NOT for single-skill auditing or one-off fixes.
---

# lazy-in-chaos

3-skill 互驱迭代的懒人版。从 in-chaos 生态复盘中提炼——**去仪式、留干货、补盲区**。

## 核心改动 (vs 原版 in-chaos)

| 原版做了什么 | 懒人版改了什么 | 理由 |
|-------------|---------------|------|
| iteration 8 状态 + 5 层目录 (log/preferences/techs/archive/references) | 0 子目录,0 状态机。只有一个 5 步流程 | 单日 $0.93 消耗中可观比例花在目录维护而非实际修复 |
| reviewing 8 维 rubric + 4 归类 + 3 专项 | 4 维致命维度 | 非致命维度 (🟡/⚪) 产出的是 polish,不是可靠性 |
| evaluating 3 层 (L1-L3) | 2 层 (L1 + L2) | agent 没有可靠审美 (L3),懒人版诚实跳过 |
| 13 项自举 checklist | 0 项 | 自举一致性由互驱轮换自然保证,不需要 checklist |
| 无人类确认, agent 闭环 | 3 个门: 人类确认 + 外部验证 + 跨 session | 补上最大缺环: agent 独判 → 人类裁决 |
| 无外部被测 skill | 每轮至少一个外部 skill 验证 | 破圈——验证方法论不是面向自身过拟合 |
| 迭代先于使用 | 无外部使用证据 → 不进迭代 | 防止迭代引擎空转 |

## 5 步流程

### Step 1: 选定被测 + 角色分配

根据上一轮结果 (查 `cycle-log.md`),确定本轮三个角色:

| 角色 | 做什么 | 分配 |
|------|--------|------|
| T (被测) | 本轮要迭代改进的 skill | 轮换规则: 上一轮的 A 变成本轮的 T |
| A (审计者) | 审 T,出审阅报告 | 从 {reviewing,evaluating,iteration} 中选 T 之外的两个之一 |
| E (评测者) | 测 T 的动态行为 | 剩下那个 |

> 首轮从任意 skill 开始,建议从 reviewing-in-chaos (三个中最成熟的) 开始。
> 详细角色分配矩阵见 `references/flow.md`。

### Step 2: A 审 T

A 加载 reviewing-in-chaos,但**只用 4 维精简 rubric** (非 8 维):

| 维度 | 核心问题 |
|------|----------|
| **D1 描述正确性** | description 写的是触发条件 (纯 when),还是混了能力清单 (what)? |
| **D2 跨上下文健壮性** | 长链路 skill 的中间态落盘了吗? 上下文压缩后能续跑吗? |
| **D3 失败模式** | 核心命令 / API 语义对吗? 失败了有兜底吗? (纯指导型 skill 此维降级为 D4) |
| **D4 职责边界** | 管什么? 明确不管什么? 和别人冲突吗? |

**只报告 🔴 和 🟠**。🟡 和 ⚪ 不出报告 (节约 token)。

### Step 3: [人类确认门] 🚪

**必须停在此时。** 将 A 的缺陷列表呈现给用户,用户确认:
- 哪些是真缺陷? 哪些是 agent 误判?
- 本轮修哪些? (至少修 1 个,否则本轮终止)

用户未确认 → 不进 Step 4。

### Step 4: E 测 T → I 修 → E 回归

**分三小步:**

1. **E 测基线**: evaluating-in-chaos 跑 L1(行为 3 次 pairwise) + L2(mock 单状态注入好/坏数据),记偏离
2. **I 修**: iteration-in-chaos 按用户确认的缺陷列表逐项修
3. **E 回归**: 同测试重跑,对比基线 → 确认改善或检出回归

### Step 5: [外部验证门 + 跨 session 门] 🚪🚪

**外部验证 (非阻塞):**
- 找一个不在 in-chaos 生态内的 skill,用 T 的当前版本跑一轮
- 记录是否发现真实问题
- 无外部 skill → 标 `⚠️外部验证未执行`,不阻塞但记录

**跨 session 模拟 (阻塞):**
- 关闭当前上下文,新 session 只给中间产物,要求续跑
- 续跑成功 → ✅
- 失败 (状态丢失、读错产物、重新开始) → 标注 🔴,回到 Step 4

## 轮换规则

```
每次迭代的 T = 上一轮的 A
```

| 轮次 | T (被测) | A (审计) | E (评测) |
|------|----------|----------|----------|
| 1 | reviewing | evaluating | iteration |
| 2 | evaluating | iteration | reviewing |
| 3 | iteration | reviewing | evaluating |
| 4 | reviewing (回到第 1 轮) | ... | ... |

## 入口条件

**开始一轮互驱的条件:**
1. 被测 skill 有至少一次外部使用记录 (非生态内 skill 用过它)
2. 或用户主动要求"跑一轮互驱"

**终止条件:**
- 连续两轮 A 未发现 🔴 或 🟠 → 该 skill 达到可发布稳定态,从互驱循环中移除
- 用户说"停"

## 文件结构

```
lazy-in-chaos/
  SKILL.md              ← 5 步流程 + 4 维 rubric + 角色轮换
  cycle-log.md          ← 轮次记录 (一行一轮)
  references/
    flow.md             ← 详细流程 + 角色分配矩阵
    gaps.md             ← 缺环复盘 (为何设计成这个版本)
```

> 不需要 log/ techs/ preferences/ archive/ events/ 子目录。需要持久化的只有 `cycle-log.md`。

## 和原版三 skill 的关系

懒人版**不替代**原版 reviewing/evaluating/iteration。它是:
- 原版的**编排层**——告诉它们什么时候、对谁、怎么协同
- 原版的**砍仪式版**——去掉原版各自独立运行时需要维护的目录和中间状态
- 原版的**安全带**——人类确认门 + 外部验证门 + 跨 session 门保证不空转

三个门是本 skill 对原版生态不可商榷的补丁。没有这三道门,互驱闭环是假闭环。

## Red Flags

| 你在想 | 现实 |
|--------|------|
| "这个缺陷看起来不重要,跳过人类确认直接修" | agent 独判 = 原版的根本问题。必须停。 |
| "没有外部 skill,先跑一轮互驱看看" | 空转。入口条件说的就是不让空转。 |
| "跨 session 太麻烦,这次跳过" | 跨 session 是唯一能抓到维度 2 缺陷的方法。跳过它就是没测。 |
| "4 维够吗?原版有 8 维" | 非致命维度产出的是 polish 不是可靠性。懒人版诚实面对这一点。 |
| "没有 checklist 会不会漏" | 互驱轮换比 checklist 更能防同构盲区——A 审 T 的毛病,下一轮 A 会被 E 查。 |
