# 成语意思与适用语境法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_idiom_context_002

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

成语辨析

## 方法名称 (`method_name`)

成语意思与适用语境法

## 检索标签 (`tags`)

- 逻辑填空
- 成语辨析
- 语境
- 褒贬

## 适用条件 (`trigger_conditions`)

- 选项为成语
- 空格处需要评价某种现象

## 不适用条件 (`anti_conditions`)

- 选项为实词且主要考语法搭配

## 解题步骤 (`steps`)

- 先确认成语本义、常见色彩和使用对象。
- 从文段判断作者态度和语境正负。
- 排除色彩不符、语体不符、时间范围不符的成语。
- 检查成语是否能与空格前后成分搭配。
- 带入后看是否准确表达文段想说明的现象。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- “打榜、刷数据”有消极色彩，‘大行其道’比‘蔚然成风’更贴合。

## 易错点 (`pitfalls`)

- 望文生义
- 只看成语表面意思
- 忽略褒贬色彩

## 避免事项 (`forbidden`)

- 把积极成语用于消极语境

## 来源文件 (`source_file`)

- 【言语理解与表达】逻辑填空.pdf
- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】逻辑填空.pdf
  - pages：
    - 1
-
  - file：花生言语理解笔记.pdf
  - pages：
    - 22

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- idiom_options
- author_attitude
- object_described

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

61

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- 褒贬色彩
- 时间范围
- 对象属性

## collocation_rules (`collocation_rules`)

- 成语使用对象必须匹配
- 成语程度与语境一致
