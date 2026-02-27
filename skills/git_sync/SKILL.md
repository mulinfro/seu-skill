# Skill: git_sync

## Goal
同步架构文档、清理执行痕迹，并生成规范化提交记录。

## Hard Rules
- 先做文档同步，再做提交建议。
- 若存在 `current_plan.md`，必须先归档到 `logs/` 再删除原文件。
- 自动提交前必须获得用户明确同意。

## Input
- 本次需求与最终实现
- 变更文件列表（`git status`）
- 项目根目录架构记忆文件（如 `agent.md`, `gemini.md`）

## Workflow
1. 读取本次核心改动并提炼架构变化。
2. 同步记忆文档：优先更新 `agent.md` / `gemini.md`，若都不存在则创建 `agent.md`。
3. 归档 `current_plan.md` 到 `logs/current_plan_<timestamp>.md` 并删除原文件。
4. 总结“原始需求 vs 最终实现”的偏差。
5. 生成 Angular 风格 commit message。
6. 询问是否执行 `git add . && git commit`。

## Commit Format
- 标题：`type(scope): summary`
- 正文：
  - 关键改动点
  - 风险与兼容性说明
  - 关联需求

## Output Template
```md
## 文档同步
- 更新: agent.md（是/否）
- 更新: gemini.md（是/否）
- 创建: agent.md（是/否）

## 计划清理
- current_plan.md: 已归档并删除/不存在
- 归档文件: logs/current_plan_<timestamp>.md（若有）

## 需求偏差总结
- 用户原始目标: ...
- 最终实现: ...
- 偏差说明: ...

## 建议 Commit Message
feat(scope): ...

- ...
- ...

关联需求: ...

请确认是否现在执行 git 提交。
```

## Done Criteria
- 文档同步状态清晰。
- 若无记忆文档，已创建 `agent.md` 并写入本次变更摘要。
- 生成可直接使用的 commit message。
- 已询问用户是否自动提交。
