# 关联词语义约束法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_relation_word_021

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

关联词提示

## 方法名称 (`method_name`)

关联词语义约束法

## 检索标签 (`tags`)

- 逻辑填空
- 关联词
- 逻辑关系
- 反向提示

## 适用条件 (`trigger_conditions`)

- 出现但、然而、既...也...更、否则、因为、因此等关联词

## 不适用条件 (`anti_conditions`)

- 关联词只是句外结构，对空格无约束

## 解题步骤 (`steps`)

- 标注关联词类型：转折、递进、并列、因果、条件。
- 判断空格与关联词前后成分的语义方向。
- 转折看反向，递进看加重，并列看同类，因果看原因结果。
- 排除与关联方向不一致的选项。
- 带入全句检查逻辑关系是否成立。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- ‘否则，失去窗口期’提示前面问题不能被束之高阁，后文空应体现难以回转。

## 易错点 (`pitfalls`)

- 只认识关联词但不判断方向
- 把并列误作递进

## 避免事项 (`forbidden`)

- 选项破坏关联词逻辑

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
    - 24

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- connective_markers
- blank_relation_to_marker
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

59

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

- 转折
- 递进
- 并列
- 因果
- 条件

## collocation_rules (`collocation_rules`)

- 关联词前后语义方向必须匹配
