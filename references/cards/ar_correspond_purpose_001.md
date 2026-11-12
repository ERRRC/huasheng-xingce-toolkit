# 目的关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_correspond_purpose_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

目的关系识别法

## 检索标签 (`tags`)

- 对应关系
- 目的
- 行为目的

## 适用条件 (`trigger_conditions`)

- 题干一个词是行为，另一个词是该行为目的
- 成语、动作与目的之间有明确关系

## 不适用条件 (`anti_conditions`)

- 如果一个词是结果而非目的，转因果关系

## 解题步骤 (`steps`)

- 判断A是否为了达到B。
- 检查选项是否也为行为-目的。
- 区别目的与实际结果：目的可能未必实现。
- 比较方向。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：刻舟-求剑被列为目的关系。

## 易错点 (`pitfalls`)

- 把结果误判为目的。

## 避免事项 (`forbidden`)

- 不得把行为后的可能结果都当目的。

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
    - 21

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- term_pair
- option_pairs

## 计算策略 (`calculation_policy`)

- mode：purpose_relation

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- must_output：
  - action
  - purpose

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-目的

## secondary_check (`secondary_check`)

- 是否能通过某种方式达到目的
- 主体是否一致
- 目的是否直接
