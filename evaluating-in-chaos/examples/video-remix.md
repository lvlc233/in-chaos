# Worked Example:video-remix 三层测试体系

> evaluating-in-chaos 的第一个实例(本 skill 正是从它提炼)。
> 完整文件在 `video-remix/evals/`(`TEST_PLAN.md` / `state-tests.md` / `quality-rubric.md` / `evals.json`)。

## 归类

- **状态流**:S3 理解 ref → S4 检索 → S5 初筛 → S6 视觉验证 → S7 编排 → S8 出片 → S9 质检(带**诊断回退环**)→ **要 L2**。
- **内容产出**:混剪视频 → **要 L3**。
- → 三层全做。

## L1(`evals.json`,8 用例)

golden-path / tune / schema-invalid(旧)+ 5 反馈环新用例(诊断回退 / FC 黑盒不回退 / 预算收敛 / 抗幸存者偏差 / 落盘)。skill-creator 跑 `with/without` + grader,多次取方差。

## L2(`state-tests.md`)

状态契约表(S3-S9 每状态的入口/输入/产出+检查/出口)+ **M1-M5 mock 单状态测**(质量评分分开打 / 诊断回退跳对阶段 / FC 黑盒不回退 / 预算收敛 / 落盘抗压缩)+ 偏离记录格式。

## L3(`quality-rubric.md`)

- **L3a 对标 ref**:色调 / 内容域 / 节奏 / 主体,带证据帧。
- **L3b 艺考 rubric**:构图 / 色彩协调 / 剪辑流畅 / 完成度 / 情绪传达,1-5 + 评分锚点;多 agent 投票方差 + 人类校准 + 诚实声明。

## 这个实例教会方法论的(已回填进 methodology / rubric)

- **mock 单状态测要给"钉在单状态"的 prompt 模板**——否则 agent 会从头重跑整个流程。
- **L3 也要记偏离**(不能只 L2 记)——否则方法论"自举双标"(要求别人记偏离,自己 L3 没记)。
- **裁判分层**:L1-S9(skill 内自检)/ L2-S9(测 S9 判得准不准)/ L3a(终检第三方)别对同一个"色调偏"重复打分。
- 这套体系**自己被 reviewing-skills 复审过**,抓出并修了上述自举双标 —— 印证"方法论型 skill 必须无双标"。

## 一条真实偏离记录长什么样(照抄模板)

来自 L1-flow eval 1 实跑(本地近似):
```json
{"test":"eval1-golden", "layer":"L1", "verdict":"partial",
 "expected":"Agentic RAG: 用 vision 工具看 ref → 构造真 query",
 "actual":"行为意图有(看 ref→关键词 query),但 Step 3 没给具体看视频工具",
 "deviation":{"sign":"负向","where":"被测 SKILL.md Step 3","input":"ref_video_url",
   "output":"计划里'用环境里能看视频的方式',无工具名",
   "why":"归因=skill 没写清(runtime 无本地 ffmpeg,却没指明 vision-model-client / FC slice)"}}
```
> 这就是「记偏离」的样子:不是 pass/fail,而是 expected vs actual + 可定位(where/input/output)+ 归因。

