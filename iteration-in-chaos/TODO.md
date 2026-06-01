# iteration-in-chaos 问题追踪

> 状态: 持续收敛中。每项修复在 events/ 下有独立记录。

## 已修复 ✅

- [x] **P0 C1-1** 去掉 `SKILL.md:12` "任何状态都是合法入口点" — 改为入口级/内部级两级分类
- [x] **P0 C1-2** 标注每个状态为入口级/内部级 — `SKILL.md:25-27`
- [x] **P0 C1-3** 内部级 fallback 指令 — `SKILL.md:28` "若从内部级状态误入，回到 new-task 重载管线再进入"
- [x] **P1 C2-1** 职责边界行消歧 — `SKILL.md:8` 改为三步闭环表述
- [x] **P2 C3-1** 新增 tech-rejected 状态 — `SKILL.md:22`
- [x] **P2 C3-2** Quick Routing 加入 rejection 入口 — `SKILL.md:50` "有哪些技术被 reject 了"
- [x] **P3 I4-1** 定义 "→ 结束" 语义 — `SKILL.md:27` "回到空闲状态"
- [x] **P4 I2-1** 路由 "看一下当前管线" — `SKILL.md:46`
- [x] **P4 I2-2** 路由 "有哪些反馈还没整理" — `SKILL.md:47`
- [x] **P4 I2-3** 路由 "评估 X" — `SKILL.md:48`
- [x] **P5 M2-1** tech-failed action 拆为三步 — `SKILL.md:21`
- [x] **P6 M3-1** applying-tech 进度追踪 — `SKILL.md:20` "执行第 i/N 项技术"
- [x] **P7 I3-1** crystallized_to resolved 格式 — `references/log-template.md`
- [x] **P8 M8-1** preference-template tech 名同步 — `references/preference-template.md`
- [x] **P8 M8-2** preference-template 管线占位符替换 — `references/preference-template.md` ✅ (2026-06-01 双线验收迭代) 
  
  证据: `todo-done-summary.md` + `events/P0-P8` 系列 6 个 event 文件 + `log/2026-06-01-dual-eval-reviewing.md`

## 已修复 ✅ (2026-06-01 lazy-in-chaos Round 3 互驱)

- [x] **🟠 D2-1** `log/_proposals/` 目录未预创建 — 已创建 + `.gitkeep`
- [x] **🟠 D2-2** 多维度管线并存时 `current_step` 断点续跑逻辑未定义 — `SKILL.md:21` new-task ③ 加多管线优先级顺序 (维度定义表从上到下) + 单管线 current_step 逻辑
- [x] **🟠 D3-1** crystallizing → new-task 链路中 draft tech 验证闭环断裂 — `SKILL.md:24` crystallizing action 改为"结晶完成立即实测 → pass→active→编入管线"，new-task ④ 保留为安全网扫 orphaned draft
- [x] **🟠 D3-2** 管线 `current_step` 标记格式无定义 — `references/preference-template.md` 新增"运行时字段 current_step"节，定义写入/读取/清除格式
  
  证据: lazy-in-chaos Round 3 审计 (A=reviewing-in-chaos)

## 待修复

(无待修复项)

## 已知 backlog

- [ ] `todo-done-summary.md` 与 TODO.md 信息重复 — 可合并或删除
