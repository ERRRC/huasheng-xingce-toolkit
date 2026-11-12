# 方式-目的-结果链检查法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_way_purpose_result_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

方式/目的/结果要素

## 方法名称 (`method_name`)

方式-目的-结果链检查法

## 检索标签 (`tags`)

- 方式
- 目的
- 结果
- 定义要素
- 链条匹配

## 适用条件 (`trigger_conditions`)

- 定义中出现“用/通过/借助/以达到/以利于/从而/结果”等链条词
- 选项行为相似但目的或结果不同

## 不适用条件 (`anti_conditions`)

- 题干没有方式、目的或结果链条时，不要强行拆链

## 解题步骤 (`steps`)

- 从定义中提取方式、目的、结果三个位置。
- 检查选项是否具有相同方式。
- 检查目的是否与定义一致。
- 检查结果是否符合定义描述。
- 任一关键链条断裂则排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：闭环思维体现用提示、应答形成封闭环，以利于把握进程和调整方向。
-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：工具性求助体现借助他人力量，以达自己解决问题或实现目标。

## 易错点 (`pitfalls`)

- 只看行为相似，忽略目的不一致。
- 把结果出现误当成方式满足。

## 避免事项 (`forbidden`)

- 不得在定义未要求目的时额外设定目的。

## 来源文件 (`source_file`)

- 【判断推理】定义判断.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】定义判断.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 20

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- definition_text
- means_clause
- purpose_clause
- result_clause
- options

## 计算策略 (`calculation_policy`)

- mode：causal_chain_check
- optional_fields_allowed：true

## 原程序优先级 (`solver_priority`)

7

## 原卡输出约束 (`output_constraints`)

- must_output：
  - means
  - purpose
  - result
  - broken_link_if_any

## definition_elements (`definition_elements`)

- 主体：辅助
- 客体/对象：辅助
- 条件：辅助
- 方式：重点检查
- 目的：重点检查
- 结果：重点检查
- 特殊要求：辅助

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
