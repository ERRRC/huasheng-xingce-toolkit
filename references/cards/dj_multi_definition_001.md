# 多定义一一对应法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_multi_definition_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

多定义/枚举型

## 方法名称 (`method_name`)

多定义一一对应法

## 检索标签 (`tags`)

- 多定义
- 枚举型
- 一一对应
- 执行性求助
- 工具性求助

## 适用条件 (`trigger_conditions`)

- 题干同时给出两个或多个定义
- 问属于其中某一种定义
- 定义之间有明显分类差异

## 不适用条件 (`anti_conditions`)

- 只有单一定义时不必使用多定义对照表

## 解题步骤 (`steps`)

- 确认题干是否给出两个或多个并列定义。
- 分别抽取每个定义的主体、对象、行为方式、目的或结果。
- 选项必须与目标定义一一对应；若落入另一个定义类别，则排除。
- 若出现同构选项，通常同时排除，剩余选项再细核定义要素。
- 不属于题中可借其他符合项理解目标定义，但不能把例子反推成新定义。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：工具性求助题中，A无求助，B自己使用工具，C为执行性求助，D为借助他人且自己努力。

## 易错点 (`pitfalls`)

- 只看到相似行为，未区分两个定义的本质差异。
- 把使用工具当成求助他人。

## 避免事项 (`forbidden`)

- 不得把非目标定义的选项当作正确项。

## 来源文件 (`source_file`)

- 【判断推理】定义判断.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】定义判断.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 20

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- definition_list
- target_definition
- options

## 计算策略 (`calculation_policy`)

- mode：multi_definition_mapping
- build_contrast_table：true

## 原程序优先级 (`solver_priority`)

6

## 原卡输出约束 (`output_constraints`)

- must_output：
  - target_definition
  - contrast_dimension
  - elimination_table

## definition_elements (`definition_elements`)

- 主体：逐定义提取
- 客体/对象：逐定义提取
- 条件：逐定义提取
- 方式：逐定义提取
- 目的：逐定义提取
- 结果：逐定义提取
- 特殊要求：逐定义提取

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
