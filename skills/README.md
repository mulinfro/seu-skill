# Agent Skills Pack

本目录将 `spec_detail.md` 的五步开发流程固化为可复用技能，采用统一的执行标准：

1. 先规划，再执行，禁止跳步。
2. 每个技能都有清晰输入、输出和完成条件。
3. 通过 `current_plan.md` 进行状态持久化，支持断点续作。

## Skills

- `dev_plan`：需求规划与约束
- `plan_review`：方案审视与补全
- `batch_execute`：稳健批量实施
- `code_refactor`：代码重构与净化
- `git_sync`：架构同步与 Git 管家

## Recommended Order

1. 运行 `dev_plan`
2. 运行 `plan_review`
3. 用户确认后运行 `batch_execute`
4. 完成主功能后运行 `code_refactor`
5. 最后运行 `git_sync`

## Shared Contract

- 所有技能默认以项目根目录作为工作目录。
- 输出内容优先 Markdown，便于复制到会话或文档。
- 除 `batch_execute` 外，技能不应直接进行大规模代码改动。
- 涉及 Git 提交时必须先征求用户确认。
- `batch_execute` 结束后应清理临时产物（如 `__pycache__`）。
- `git_sync` 对 `current_plan.md` 先归档到 `logs/`，再删除原文件。
