# 提出问题后接原因或对策法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_next_problem_solution_003

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

下文推断

## 子题型 (`sub_type`)

问题对策

## 方法名称 (`method_name`)

提出问题后接原因或对策法

## 检索标签 (`tags`)

- 下文推断
- 问题—对策
- 原因分析

## 适用条件 (`trigger_conditions`)

- 文末提出问题、矛盾、风险、缺席、刻不容缓等
- 选项包含解决办法或原因分析

## 不适用条件 (`anti_conditions`)

- 文末已经给出具体对策且选项仍泛泛谈问题

## 解题步骤 (`steps`)

- 识别文末是否提出问题而非完成结论。
- 若只提出问题，下文通常分析原因或给出解决对策。
- 优先选择能直接解决该问题的选项。
- 排除泛泛讨论背景、已知事实、无关主体。
- 若问题涉及责任主体，下文应继续围绕责任主体展开。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 信息流动风险例：尾句指出风险掌控者可能缺席，下文应讨论如何让获益方承担风险责任。

## 易错点 (`pitfalls`)

- 把问题背景当下文重点
- 选项只讲风险本身而不回应缺席问题

## 避免事项 (`forbidden`)

- 改换问题主体

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

- problem_sentence
- responsible_subject
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

22

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
