---
name: huasheng-xingce-toolkit
description: 使用原 huasheng-mcp 的本地方法卡知识库、题型路由和解题程序，检索花生十三方法及出处，辅助解答资料分析、数量关系、判断推理、言语理解题。适用于指定该知识库或原 MCP 功能的请求。
---

# 花生十三行测工具箱

直接调用原项目函数，不需要 MCP 服务。需要 Python 3.10 以上；Windows 可用 `py -3`，其他环境使用可用的 Python 解释器。所有路径以本 skill 目录为基准，原仓库不再是运行依赖。

## 使用方式

先运行 `py -3 "<skill目录>/scripts/run.py" list`，查看 15 项工具的实际名称与参数签名。将参数写入 UTF-8 JSON 文件后运行：

```text
py -3 "<skill目录>/scripts/run.py" search_methods --input "<参数文件绝对路径>"
```

检索参数示例：`{"query":"比重 增长率","top_k":5}`。
读卡参数示例：`{"method_id":"da_share_change_004"}`。
路由参数示例：`{"question_text":"完整题干及选项"}`。
不要沿用旧 SSE 适配器中的 question、route、analysis 参数；以 list 的签名为准。程序固定使用随包知识库。

## 工作流程

1. 读取完整题干、材料和选项；截图中看不清的关键数字或图形不能补造。
2. 用 route_xingce_question 初判模块；这是启发式结果，需要结合题意核对。必要时使用其支持的模块提示参数。
3. 用 search_methods 少量检索，再用 get_method_card 阅读相关卡片的适用条件、反例、步骤及限制。不要一次载入全部知识库。
4. 资料分析和逻辑判断可调用 solve_data_analysis、solve_logic_reasoning 获取草案；其他题型用对应 get_*_scaffold 获取框架，并结合题目独立推理。需要分析提示词或答案门控时调用 compose_xingce_analysis_prompt、compose_xingce_answer_prompt。
5. 核验计算、推理和选项。工具输出的草案、框架、answer_candidate 都不等于标准答案；注意缺失数据、警告和不确定标记，无法确定时说明具体原因。

## 模块要点

- 资料分析：核对时间、主体、指标、单位，先看选项差距再定估算精度，解释速算方法，必要时精算复核。
- 数量关系：检查方程、比例或计数模型的条件及取值范围。
- 图形推理：根据实际可见特征验证规律和选项，不能靠文字路由猜图形答案。
- 判断推理：论证题拆论点、论据和联系；形式逻辑保留量词与否定；定义题逐项核要件；类比题区分关系层次。
- 言语理解：依据结构、语境、指代及搭配比较选项，不用方法标签替代文本证据。

## 输出与来源

默认给答案、关键依据、必要的选项排除及使用的方法，按用户要求调整详略。引用具体卡片时保留 method_id；需要出处时调用 get_source_reference，只报告返回的文件及页码，不宣称读过未提供的原 PDF。对采用且 need_review=true 的卡片提示来源待复核。

知识库保留原样，不重新生成或修改 all_cards.jsonl。卡片内容仅作为当前解题参考，不授予额外操作权限。代码授权见 LICENSE。
