# 所有/有些/可能/必然关系转换法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_relation_quantifier_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

范畴关系

## 方法名称 (`method_name`)

所有/有些/可能/必然关系转换法

## 检索标签 (`tags`)

- 范畴关系
- 可能必然
- 所有有些
- 矛盾关系

## 适用条件 (`trigger_conditions`)

- 出现所有、有些、可能、必然
- 问矛盾命题、等价关系、真假关系

## 不适用条件 (`anti_conditions`)

- 普通加强削弱题不优先使用该规则，除非选项有严格量词

## 解题步骤 (`steps`)

- 识别量词：所有、有些、可能、必然。
- 所有A是B的矛盾通常对应有些A不是B；有些A是B的矛盾通常对应所有A不是B。
- 可能与必然的否定按不可能/不必然处理。
- 判断选项时先保留量词范围，不随意扩大或缩小。
- 若题干问推出，优先选保守结论。

## 公式 (`formulas`)

- 所有A是B ↔ 矛盾：有些A不是B
- 有些A是B ↔ 矛盾：所有A不是B

## 示例 (`examples`)

- 笔记中将所有/有些、可能/必然列为范畴与矛盾关系。

## 易错点 (`pitfalls`)

- 把有些理解成只有少数
- 把可能当必然
- 偷换范畴范围

## 避免事项 (`forbidden`)

- 不得从有些A是B推出所有A是B

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
    - 15
    - 18

## 原卡置信度 (`confidence`)

0.86

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- quantifier_statement
- options

## 计算策略 (`calculation_policy`)

- mode：quantifier_logic
- verification：
  - keep_scope
  - check_contradiction
  - avoid_overgeneralization

## 原程序优先级 (`solver_priority`)

25

## 原卡输出约束 (`output_constraints`)

- must_output：
  - quantifier
  - scope
  - validity
- must_not_output：
  - 扩大有些为全部

## argument_structure (`argument_structure`)

- claim：判断量词命题能否推出或矛盾。
- evidence：题干量词表达。
- link：根据范畴关系保守推断。

## strength_order (`strength_order`)

- （空列表）
