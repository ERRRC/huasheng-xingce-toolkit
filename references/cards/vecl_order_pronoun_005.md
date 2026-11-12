# 指示代词寻找上句法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_pronoun_005

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

代词指代

## 方法名称 (`method_name`)

指示代词寻找上句法

## 检索标签 (`tags`)

- 语句排序
- 代词指代
- 衔接

## 适用条件 (`trigger_conditions`)

- 句中有这/这些/此/该/其/这个前提等
- 选项可比较其前句

## 不适用条件 (`anti_conditions`)

- 代词在句内已有明确指代对象

## 解题步骤 (`steps`)

- 圈出指示代词和代词后的名词。
- 在其他句子中找能被代词指代的先行内容。
- 将先行句放在指代句之前并优先相邻。
- 若找不到先行词，该句不能作首句。
- 验证相邻后语义是否顺畅。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 生物寿命例：④含“这些基因”，不能作首句，应前置关于基因的句子。

## 易错点 (`pitfalls`)

- 忽略代词导致句序断裂
- 代词指向范围过宽

## 避免事项 (`forbidden`)

- 指代句无先行词

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
    - 18
    - 19

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- pronoun_sentences
- candidate_antecedents

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

44

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 这/这些/该/其
- 先行词
- 相邻验证

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
