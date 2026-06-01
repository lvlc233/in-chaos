# Preference 文件格式

## 偏好文件 `preferences/{dimension}.md`

```markdown
# 维度名
## 管线
1. [技术A] → 2. [技术B]
## 理由
## 适用上下文
## 证据
- log/xxx.md §1
## 生效记录
| 日期 | 项目 | 结果 | 调整 |
```

偏好指回日志证据。管线中只允许 active 技术。

## 偏好索引 `preferences/index.md`

```markdown
| dimension | 管线 | 适用上下文 |
|-----------|------|-----------|
| error-handling | api-error-classification → structured-error-logging | API 调用相关代码 |
| skill-design | state-machine-check → decision-framework-check | 编写 skill 时 |
```

匹配规则：当前任务涉及哪个 dimension，就加载对应管线。一个任务可匹配多个 dimension。
