# 下文推断干扰项排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_next_option_elimination_023

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

下文推断

## 子题型 (`sub_type`)

下文干扰项

## 方法名称 (`method_name`)

下文推断干扰项排除法

## 检索标签 (`tags`)

- 下文推断
- 干扰项
- 话题一致

## 适用条件 (`trigger_conditions`)

- 下文选项有危害、原因、对策、背景混杂
- 末句已有明显接续方向

## 不适用条件 (`anti_conditions`)

- 选项全都围绕尾句且差异很细

## 解题步骤 (`steps`)

- 排除上文已经谈过的选项。
- 排除与尾句话题不一致的选项。
- 排除过度跳跃到更大主题的选项。
- 排除与尾句语义方向相反的选项。
- 保留最能承接尾句新信息或大对策的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 社交恐惧症题中，危害和机制不是尾句‘治疗方法’的新方向，应排除。

## 易错点 (`pitfalls`)

- 只看题材相似，不看尾句关键词

## 避免事项 (`forbidden`)

- 选择已谈内容或话题漂移内容

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
    - 14
    - 15

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- last_sentence_topic
- covered_topics
- option_topics

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

25

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
