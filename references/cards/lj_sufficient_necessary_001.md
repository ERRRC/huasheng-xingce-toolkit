# 充分条件与必要条件识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_sufficient_necessary_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

必要/充分条件

## 方法名称 (`method_name`)

充分条件与必要条件识别法

## 检索标签 (`tags`)

- 逻辑基本知识
- 充分条件
- 必要条件
- 翻译推理

## 适用条件 (`trigger_conditions`)

- 出现必要前提、基础、关键、必须、需要、离不开、必不可少、不可或缺
- 出现如果/只有/除非等条件词

## 不适用条件 (`anti_conditions`)

- 问法要求解释矛盾或加强削弱时，条件翻译只能作为辅助结构

## 解题步骤 (`steps`)

- 识别 A 与 B：A→B 中 A 是充分条件，B 是必要条件。
- 看到必要类词语时，谁是必要条件谁放箭头后件。
- 翻译后忠于箭头：肯定前件可推出后件，否定后件可推出否定前件。
- 不要把肯定后件推出前件，也不要把否定前件推出否定后件。
- 用逆否命题核对选项。

## 公式 (`formulas`)

- A→B
- ¬B→¬A
- 必要条件位于箭头后件

## 示例 (`examples`)

- 经济可持续发展需要保护生态环境：经济可持续发展→保护生态环境。

## 易错点 (`pitfalls`)

- 把必要条件放到箭头前
- 把只有A才B误译为A→B
- 肯后或否前错误

## 避免事项 (`forbidden`)

- 禁止把 A→B 推成 B→A
- 禁止把 ¬A 推成 ¬B

## 来源文件 (`source_file`)

- 【判断推理】逻辑基本知识.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】逻辑基本知识.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 14

## 原卡置信度 (`confidence`)

0.98

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- conditional_sentence
- option_sentence

## 计算策略 (`calculation_policy`)

- mode：formal_translation
- allow_symbols：
  - →
  - ¬
- verification：
  - 肯前必肯后
  - 否后必否前
  - 肯后否前不推出

## 原程序优先级 (`solver_priority`)

8

## 原卡输出约束 (`output_constraints`)

- must_output：
  - translated_form
  - valid_inference
- must_not_output：
  - 凭语感判断条件方向

## argument_structure (`argument_structure`)

- claim：结论推出题中需判断选项是否由条件命题必然推出。
- evidence：题干给出的条件词和命题关系。
- link：通过充分/必要翻译和逆否等价判断可推出项。

## strength_order (`strength_order`)

- （空列表）
