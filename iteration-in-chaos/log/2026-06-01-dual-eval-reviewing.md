## trigger: evaluating-in-chaos + reviewing-in-chaos 双线验收 iteration-in-chaos，两份报告同时产出
## context: 用户要求用 evaluating 和 reviewing 分别验收 iteration-in-chaos，subagent 并行执行
## method: subagent 并行分派 (dispatching-parallel-agents)

## what_changed
reviewing 发现 1🟠 + 6🟡 + 1⚪，根因: 状态机设计扎实但基础设施未同等级审查。evaluating 发现 1🔴 + 6🟡 + 2🟢，根因: 原则→工程化断层 (5 个偏离共因)、增量修复不完整、生命周期字段同步缺失。

两份报告高度互补——reviewing 从架构角度指出规则分层/路由/边界问题，evaluating 从运行时角度指出执行层缺失。两线共识: 状态机本身优秀，但 dogfooding 不可执行、核心规则无分级、执行动作多处依赖 agent 语义推断。

## extracted_principles:
### 1. 原则正确 ≠ 可执行
  证据: evaluating L1_A12 — dogfooding 只有一句话 "额外加载自身 techs/ 做 dogfooding 检查"，选哪些/什么顺序/判定标准全无。核心规则 #4 在原则层正确，在执行层不成立。
  原则: 任何写在状态机里的 "执行动作" 都必须是 agent 能直接执行的步骤——包括选哪个文件、按什么顺序、判定什么标准。原则写进 Red Flags，执行动作写进行为列，两者不互相替代。

### 2. 原则层需要 Rigid/Flexible 声明
  证据: reviewing — 核心规则 4 条中 1/2/4 是硬约束、3 是哲学指导，但并列在同一列表无区分。agent 无法判断哪些碰了即崩。
  原则: 面向 agent 的规则文件必须有刚性层级。硬约束用 `<HARD-GATE>` 或 Rigid 标签宣示；弹性指导标 Flexible。不能把 "不执行就崩" 和 "最好有" 放在同一优先级。

### 3. 路由表语义必须统一
  证据: reviewing — 快速路由表混装了 "状态跳转" (10 条中 5 条)、"只读查询" (3 条)、"独立操作" (2 条，含外部技术引入)。"外部技术引入" 完全没有状态机映射。
  原则: 路由表的每一行要么映射到一个状态 (入口级或内部级+fallback)，要么明确标为 "独立操作 / 不进状态机"。混合语义会导致 agent 在不知道该不该走 transition 时自行猜测。

### 4. 执行动作必须显式声明落盘目标
  证据: evaluating L2 — applying-tech "记录生效结果" 没写写到哪；tech-failed "失败记录比成功更值钱" 没写存到哪。agent 在新 session 中无法推断。
  原则: 任何涉及 "写/记录/存储" 的执行动作，必须在同一行给出明确的文件路径或命名规则。`记录到 tech 文件的生效记录表` 优于 `记录生效结果`。

### 5. 跨 session 状态依赖需要持久化机制
  证据: evaluating — "同类纠正3+" 依赖 agent 记忆，"同方向日志" 靠语义推断。两者在 session 断裂后均不可靠。
  原则: 任何依赖跨 session/cross-turn 累计状态的条件判断，必须在文件系统中持久化计数器或明确分组 tags。不能假设 agent 会记住上一轮。

### 6. 双线审计互补价值
  证据: 两个报告都指向相同根因但路径不同——reviewing 走结构分析发现基础设施薄弱，evaluating 走执行模拟发现工程化断层。架构审视 + 动态评测 = 完整诊断。
  原则: 对长链路有状态型 skill，仅做架构审视 (reviewing) 会漏掉执行层盲区，仅做动态评测 (evaluating) 会漏掉设计层缺陷。两者并行是最小有效审计。

## tags: meta-iteration, dual-eval, reviewing-in-chaos, evaluating-in-chaos, dogfooding, engineering-gap, state-machine
## crystallized_to:
- SKILL.md (description + 职责边界 ❌不做 + dogfooding 可执行化 + 核心规则 Rigid/Flexible + 状态表 6 项修正 + 快速路由拆分)
- preferences/index.md (维度定义表 + structure-audit 编入管线)
- references/preference-template.md (占位符替换)
- references/tech-template.md (失败记录列)
- techs/responsibility-boundary-check.md (效果对比刷新)
- TODO.md + todo-done-summary.md (矛盾消除)
