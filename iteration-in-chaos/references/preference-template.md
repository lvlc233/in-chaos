# Preference 文件格式

## 偏好文件 `preferences/{dimension}.md`

```markdown
# 维度名
## 管线
1. [state-machine-check] → 2. [responsibility-boundary-check]
## 理由
## 适用上下文
## 证据
- log/xxx.md §1
## 生效记录
| 日期 | 项目 | 结果 | 调整 |
```

偏好指回日志证据。管线中只允许 active 技术。

### 运行时字段 `current_step`

`current_step` 是 applying-tech 状态写入管线文件底部的纯文本行，用于跨 session 断点续跑。不写进管线模板（运行时不创建该行）。

- **写入**: applying-tech 在执行第 N 项技术前，在管线文件底部追加 `current_step: N`
- **读取**: new-task 状态读管线文件时，若底部存在该行且值不是 `done`，从第 N 项续跑
- **清除**: 管线全部完成时，将 `current_step: N` 改为 `current_step: done`
- **格式**: 必须是文件最后一行，格式为 `current_step: N`（N 为正整数）或 `current_step: done`

## 偏好索引 `preferences/index.md`

```markdown
| dimension | 管线 | 适用上下文 |
|-----------|------|-----------|
| skill-design | state-machine-check → responsibility-boundary-check | 编写 skill 时 |
| (其他维度) | 管线由实际存在的 techs 构成 | |
```

匹配规则：当前任务涉及哪个 dimension，就加载对应管线。一个任务可匹配多个 dimension。
