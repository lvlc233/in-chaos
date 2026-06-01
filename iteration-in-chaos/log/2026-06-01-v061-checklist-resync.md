## trigger: reviewing-in-chaos + iteration-in-chaos 二次验收 evaluating-in-chaos v0.6，两线报告汇聚于 checklist 行级证据过时
## context: 用户要求用 iteration + reviewing 分别验收 evaluating-in-chaos，两线报告均指向同一病灶——自举一致性 checklist 在 v0.6 修改 methodology.md 后行号引用/证据内容集体过时
## method: reviewing subagent (架构审计) + iteration subagent (状态机走查) → 缺陷汇总 → iteration state machine (new-task → applying-tech → 修复 → 记录)

## what_changed
两线报告共发现 10 项缺陷/改进点，5 项合并修复：

**checklist 重跑** (修复端):
- #2/#3/#5/#6 行号引用: `:80-88`→`:85-93`, `:74`→`:76`, `:76`→`:78`, `:78`→`:79`
- #12: 行号 `:64/66`→`:69`, 证据从 v0.3 更新为 v0.6
- #13: ⚠️→✅, 行号 `:92-94`→`:99-101`
- "本次结果"段: 二次跑→三次跑, 偏离记录 partial→pass
- header "最近检查": 更新为 v0.6.1 三次跑

**日志修复**:
- log/2026-06-01-reviewing-audit-evaluating.md: crystallized_to 从 pending 改为具体文件清单

**events 补齐**:
- 创建 events/v0.6-reviewing-audit-response.md

**盲区扩展**:
- structure-audit.md 盲区 +1: "不检查 skill 间配对契约完整性"

**版本更新**:
- SKILL.md: STATUS v0.6→v0.6.1, CHANGELOG 新条

## extracted_principles:
### 1. Checklist 行级证据是结构化的运维负债
  证据: v0.6 修改 methodology.md 后，checklist 的 13 条中有 6 条行号引用过时 (#2/#3/#5/#6/#12/#13)。原因是 checklist 行级证据列是静态文本——每次 methodology.md 行号偏移后需手工逐行更新。这是 checklist 格式设计缺陷，不是内容疏漏。
  原则: 包含行号引用的 checklist/对照表必须设计更新机制——要么行证据打"截至 vX.Y"版本锚点（header 更新后行证据仍成立），要么行号改为语义锚点（如 `§Hard Rule #2`）。纯文本行号在迭代频率高的文档中是不可维护的。

### 2. 二次验收比首次验收更深——首次审"有什么缺陷"，二次审"修完后还剩下什么"
  证据: 首次 reviewing 审计发现 7 项抛光层（方法论无缺陷），全部修完。二次验收发现的是**首次修复引入的新问题**（methodology.md 重构导致 checklist 行号偏移）。两轮审计的焦点从"方法论对不对"下沉到"修复副作用有没有被跟踪"。
  原则: 迭代后的二次验证必须检查"上次修的引入新副作用了吗"——尤其是修改了其他文件引用锚点的改动（行号、section 名、字段名）。这是重构型修复的遗留扫描，但在 checklist 这类绑定行号的文件中尤其隐蔽。

### 3. 配对回链原则从日志到 tech 盲区的转化路径
  证据: log/2026-06-01-reviewing-audit-evaluating.md 原则 #3 "配对回链是架构面而非文档面" 在首次修复中只实现了 evaluating→reviewing 回链，但未将原则转化为可执行检查。本次迭代将其写入 structure-audit.md 盲区（"不检查 skill 间配对契约完整性"），完成原则→日志→tech 盲区 的转化闭环。
  原则: 日志中提取的原则有两条路径落地——立即修复（代码改）和 tech 扩展（盲区声明）。前者一次修完，后者让下次外部审计能自动复用。两者不同步是常见的半闭环（只修了代码但没更新检查体系）。

## tags: evaluating-in-chaos, checklist-maintenance, line-number-drift, second-pass-audit, pairing-contract, blind-spot-expansion
## crystallized_to:
- evaluating-in-chaos/references/self-consistency-checklist.md (13 项行号全量更新)
- evaluating-in-chaos/SKILL.md (v0.6→v0.6.1)
- evaluating-in-chaos/events/v0.6-reviewing-audit-response.md (新建)
- iteration-in-chaos/techs/structure-audit.md (盲区 +1: 配对契约)
- iteration-in-chaos/log/2026-06-01-reviewing-audit-evaluating.md (crystallized_to 更新)
