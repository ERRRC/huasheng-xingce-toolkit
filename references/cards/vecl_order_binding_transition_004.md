# 转折关系寻找上句法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_binding_transition_004

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

转折捆绑

## 方法名称 (`method_name`)

转折关系寻找上句法

## 检索标签 (`tags`)

- 语句排序
- 转折
- 捆绑
- 关联词

## 适用条件 (`trigger_conditions`)

- 某句以然而/但是/却/不过开头
- 选项中转折句前句不同

## 不适用条件 (`anti_conditions`)

- 转折词只是句内轻微转折且不影响大结构

## 解题步骤 (`steps`)

- 定位转折句的转折词和转折后重点。
- 上句应表达与转折后相反或形成对比的内容。
- 在选项中优先寻找“上句+转折句”捆绑。
- 再看转折后是否接解释说明或结果。
- 排除转折前后不构成对比的组合。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 稀土例：④“然而”说国际市场受制于人，前句应说我国曾有领先地位，对应⑤④相连。

## 易错点 (`pitfalls`)

- 只看到同一主题就捆绑，未验证转折方向

## 避免事项 (`forbidden`)

- 转折前后语义同向

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

- transition_sentence
- candidate_previous_sentences

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

43

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 然而/但是/不过
- 语义相反
- 转折后重点

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
