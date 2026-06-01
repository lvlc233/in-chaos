## trigger: evaluating-in-chaos + reviewing-in-chaos v2 二次验收，iteration-in-chaos 经 v1 大幅修复后再测
## context: 用户要求用 evaluating 和 reviewing 再次分别验收修复后的 iteration-in-chaos
## method: subagent 并行分派，独立运行，两份报告同时产出

## what_changed
v1 的 1🔴 + 12 条缺陷全部消除。v2 仅剩 4 项精度级优化：验证门未自包含(🟠)、i/N 进度不落盘/tech-rejected 分支条件/路由入口缺失(🟡)、3 项轻微(⚪)。evaluating 确认 L3a 全合规、自举一致性全通过、description 范本级。状态机骨架已生产级，剩余为参数化完善。

## extracted_principles:
### 1. 硬规则核心定义必须自包含
  证据: reviewing — Rigid #1 "技术先过验证门" 的核心定义依赖 cross-ref，压缩后 agent 可能跳过。superpowers Iron Law 用代码块自包含宣示。
  原则: 任何 Rigid 规则的完整定义必须在规则文本自身中给出。cross-ref 只能作为"详见"的补充，不能作为定义的唯一载体。简单规则（如三要素）用一行写全，不要为了"简洁"把定义藏到 references。

### 2. transition 的分支条件必须可机械判断
  证据: reviewing — tech-rejected "→ accumulated / → new-task" 二选一，分支条件未写清。agent 需语义推断何时走哪条。
  原则: 任何有多个出口的状态，必须在执行动作列（或 transition 列）写出分支条件。条件必须可机械判断——不能依赖 agent 的上下文理解。

### 3. 信号检测的时间窗口需要量化
  证据: evaluating — feedback-received "近期" 未定义时间窗，"持续通过"阈值未量化。导致不同 agent/session 间触发一致性低。
  原则: 任何含"近期/持续/频繁/多次"的时间相关判断，必须给数值窗口（如 7 天），否则跨 session 可复现性为零。

## tags: meta-iteration, v2, reviewing-in-chaos, evaluating-in-chaos, precision-refinement, self-contained, threshold
## crystallized_to:
- SKILL.md Rigid #1 (验证门三要素自包含)
- SKILL.md feedback-received (时间窗口量化: 近7天)
- SKILL.md accumulated (聚类 fallback 策略)
- SKILL.md tech-rejected (分支条件显式化)
- SKILL.md revalidate-preference (阈值量化: 连续≥2次)
- SKILL.md 快速路由 (外部技术引入标记修正)
