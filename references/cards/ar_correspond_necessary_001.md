# 必要性对应识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_correspond_necessary_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

必要性对应识别法

## 检索标签 (`tags`)

- 对应关系
- 必要性
- 条件

## 适用条件 (`trigger_conditions`)

- 题干体现做某事必须满足某条件或互为必要提示
- 词组呈规则/约束型对应

## 不适用条件 (`anti_conditions`)

- 只是功能、因果或目的，不要误判必要性

## 解题步骤 (`steps`)

- 判断题干是否表达必要条件或约束关系。
- 识别选项中是否存在同样必要约束。
- 比较条件方向是否一致。
- 若选项只是通常相关但非必要，排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：喝酒不开车：开车不喝酒被列为必要性对应。

## 易错点 (`pitfalls`)

- 把常见搭配误判为必要条件。

## 避免事项 (`forbidden`)

- 不得把非必要经验关系判为必要性。

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

- stem_terms
- option_terms

## 计算策略 (`calculation_policy`)

- mode：necessary_condition_relation

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- must_output：
  - necessity_direction

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-必要性

## secondary_check (`secondary_check`)

- 方向一致
- 是否必要而非经验相关
