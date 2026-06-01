## trigger: 用户主动澄清 skill 的核心定位
## context: 用 superpowers 审核 iteration-engine 时，用户补充说明重点
## method: 对话（用户强调方向）
## what_changed: 尚未改，记录方向

## extracted_principles:
### 1. iteration-engine 的核心是"迭代方案"本身，不是反馈记录机制
  证据: "重点其实是迭代的方案，就是要去迭代也就是迭代的方案，记录模式也是记录并整理可复用的迭代方案"
  原则: techs/ 才是这个 skill 的核心产出物——可复用的迭代方案。log/crystallize 管线是发现新方案的机制，不是目的本身。skill body 的重心应放在"怎么选方案、怎么执行方案、怎么验证方案有效"，而非"怎么记日志"。
### 2. 审核/评测职责归另一个 skill，iteration-engine 不负责审核
  证据: "我现在还有一个审核和评测的skill，到时可以联合使用"
  原则: iteration-engine 的边界是"提供和管理迭代方案"。发现问题（审核）和验证质量（评测）由另一个 skill 负责。两者联合使用时：审核 skill 发现问题 → iteration-engine 提供对应的迭代方案去修。职责分离，不重叠。
### 3. 记录是为了积累方案，不是为了记录本身
  证据: "记录模式也是记录并整理可复用的迭代方案"
  原则: log 的价值不在"记了多少条"，在"最终结晶出多少可复用的迭代方案"。如果 log 积累了但没结晶成 techs/，说明结晶阈值或流程有问题。
## tags: skill-identity, iteration-scheme, responsibility-boundary, review-separation
## crystallized_to: techs/responsibility-boundary-check.md
