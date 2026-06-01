## trigger: reviewing-in-chaos 外部审计 evaluating-in-chaos，发现 7 项抛光层缺陷
## context: 用户要求用 iteration + reviewing 分别验收 evaluating-in-chaos，reviewing subagent 产出完整审计报告
## method: subagent 并行分派 (dispatching-parallel-agents) → reviewing audit → iteration state machine (new-task → applying-tech → crystallizing)

## what_changed
reviewing-in-chaos 审计发现 7 项缺陷（3🟡 + 4⚪），无架构级/结构级问题。全部修复：
- methodology.md: 总则 hard/best-practice 分层 → 5 条 Hard Rules + 1 条 Best Practice
- SKILL.md: L3 诚实底线段补 `references/methodology.md` 引用指针
- SKILL.md: References 段补 `self-consistency-checklist.md`
- SKILL.md: Limitations 加 `reviewing-in-chaos` 配对回链
- examples/video-remix.md: 统一 "why" 分隔符 (`归因=` → `归因: `) + 母体版本锚点
- self-consistency-checklist.md: "最近检查" 更新为 v0.5 二次跑 + 外部审计
- SKILL.md: STATUS v0.5→v0.6, CHANGELOG 新条
- structure-audit + blind-spot-driven-design 生效记录更新

## extracted_principles:
### 1. 方法论型 skill 的缺陷集中在抛光层是健康的
  证据: reviewing-in-chaos 审计 evaluating-in-chaos 结论——内核扎实 (自举一致性 13/13 ✅)，7 项缺陷全是抛光层（引用完整性、格式一致性、配对回链）。无架构缺陷。
  原则: 对方法论型 skill，内核的正确性（自举一致性、单一源头、诚实分层）是架构级底线；抛光层缺陷（交叉引用、格式一致性）说明 skill 质量已到精细打磨阶段，不是地基问题。区分"抛光"和"缺陷"有工程价值——抛光层修复成本低、风险低，不应被同等对待。

### 2. 外部审计的成果闭环：从审计报告到迭代日志到修复到生效记录
  证据: 本次流程完整走通——reviewing 审计 → 7 缺陷 → iteration new-task 识别 review-methodology 维度 → 应用 structure-audit → 逐项修复 → 更新生效记录 → 写日志。四步闭环：审计发现 → 迭代匹配技术 → 执行修复 → 验证记录。
  原则: 对生态内 skill，外部审计是 iteration-in-chaos 的有效输入源。审计报告 = feedback，映射到维度 → 加载管线 → 执行 tech → 记生效。这是"技能自演进"的完整路径。

### 3. 配对回链是"架构面"而非"文档面"
  证据: reviewing 审计指出 evaluating-in-chaos 与 reviewing-in-chaos 同仓互补但无回链。这不是文档完整性 bug，是"配对契约只落一半"——reviewing 多次引用 evaluating，但 evaluating 不声明"架构审计 → reviewing"，下游 agent/skill 无法自动感知配对关系。
  原则: skill 间的交叉引用不是文档层面的 nice-to-have，是架构层面的契约。声明"我和谁配对"的 skill 必须被对方回链，否则契约不成立。这与 API 文档声明的 "depends on / consumed by" 同构。

## tags: reviewing-in-chaos, evaluating-in-chaos, polish-layer, pairing, external-audit, iteration-closed-loop
## crystallized_to:
- evaluating-in-chaos/SKILL.md (v0.5→v0.6, STATUS+CHANGELOG+L3 指针+References 补 checklist+Limitations 配对回链)
- evaluating-in-chaos/references/methodology.md (总则 hard/best-practice 分层)
- evaluating-in-chaos/examples/video-remix.md ("why" 分隔符统一 + 母体版本锚点)
- evaluating-in-chaos/references/self-consistency-checklist.md ("最近检查"更新)
- iteration-in-chaos/techs/structure-audit.md (生效记录追加)
- iteration-in-chaos/techs/blind-spot-driven-design.md (生效记录追加)
