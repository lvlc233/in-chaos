# event: P2 — C3 tech-rejected 状态
## 日期: 2026-06-01
## 操作
- 状态表新增**tech-rejected**状态：触发条件"技术在实测中稳定不出正效果/反优化"，动作"归档到 archive/，从所有偏好管线中移除"，transition → accumulated 或 → new-task
- tech-failed 的 transition 从单一 → applying-tech 扩展为 → applying-tech / → tech-rejected
- tech-failed 的 action 拆为三步：①分析根因 ②修改文件 ③重试
- 至此 tech template 的三条路径 (active / draft / rejected) 在状态机里都有对应状态
## 结果: 通过
- rejected 路径从不可达变为可达
- 状态数 7→8
