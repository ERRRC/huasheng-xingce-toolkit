# 逆否命题等价验证法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_inverse_contrapositive_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

命题等价

## 方法名称 (`method_name`)

逆否命题等价验证法

## 检索标签 (`tags`)

- 逆否命题
- 真假表
- 翻译推理

## 适用条件 (`trigger_conditions`)

- 问由此可以推出
- 选项为条件命题变形
- 需要判断真假等价

## 不适用条件 (`anti_conditions`)

- 题干是归因论证时不要只用真假表替代论证分析

## 解题步骤 (`steps`)

- 将题干条件命题写成 A→B。
- 写出逆否命题 ¬B→¬A，二者等价。
- 识别逆命题 B→A 与否命题 ¬A→¬B，二者互相等价但不等价于原命题。
- 用真假表或箭头规则排除肯后、否前选项。
- 只选择原命题或逆否命题能推出的选项。

## 公式 (`formulas`)

- A→B ⇔ ¬B→¬A
- ¬A→¬B ⇔ B→A

## 示例 (`examples`)

- 经济可持续发展→保护生态环境；经济不可持续发展不能推出没有保护生态环境。

## 易错点 (`pitfalls`)

- 肯定后件
- 否定前件
- 把逆命题当等价

## 避免事项 (`forbidden`)

- 不得用生活常识补足 B→A

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
    - 16

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- translated_condition
- options

## 计算策略 (`calculation_policy`)

- mode：formal_equivalence
- verification：
  - original
  - contrapositive
  - reject_converse
  - reject_inverse

## 原程序优先级 (`solver_priority`)

15

## 原卡输出约束 (`output_constraints`)

- must_output：
  - equivalent_form
  - invalid_forms
- must_not_output：
  - 把可能成立当必然推出

## argument_structure (`argument_structure`)

- claim：判断条件命题选项是否等价。
- evidence：题干条件命题。
- link：原命题仅与逆否命题等价。

## strength_order (`strength_order`)

- （空列表）
