---
name: operator-knowledge
description: |
  Use when the user wants to store personal raw material, review notes for patterns,
  or internalize a concept without letting the LLM replace their thinking.
  Trigger words: 记一下, 存下来, 彻底理解, 帮我推导, 扫一下raw, 我想消化, 不想让AI代写.
  Keywords: knowledge management, concept internalization, note-taking, Socratic derivation, raw archive.
---

# Operator Knowledge

0.1.1-beta 知识发生辅助系统：capture（存原文）、distill（找候选）、derive（推理解）。

核心目标不是把笔记整理漂亮，而是让用户的计算发生，同时让 agent 承担读写、检索、对照这些杂务。

## When to Use

- 用户要保存、查找个人原文材料。
- 用户想从 raw/ 里看重复、矛盾或候选问题。
- 用户想理解、验证、更新一个概念，但不想让 AI 代写成"已掌握"。

## When NOT to Use

- 用户只要查 API、命令、事实资料。
- 用户要快速整理外部资料成百科或团队文档。
- 用户明确只想聊天，不想归档、筛选或推导。

## Common Mistakes

| 错误 | 正确做法 |
|------|---------|
| 把 raw/ 当可维护笔记 | raw/ 冻结，维护信息写 overlays/ |
| 让 agent 替用户判断什么最重要 | agent 给候选，用户选 |
| 把半成品说成已掌握 | 标成 pending / draft，等待用户消化 |

## 架构

| Skill | 职责 | 入口条件 |
|-------|------|---------|
| [capture](skills/capture/SKILL.md) | 保存和检索原文；标签、状态、删除都走外部覆盖层 | 用户想存东西或找东西 |
| [distill](skills/distill/SKILL.md) | 扫 raw/ ↔ 对照 operators/，提出候选而不替用户决定 | 用户问"有什么值得看"或想扫 raw/ |
| [derive](skills/derive/SKILL.md) | 引导用户形成自己的知识算子；允许卡住、降档、暂停 | 用户想理解、练习、更新一个概念 |

## 数据流

```
raw/ (冻结原文) ──[distill]──→ 候选问题 ──[derive/apply]──→ operators/ (知识算子)
       │                                │                         │
       └──────── overlays/ 记录标签、状态、关联、删除、修改意图 ─────┘
```

## 不变量

- **原文冻结**：`raw/` 是证据层。写入后不修改、不追加元数据、不打状态；标签、删除、关联、修正意图都写到 `overlays/` 或索引文件。
- **计算归属**：agent 可以减负，但不能把自己的推导伪装成用户已经理解。
- **低负担交互**：面向用户少用术语、少用大表格、少问流程确认。只在知识所有权或原文归档会变化时停下。
- **自适应验证**：验证必须发生，但难度随用户状态调整；不要把"三场景跑通"当硬门槛。
- **可暂停**：用户累、卡住或开始绕远时，可以保存当前问题状态，不强行完成。

## 快速路由

| 用户说 | 加载 |
|--------|------|
| "记一下"、"存下来"、"找一下之前的" | [capture](skills/capture/SKILL.md) |
| "扫一下 raw"、"有什么值得看"、"对照一下" | [distill](skills/distill/SKILL.md) |
| "彻底理解"、"帮我推导"、"我有点卡"、"我累了先放着"、"我有个新理解" | [derive](skills/derive/SKILL.md) |

## 面向用户的语气

内部可以使用 `raw / overlays / distill / derive / operator`。对用户优先说：原文、旁边的记录、候选、你的理解、试一下能不能用。

避免把用户拖进系统术语。优先短句，例如："我先不改原文，只在旁边记标签。"

## 项目结构

```text
operator-knowledge/
  raw/                         # 原文，只写入一次
  overlays/
    raw-index.md               # 标题、来源、标签、状态
    raw-links.md               # raw 与知识算子的关联
    raw-changes.md             # 删除、修正、废弃等外部记录
  operators/
    index.md                   # 知识算子索引
    log.md                     # 推导和演化日志
```

| 路径 | 用途 |
|------|------|
| `raw/` | 冻结原文（日记、摘录、想法） |
| `overlays/` | 原文外部覆盖层：标签、状态、关联、删除、修改意图 |
| `operators/` | 知识算子（index.md + *.md） |
| `operators/log.md` | 推导日志 |
| `skills/capture/SKILL.md` | 素材管理 skill |
| `skills/distill/SKILL.md` | 概念筛选 skill |
| `skills/derive/SKILL.md` | 推导引擎 skill |
