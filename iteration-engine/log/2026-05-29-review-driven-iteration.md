## trigger: superpowers code review 发现 4 个 critical + 4 个 important + 若干 minor 问题
## context: 用 requesting-code-review 技能审查 iteration-engine，reviewer 发现了 self-consistency 问题（draft/active 不一致、orphaned state、dead-end transition）
## method: code review（外部审核 → 匹配迭代方案修复）
## what_changed:
- Critical #1,#4: 3 个 tech 从 draft 提升到 active，techs/index.md 同步更新
- Critical #2: 修复 transition graph——new-task → applying-tech，applying-tech 自循环处理管线多技术，tech-failed → applying-tech 重试
- Critical #3: revalidate-preference → accumulated（失效时）替代 → 结束
- Important #5: structure-audit 和 responsibility-boundary-check 补充 5 步使用说明
- Important #6: new-task 新增第⑤步 dogfooding 检查
- Important #7: 统一 crystallized_to 格式
- Minor: 创建 archive/ 目录，修复 log typo (supperpwoer → superpower)

## extracted_principles:
### 1. 审核是迭代引擎的输入源
  证据: superpowers code review 发现了状态机 transition graph 的 3 个问题——这些问题在自己走 skill-design 管线时没有被 state-machine-check 发现（因为该技术的盲区恰好是"不检查 transitions 闭环"）
  原则: 外部审核暴露的是当前技术体系的盲区——不是因为审核的人更聪明，而是因为外部视角天然不被现有技术覆盖。审核 → 暴露盲区 → 更新技术或创建新技术 → 形成闭环
### 2. 技术盲区需要对应技术的 overlap 来补
  证据: state-machine-check 盲区声明了"不检查 transitions 是否形成闭环"，但这个盲区恰好被 superpowers reviewer 覆盖了。盲区不是"审不了就算了"的免责声明，而是"这里需要一个配套技术来补"的 todo
  原则: 每个技术的盲区声明 = 对配套技术的需求规格。盲区不是缺陷，是接口——定义了另一个技术应该审什么
### 3. 架构诚实性
  证据: reviewer 指出"一个宣扬验证门的 skill 却跳过自己的验证门是架构上的不诚实"——draft techs 在 pipeline 里跑了 2 轮但从未被 promote
  原则: 一个 meta-skill（规定别人该怎么做的 skill）如果自己违规，比普通 skill 违规严重 10 倍——因为它在示范"规则可以被打破"。meta-skill 的合规性是 existence-proof：如果自己都做不到，凭什么要求别人做到
## tags: code-review, superpowers, transition-graph, blind-spot, architecture-honesty, meta-compliance
## crystallized_to: pending
