## trigger: evaluating-in-chaos + reviewing-in-chaos v3 终验，iteration-in-chaos 经两轮迭代后再测
## context: v1 消除 1🔴+12🟡，v2 消除 1🟠+4🟡，v3 发现 1🟠+6🟡 均在衔接面精度层
## method: subagent 并行分派

## what_changed
v3 reviewing 发现 1🟠 (i/N 进度不落盘) + 6🟡 (聚类语义依赖/in-memory提案/反向索引缺失/dogfooding终止声明/来源歧义/下游感知契约) + 2⚪。v3 evaluating 确认 L1 12/12 pass，L2 6/8 pass + 1 fail (tech生效记录缺失败根因列) + 1 untested (tech-rejected从未触发)，L3a 4.50/5，L3b 3.60/5。定级 B+ → A- 区间。核心骨架已生产级，剩余为衔接面精度打磨。

## extracted_principles:
### 1. 管线进度必须可落盘恢复
  证据: reviewing — i/N 仅在 applying-tech 触发条件字符串中，压缩后不可恢复。虽然生效记录可推断进度，但不机械。
  原则: 任何状态机的"第几步/N" 进度标记必须有独立的落盘点。可以是最简形式（tech 文件一行 `current_step: i`），但必须在文件系统中可查询，不能只存在于触发条件的字符串里。

### 2. 模板与实际文件必须同步回填
  证据: evaluating L2_S5 — references/tech-template.md 有"失败根因"列但 4 个实际 tech 文件均无。v2 更新了模板但未回填。
  原则: 修改模板/标准后，必须扫描所有依赖该标准的文件并同步更新。模板说"要有"但实际"没有" = 自举性断裂。这对方法论型 skill 是致命伤——要求别人遵守的格式自己没做到。

### 3. 状态机内部提案应有落盘载体
  证据: reviewing — accumulated 提议和 crystallizing 确认之间存 in-memory 窗口。压缩后 agent 不知道要结晶什么。
  原则: 任何需要用户确认的"中间提案"（不仅限于 crystallizing），在确认前应有落盘文件。即使可重算恢复，恢复成本应尽可能低。"可恢复但不能原地恢复" 是 🟡，"不可恢复" 是 🔴。

### 4. 未触发过的状态路径是隐蔽债务
  证据: evaluating — tech-rejected 从未被真实触发，其与管线移除/日志更新的联动未经真实数据验证。
  原则: 状态机中从未在生产中触发过的路径，应在审计报告中醒目标注为 U NTESTED PATH。这不是 bug 但是风险——如果设计时就假定某个路径"以后会用"，那这个路径的联动逻辑就是 untested assumption。

## tags: meta-iteration, v3, precision-final, pipeline-progress, template-sync, untested-path
## crystallized_to:
- SKILL.md new-task ③ (管线断点续跑 + ⑤ dogfooding 最多2轮)
- SKILL.md accumulated (提案落盘 log/_proposals/)
- SKILL.md crystallizing (读提案文件执行)
- SKILL.md applying-tech (current_step 标记 + 生效记录含失败根因列)
- SKILL.md revalidate-preference (明确查本偏好文件生效记录表)
- techs/state-machine-check.md (生效记录表加失败根因列)
- techs/structure-audit.md (生效记录表加失败根因列)
- techs/blind-spot-driven-design.md (生效记录表加失败根因列)
- techs/responsibility-boundary-check.md (生效记录表加失败根因列)
