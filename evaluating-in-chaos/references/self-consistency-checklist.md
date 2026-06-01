# 自举一致性对照检查

> evaluating-in-chaos 对外立了标准 → 自己的文档必须遵守。
> **每次修改 methodology.md 的总则或 L3 规则后，跑一遍本表。**
> 最近检查: 2026-06-01 (v0.6.1, methodology.md 总则重构后重跑, 13/13 ✅, 行号引用全量更新)

## 检查清单

| # | 对外立的规则 | 验证问题 | 检查位置 | 通过? | 证据/偏离 |
|---|-------------|----------|----------|-------|-----------|
| 1 | **先有标准后测** | methodology.md 里每条判定规则是否**先定义 pass/fail 标准**，再描述怎么跑？ | `methodology.md` L1/L2/L3 各段 | ✅ | L1:18 "每个用例先写 expected assertion 清单"; L2:29-31 状态契约表定义入口/输入/产出/出口; L3a:59 维度+证据; L3b:64 艺考式 rubric |
| 2 | **记偏离 + 归因** | ① methodology.md 是否定义了统一的偏离记录格式（`test/layer/verdict/expected/actual/deviation`）？② 本 skill 自身的事件/自测记录中，偏离是否按此格式记录？ | ① `methodology.md:85-93` ② `events/*.md`（迭代事件）+ 本 checklist 的"本次结果"段（自测偏离） | ✅ | ① methodology.md:85-93 定义了 JSON schema（含 sign/where/input/output/why 可定位字段）。② 本次自测偏离已按此格式记录在 checklist 的"本次结果"段。`events/` 目录存放的是**迭代操作记录**（修复了什么→结果），测试偏离记录应存放在被测 skill 的 evals/ 中。 |
| 3 | **记偏离不限 L2** | 三层（L1/L2/L3）是否**都**记偏离，不只 L2？ | `methodology.md:76` (Hard Rule #2 "记偏离") + events 实际记录是否覆盖多层 | ✅ | methodology.md:76 明确写"三层(L1/L2/L3)都记,不只 L2" |
| 4 | **多次跑抗随机** | L1 测试说明是否包含"多次跑取方差"指引？ | `methodology.md:16` L1 段 | ✅ | methodology.md:16 "多次跑取 mean/stddev(抗随机)" |
| 5 | **最小上下文** | methodology.md 是否包含"执行前确认输入只来自上游产物 + 该状态指令"的 pre-flight 检查？ | `methodology.md:78` (Hard Rule #4) | ✅ | methodology.md:78 "执行前确认:被测 state/S_n 的输入是否只来自上游产物 + 该状态指令？无额外 skill body 全文注入" |
| 6 | **裁判分层别混用** | L1/L2/L3a/L3b 的判定 territory 是否互斥？同一观测量是否只被一层打分？ | `methodology.md:79` (Hard Rule #5) + SKILL.md 三层表 (:19-23) | ✅ | L1 测功能行为, L2 测中间状态质量, L3 测内容审美。methodology.md:79 明确列出各层 territory。SKILL.md:19-23 三层表列清晰 |
| 7 | **L3a 客观对标** | L3a 是否要求对照参照物 + 证据（具体帧/片段/引文）？ | `methodology.md:58-61` L3a 段 | ✅ | methodology.md:59-61 "维度=跟目标参照物可锚定的对比维" + "每维打分+证据(具体帧/片段/引文)" |
| 8 | **L3b 艺考式 rubric** | L3b 是否有维度 + 1-5 评分锚点（5/3/1 各长什么样）？ | `methodology.md:63-66` L3b 段 | ✅ | methodology.md:64 "维度+1-5 评分锚点(5/3/1 各长什么样)" |
| 9 | **禁止无锚点判断** | 全文是否没有任何"我觉得不错"/"看起来还行"类无锚点审美判断当结论？ | 全文 grep `我觉得` / `看起来` | ✅ | 全文 3 处"我觉得不错"均在**禁令语句**中（SKILL.md:51, methodology.md:67, checklist.md:19），无一处作为实际判断。 |
| 10 | **方差大标"需人类裁决"** | L3b 是否要求方差 > 1.5 或偏离校准 > 1 标"需人类裁决"？ | `methodology.md:65` | ✅ | methodology.md:65 "方差 > 1.5 (on 1-5 scale) 或偏离校准 > 1 标「需人类裁决」" |
| 11 | **单一源头** | 总则的完整定义是否只在 methodology.md 一份文件里？SKILL.md 是否只列标题不存全文？ | `methodology.md` vs `SKILL.md:37-44` 总则段 | ✅ | SKILL.md:37-44 只列 6 条标题 + 声明"完整定义和细节均在 methodology.md(权威源)"。L3 诚实底线在 SKILL.md:46-51 有 5 行摘要（非全文拷贝，是重要硬规则的醒目展示）。 |
| 12 | **CHANGELOG 与版本一致** | SKILL.md 状态行、CHANGELOG 最后一条、最近 events 记录的版本号是否一致？ | `SKILL.md:8` vs `SKILL.md:69` vs `events/` | ✅ | 状态行 v0.6 (`SKILL.md:8`) = CHANGELOG 最新条 v0.6 (`SKILL.md:69`) = events/v0.6-reviewing-audit-response.md 记录 v0.6 |
| 13 | **用完回填** | 最近一次真实测试后，是否把新踩的坑回填进了 methodology.md + CHANGELOG？ | `methodology.md:99-101` + CHANGELOG 是否 ≥ events 记录 | ✅ | v0.5 自测发现 checklist #2 设计缺陷 → methodology.md:95 存放位置说明已回填。v0.6 reviewing 审计 → 7 项修复已回填 CHANGELOG。events/ 记录了 C1 操作化、修复回归、首跑、二次跑、v0.6 审计响应 |

## 判定

- **全 ✅** → 自举一致，无双标
- **有 ❌** → 逐条修，修完重跑本表
- **连续 3 次检查同一项 ❌** → 规则本身可能有问题（过于理想/不可操作），提 issue 讨论是否修改规则

## 本次结果 (2026-06-01, 三次跑: v0.6.1 重跑)

**13/13 ✅** — methodology.md 总则重构 (hard/best-practice 分层) 后全量重跑，所有行号引用已更新至当前版本。既往 v0.5 残余数据 (#13 ⚠️ / 偏离记录 partial) 均已清理。无双标。

### 偏离记录

```json
{"test":"自举一致性三次跑 v0.6.1","layer":"自举","verdict":"pass",
 "expected":"13 项全 ✅","actual":"13 项全 ✅",
 "deviation":null}
```

### 本次重跑修正
- #2: 行号 `:80-88` → `:85-93`
- #3: 行号 `:74` → `:76`
- #5: 行号 `:76` → `:78`
- #6: 行号 `:78` → `:79`
- #12: 行号 `:64/66` → `:69`，证据从 v0.3 更新为 v0.6
- #13: ⚠️ → ✅ (既往回填已全部完成)

### 历史回填 (v0.5 已完成, 仅供参考)

- [x] **checklist #2 改措辞**: 已改为两步验证——①格式是否在 methodology.md 定义 ②本 skill 自身事件/自测中是否按格式记录。不再假设 events/ = 测试偏离主存储
- [x] **methodology.md 回填**: 已在 methodology.md:95 补充存放位置说明，区分 events/(迭代操作记录) vs 测试偏离记录(被测 skill 的 evals/)
- [x] **checklist 加注**: events/ vs 测试偏离记录的用途区分已写入 methodology.md

## 自举特例: evals/ 目录

evaluating-in-chaos 要求被测 skill 的测试偏离存放在 `evals/*.json`。本 skill 自身无 `evals/` 目录——因为被测者即自身时，测试偏离与本 skill 的迭代事件同源，强行分离会产生双副本漂移。自测偏离以本 checklist 的 inline JSON 为准。这不是双标逃避，是"被测=自身"场景下的合法简化——在 checklist 中显式声明此特例，满足自举透明性。
