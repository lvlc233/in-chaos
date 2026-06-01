# structure-audit
## status: active
## 覆盖维度
review-methodology
## 边界
- 覆盖: 在内容审查之前，审计文档/代码的结构——什么东西放在哪里、职责划分对不对、加载时机是否合理
- 不覆盖: 内容质量（措辞、格式、完整性），那是内容审查的职责
- 失效条件: 对结构固定的文件（如标准化配置文件）不需要结构审计
## 测试案例
| 输入 | 应用 | 预期输出 | 实测结果 |
|------|------|----------|----------|
| iteration-engine SKILL.md (含模板，166行) | 审计结构：skill body vs reference | 识别出模板不应在 body 中，应拆到 references/ | 通过（已在 2026-05-29 执行）|
## 效果对比
| before | after | 是否改善 | 证据 |
|--------|-------|----------|------|
| 166行 body，含模板，每次加载浪费 context | 77行 body，模板在 references/，按需加载 | 改善 | log/2026-05-29-structural-review-blind-spot.md |
## 验收标准
- 每个组成部分的加载时机和理由明确
- 没有"不该加载的东西被加载"的情况
- 职责边界清晰，同层内容不重叠
## 使用说明
1. 列出目标产出物的所有组成部分（body、references、dependencies、data files）
2. 画出加载时机图：哪些在所有场景都加载，哪些按需加载
3. 对每个部分问：它在这里的理由是什么？换到其他层会怎样？
4. 标记出"不该加载但被加载了"和"该加载但没加载"的内容
5. 对不明确归属的内容：优先放 references/（按需加载），除非它是决策必需的（放 body）
## 盲区
- 不判断内容本身正确性
- 不判断结构拆分后各部分质量
- 过度拆分也可能导致碎片化——本技术不判断最优粒度
- **不检查 skill 间配对契约完整性**（skill A 声明与 B 配对，B 是否回链？）——这属于跨 skill 架构审计，需 reviewing-in-chaos 或专用配对契约检查覆盖
## 来源
user, log/2026-05-29-structural-review-blind-spot.md §1
## 生效记录
| 日期 | 项目 | 通过? | 失败根因 | 备注 |
|------|------|------|------|
| 2026-05-29 | iteration-engine | 通过 | 模板拆到 references/，body 从 166→77 行 |
| 2026-06-01 | evaluating-in-chaos | 通过 | body 77 行精简,核心/参考分离清晰,events/ 迭代记录与测试偏离不混用,无冗余加载 |
| 2026-06-01 | evaluating-in-chaos v0.6 | 通过 | | reviewing 外部审计 → 7 项抛光层修复 |
| 2026-06-01 | evaluating-in-chaos v0.6.1 | 通过 | | 二次验收暴露 checklist 行号过时 → 6 项行号引用更新 + events 补齐 + 盲区扩展 (配对契约) |
