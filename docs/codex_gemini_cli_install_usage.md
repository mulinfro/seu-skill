# Codex CLI 与 Gemini CLI 安装与使用说明（2026-02-27）

本文档面向本地开发环境，给出两款 CLI 的最小可用安装、鉴权和日常使用方法。

## 1. 适用范围

- 系统：macOS / Linux（Windows 建议在 WSL 中使用）
- 网络：需要可访问各自官方服务
- 目标：10 分钟内跑通首条指令

## 2. Codex CLI

### 2.1 安装

优先使用 npm：

```bash
npm i -g @openai/codex
```

可选（Homebrew）：

```bash
brew install --cask codex
```

验证安装：

```bash
codex --version
```

升级：

```bash
npm i -g @openai/codex@latest
```

### 2.2 登录与鉴权

首次运行：

```bash
codex
```

按提示选择登录方式：
- ChatGPT 账号登录（推荐）
- API Key 登录（适合 API 计费/自动化场景）

### 2.3 最小可用示例

在项目根目录运行：

```bash
codex
```

会话中直接输入：

```text
请先阅读当前仓库结构，然后给出一个最小重构计划，不要改代码。
```

### 2.4 常用操作

- 启动交互式 TUI：`codex`
- 切换模型/推理档位：会话内使用 `/model`
- 在执行命令与改文件前，根据提示确认 approval mode

### 2.5 平台注意事项

- Codex CLI 官方可用平台为 macOS/Linux。
- Windows 为实验支持，建议在 WSL 中使用。

## 3. Gemini CLI

### 3.1 前置条件

- Node.js 20+

检查版本：

```bash
node -v
npm -v
```

### 3.2 安装

零安装试跑（推荐先验证）：

```bash
npx @google/gemini-cli
```

全局安装：

```bash
npm install -g @google/gemini-cli
```

可选（macOS/Linux）：

```bash
brew install gemini-cli
```

验证安装：

```bash
gemini --version
```

### 3.3 登录与鉴权

方式 A：Google OAuth（推荐个人开发）

```bash
gemini
```

按提示选择 Login with Google。

方式 B：Gemini API Key

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
gemini
```

若你使用组织版 Code Assist，先设置：

```bash
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
gemini
```

### 3.4 最小可用示例

```bash
gemini
```

会话中输入：

```text
请总结当前目录结构，并给出三个可落地的改进建议。
```

## 4. 并行使用建议（同一仓库）

1. 用 Codex 做“代码修改主流程”（计划、实施、重构、提交）。
2. 用 Gemini 做“补充型任务”（方案备选、文档改写、跨文件总结）。
3. 两者都启用前，先确认当前目录与分支，避免误改。

## 5. 常见问题排查

### 5.1 命令不存在

- 现象：`codex: command not found` 或 `gemini: command not found`
- 处理：确认 `npm -g bin` 在 `PATH` 中，或重开 shell

### 5.2 Node 版本不满足（Gemini）

- 现象：安装或运行报版本错误
- 处理：升级到 Node.js 20+ 后重试

### 5.3 登录页打不开

- 检查代理/防火墙
- 在可打开浏览器的本机终端执行登录流程

### 5.4 速率限制或额度问题

- Codex：检查 ChatGPT 方案或 API 计费状态
- Gemini：检查 OAuth 配额或 API key 配额/计费

## 6. 快速对比

| 项目 | Codex CLI | Gemini CLI |
|---|---|---|
| 安装 | `npm i -g @openai/codex` | `npm i -g @google/gemini-cli` |
| 免安装运行 | 无常用免安装入口（建议直接全局安装） | `npx @google/gemini-cli` |
| 常见登录 | ChatGPT 登录 | Google OAuth |
| API Key | 支持 | 支持（`GEMINI_API_KEY`） |
| Windows 建议 | WSL | 可用（仍建议开发时统一环境） |

## 7. 官方文档（建议收藏）

- OpenAI Codex CLI（开发者文档）：https://developers.openai.com/codex/cli
- OpenAI Codex GitHub： https://github.com/openai/codex
- Gemini CLI（Google 开发者文档）：https://developers.google.com/gemini-code-assist/docs/gemini-cli
- Gemini CLI GitHub：https://github.com/google-gemini/gemini-cli

