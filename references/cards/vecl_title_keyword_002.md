# 标题关键词主语一致法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_title_keyword_002

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

标题填入

## 子题型 (`sub_type`)

关键词与主语

## 方法名称 (`method_name`)

标题关键词主语一致法

## 检索标签 (`tags`)

- 标题拟定
- 关键词
- 主语一致
- 观点对策

## 适用条件 (`trigger_conditions`)

- 标题选项多个都像主旨
- 选项主题词不同
- 文段有明确主语或高频词

## 不适用条件 (`anti_conditions`)

- 选项主语全部一致且只需比较结构覆盖

## 解题步骤 (`steps`)

- 圈出文段反复出现的主体词和核心名词。
- 检查选项主语是否与文段谈论对象一致。
- 若文段有观点/对策，标题需体现观点/对策而不是只写话题。
- 排除缺少核心主体词、换成泛化概念或扩大范围的标题。
- 同等条件下选更能同时覆盖主题词和态度的标题。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 心梗例：文段强调夏秋之交要警惕心肌梗死，标题需包含时间和预防方向。

## 易错点 (`pitfalls`)

- 选项表述很顺但主语换了
- 只看高频词不看作者态度

## 避免事项 (`forbidden`)

- 用上位词替代核心话题导致范围扩大

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

- topic_words
- high_frequency_terms
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

11

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

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
