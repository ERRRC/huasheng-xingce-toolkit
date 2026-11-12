# 二级辨析总控法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_secondary_check_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

二级辨析

## 方法名称 (`method_name`)

二级辨析总控法

## 检索标签 (`tags`)

- 二级辨析
- 难点
- 种属组成
- 矛盾反对
- 特指泛指

## 适用条件 (`trigger_conditions`)

- 多个选项都满足一级关系
- 题干关系看似简单但选项相近

## 不适用条件 (`anti_conditions`)

- 一级关系已唯一确定答案时，不必过度二级辨析

## 解题步骤 (`steps`)

- 先确认所有候选项是否满足同一一级关系。
- 若为包含关系，区分种属与组成。
- 若为互斥关系，区分矛盾与反对。
- 若为包含/种属关系，区分特指与泛指。
- 补充检查词性、方向、关系强弱和对象类别。
- 选择二级关系与题干最一致的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：资料列出类比三难点：种属/组成区别，矛盾/反对区别，特指/泛指区别。

## 易错点 (`pitfalls`)

- 一级关系一致就匆忙选项。
- 忽略方向与层级。

## 避免事项 (`forbidden`)

- 不得过度使用冷门知识做二级辨析。

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
    - 22

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- candidate_options
- primary_relation
- stem_relation

## 计算策略 (`calculation_policy`)

- mode：secondary_disambiguation
- only_when_needed：true

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- must_output：
  - primary_relation
  - secondary_dimension
  - final_relation_match

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

二级辨析

## secondary_check (`secondary_check`)

- 种属 vs 组成
- 矛盾 vs 反对
- 特指 vs 泛指
- 方向一致
- 词性一致
