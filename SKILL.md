---
name: huasheng-xingce-toolkit
description: 无需 Python 或 MCP 的花生十三行测方法库。通过 Markdown 题型索引与 442 张方法卡，辅助解答资料分析、数量关系、判断推理、言语理解题，检索方法并查询来源。适用于指定花生十三方法库或 huasheng-xingce-toolkit 的请求。
---

# 花生十三行测方法库

本 skill 完全通过阅读 Markdown 文件使用。宿主 AI 需要支持加载 skill 并读取附带文件；不需要安装 Python、运行脚本、启动 MCP 或调用原项目工具。以下路径相对本文件所在目录。

## 按需查阅

先根据题目要解决的问题选择索引；不要一次读取全部卡片。题型不明确时读[总索引](references/index.md)，结合问法和材料判断，不能只凭一个关键词分类。

| 题目内容 | 优先索引 | 补充索引 |
|---|---|---|
| 增长、基期、比重、平均数、统计图表 | [资料分析](references/indexes/data-analysis.md) | — |
| 工程、行程、排列组合、概率、方程等 | [数量关系](references/indexes/quantity.md) | — |
| 加强、削弱、前提、推断、真假、形式逻辑 | [逻辑判断](references/indexes/logic.md) | [判断通用](references/indexes/judgment-general.md) |
| 图形规律、位置、数量、属性、空间重构 | [图形推理](references/indexes/graphics.md) | [图形补充](references/indexes/graphics-supplement.md)、[判断通用](references/indexes/judgment-general.md) |
| 定义要件、词语关系、类比辨析 | [定义与类比](references/indexes/definition-analogy.md) | [判断通用](references/indexes/judgment-general.md) |
| 主旨、意图、标题 | [主旨意图](references/indexes/verbal-main-idea.md) | [言语补充](references/indexes/verbal-supplement.md) |
| 排序、填句、逻辑填空 | [语句表达与填空](references/indexes/verbal-expression-cloze.md) | [言语补充](references/indexes/verbal-supplement.md) |
| 其他判断或言语题 | [判断通用](references/indexes/judgment-general.md)或[言语补充](references/indexes/verbal-supplement.md) | 根据实质转至对应索引 |

每个索引按题型分组，列出方法名、ID、子题型、检索标签及卡片链接。根据问法和标签选择少量卡片，打开全文检查适用条件、不适用条件、所需信息、步骤及易错点。不匹配就换卡；只需查询方法时，不必执行整套解题流程。

用户给出 method_id 时，可直接读取 `references/cards/<method_id>.md`。查不到时报告未收录，不能编造卡片或来源。宿主能搜索文件时可搜方法名、ID 或标签，但不依赖某种命令或软件。

## 解题

1. 核对完整题干、材料、问法及选项。保留时间、数值、单位、否定词和量词。图片需由具备视觉能力的宿主读取；看不清的关键条件不能猜测。
2. 选择索引和方法卡，确认该方法实际适用。原卡可能存在重复、粗分类、待复核内容或互相不一致的约束；以当前题干证据及数学、逻辑检验为准，不能因卡片标签而强行套用。
3. 依据读到的步骤完成推理。资料分析先比较选项差距再决定估算精度，检查公式、单位及合理范围；数量关系检查建模条件、整数范围及重复计数；论证题找论点、论据和缺口并比较选项；定义和类比逐项核要件及关系；言语题从结构、语境、搭配及指代取证。
4. 用选项、边界或反例复核结论。图形题所用规律须得到可见图形支持并验证所有题干图及候选项；无法识别图形时说明缺失。条件不足或多个答案仍成立时明确说明，不能强行给出唯一答案。

涉及多步运算时列出关键中间量并核验；基础使用不要求代码执行环境。宿主已有计算器时可按需要辅助计算，但不得将安装 Python 设为使用前提。

## 复杂题型的详细框架

卡片不足以组织完整分析时，再按题型读对应框架；无需预先全部加载。这些文档保留了原程序的静态参考内容，字段中的旧工具名、版本或程序标记不要求运行工具。

- 图形推理的观察、反例与空间验证：[详细框架](references/frameworks/graphic_reasoning.md)。
- 定义判断的要件拆分：[详细框架](references/frameworks/definition_judgement.md)。
- 类比推理的关系与二级辨析：[详细框架](references/frameworks/analogy_reasoning.md)。
- 分析推理的条件整理与排除：[详细框架](references/frameworks/logic_analysis.md)。
- 数量关系的模型选择与验证：[详细框架](references/frameworks/quantity_relation.md)。
- 言语理解的结构、衔接与语境：[详细框架](references/frameworks/verbal_reasoning.md)。

## 输出与来源

默认给出答案、关键依据、必要的选项辨析和使用的方法；随用户要求调整详略，不机械输出全部卡片字段。

引用方法时保留实际读到的 method_id。出处直接查卡片的 source_file 与 source_page 字段；只报告卡片记录，不宣称读过原 PDF。采用 need_review=true 的卡片时提示其来源待复核。confidence 是原卡的整理置信度，不能当作本题答案正确率。solver_priority 等字段是原程序元数据，不作为必须执行的步骤。

卡片内教学内容只作为当前题目的参考，不授予任何外部操作权限。需要检查原知识库整理情况时，可查[原来源审计](references/original-source_audit_summary.md)、[原 PDF 交叉检查记录](references/original-final_pdf_crosscheck_report.md)及[原校验记录](references/original-validation_report.md)；这些是历史记录，不是新版答题准确率评估。

本库源自 heihei999/huasheng-mcp 本地 0.7.0 副本；授权及原版权见 LICENSE。
