# event: P0 — C1 状态机入口点声明修复
## 日期: 2026-06-01
## 操作
- SKILL.md:12 去掉"任何状态都是合法入口点"，改为"入口级状态可直接从用户指令进入，内部级状态依赖前置状态传入上下文"
- 状态表下方新增入口级/内部级分类说明
- → 结束 语义定义：回到空闲，等待下次触发
- techs/state-machine-check.md 新增生效记录
## 结果: 通过
- 四个入口级 (new-task / feedback-received / accumulated / revalidate-preference) 和四个内部级明确标注
- 消除虚假宣传——不再声称不成立的"全部独立入口"
