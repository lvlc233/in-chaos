# event: 自举一致性首跑 (v0.3 checklist 实测)
## 触发
C1 修复后首次运行 `self-consistency-checklist.md` 13 项自查
## 结果: 11/13 ✅, 2 ⚠️
- ✅ 1 先有标准后测 / 3 记偏离不限L2 / 4 多次跑抗随机 / 5 最小上下文 / 6 裁判分层 / 7 L3a客观对标 / 8 L3b rubric / 9 禁止无锚点判断 / 10 方差大标人类裁决 / 11 单一源头 / 12 版本一致
- ⚠️ #2: checklist 设计缺陷——假设 events/ = 测试偏离记录，但 events/ 实际用途是迭代事件。偏离格式定义在 methodology.md:80-88，但 events/ 不存放测试偏离
- ⚠️ #13: 本次发现 (#2 设计缺陷) 尚未回填 methodology.md
## 偏离
```json
{"test":"自举一致性首跑","layer":"自举","verdict":"partial",
 "expected":"13 项全 ✅","actual":"#2 ⚠️ (events/ 用途错配), #13 ⚠️ (回填待执行)",
 "deviation":{"sign":"中性","where":"checklist 自身设计","input":"events/ 目录当前存放迭代事件","output":"checklist #2 假设 events/ = 测试偏离记录",
   "why":"归因: checklist 设计时未区分 events/(迭代事件) vs 测试偏离记录"}}
```
## 待办
- [ ] checklist #2 改措辞，区分 events/ 与测试偏离记录
- [ ] 暴露二阶自举问题: checklist 自己也需要被自举
