# 词性一致检查法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_grammar_pos_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

语法关系

## 方法名称 (`method_name`)

词性一致检查法

## 检索标签 (`tags`)

- 语法关系
- 词性
- 名词
- 动词
- 形容词

## 适用条件 (`trigger_conditions`)

- 题干词语关系不易从语义直接判断
- 选项一级关系相近，需要二级筛选

## 不适用条件 (`anti_conditions`)

- 题干一级关系已足以唯一确定答案时，词性只作复核

## 解题步骤 (`steps`)

- 标注题干各词词性：名词、动词、形容词等。
- 标注选项对应位置词性。
- 排除词性排列与题干不一致的选项。
- 再回到语义或逻辑关系确认。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：资料将词性列为语法关系，并举责任-推诿-承担类题。

## 易错点 (`pitfalls`)

- 只看词性一致而忽略内在关系。

## 避免事项 (`forbidden`)

- 不得用词性一致替代关系一致。

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
- part_of_speech

## 计算策略 (`calculation_policy`)

- mode：secondary_filter
- not_primary_if_relation_clear：true

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- must_output：
  - pos_pattern

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

语法关系-词性

## secondary_check (`secondary_check`)

- 词性排列一致
- 对应位置一致
- 不能替代语义关系
