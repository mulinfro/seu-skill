# AGENTS

本仓库采用 Skills 驱动的标准开发流程。默认按以下顺序执行：

1. `dev_plan`
2. `plan_review`
3. `batch_execute`
4. `code_refactor`
5. `git_sync`

## Skill Discovery

- Skills 根目录：`skills/`
- 每个技能入口：`skills/<skill_name>/SKILL.md`
- 共享模板：`skills/_templates/current_plan.md`

## Trigger Rules

- 当用户输入包含以下关键词时，必须触发对应技能：
  - `dev_plan`：规划、计划、先别写代码、先分析
  - `plan_review`：review plan、挑刺、补全方案、优化计划
  - `batch_execute`：批量实现、按计划执行、继续上次执行
  - `code_refactor`：重构、清理坏味道、代码净化
  - `git_sync`：提交、同步文档、生成 commit
- 若用户未指定技能，默认从 `dev_plan` 开始。
- 若用户明确说“跳过规划直接改”，也必须先给最小计划并确认后再执行。

## Workflow Contract

### 1) dev_plan
- 只输出分析与计划，禁止代码。
- 输出必须含：范围边界、分步计划、技术建议、文件清单、验证回滚。
- 结尾固定：`请问是否同意按此计划执行？`

### 2) plan_review
- 必须对 `dev_plan` 进行缺陷审查与顺序审查。
- 输出必须含：修改说明、最终版计划、1-3 条 Bonus 建议。

### 3) batch_execute
- 开始前必须创建/更新 `current_plan.md`。
- 每完成一步都要将 `[ ]` 更新为 `[x]` 并写执行日志。
- 若中断，优先读取 `current_plan.md` 并从首个未完成步骤恢复。
- 收尾必须清理临时产物（如 `__pycache__`）并记录清理结果。

### 4) code_refactor
- 先列出 Code Smells，再执行重构。
- 清理死代码/重复逻辑/冗余注释，保持行为一致。
- 输出必须包含“重构前问题 vs 重构后收益”。

### 5) git_sync
- 先同步架构记忆文档（如 `agent.md`, `gemini.md`，存在则更新；都不存在时创建 `agent.md`）。
- 将 `current_plan.md` 归档到 `logs/` 后再删除原文件。
- 生成 Angular 风格 commit message。
- 自动执行 `git add`/`git commit` 前必须获得用户确认。

## Default Quality Bar

- 前端：复用、状态清晰、Loading/Empty/Error 完整、响应式可用。
- 后端：接口规范、输入校验、异常处理、性能与查询效率。
- 通用：可验证（测试/构建/检查）、可回滚、变更可追踪。

## Operational Notes

- 优先小步提交，避免大批量无验证改动。
- 输出以 Markdown 为主，避免冗余叙述。
- 修改完成后，报告实际变更文件和验证结果。
