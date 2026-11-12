# 近义关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_semantic_synonym_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

语义关系

## 方法名称 (`method_name`)

近义关系识别法

## 检索标签 (`tags`)

- 语义关系
- 近义
- 同义
- 词义

## 适用条件 (`trigger_conditions`)

- 题干两个词语意思相近或可互相解释
- 选项中存在近义词组

## 不适用条件 (`anti_conditions`)

- 词语只是同领域、同类别但语义不近时不要判近义

## 解题步骤 (`steps`)

- 判断题干两词是否可以近义替换。
- 排除只是在情境上相关但语义不近的选项。
- 若多个选项近义，进一步看感情色彩、词性和语体是否一致。
- 选出近义程度和词性最一致的项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：历练与磨砺类题属于近义语义关系。

## 易错点 (`pitfalls`)

- 把相关关系误判为近义。
- 忽略褒贬色彩。

## 避免事项 (`forbidden`)

- 不得只因两个词都常同时出现就判近义。

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

- mode：semantic_similarity
- use_common_sense：ordinary_language

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- must_output：
  - synonym_evidence
  - secondary_difference

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

语义关系-近义

## secondary_check (`secondary_check`)

- 词性一致
- 感情色彩一致
- 语义强弱一致
