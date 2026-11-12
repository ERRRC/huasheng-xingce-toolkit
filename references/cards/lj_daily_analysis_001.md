# 日常分析列表/代入/画图法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_daily_analysis_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

分析推理

## 子题型 (`sub_type`)

日常分析

## 方法名称 (`method_name`)

日常分析列表/代入/画图法

## 检索标签 (`tags`)

- 日常分析
- 列表法
- 代入法
- 画图法

## 适用条件 (`trigger_conditions`)

- 题干给多人多条件匹配
- 问谁对应谁、顺序、位置或安排
- 条件较多且非形式逻辑

## 不适用条件 (`anti_conditions`)

- 条件命题清晰且可翻译时先用翻译推理

## 解题步骤 (`steps`)

- 识别对象、属性和限制条件。
- 条件少可直接代入选项。
- 多对象多属性优先列表。
- 位置或顺序关系优先画图。
- 每代入一步都回到题干验证全部条件。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记日常分析页列出识别方法和解题技巧：代入法、顺序法、画图法。

## 易错点 (`pitfalls`)

- 不建立表格导致漏条件
- 只验证选项局部条件

## 避免事项 (`forbidden`)

- 不得凭印象跳过条件核验

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 19

## 原卡置信度 (`confidence`)

0.87

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- objects
- attributes
- constraints
- options

## 计算策略 (`calculation_policy`)

- mode：constraint_solving
- prefer：
  - 代入法
  - 列表法
  - 画图法
- verification：
  - all_constraints_checked

## 原程序优先级 (`solver_priority`)

37

## 原卡输出约束 (`output_constraints`)

- must_output：
  - constraint_table_or_path
  - validated_option
- must_not_output：
  - 未逐条验证条件

## argument_structure (`argument_structure`)

- claim：确定对象匹配或安排结果。
- evidence：题干多个限制条件。
- link：通过代入、列表或画图满足所有约束。

## strength_order (`strength_order`)

- （空列表）
