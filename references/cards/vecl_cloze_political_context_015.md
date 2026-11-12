# 政策语境与正向表达法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_political_context_015

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

政治语境

## 方法名称 (`method_name`)

政策语境与正向表达法

## 检索标签 (`tags`)

- 逻辑填空
- 政治语境
- 规范表达
- 反义对应

## 适用条件 (`trigger_conditions`)

- 文段涉及基层干部、管理干部、严管厚爱、担当作为等政策语境

## 不适用条件 (`anti_conditions`)

- 普通生活语境或文学语境

## 解题步骤 (`steps`)

- 先识别是否为政策治理语境。
- 优先使用符合政策表达习惯的词，如严管与厚爱对应。
- 避免选择现实语境中不成立或过度惩罚化的词。
- 结合前后反义或并列关系验证。
- 确保答案符合积极、规范、稳妥的语体。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 管理干部时与‘厚爱’对应的是‘严管’，而不是‘薄惩’。

## 易错点 (`pitfalls`)

- 不结合真实治理语境
- 选词过激或不规范

## 避免事项 (`forbidden`)

- 选择与政策语境不协调的词

## 来源文件 (`source_file`)

- 【言语理解与表达】逻辑填空.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】逻辑填空.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- policy_context_terms
- contrast_terms
- candidate_words

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

74

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

- 政治语境
- 反义对应
- 规范表达

## collocation_rules (`collocation_rules`)

- 严管厚爱
- 担当作为
- 换位思考/理解包容
