# 或且关系否定法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_or_and_negation_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

选言/联言命题

## 方法名称 (`method_name`)

或且关系否定法

## 检索标签 (`tags`)

- 或且关系
- 矛盾关系
- 命题否定

## 适用条件 (`trigger_conditions`)

- 题干或选项出现A或B、A且B、并非、不同意
- 问某人不同意是什么意思

## 不适用条件 (`anti_conditions`)

- 题干是比例/实验论证时，仅作为局部命题工具

## 解题步骤 (`steps`)

- A或B 的否定为 ¬A且¬B。
- A且B 的否定为 ¬A或¬B。
- 要么A要么B同真同假均为假；或者A或者B同假为假。
- 先翻译原句，再整体取否定。
- 避免只否定其中一个分支。

## 公式 (`formulas`)

- ¬(A∨B)=¬A∧¬B
- ¬(A∧B)=¬A∨¬B

## 示例 (`examples`)

- 衣服不搭配无所谓，不买基金会心碎；不同意即至少否定其中一个分支。

## 易错点 (`pitfalls`)

- 只否定A不处理B
- 把要么和或者混同
- 忽视同真同假情况

## 避免事项 (`forbidden`)

- 不得把自然语言的'或者'随意当作排他或

## 来源文件 (`source_file`)

- 【判断推理】逻辑基本知识.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】逻辑基本知识.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 14
    - 15

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- compound_statement
- negation_prompt
- options

## 计算策略 (`calculation_policy`)

- mode：symbolic_negation
- verification：
  - identify connective
  - negate whole statement
  - check option

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- must_output：
  - original_form
  - negated_form
- must_not_output：
  - 只取局部否定

## argument_structure (`argument_structure`)

- claim：判断复合命题否定或推出关系。
- evidence：A或B、A且B、不同意等表达。
- link：使用德摩根律和选言命题真假关系。

## strength_order (`strength_order`)

- （空列表）
