# 中心理解结构概括法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_center_understanding_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

中心题

## 方法名称 (`method_name`)

中心理解结构概括法

## 检索标签 (`tags`)

- 中心理解
- 主要说明
- 概括
- 结构

## 适用条件 (`trigger_conditions`)

- 题干问“主要说明/主要介绍/这段文字主要讲了/概括最准确”
- 文段没有要求推断作者意图，只需概括中心

## 不适用条件 (`anti_conditions`)

- 题干明确要求标题或下文推断

## 解题步骤 (`steps`)

- 完成结构切分
- 找中心层：总句、观点句、对策句、原因句或并列整体
- 选项必须覆盖文段中心而不扩大引申
- 排除只对应局部材料或表达过度的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生言语理解笔记.pdf
  - page：6
  - summary：中心理解笔记按常见引出方式和常见结构进行题干分析。
  - lesson：中心题以结构概括为主，少做主观引申。

## 易错点 (`pitfalls`)

- 把意图题做成过度对策
- 把中心题做成细节题

## 避免事项 (`forbidden`)

- 无依据引申作者未说内容

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 6
    - 7
    - 9
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：center_understanding
- focus_rule：概括中心层，避免过度推断

## option_elimination (`option_elimination`)

-
  - type：过度引申
  - rule：中心题中超出原文的对策、意义、目的表达排除

## 所需信息 (`required_inputs`)

- 文段结构
- 中心句
- 选项覆盖范围
- 是否过度引申

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

5

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
