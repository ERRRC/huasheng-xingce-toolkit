# 反义关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_semantic_antonym_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

语义关系

## 方法名称 (`method_name`)

反义关系识别法

## 检索标签 (`tags`)

- 语义关系
- 反义
- 近义反义

## 适用条件 (`trigger_conditions`)

- 题干两个词语意义相反或方向相反
- 选项中存在明显反义词组

## 不适用条件 (`anti_conditions`)

- 两个概念可以并存或有第三种可能时，不一定是矛盾关系，应考虑反对关系

## 解题步骤 (`steps`)

- 判断题干是否是语义层面的反义。
- 识别选项中是否也为反义，而非因果、并列或对应。
- 若涉及非A即B，转入逻辑关系中的矛盾/反对二级辨析。
- 比较反义强度、词性和结构。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：锦上添花与雪上加霜体现语义反向。

## 易错点 (`pitfalls`)

- 把反义与逻辑矛盾混同。
- 忽略有无第三种可能。

## 避免事项 (`forbidden`)

- 不得把任意不同词当成反义。

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

## 计算策略 (`calculation_policy`)

- mode：semantic_opposition

## 原程序优先级 (`solver_priority`)

11

## 原卡输出约束 (`output_constraints`)

- must_output：
  - antonym_basis
  - whether_third_possibility_exists

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

语义关系-反义

## secondary_check (`secondary_check`)

- 词性一致
- 反义方向一致
- 是否属于矛盾/反对
