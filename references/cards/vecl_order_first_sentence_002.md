# 首句下定义与范围优先法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_first_sentence_002

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

首句判断

## 方法名称 (`method_name`)

首句下定义与范围优先法

## 检索标签 (`tags`)

- 语句排序
- 首句判断
- 下定义
- 范围

## 适用条件 (`trigger_conditions`)

- 选项首句不同
- 候选首句中有下定义、设问、背景、指代句

## 不适用条件 (`anti_conditions`)

- 各选项首句相同

## 解题步骤 (`steps`)

- 优先考虑下定义、话题引入、背景范围句作为首句。
- 排除含“这/这些/其/该”等无先行词的句子作首句。
- 排除转折后半句、结论句、例子句作首句。
- 比较候选首句的范围：大范围通常先于小范围。
- 用后续句是否能承接首句验证。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 生态红线例：先介绍更大范围“生态系统”，再介绍“生态红线”。

## 易错点 (`pitfalls`)

- 把论证句放开头
- 忽略指代词不能无前文

## 避免事项 (`forbidden`)

- 让含明确指代的句子作首句

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

- candidate_first_sentences
- pronoun_markers
- definition_sentences

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

41

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 下定义优先
- 大范围在前
- 指代句不能首句
- 转折句通常不首句

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
