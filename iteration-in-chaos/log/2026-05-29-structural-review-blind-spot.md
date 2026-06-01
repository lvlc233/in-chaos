## trigger: 用户指出多次 superpowers 审核都没发现结构问题
## context: iteration-engine skill 迭代过程中，用superpowers反复审核内容质量、GATE有效性、description精度，但始终没人从"什么应该在skill body里，什么应该是reference"这个结构层面去分析
## method: 对话（用户主动点出盲区）
## what_changed: 把模板从 SKILL.md 拆到 references/，skill body 从 166行降到 77行

## extracted_principles:
### 1. 审核要先看结构，再看内容
  证据: "用superpower检查那么多次，结果还是没有从根本上去分析结构本身的问题"
  原则: 迭代审核的第一步是结构审计（什么东西放在哪里、职责划分对不对），不是内容审计（措辞、格式、完整性）。结构错了，内容再好也是在错误的框架里打转。
### 2. 为什么结构优先
  证据: "从结构上审核迭代（为什么要在意结构呢？）"
  原则: 结构决定了信息的加载时机和成本。错误的结构 = 不该加载的东西被加载（浪费 context）、该加载的东西没被加载（功能缺失）。内容层的优化上限被结构层锁死。
## tags: structure-first, review-methodology, skill-design, context-efficiency
## crystallized_to: techs/structure-audit.md
