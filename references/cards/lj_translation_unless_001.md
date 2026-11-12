# 除非/否则翻译法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_translation_unless_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

假言命题

## 方法名称 (`method_name`)

除非/否则翻译法

## 检索标签 (`tags`)

- 翻译推理
- 除非否则
- 必要条件

## 适用条件 (`trigger_conditions`)

- 除非A否则B
- 必须A否则B
- 不A就B

## 不适用条件 (`anti_conditions`)

- 如果题干没有否则结构，优先使用对应条件词规则

## 解题步骤 (`steps`)

- 识别除非或必须后的条件 A。
- 识别否则后的结果 B。
- 基础翻译为 ¬A→B。
- 必要时转逆否为 ¬B→A。
- 用两个等价式验证选项。

## 公式 (`formulas`)

- 除非A否则B：¬A→B
- ¬B→A

## 示例 (`examples`)

- 除非采取举措，否则经济不可能稳健增长：¬采取举措→经济不可能稳健增长。

## 易错点 (`pitfalls`)

- 把除非A否则B误译为A→B
- 忘记对A取否定

## 避免事项 (`forbidden`)

- 不得把日常语气理解替代逻辑式

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

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- conditional_text
- options

## 计算策略 (`calculation_policy`)

- mode：symbolic_logic
- verification：
  - not_A_to_B
  - not_B_to_A

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- must_output：
  - A
  - B
  - not_A_to_B
- must_not_output：
  - 漏掉否定符号

## argument_structure (`argument_structure`)

- claim：判断除非结构的必然推出。
- evidence：除非/否则句。
- link：不满足除非条件则出现否则结果。

## strength_order (`strength_order`)

- （空列表）
