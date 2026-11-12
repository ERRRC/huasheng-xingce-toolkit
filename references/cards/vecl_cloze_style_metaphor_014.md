# 语体色彩和比喻一致法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_style_metaphor_014

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

语体与比喻

## 方法名称 (`method_name`)

语体色彩和比喻一致法

## 检索标签 (`tags`)

- 逻辑填空
- 语体色彩
- 比喻一致
- 形象表达

## 适用条件 (`trigger_conditions`)

- 文段有长河、潮头、高峰、深谷等比喻链
- 选项有口语/书面差异

## 不适用条件 (`anti_conditions`)

- 文段无比喻或语体差异不明显

## 解题步骤 (`steps`)

- 识别文段中的比喻域或语体风格。
- 候选词应与同一比喻域保持一致。
- 正式语境优先书面表达，生活口语语境可选口语化。
- 排除破坏比喻链或气势不协调的词。
- 带入后通读看文气是否一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- ‘历史长河’对应‘乘风破浪’，‘高峰’可与‘深谷’形成比喻一致。

## 易错点 (`pitfalls`)

- 词义对但比喻不搭
- 语体过俗或过雅

## 避免事项 (`forbidden`)

- 同一句中比喻域混乱

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
    - 26

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- metaphor_terms
- style_register
- candidate_words

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

73

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

- 比喻一致
- 语体色彩
- 画面协调

## collocation_rules (`collocation_rules`)

- 同一比喻域内搭配
- 正式/口语语体匹配
