---
description: Use when the user wants to iterate or improve a skill/system based on accumulated feedback, when code review or skill audit reports need to be turned into reusable techniques, or when the user says 迭代 / 整理反馈 / 记下来. NOT for initial skill creation (writing-skills) or one-off fixes with no reuse value.
---

# iteration-in-chaos

把用户反馈转化为可复用的迭代技术体系。

**核心产出：** `techs/` — 可复用的迭代方案（检查方法、设计模式、执行流程）。  
**输入机制：** 从用户反馈中感知模式 → 记日志 → 浮现结晶为 techs/。外部审核报告（如 `reviewing-in-chaos` 审阅、code review）同样是有效输入源——审核暴露盲区 → 更新技术 → 闭环。  
**编排层：** `preferences/` — 用户在多维度上选择的技术管线（什么维度用什么技术、什么顺序）。  
**职责边界：** 提供和管理迭代方案。识别问题 → 匹配技术去修 → 验证修复效果，三步闭环。每一步的具体方法由对应的 tech 定义。  
❌ 不做：审核 skill 架构（→ reviewing-in-chaos）、评测 skill 产出（→ evaluating-in-chaos）、在迭代对象外引入新职责。

## 状态机

识别当前状态，执行对应动作，然后按 transition 进入后续状态。入口级状态可直接从用户指令进入，内部级状态依赖前置状态传入上下文。**多状态同时触发时，按本表从上到下的优先级执行。**

| 状态 | 触发条件 | 执行动作 | → 后续状态 |
|------|----------|----------|------------|
| **new-task** | 开始新开发/迭代任务 | ①识别当前产出物涉及的维度 ②扫 `preferences/index.md` 匹配各维度管线（用维度关键词匹配，见 preferences/index.md 维度定义表）③加载管线：若匹配到多条管线，按维度优先级顺序执行（preferences/index.md 维度定义表从上到下为优先级顺序），前一条管线全部完成后再执行下一条；单管线内：读管线定义 → 若管线文件底部有 `current_step: N` 则从第 N 项续跑，否则从第一项开始 ④扫描 `techs/` 中 status: draft 的技术，逐项走验证门（对照验收标准，pass→promote 为 active，fail→保持 draft 并记录），通过验证的 draft tech 立即编入对应管线 ⑤检查是否有 pending 日志可结晶 ⑥若迭代对象是自身（本 skill）→ 执行 dogfooding：按 `state-machine-check → responsibility-boundary-check` 顺序跑自身 techs/，每项对照验收标准输出 pass/fail + 偏离记录到 `events/`，失败项走 tech-failed。**dogfooding 最多重试 2 轮，超限记录偏离并继续主迭代** | → applying-tech（执行首条管线第一项技术） |
| **feedback-received** | 用户给出纠正/原则/方向 | 检测是否触发原则信号（原则陈述/同类纠正 ≥3 次/引用外部标准/覆盖方案/强调整体方向）。**同类纠正计数**：扫 `log/`，匹配相同 tags 的**近 7 天内**日志条数 ≥3 → 触发。触发 → 写 `log/{date}-{关键词}.md`，`extracted_principles` 必填。不触发（单次命名/一次性修改/闲聊风格）→ 不记 | → new-task（反馈即要求改，改完继续走管线） |
| **accumulated** | 用户说"整理反馈" / 同方向日志 ≥2 条 / new-task 第⑤步检测到 pending 日志 | 扫 `log/`，按 tags 交集 + extracted_principles 关键词分组识别同方向日志。分组策略：严格 tags 交集匹配 → 关键词相似度 → 人工确认。→ **落盘结晶提案到 `log/_proposals/{date}-{关键词}.md`**，内容：候选日志列表 + 提议方向（tech/preference）+ 理由 → 等待用户确认 | → crystallizing（确认）/ → 结束（拒绝） |
| **crystallizing** | 用户确认结晶提议 / 主动要求"记下来" | 读 `log/_proposals/` 中对应提案文件（如直接触发则从上下文提取）。tech: 创建 `techs/{name}.md`，status: draft，填写边界/测试案例/效果对比。preference: 创建 `preferences/{dimension}.md`，管线指向 techs，证据指回 log。更新日志 crystallized_to。**结晶完成后立即在本次迭代中实测验证：对照验收标准 test case 跑一遍 → pass → status 改为 active → 编入对应偏好管线；fail → 保持 draft → 记录失败原因 → 走 tech-failed**。不等到下一轮 new-task | → new-task（重载管线，已验证通过的技术已编入管线中） |
| **applying-tech** | 管线中执行第 i/N 项技术 | 执行技术流程 → 对照验收标准检查 → 在 tech 文件的生效记录表追加一行记录（日期/项目/通过?/失败根因/备注）→ **更新管线文件的 `current_step: N` 标记**（格式: 在管线文件底部追加 `current_step: N` 行；全部完成时将该行改为 `current_step: done`）。完成进入下一项，全部完成清除标记 | → tech-failed（验收不通过）/ → applying-tech（继续下一项）/ → new-task（管线完成，回第⑤步检查 pending 日志） |
| **tech-failed** | 技术验收没过 | ①分析根因（技术本身不行 vs 编排问题）②修改对应文件：技术不行 → 更新验收标准/盲区，若稳定反优化则标记 rejected 归档；编排问题 → 调整偏好管线。③在 tech 文件生效记录表追加失败记录（通过?=no + 失败根因）。**失败记录比成功更值钱**（暴露盲区）| → applying-tech（修正后重试）/ → tech-rejected（结构性失败，技术本身不可用） |
| **tech-rejected** | 技术在实测中稳定不出正效果 / 反优化 | 归档到 `archive/`，从所有偏好管线中移除，更新日志 crystallized_to。→ accumulated：存在可替代方案且需要浮现新技术。→ new-task：无替代方案且继续当前迭代任务 | → accumulated / → new-task（依上条件） |
| **revalidate-preference** | 用户问"这个偏好还成立吗" | 查**本偏好文件的生效记录表**：连续 ≥2 次通过 → 确认有效；出现模式性失败（≥2 次连续不通过）→ 提议调整或归档 | → accumulated（失效，需替代方案）/ → 结束（有效，不需变更） |

> **入口级状态**（可直接从用户指令进入）：new-task / feedback-received / accumulated / revalidate-preference  
> **内部级状态**（依赖前置状态传入上下文）：crystallizing / applying-tech / tech-failed / tech-rejected  
> **→ 结束**：回到空闲状态，等待下一次用户触发。阶段性的"不做了"或"不需要改"是合法出口，不是 bug。
> 若从内部级状态误入（缺少前置上下文），回到 new-task 重载管线再进入。

## 核心规则

### Rigid（不可跳过，触犯即崩）

1. **技术先过验证门再进管线。** 验证门三要素：边界（覆盖/不覆盖/失效条件）+ 测试案例（≥1 个，输入→应用→预期→实测）+ 效果对比（before/after + 证据）。draft → 通过三要素 → active；不明确 → 保持 draft；反优化 → rejected → archive/。用户直觉是触发信号，不是豁免。
2. **偏好必须指回日志证据。** 没有证据的偏好不成立。证据链：log → tech/preference → 管线引用。
3. **对自己用自己 (dogfooding)。** 用自身流程迭代自身。new-task 第⑤步定义了具体执行流程。自己流程在自己场景下走不通 → 流程需要调整。

### Flexible（弹性指导）

4. **状态机是编辑过滤器。** 把内容放进状态表的过程本身就暴露了哪些有执行价值、哪些只是参考说明。写不进状态表的内容 → 进 `references/`。

## 快速路由

### 状态跳转路由（→ 进入状态机）

| 用户说 | 目标状态 | 说明 |
|--------|----------|------|
| 日常纠正/引导 | → feedback-received | 纠正后立即走 new-task 应用改进 |
| "整理一下最近的反馈" | → accumulated | |
| 开始新任务 / "迭代 X" | → new-task | 先加载管线，再查 pending 日志 |
| "这个偏好还成立吗" | → revalidate-preference | |
| "把这个记下来"（主动要求） | → crystallizing | 跳过浮现阈值和确认 |

### 只读查询 / 独立操作（不进状态机）

| 用户说 | 动作 |
|--------|------|
| "看一下当前管线" | 加载 `preferences/index.md`，列出各维度管线结构 |
| "有哪些反馈还没整理" | 扫 `log/` 中 `crystallized_to: pending` |
| "评估一下 X" | 加载对应 tech 文件，独立技术评估，不进管线 |
| "有哪些技术被 reject 了" | 扫 `archive/` |
| 外部技术/Skill 发现可用方法 | **独立操作**：引入 `techs/`，标注 `status: pending-review`，待用户审核。不进状态机，审核通过后通过 crystallizing 进入管线 |

## 外部技术引入

1. 放入 `techs/`，标注 `status: pending-review` 和来源
2. 填写盲区——"这个方法审不了什么"
3. 用户审核确认后才标 `status: active`，允许进入偏好管线

## Red Flags

| 借口 | 现实 |
|------|------|
| "我先记在脑子里" | 不写 = 不存在。下次 session agent 什么都不知道 |
| "只记事件不提取原则" | `extracted_principles` 是日志唯一的价值 |
| "技术文件和偏好差不多，合并了吧" | 技术 = 可复用方法（独立于用户），偏好 = 用户编排选择。生命周期不同 |
| "用户提的技术直接进 preferences" | 技术先独立存 `techs/`，过验证门后再编入管线 |
| "这个太简单不值得提取原则" | 简单原则复用价值最高 |
| "等积累多了再一起写" | 每触必写，积累后是浮现阶段的事 |
| "生效记录不重要" | 没过的那次比过的那次更值钱——暴露盲区 |

## 文件结构

```
iteration-in-chaos/
  SKILL.md              ← 状态机 + transitions + 核心规则 + 快速路由
  techs/                ← 可复用迭代方案
    index.md
    *.md
  preferences/          ← 用户的技术管线编排
    index.md
    *.md
  log/                  ← 反馈事件 + 提取的原则
    *.md
  archive/              ← 被覆盖的旧偏好/废弃技术
  references/           ← 详细模板和格式说明
    log-template.md
    tech-template.md
    preference-template.md
```
