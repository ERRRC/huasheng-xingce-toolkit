# 时间顺序关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_correspond_time_sequence_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

时间顺序关系识别法

## 检索标签 (`tags`)

- 对应关系
- 时间顺序
- 流程

## 适用条件 (`trigger_conditions`)

- 题干词语构成先后流程
- 三词或多词类比中出现阶段顺序

## 不适用条件 (`anti_conditions`)

- 存在因果关系时需判断是否主要考因果而非先后

## 解题步骤 (`steps`)

- 确定题干词语是否按时间先后排列。
- 判断选项是否具有相同阶段顺序。
- 排除顺序错乱或缺少关键阶段的选项。
- 若同时存在因果，比较题干是否强调流程顺序。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：生产-运输-零售被列为时间顺序关系。

## 易错点 (`pitfalls`)

- 把时间先后等同于因果。
- 忽略三词顺序。

## 避免事项 (`forbidden`)

- 不得更改题干词序来适配选项。

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

- ordered_stem_terms
- option_terms

## 计算策略 (`calculation_policy`)

- mode：sequence_matching
- direction_required：true

## 原程序优先级 (`solver_priority`)

23

## 原卡输出约束 (`output_constraints`)

- must_output：
  - sequence_order

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-时间顺序

## secondary_check (`secondary_check`)

- 时间先后
- 主体是否一致
- 主体数量是否一致
