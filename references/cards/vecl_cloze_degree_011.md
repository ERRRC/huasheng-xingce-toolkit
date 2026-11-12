# 程度轻重匹配法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_degree_011

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

程度轻重

## 方法名称 (`method_name`)

程度轻重匹配法

## 检索标签 (`tags`)

- 逻辑填空
- 程度轻重
- 强弱比较

## 适用条件 (`trigger_conditions`)

- 语境出现严重后果、前所未有、水火不容、分庭抗礼等程度提示
- 选项词义强弱不同

## 不适用条件 (`anti_conditions`)

- 文段没有程度提示，主要考搭配或色彩

## 解题步骤 (`steps`)

- 找出表达程度的上下文提示。
- 给候选词按强弱排序。
- 选择与语境严重程度匹配的词。
- 多空题中注意程度递进或程度一致。
- 排除过轻、过重或不符合对象的问题词。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 诗歌内部问题由‘分庭抗礼、水火不容’提示程度严重，应选‘分裂’而非‘分歧’。

## 易错点 (`pitfalls`)

- 词义方向对但程度不够
- 忽略程度提示词

## 避免事项 (`forbidden`)

- 用轻词表达重问题或反之

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
    - 24

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- degree_markers
- candidate_strength
- context_severity

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

70

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

- 程度提示
- 严重性
- 强弱排序

## collocation_rules (`collocation_rules`)

- 程度与对象状态匹配
