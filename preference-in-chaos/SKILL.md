---
name: preference-in-chaos
description: Use when the user wants to record, view, or modify personal preferences — 记下偏好、看看偏好、我的习惯、我倾向于、偏好、preference. Triggers 记一下、我的偏好、我习惯、我倾向于、偏好是什么、改一下偏好、记录偏好.
---

# preference-in-chaos

记录个人做任何事情的喜好。数据在 `resource-package/`（git submodule → 独立私有仓库）。

## 路由

用户输入 → agent 自动归类到一个维度目录，不确定归哪则问用户。

| 维度 | 目录 | 管什么 |
|---|---|---|
| tech | `tech/` | 代码风格、工具选择、命名习惯、架构偏好 |
| work | `work/` | 会议节奏、文档习惯、排期方式、沟通偏好 |
| life | `life/` | 作息、饮食、购物、生活工具 |
| aesthetics | `aesthetics/` | 颜色、布局、风格、审美倾向 |

维度目录可随时扩充——用到新维度时新建目录即可。

## 记偏好（写入）

1. agent 识别维度，确定 `resource-package/{维度}/` 目录
2. 建文件 `resource-package/{维度}/{slug}.md`，内容模板：

```markdown
# {slug}

- **维度**: {dimension}
- **偏好**: {用户原话}
- **场景**: {触发时的上下文}
- **记录时间**: {timestamp}
```

3. 追加一行到 `resource-package/{维度}/index.md`：
   ```markdown
   - [{slug}](./{slug}.md) — {一句话概括}
   ```
4. 告知用户「已记到 {维度}/ 下」

## 查偏好（读取）

| 用户说 | 动作 |
|---|---|
| 我有什么偏好 / 看看偏好 | 扫所有 index.md，列总览 |
| 看看{维度}偏好 | 读对应 `{维度}/index.md` |
| 我关于 X 的偏好是什么 | grep 所有维度搜关键词 |

## 改偏好 / 删偏好

直接编辑对应 markdown 文件，更新时同步改 index.md 中的摘要行。

## 快捷命令

| 用户说 | 对应动作 |
|---|---|
| 记一下 / 记下偏好 / preference | → 写入新偏好 |
| 看看偏好 / 我的偏好 | → 查所有偏好 |
| 看看{维度}偏好 | → 查特定维度 |
| 有没有关于 X 的偏好 | → grep 搜索 |
| 改那个偏好 / 删那个偏好 | → 编辑或删除 |
