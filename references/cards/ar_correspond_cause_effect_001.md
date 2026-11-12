# 因果关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_correspond_cause_effect_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

因果关系识别法

## 检索标签 (`tags`)

- 对应关系
- 因果关系
- 原因结果

## 适用条件 (`trigger_conditions`)

- 题干一个词是原因，另一个词是结果
- 选项存在原因-结果结构

## 不适用条件 (`anti_conditions`)

- 两个词只是时间先后或功能目的，不要误判为因果

## 解题步骤 (`steps`)

- 判断A是否导致B，或B是否由A引起。
- 明确因果方向。
- 检查选项是否同方向因果。
- 排除只是同时出现、先后发生、功能用途的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：唇亡-齿寒被列为因果对应。

## 易错点 (`pitfalls`)

- 把时间顺序误判为因果。
- 因果方向倒置。

## 避免事项 (`forbidden`)

- 不得没有因果机制就判因果。

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

- mode：causal_relation
- direction_required：true

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- must_output：
  - cause
  - effect
  - direction

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-因果

## secondary_check (`secondary_check`)

- 因果方向一致
- 区别于时间顺序
- 区别于功能目的
