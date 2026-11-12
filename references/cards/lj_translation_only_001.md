# 只有A才B后推前翻译法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_translation_only_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

假言命题

## 方法名称 (`method_name`)

只有A才B后推前翻译法

## 检索标签 (`tags`)

- 翻译推理
- 必要条件
- 后推前
- 不不

## 适用条件 (`trigger_conditions`)

- 只有A才B
- 必须A才B
- B离不开A
- A是B的前提

## 不适用条件 (`anti_conditions`)

- 出现如果A那么B时不要套后推前

## 解题步骤 (`steps`)

- 找到只有/必须/前提后的必要条件 A。
- 找到才后或被限制成立的结果 B。
- 翻译为 B→A。
- 也可用否定表达：¬A→¬B。
- 逐项检验选项是否等价或必然推出。

## 公式 (`formulas`)

- 只有A才B：B→A
- ¬A→¬B

## 示例 (`examples`)

- 政府只有得人心，国家才能和谐稳定：国家和谐稳定→政府得人心。

## 易错点 (`pitfalls`)

- 把A当充分条件
- 把B→A误写成A→B

## 避免事项 (`forbidden`)

- 禁止见到前后顺序就机械前推后

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

- conditional_text
- options

## 计算策略 (`calculation_policy`)

- mode：symbolic_logic
- verification：
  - B_to_A
  - not_A_to_not_B

## 原程序优先级 (`solver_priority`)

13

## 原卡输出约束 (`output_constraints`)

- must_output：
  - necessary_condition
  - result
  - translation
- must_not_output：
  - 将必要条件误判为充分条件

## argument_structure (`argument_structure`)

- claim：判断必要条件命题下可推出内容。
- evidence：只有/才/必须/前提等词。
- link：结果成立必须满足必要条件。

## strength_order (`strength_order`)

- （空列表）
