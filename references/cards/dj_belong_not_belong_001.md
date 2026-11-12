# 属于/不属于方向控制法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_belong_not_belong_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

题干方向

## 方法名称 (`method_name`)

属于/不属于方向控制法

## 检索标签 (`tags`)

- 属于
- 不属于
- 问法识别
- 方向控制

## 适用条件 (`trigger_conditions`)

- 题干问属于/不属于/符合/不符合/最符合/最不符合
- 选项中多个看似符合定义

## 不适用条件 (`anti_conditions`)

- 题目不是定义判断，或问法不涉及符合/不符合定义

## 解题步骤 (`steps`)

- 先在草稿中写明本题要找“符合”还是“不符合”。
- 属于题：排除不符合定义项，保留最符合项。
- 不属于题：先确认多个符合项可作为理解定义的例子，再寻找唯一不符合项。
- 最后核对被选项是否与问法方向一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：闭环思维不属于题中，错误选项都是例子，可借用例子理解定义。

## 易错点 (`pitfalls`)

- 不属于题误选符合定义的典型项。
- 看完选项后忘记回到题干问法。

## 避免事项 (`forbidden`)

- 不得在未确认题干方向时输出答案。

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

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- ask_polarity
- definition_text
- options

## 计算策略 (`calculation_policy`)

- mode：polarity_control
- final_check_required：true

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- must_output：
  - ask_polarity
  - final_direction_check

## definition_elements (`definition_elements`)

- 问法：属于/不属于必须先定
- 主体：null
- 客体/对象：null
- 条件：null
- 方式：null
- 目的：null
- 结果：null
- 特殊要求：null

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
