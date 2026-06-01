## trigger: 用户要求迭代 iteration-engine skill 本身
## context: 已积累 3 条 pending 日志（state-driven-execution, structural-review-blind-spot, identity-is-iteration-schemes），需要结晶 + 重写 SKILL.md
## method: 对话 + 文件操作（结晶 techs + 重写 skill body）
## what_changed: 
- 结晶 3 条日志为 techs/: state-machine-check, structure-audit, responsibility-boundary-check
- 创建 skill-design 偏好管线: state-machine-check → responsibility-boundary-check
- SKILL.md 从线性叙事（架构→检测→日志→结晶→应用→元迭代）重写为状态机结构（7 状态表 + 核心规则 + 快速路由）
- 更新所有日志的 crystallized_to 和索引

## extracted_principles:
### 1. 结晶驱动重构
  证据: 先结晶 3 条日志为 techs，techs 的内容直接指导 SKILL.md 的重写方向（状态机是核心结构、techs/ 是核心产出、职责边界清晰）
  原则: 结晶和重构不应分先后——结晶出来的技术应立刻应用到迭代对象上，形成验证闭环
### 2. 状态机是编辑过滤器
  证据: 用状态机结构重写 SKILL.md 后，原本 166 行的线性叙事被压缩为 ~90 行的状态表+规则。写不进状态表的内容（如详细的日志格式、模板字段说明）自动被识别为应放入 references/
  原则: 状态机不只是组织结构——把内容放进状态表的过程本身就暴露了哪些内容有执行价值、哪些只是参考说明
### 3. meta-iteration 是最诚实的测试
  证据: 用 iteration-engine 自己的流程（日志→结晶→重写→自检）来迭代 iteration-engine，暴露了两个问题：(a) tech 的验证门（边界/测试/效果对比）在 draft 阶段只能部分填写，实测才能完整；(b) preferences 从日志到管线的映射需要更多生效记录来验证管线顺序是否合理
  原则: 对自己用自己——如果自己的流程在自己的场景下走不通，说明流程需要调整
## tags: meta-iteration, skill-design, state-machine, crystallization, dogfooding
## crystallized_to:
- techs/state-machine-check.md (盲区新增"编辑过滤器"使用说明)
- SKILL.md 规则3, 规则4
