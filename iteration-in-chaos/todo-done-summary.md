# iteration-in-chaos 修复总结

## 根因 A: 状态机语义不完整

**SKILL.md** — 状态表结构修复:
- 入口点声明 (C1): 去掉"任何状态都是合法入口点"，改为入口级/内部级两级分类，4 个入口级 + 4 个内部级明确标注
- 新增 tech-rejected 状态 (C3): 技术在实测中稳定不出正效果/反优化 → 归档 & 从管线移除，补全了 tech template 三条路径 (active/draft/rejected) 在状态机中的对应
- tech-failed transition 扩展 (C3): 从单一 → applying-tech 扩展为 → applying-tech / → tech-rejected
- 结束态语义定义 (I4): "→ 结束" 明确定义为"回到空闲状态，等待下次触发"

**SKILL.md** — Quick Routing 补全 (I2):
- 新增 3 条路由: "看一下当前管线"、"有哪些反馈还没整理"、"评估一下 X"
- 路由从 7 行增至 10 行

**SKILL.md** — applying-tech 进度追踪 (M3):
- 触发条件加入 pipeline index: "管线中执行第 i/N 项技术"，防止上下文压缩后丢失位置

## 根因 B: 文档声明与现实不一致

**SKILL.md:8** — 职责边界行消歧 (C2):
- 从"审核/评测是本 skill 流程中的独立阶段"改为"识别问题 → 匹配技术去修 → 验证修复效果"三步闭环表述，与 techs/logs 的实际描述不再矛盾

**references/log-template.md** — crystallized_to 格式补全 (I3):
- 新增 resolved 阶段的格式示例（单条和多条两种），从"只示范 pending"补充为"pending 和 resolved 都有格式"，与 meta-iteration 日志对齐

**references/preference-template.md** — 示例同步 (M1/M4):
- 示例 tech 名从 decision-framework-check 换为实际存在的 responsibility-boundary-check
- 删除不存在的 api-error-classification 维度示例

## 根因 C: action 粒度不足

**SKILL.md** — tech-failed action 拆分 (M2):
- 从合并描述改为三步: ①分析根因（技术本身不行 vs 编排问题）②修改对应文件 ③重试
- 诊断和修改分步执行，agent 不会混淆诊断与修复

## 未修复项

- **C1-3**: 3 个内部级状态 (applying-tech / tech-failed / crystallizing) 未添加"缺少前置状态上下文时，先回到 new-task 重载"的 fallback 指令。当前仅标注了"入口级/内部级"分类，但内部级缺乏从错误入口点恢复的明确指引。
- **C3-2**: Quick Routing 未加入 tech-rejected 相关入口路由；缺少"这个技术废掉了吗"或"有哪些被 reject 的技术"等用户常见查询的快速路由。
- **M8-2**: preference-template 中的样例管线 `api-error-classification → structured-error-logging` 声称已删除但当前文件中仍存在；管线占位符 `[技术A] → [技术B]` 未替换为实际存在的管线示例。

## 变更文件清单

- `SKILL.md` — 状态表 (入口点分类、tech-rejected 状态、tech-failed transition 扩展、结束态定义、applying-tech 进度追踪)、职责边界行、Quick Routing、tech-failed action 拆分
- `references/log-template.md` — crystallized_to resolved 格式示例
- `references/preference-template.md` — tech 名示例同步、删除虚构维度示例
