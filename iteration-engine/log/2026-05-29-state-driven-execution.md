## trigger: 用户对 skill 设计提出原则性要求
## context: 准备迭代修改 iteration-engine skill 时，用户补充设计原则
## method: 对话（原则陈述）
## what_changed: 尚未改，记录原则

## extracted_principles:
### 1. Skill 应该是状态驱动的，不是流程驱动的
  证据: "一个好的skill应该可以从某个状态直接推出，即给定一个状态，skill中符合了某个状态就可以执行某个状态的量"
  原则: skill 不应该是线性流程（step1→step2→step3），而应该是状态机——agent 识别当前处于什么状态，直接跳到对应的动作。任何状态都是合法的入口点，不需要从头走。这意味着 skill 的结构应该是"状态→动作"的映射表，而非"阶段→阶段"的管线叙事。
### 2. 状态决定执行量
  证据: "符合了某个状态就可以执行某个状态的量"
  原则: 每个状态自带明确的执行范围（做什么、做多少）。agent 不需要判断"现在该做哪一步"，只需要识别状态，状态本身就定义了要执行的动作集。减少 agent 的判断负担，降低跳步/漏步的风险。
## tags: state-machine, skill-design, execution-model, anti-linear-flow
## crystallized_to: techs/state-machine-check.md
