# iteration-in-chaos

把反复出现的反馈模式转化为可复用的迭代技术，让 agent 不是每次从零开始修东西。

## 定位

in-chaos 生态里的"迭代引擎"——不审核架构（→ reviewing-in-chaos），不评测产出（→ evaluating-in-chaos），只管一件事：**从反馈中提取可复用的技术，编入管线，验证效果，闭环**。

和另外三个 skill 的关系：
- **reviewing-in-chaos** 审出来的缺陷 → iteration 转化为可复用的检查方法
- **evaluating-in-chaos** 测出来的问题 → iteration 转化为修复流程
- **lazy-in-chaos** 是一次性跑三者的编排层，iteration 是持续积累的技术库

## 核心概念

### 用户反馈
用户在迭代过程中给的纠正、原则声明、方向调整。一句话也算，累积成模式也算。关键判据：**反馈里能提取出可复用的原则**。

### 迭代对象
当前正在迭代的目标——可以是一个 skill、一个系统组件、或一组关联文件。同一个迭代会话内，迭代对象固定。

### 技术 (tech)
从反馈中提取的**可复用方案**，落盘为 `techs/{name}.md`。一个技术包含三个要素：边界（覆盖/不覆盖）、测试案例（怎么验证）、效果对比（用了之后改了什么）。三类技术：检查方法、执行流程、设计约束。

### 偏好 (preference)
用户在**多个可用技术中做编排选择**——什么维度用什么技术、什么顺序。存为 `preferences/{dimension}.md`，必须指向日志证据。

### 管线 (pipeline)
偏好里的技术执行序列，带 `current_step` 标记支持断点续跑。一条管线是一组有序的技术。

## 文档地图

| 读者 | 读什么 | 用途 |
|------|--------|------|
| **agent（执行时）** | `SKILL.md` | 状态机、路由、规则——可执行指令 |
| **人类（了解/开发）** | `README.md`（本文件） | 背景、概念、文件结构 |
| **人类（写日志）** | `references/log-template.md` | 日志格式 |
| **人类（写技术）** | `references/tech-template.md` | 技术文件格式 |
| **人类（写偏好）** | `references/preference-template.md` | 偏好文件格式 |

```text
iteration-in-chaos/
  README.md              ← 你在看的：背景 + 概念 + 文档导航（给人看）
  SKILL.md               ← agent 加载的可执行指令
  techs/                 ← 可复用迭代方案
    index.md
    *.md
  preferences/           ← 技术管线编排
    index.md
    *.md
  log/                   ← 反馈事件 + 提取原则
    _proposals/          ← 待确认的结晶提案
    *.md
  archive/               ← 废弃技术/偏好
  references/            ← 模板文件
    log-template.md
    tech-template.md
    preference-template.md
  events/                ← 运行事件记录（dogfooding偏离等）
  TODO.md                ← 问题追踪
```

## 状态机概览

8 个状态，分两级：

**入口级**（可直接从用户指令进入）：new-task、feedback-received、accumulated、revalidate-preference

**内部级**（需要前置状态）：crystallizing、applying-tech、tech-failed、tech-rejected

主环：反馈 → 记日志 → 浮现结晶 → 生成技术 → 入管线 → 验证 → 闭环。详见 `SKILL.md`。
