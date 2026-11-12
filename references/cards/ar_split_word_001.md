# 拆词关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_split_word_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

拆词关系

## 方法名称 (`method_name`)

拆词关系识别法

## 检索标签 (`tags`)

- 拆词
- 字词关系
- 寒冷
- 寒舍

## 适用条件 (`trigger_conditions`)

- 题干由单字与含该字的词组成
- 选项也可拆出相同字义变化

## 不适用条件 (`anti_conditions`)

- 题干词语没有共同字或拆分后无稳定含义时不用

## 解题步骤 (`steps`)

- 拆出题干词语中的共同字。
- 判断共同字在不同词中的含义是否相同或不同。
- 检查选项是否也能进行同样拆词。
- 若多个选项可拆，比较字义关系。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：寒-寒冷-寒舍为拆词示例。

## 易错点 (`pitfalls`)

- 只看字形重复，不看字义。

## 避免事项 (`forbidden`)

- 不得忽略共同字在词中的实际含义。

## 来源文件 (`source_file`)

- 【判断推理】类比推理.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】类比推理.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 22

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_terms
- option_terms
- shared_character

## 计算策略 (`calculation_policy`)

- mode：morpheme_analysis

## 原程序优先级 (`solver_priority`)

28

## 原卡输出约束 (`output_constraints`)

- must_output：
  - shared_character
  - meaning_in_each_word

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

拆词关系

## secondary_check (`secondary_check`)

- 共同字位置
- 共同字含义
- 词性结构
