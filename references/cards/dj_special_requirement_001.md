# 特殊条件锁定法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_special_requirement_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

特殊要求

## 方法名称 (`method_name`)

特殊条件锁定法

## 检索标签 (`tags`)

- 特殊要求
- 条件
- 时间限定
- 场景限定

## 适用条件 (`trigger_conditions`)

- 定义中出现时间、场景、对象范围、关系类型等限定
- 选项主体行为相似但缺少限定条件

## 不适用条件 (`anti_conditions`)

- 定义没有限定条件，只有一般描述时，不要凭常识添加特殊要求

## 解题步骤 (`steps`)

- 圈出定义中的特殊要求，例如传统节日期间、工作学习过程中、借助他人等。
- 检查选项是否满足该要求。
- 若选项只满足一般行为但不满足特殊要求，排除。
- 特殊要求与主体/对象冲突时，以题干定义为准。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：亲情经济要求传统节日期间，店庆三周年不是传统节日。

## 易错点 (`pitfalls`)

- 把店庆、周年庆等商业节点误判为传统节日。
- 忽略定义中的时间或场景限定。

## 避免事项 (`forbidden`)

- 不得用现实中可能有关联的场景替代题干明示限定。

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

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- special_requirements
- option_context
- ask_polarity

## 计算策略 (`calculation_policy`)

- mode：hard_constraint_check
- eliminate_on_violation：true

## 原程序优先级 (`solver_priority`)

5

## 原卡输出约束 (`output_constraints`)

- must_output：
  - special_requirement
  - option_violation

## definition_elements (`definition_elements`)

- 主体：可选
- 客体/对象：可选
- 条件：重点检查
- 方式：null
- 目的：null
- 结果：null
- 特殊要求：必须匹配

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
