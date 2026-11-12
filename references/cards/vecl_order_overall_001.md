# 语句排序整体结构套入法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_overall_001

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

整体结构

## 方法名称 (`method_name`)

语句排序整体结构套入法

## 检索标签 (`tags`)

- 语句排序
- 整体分析
- 结构套入

## 适用条件 (`trigger_conditions`)

- 题干给出编号句子要求排序
- 选项为句序组合

## 不适用条件 (`anti_conditions`)

- 不是排序题

## 解题步骤 (`steps`)

- 先看选项首句和尾句，缩小范围。
- 判断材料可套入的结构：总分、分总、提出问题—分析—对策、时间顺序、转折对比。
- 再找局部捆绑：指代、关联词、重复词、同话题、逻辑递进。
- 用选项差异快速验证，而非从零排列。
- 最后通读所选序列，确认无断裂。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 航母例：可套入“引出话题—我国现状—对策”，并用代词“它”验证④②相连。

## 易错点 (`pitfalls`)

- 只靠语感排列
- 忽略选项差异
- 不通读验证

## 避免事项 (`forbidden`)

- 不验证首尾句直接选

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

- numbered_sentences
- candidate_orders

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

40

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 首尾句
- 总分/分总
- 问题—对策
- 时间顺序
- 指代
- 关联词
- 尾首相连

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
