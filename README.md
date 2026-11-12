# 花生十三行测工具箱 Skill

将 [heihei999/huasheng-mcp](https://github.com/heihei999/huasheng-mcp) 的本地知识库与工具函数改造为可直接使用的 Agent Skill，无需启动 MCP 服务。

## 功能

- 442 张方法卡片，涵盖资料分析、数量关系、判断推理、言语理解。
- 保留 15 项工具函数：方法检索、卡片读取、出处查询、题型分类与路由、解题草案及模块框架。
- 知识库随包携带，运行时无需访问原仓库或联网。

## 安装到 Codex

需要 Python 3.10 或更高版本。将本仓库克隆到 `~/.codex/skills/huasheng-xingce-toolkit`（若设置了 CODEX_HOME，则放到对应 skills 目录）。Windows 默认目录为 `%USERPROFILE%\.codex\skills\huasheng-xingce-toolkit`。已有同名目录时先备份，避免覆盖本地修改。

新开聊天后说：**用 huasheng-xingce-toolkit 帮我解这道题。**

## 直接运行

在仓库目录下：

```powershell
py -3 scripts/run.py list
py -3 scripts/run.py search_methods --input params.json
```

其他平台可将 `py -3` 替换为 `python3`。params.json 使用 UTF-8 编码，例如：

```json
{"query":"比重 增长率","top_k":5}
```

更多工作流程见 [SKILL.md](SKILL.md)。参数以 list 输出为准，不需要安装 MCP 或启动服务器。

## 验证与限制

已完成 skill 格式校验及全部 15 项函数的基础调用检查，确认 442 张方法卡片与来源版本逐字节一致。基础检查不代表每个题型、每道题的答案都经过正确性验证。路由使用启发式，解题输出可能只是草案，需结合题目核验。

## 来源与授权

原项目：heihei999/huasheng-mcp；本次转换依据本地副本，项目元数据版本为 0.7.0。保留原知识库与 Python 核心代码，新增 SKILL.md 与无服务调用入口 scripts/run.py。原项目使用 MIT License，版权与许可文本完整保留于 [LICENSE](LICENSE)。本项目不是花生十三官方产品。
