# Worked Example:video-remix(单体版)架构审视

> 这是 reviewing-in-chaos 的第一个范例:一份合格的 skill 架构审视长什么样。
> 审视对象 = 分支 `feat/video-remix` 的**单体版** video-remix
> (kanban 扩展在另一分支,是后来为补救"缺陷 1"而生的)。
> 日期:2026-05-29。标尺:superpowers / writing-skills + video-use。

## 一句话根因

video-remix 把 video-use 请进门当"剪辑工具"(整个 vendor 进自己目录),却没继承它的立身之本
——**"永不信任记忆,一切落盘"**。最好的反例就躺在被审视对象自己的目录里,而 video-remix 恰恰丢掉了它最值钱的那层。

## 体量(先澄清:缺陷不在"字多")

video-remix 自写 ≈ 709 行(SKILL.md 171 + 4 references 538),SKILL.md 落在 superpowers 健康区间。
真正的体量黑洞是 vendor 进来的 `video-use/`:manim-video 子 skill 2700+ 行、`video-use-banner.png` **512 KB**、
`poster.html` / `install.md` / `LICENSE` 全被拷进 skill 目录。

→ **审视心得:体量要先量,且要把"自写"和"vendor 进来"的分开数,否则会错判病灶。**

## 6 项缺陷(按架构严重度)

| 维度 | 缺陷 | 证据 | 对照标尺 |
|---|---|---|---|
| 3 🔴 **1** | **长链路 + 状态只活在上下文 + 显式拒绝落盘 → 对上下文压缩零容错** | handoff:46「Brief 不落盘」、handoff:141「video-use 中间产物不读不动不依赖」、SKILL:27「信任 runtime 已拼好」、SKILL:158「截断/摘要不归我们管」 | video-use 用 project.md/edl.json/takes_packed.md 落盘,**启动先读** |
| 4 🟠 **2** | **控制流+执行细节糊在一个 ~120 行 ASCII 巨块**(SKILL:33-152) | 11 step×(输入/动作/输出/门/example)全塞一张图 | superpowers graphviz 只画决策骨架;writing-skills 反模式「Code in Flowcharts」 |
| 3/5 🟡 **3** | **重做/回退上限散落、数字不一**(2 轮/1 次/1 次/3 次,4 处) | SKILL:18,80,127 + callback:85 | video-use「Cap at 3 passes」一处集中 |
| 5 🟡 **4** | **防幻觉规则散落,无集中红旗区**(压缩时最先被摘 → 放大缺陷1) | SKILL:58,69,106 + handoff:83 | superpowers 每个纪律 skill 都有集中 Red Flags + 借口-现实表 |
| 6 🟡 **5** | **复用靠 vendor 整目录**(连 512KB banner、manim 2700 行、poster.html 一起拷) | handoff:6-16(helpers 改 wrapper 有理,拖家带口无理) | writing-skills 主张 cross-reference;反模式「维护负担」+ 双版本漂移 |
| 7 ⚪ **6** | description 混了 what+when(触发信号部分其实写得好) | SKILL:4 | CSO 铁律「Description=触发条件」 |

## 它做对的(避免一边倒)

- **CORRECTNESS/CRAFT 两层分离**(SKILL:17)= video-use 的 hard rules vs artistic freedom,学到位了。
- **契约单一源头**(prompt-contract:3「所有 schema 单一源头在本文件」)。
- **下游感知扎实**:handoff 讲清 vendor / wrapper / 端点白名单 / mapper 归属,brief 字段标"来自 Step X"。
- **兜底哲学成熟**(SKILL:111「素材差不是 failed 回调的理由」,防过度阻断)。

## 根因升华

> 流程做长(9 步)、状态留上下文、再亲手把落盘那层划成"不归我们管",于是健壮性完全依赖它控制不了的
> 运行时假设。其余缺陷(巨块流程图、散落的封顶与红旗)都是同一病灶并发症:
> **结构没有为"对抗上下文压缩"而设计。**

## 改进方向(6 条,对应 6 缺陷)

1. **落盘状态层(根治缺陷1)**:每阶段产物落成可重读产物,启动/续跑先读(kanban 已走此路,可上移为单体硬规则)。
2. **流程图瘦身(缺陷2)**:SKILL 主流程只留决策骨架,细节下沉 references。
3. **状态机集中(缺陷3)**:所有重试/重做封顶收进一张表,数字统一。
4. **加集中 Red Flags/反幻觉清单(缺陷4)**。
5. **vendor 瘦身(缺陷5)**:只留用到的 helpers + video-use/SKILL.md,删 manim/banner/poster;记同步策略。
6. **description 去 "what"(缺陷6)**。

---

## 从本次审视提炼进 rubric 的方法论心得

- **最好的反例可能就在被审对象自己的目录里**(video-use 被 vendor 进来)——审视时留意它"引用了什么/拷了什么",
  那些往往就是它本该学却没学的范式。
- **体量要拆开数**(自写 vs vendor),否则错判"臃肿"。
- **维度 3(状态落盘)用一句话试金**:"第 K 步压缩了,前面的还在吗?" 长链路答"不在"即 🔴。
- **缺陷常同源**:6 个缺陷里 2/3/4 都是"没为对抗压缩而设计"的并发症 → 根因升华能让报告从清单变成洞察。
