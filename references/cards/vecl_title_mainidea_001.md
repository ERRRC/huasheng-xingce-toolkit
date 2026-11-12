# 标题拟定主旨变形法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_title_mainidea_001

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

标题填入

## 子题型 (`sub_type`)

主旨题变形

## 方法名称 (`method_name`)

标题拟定主旨变形法

## 检索标签 (`tags`)

- 标题拟定
- 主旨变形
- 结构概括

## 适用条件 (`trigger_conditions`)

- 题干出现“最适合做标题”“标题最恰当”
- 文段有明确中心或并列结构

## 不适用条件 (`anti_conditions`)

- 文段只问下文或语句填入
- 标题选项没有概括中心而只是细节句

## 解题步骤 (`steps`)

- 按主旨题方法先确定文段中心：总分、分总、问题—对策、并列、转折等。
- 标题必须覆盖中心话题，不选背景、例子、解释句。
- 若文段是并列，标题要能概括并列各分支，而不能只取其一。
- 若文段有对策，标题优先体现对策或问题解决方向。
- 最后比较标题可读性，优先简洁、准确、覆盖核心的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 桥头堡例：文段讲桥头堡过去目的、现在目的和作用，标题应概括“为什么大桥要造桥头堡”，不能只写“初衷”。

## 易错点 (`pitfalls`)

- 只抓最后一句造成片面
- 把解释性细节当标题
- 标题太宽泛导致主题词缺失

## 避免事项 (`forbidden`)

- 标题中出现原文未提及的新概念
- 标题只对应某一个例子

## 来源文件 (`source_file`)

- 【言语理解与表达】标题、下文、语句填入、排序.pdf
- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】标题、下文、语句填入、排序.pdf
  - pages：
    - 1
-
  - file：花生言语理解笔记.pdf
  - pages：
    - 12
    - 13

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- passage_structure
- topic_words
- author_viewpoint
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_basis：标题必须同时说明对应的文段结构和关键词覆盖情况
- avoid：
  - 只因选项好听就选
  - 只取文段一句话

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
