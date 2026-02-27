# 开发 Skills 在 Codex/Gemini CLI 的安装与使用说明（项目版）

本文档针对本仓库已生成的技能体系：
- `skills/dev_plan`
- `skills/plan_review`
- `skills/batch_execute`
- `skills/code_refactor`
- `skills/git_sync`
- 统一规则入口：`AGENTS.md`

## 1. 先说结论

这套 Skills 已经是“项目内置版”，最稳妥的使用方式是：
1. 在仓库根目录启动 CLI。
2. 先让模型读取 `AGENTS.md` 与 `skills/README.md`。
3. 按 5 步流程执行，不需要额外插件开发。

## 2. 准备工作

确保你已安装 CLI（安装方法见：`docs/codex_gemini_cli_install_usage.md`）。

在仓库根目录确认文件存在：

```bash
ls AGENTS.md skills/README.md
```

### 2.1 一键安装到 Codex 全局技能目录（可选）

仓库已提供脚本：

```bash
./scripts/install_skills.sh
```

脚本行为：
- 安装目标：`~/.codex/skills/seu-dev-flow`
- 若已存在旧版本，会先自动备份为 `seu-dev-flow.bak_<timestamp>`
- 安装后会打印已复制文件清单

安装后可快速验证：

```bash
find ~/.codex/skills/seu-dev-flow -maxdepth 3 -type f | sort
```

## 3. Codex CLI 用法

### 3.1 项目内直接使用（推荐）

```bash
cd /你的项目路径/seu-skill
codex
```

进入会话后先输入：

```text
请先读取 AGENTS.md 和 skills/README.md，然后严格按 dev_plan -> plan_review -> batch_execute -> code_refactor -> git_sync 执行。现在先从 dev_plan 开始，不要写代码。
```

后续触发示例：

```text
执行 plan_review：请对刚才的计划挑刺并补全边界情况。
```

```text
执行 batch_execute：把最终计划写入 current_plan.md，然后逐步实现并每步打勾。
```

```text
执行 git_sync：先归档 current_plan.md 到 logs/，再生成 Angular 风格 commit message。
```

### 3.2 全局复用（可选，手动方式）

如果你希望在多个项目复用同一份技能，可把 `skills/` 复制到 `~/.codex/skills/`：

```bash
mkdir -p ~/.codex/skills/seu-dev-flow
cp -R skills/* ~/.codex/skills/seu-dev-flow/
```

说明：
- 项目级规则仍建议以当前仓库 `AGENTS.md` 为准。
- 全局技能适合放通用流程，项目差异放仓库内文档。

## 4. Gemini CLI 用法

Gemini CLI 建议采用同样的“项目内置文档驱动”方式。

### 4.1 项目内直接使用（推荐）

```bash
cd /你的项目路径/seu-skill
gemini
```

首条提示词建议：

```text
先完整读取 AGENTS.md 与 skills 目录下的 SKILL.md。后续严格按该流程执行。现在先执行 dev_plan，禁止输出代码，并以“请问是否同意按此计划执行？”结尾。
```

继续执行时，显式点名技能：

```text
现在执行 plan_review。
```

```text
现在执行 batch_execute，并维护 current_plan.md。
```

```text
现在执行 code_refactor。
```

```text
现在执行 git_sync。
```

## 5. 标准执行节奏（两端通用）

1. `dev_plan`：先规划，等待你确认。
2. `plan_review`：挑刺补全，形成最终计划。
3. `batch_execute`：写 `current_plan.md`，逐步实现与打勾。
4. `code_refactor`：先审查坏味道，再重构。
5. `git_sync`：同步文档、归档计划、给 commit message。

## 6. 常见问题

### 6.1 模型跳过规划直接改代码

处理：在提示词里明确加一条硬约束：

```text
禁止跳过 dev_plan，未获得我确认前不得输出代码。
```

### 6.2 `current_plan.md` 没有持续更新

处理：在每次回复前加一句：

```text
先汇报 current_plan.md 当前进度，再继续下一步。
```

### 6.3 结束时忘了清理临时文件

处理：在 `batch_execute` 收尾追加：

```text
执行临时文件清理（如 __pycache__）并报告结果。
```

### 6.4 忘记归档计划文件

处理：在 `git_sync` 阶段强制检查：

```text
先把 current_plan.md 归档到 logs/current_plan_<timestamp>.md，再删除原文件。
```

## 7. 推荐的最小命令模板

适合你日常直接复制：

```text
读取 AGENTS.md + skills/*/SKILL.md，严格按 5 步流程执行。
当前阶段：dev_plan。
约束：未确认前禁止写代码；必须输出文件修改清单与验证方案。
```
