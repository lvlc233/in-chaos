# iteration-in-chaos

把用户反馈转化为可复用的迭代技术体系。

**核心产出：** `techs/` — 可复用的迭代方案（检查方法、设计模式、执行流程）。  
**输入机制：** 从用户反馈中感知模式 → 记日志 → 浮现结晶为 techs/。  
**编排层：** `preferences/` — 用户在多维度上选择的技术管线（什么维度用什么技术、什么顺序）。  
**职责边界：** 提供和管理迭代方案。发现问题（审核）和验证质量（评测）是本 skill 流程中的独立阶段，不做额外跨 skill 依赖。

## 状态机

识别当前状态，执行对应动作，然后按 transition 进入后续状态。任何状态都是合法入口点。**多状态同时触发时，按本表从上到下的优先级执行。**

| 状态 | 触发条件 | 执行动作 | → 后续状态 |
|------|----------|----------|------------|
| **new-task** | 开始新开发/迭代任务 | ①识别当前产出物涉及的维度 ②扫 `preferences/index.md` 匹配各维度管线 ③加载管线，准备执行 ④检查是否有 pending 日志可结晶 **⑤若迭代对象是 iteration-engine 自身，额外加载自身 techs/ 做 dogfooding 检查（用自己迭代自己）** | → applying-tech（执行管线第一项技术） |
| **feedback-received** | 用户给出纠正/原则/方向 | 检测是否触发原则信号（原则陈述/同类纠正3+/引用外部标准/覆盖方案/强调整体方向）。触发 → 写 `log/{date}-{关键词}.md`，`extracted_principles` 必填。不触发（单次命名/一次性修改/闲聊风格）→ 不记 | → new-task（反馈即要求改，改完继续走管线） |
| **accumulated** | 用户说"整理反馈" / 同方向日志 ≥2 条 / new-task 第④步检测到 pending 日志 | 扫 `log/`，识别同方向日志 → 提议结晶方案：结为 tech 还是 preference？→ 等待用户确认 | → crystallizing（确认）/ → 结束（拒绝） |
| **crystallizing** | 用户确认结晶提议 / 主动要求"记下来" | tech: 创建 `techs/{name}.md`，status: draft，填写边界/测试案例/效果对比。preference: 创建 `preferences/{dimension}.md`，管线指向 techs，证据指回 log。更新日志 crystallized_to。**结晶完成后立即应用到当前迭代对象** | → new-task（重载管线，新技术将进入验证闭环） |
| **applying-tech** | 管线中执行某项技术 | 执行技术流程 → 对照验收标准检查 → 记录生效结果 | → tech-failed（验收不通过）/ → applying-tech（继续下一项技术）/ → new-task（管线完成，回第④步检查 pending 日志） |
| **tech-failed** | 技术验收没过 | 分析根因：技术本身不够好 → 更新验收标准/盲区；管线编排问题 → 调整偏好管线，旧版进 `archive/`。**失败记录比成功更值钱** | → applying-tech（修正后重试同一技术） |
| **revalidate-preference** | 用户问"这个偏好还成立吗" | 查生效记录：持续通过 → 确认有效；模式性失败 → 提议调整或归档 | → accumulated（失效，需替代方案）/ → 结束（有效，不需变更） |

## 核心规则

1. **技术先过验证门再进管线。** draft → 实测 → active/rejected（详见 `references/tech-template.md`）。用户直觉是触发信号，不是豁免。
2. **偏好必须指回日志证据。** 没有证据的偏好不成立。
3. **状态机是编辑过滤器。** 把内容放进状态表的过程本身就暴露了哪些有执行价值、哪些只是参考说明。写不进状态表的内容 → 进 `references/`。
4. **对自己用自己 (dogfooding)。** 用 iteration-engine 自己的流程迭代自身。自己流程在自己场景下走不通 → 流程需要调整。

## 快速路由

| 用户说 | 目标状态 | 说明 |
|--------|----------|------|
| 日常纠正/引导 | → feedback-received | 纠正后立即走 new-task 应用改进 |
| "整理一下最近的反馈" | → accumulated | |
| 开始新任务 / "迭代 X" | → new-task | 先加载管线，再查 pending 日志 |
| "这个偏好还成立吗" | → revalidate-preference | |
| "把这个记下来"（主动要求） | → crystallizing | 跳过浮现阈值和确认 |
| 外部技术/Skill 发现可用方法 | → 引入 `techs/`，标注 `status: pending-review`，待用户审核 | |

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
