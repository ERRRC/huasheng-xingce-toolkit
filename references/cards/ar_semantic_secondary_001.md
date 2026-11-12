# 语义关系感情色彩与程度二级辨析法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 模块 (`module`)

判断推理-定义判断与类比推理

## 检索标签 (`tags`)

- 类比推理
- 语义关系
- 近义反义
- 感情色彩
- 程度轻重
- 二级辨析

## 适用条件 (`trigger_conditions`)

- 题干为近义、反义或比喻/象征关系，多个选项一级关系均成立
- 选项近义反义关系相似但褒贬或程度不同

## 不适用条件 (`anti_conditions`)

- 题干主关系不是语义关系时，不优先调用

## 解题步骤 (`steps`)

- 先确认题干是近义、反义、比喻义、象征义或引申义。
- 若是近义/反义，继续比较感情色彩：褒义、贬义、中性。
- 再比较程度轻重：好感、喜欢、热爱等强度是否一致。
- 若是比喻/象征义，检查词性是否一致。
- 只有一级关系和二级属性都一致时才保留选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生判断笔记总结.pdf
  - page：22
  - summary：笔记将近义/反义的二级辨析细化为感情色彩、程度；比喻/象征义需看词性。

## 易错点 (`pitfalls`)

- 只看近义反义，不看褒贬色彩。
- 忽略程度强弱差异。

## 避免事项 (`forbidden`)

- 不得用“意思差不多”代替二级辨析。

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 22

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_terms
- option_terms
- candidate_semantic_relation

## 计算策略 (`calculation_policy`)

- mode：analogy_secondary_check
- checks：
  - 感情色彩
  - 程度轻重
  - 词性

## 原程序优先级 (`solver_priority`)

6

## 原卡输出约束 (`output_constraints`)

- must_output：
  - 一级语义关系
  - 二级检查结果

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

语义关系

## secondary_check (`secondary_check`)

- 感情色彩:褒义/贬义/中性
- 程度:好感/喜欢/热爱
- 词性一致

## 方法 ID (`id`)

ar_semantic_secondary_001

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

语义关系二级辨析

## 方法名称 (`method_name`)

语义关系感情色彩与程度二级辨析法
