# Worked Example:git-sync 架构审视(短链路工具型)

> reviewing-skills 第二个范例,与 video-remix(长链路)对照。
> **这次审视本身催生了维度 8**(见 CHANGELOG v0.2)——一个 skill 的招牌功能命令语义错了,
> 前 7 维(全审信息架构)一格都接不住。
> 日期 2026-05-29。

## 归类

**短链路工具型**(check→pull / clone→list→move,2–4 步闭环,近乎无状态)。
→ 主战场是**维度 8(执行层正确性)**,不是维度 3。审前先归类,避免对短链路硬套 🔴。

## 体量

SKILL.md 193 行(健康区间)+ `references/examples.md` 108 + 10 个 `scripts/*.sh`(488)+ evals。
无 vendor 拖累、无横幅图。体量与下沉得当 ✅。

## 8 维结论(精要)

| 维 | 结论 |
|---|---|
| 1 体量 | ✅(轻微:正文"触发条件"9 条与 description 重复,⚪) |
| 2 职责 | ✅ **范本**:显式「不做什么」边界(`SKILL.md:26-30` 不做 conflict/分支/push/stash) |
| 3 状态 | 🟡 **降级**:短链路无需跨压缩携带状态;唯一脆弱点 = clone 临时目录路径口头跨步(`clone-to-temp.sh:16`→`move-from-temp.sh:18`,但可从路径自恢复) |
| 4 控制流 | 🟠:无任何 flowchart/状态机,全散文(`SKILL.md:58-156`),"顺序不能颠倒"(`:71`)埋散文 → **反向翻车(该有却没有)** |
| 5 强制力 | 🟠:hard/soft 混排,两条硬规则语义打架(`:81` 软化 `:77-79`),防误操作叮嘱散 3+ 处无红旗区 |
| 6 下游/组合 | 🟡:重写同仓 `git-clone-with-credentials` 的凭证内嵌逻辑(`clone-to-temp.sh:55`)未 cross-ref;多身份污染机风险无提示 |
| 7 description | 🟡:后半"支持 X、Y、Z"混入能力清单(`SKILL.md:3`) |
| 8 执行层 | 🔴:**招牌功能 `git pull origin test -- <subdir>` 不做部分拉取**(经 `git pull -h` 核对无 pathspec 语法;普通仓 pull 永远整树更新)`pull-subdir.sh:21`、`pull-multiple-subdirs.sh:43`;另 `grep -oP` 解析 JSON 在 mac BSD grep 静默失败 `clone-to-temp.sh:36` 🟠 |

## 一句话根因

> 体量与职责边界都健康的短链路工具 skill;病灶**不在"对抗压缩"**,而在 ① 核心 git 命令语义用错
> (招牌功能原理不成立)② 控制流/强制力全靠散文 + 重复造轮子。**架构组织尚可,功能地基有洞。**

## 它做对的(避免一边倒)

职责边界声明范本(比 video-remix 还干脆)、体量下沉得当、认证 retry 三段降级成熟、
空触发先说明后询问、脚本错误码规范(`SUCCESS:`/`ERROR:` 前缀便于上游解析)。

## 改进方向

1. **(🔴 最优先)修招牌功能**:改 `git sparse-checkout set <dir>` + `git pull` 实现真部分检出,
   或坦诚降级为"整仓 pull + 只**报告**子目录变更"。
2.(🟠)加决策骨架图(`is_repo?→pull/clone`、`选 A/B`、`凭证 retry`)。
3.(🟠)强制力分层 + 解决 `:81` 软化 `:77-79` 的规则打架。
4.(🟡)cross-reference 同仓 `git-clone-with-credentials`,补多身份污染机提示。
5.(🟡)集中红旗区。 6.(⚪)`grep -oP` → `jq`。 7.(⚪)description 去 "what"。

## 方法论心得(已回填进 rubric v0.2)

- **工具型 skill 的致命点常在执行层命令语义,不在信息架构** → 催生维度 8。
- **审前先归类**:短链路工具型对维度 3 钝感,别硬套 🔴。
- **维度 4 双向翻车**:video-remix 塞太多 / git-sync 全散文,同一维两端都翻。
- **"未复用现成 skill"比"vendor 拷多了"更隐蔽**——得主动扫同目录其他 skill 才发现。
