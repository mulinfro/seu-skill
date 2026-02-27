## 需求理解
实现一个最小可用 CLI 计算器，支持 `add/sub` 两个整数运算，包含错误处理与最基础测试覆盖。

## 范围与边界
- In Scope: 命令行参数解析、加减运算、错误提示、退出码、单元测试。
- Out of Scope: 浮点运算、乘除、交互式 REPL、打包发布。

## 实施计划
1. 新建 `calc.py`，实现 `add/sub` 命令分发与参数校验。
2. 为非法命令与非法参数增加错误输出和非 0 退出码。
3. 新建单元测试覆盖成功路径与错误路径。
4. 执行单测并修正问题。

## 技术选型建议
- 使用 Python 标准库 `sys` 和 `unittest`，避免引入第三方依赖。

## 预计修改文件
- [新增] demo_run/src/calc.py
- [新增] demo_run/tests/test_calc.py
- [新增] demo_run/current_plan.md
- [新增] demo_run/outputs/*.md

## 验证与回滚
- 测试: `python -m unittest discover -s demo_run/tests -v`
- 验收: 手工运行 add/sub/非法命令三类示例
- 回滚: 删除 `demo_run/src` 和 `demo_run/tests` 新增文件

请问是否同意按此计划执行？
