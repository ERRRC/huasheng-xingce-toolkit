# 等价命题与选项替换法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_conclusion_equivalent_inference_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

等价推出

## 方法名称 (`method_name`)

等价命题与选项替换法

## 检索标签 (`tags`)

- 等价推出
- 逆否
- 推出类

## 适用条件 (`trigger_conditions`)

- 选项与题干条件命题形式不同但可能等价
- 问一定可以推出

## 不适用条件 (`anti_conditions`)

- 归因论证题不要用等价命题替代论证分析

## 解题步骤 (`steps`)

- 将题干命题标准化。
- 寻找等价变形，如逆否命题。
- 若选项只是逆命题或否命题，不能当作等价。
- 逐项转换为标准式后比较。
- 选择完全等价或必然被推出的选项。

## 公式 (`formulas`)

- A→B ⇔ ¬B→¬A

## 示例 (`examples`)

- 笔记推出类页面将等价推出和比较选项逻辑关系作为推出类技巧。

## 易错点 (`pitfalls`)

- 形式相似但方向相反
- 命题范围变化

## 避免事项 (`forbidden`)

- 不得因语序相近就判等价

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
    - 16

## 原卡置信度 (`confidence`)

0.86

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- logical_form
- options

## 计算策略 (`calculation_policy`)

- mode：equivalence_check
- verification：
  - normalize
  - compare_equivalent_forms

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- must_output：
  - normalized_form
  - equivalence_result
- must_not_output：
  - 忽略方向和否定

## argument_structure (`argument_structure`)

- claim：选项是否与题干命题等价。
- evidence：题干命题形式。
- link：形式等价才可推出。

## strength_order (`strength_order`)

- （空列表）
