# event: C1 自举一致性操作化
## 触发
reviewing-in-chaos 审视 evaluating-in-chaos 发现 C1: 自举一致性检查是空壳口号（"每次修改后重跑对照检查"从未定义检查内容）
## 操作
- 新建 `references/self-consistency-checklist.md`: 13 项逐条验证表，每条映射"对外立的规则 → 验证问题 → 检查位置 → 通过? → 证据"
- SKILL.md 自举段: 将一句话宣言改为引用 checklist，加"改完即查"约束
- SKILL.md 状态行: v0.1 → v0.3
- SKILL.md CHANGELOG: 补 v0.2 条(之前 events 声称更新但 CHANGELOG 未同步) + 新增 v0.3 条
## 结果: 通过
- 自举一致性从宣言变为可执行: 13 项逐条对照，有判定标准（全✅→一致 / 有❌→逐条修 / 连续3次同项❌→规则本身可能有问题）
