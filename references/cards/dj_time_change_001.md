# 时间前后与变化对比法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 模块 (`module`)

判断推理-定义判断与类比推理

## 检索标签 (`tags`)

- 定义判断
- 时间前后
- 变化
- 现在情况
- 以前情况

## 适用条件 (`trigger_conditions`)

- 定义或选项涉及时间前后、状态变化、过程变化
- 选项设置存在“以前情况”和“现在情况”对比

## 不适用条件 (`anti_conditions`)

- 定义只描述静态属性且无时间变化信息时不优先调用

## 解题步骤 (`steps`)

- 定位定义中的时间词或变化词。
- 区分初始状态、过程行为、变化后结果。
- 检查选项是否同时满足前后状态或变化方向。
- 若只描述某一时间点而缺失变化过程，谨慎排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生判断笔记总结.pdf
  - page：20
  - summary：笔记提示涉及时间前后需注意选项时间点设置，涉及变化需看“以前情况”和“现在情况”对比。

## 易错点 (`pitfalls`)

- 只看现在状态，忽略是否发生了定义要求的变化。
- 把时间点错位当成符合定义。

## 避免事项 (`forbidden`)

- 不得用结果相似替代过程变化。

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 20

## 原卡置信度 (`confidence`)

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- definition_time_clues
- option_time_clues
- option_state_before_after

## 计算策略 (`calculation_policy`)

- mode：temporal_state_check
- must_compare：
  - before
  - after

## 原程序优先级 (`solver_priority`)

8

## 原卡输出约束 (`output_constraints`)

- must_output：
  - 时间线
  - 变化方向
  - 是否满足定义

## definition_elements (`definition_elements`)

- 条件：时间前后
- 方式：变化过程
- 结果：变化后状态

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）

## 方法 ID (`id`)

dj_time_change_001

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

时间变化

## 方法名称 (`method_name`)

时间前后与变化对比法
