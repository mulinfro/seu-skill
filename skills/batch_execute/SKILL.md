# Skill: batch_execute

## Goal
将已确认的最终计划稳定落地为代码，支持断点续作，避免上下文丢失。

## Hard Rules
- 开始执行前必须创建或更新 `current_plan.md`。
- 每完成一步必须更新状态（`[ ]` -> `[x]`）并记录简短日志。
- 执行顺序严格按计划，不允许跳步。
- 收尾时必须清理临时产物（如 `__pycache__`、临时日志）。

## Input
- 已确认的最终计划
- 当前仓库代码

## Workflow
1. 初始化 `current_plan.md`（参考模板）。
2. 读取第一个未完成步骤。
3. 实施代码改动。
4. 自检：编译/测试/静态检查（可运行时尽量运行）。
5. 回写 `current_plan.md`：勾选完成项并记录结果。
6. 循环直至所有步骤完成。
7. 执行临时文件清理并记录清理结果。

## Resume Rules
- 若输出中断，下一次必须先读取 `current_plan.md`。
- 自动定位第一个 `[ ]` 项作为恢复点。
- 记录“上次完成到第 N 步，本次从第 N+1 步继续”。

## Logging Format
`current_plan.md` 每步至少记录：
- 状态（[ ]/[x]）
- 代码改动文件
- 自检结果
- 备注（可选）

## Cleanup Rules
- 推荐清理命令：`find . -type d -name '__pycache__' -prune -exec rm -rf {} +`
- 若项目有 `.gitignore`，应确认临时文件已被忽略或已删除。

## Output Template
```md
## 执行进度
- 已完成: X/Y
- 当前步骤: ...

## 本轮改动
- path/a: ...
- path/b: ...

## 自检结果
- 命令: ...
- 结果: ...

## 清理结果
- 命令: ...
- 结果: ...

## 下一步
- ...
```

## Done Criteria
- `current_plan.md` 所有步骤为 `[x]`。
- 至少完成一次可验证的自检。
