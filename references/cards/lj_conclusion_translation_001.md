# 结论推出翻译-匹配-排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_conclusion_translation_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

推出类总流程

## 方法名称 (`method_name`)

结论推出翻译-匹配-排除法

## 检索标签 (`tags`)

- 结论推出
- 推出类
- 翻译推理
- 必然推出

## 适用条件 (`trigger_conditions`)

- 由此可以推出
- 以下哪项一定为真
- 可以得出
- 据此可知

## 不适用条件 (`anti_conditions`)

- 问加强/削弱/解释时不适用

## 解题步骤 (`steps`)

- 先判断是否为翻译推理、真假分析、范畴分析或日常分析。
- 若有条件词，先翻译为箭头式。
- 若有量词或真假话，保留命题范围并做真假约束。
- 只选择题干必然推出的保守结论。
- 排除可能为真但不必然为真的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 推出类笔记将逻辑基础、等价推出、正推/逆推、两难推理等作为推出题相关知识。

## 易错点 (`pitfalls`)

- 把可能推出当必然推出
- 用常识补充题干没有的信息

## 避免事项 (`forbidden`)

- 不得选超过题干信息范围的结论

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
    - 16

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem
- logical_statements
- options

## 计算策略 (`calculation_policy`)

- mode：deductive_inference
- verification：
  - translate_if_needed
  - derive_only_necessary
  - reject_extra_info

## 原程序优先级 (`solver_priority`)

7

## 原卡输出约束 (`output_constraints`)

- must_output：
  - inference_type
  - valid_option_basis
- must_not_output：
  - 加入题干外假设

## argument_structure (`argument_structure`)

- claim：选项是否为题干必然结论。
- evidence：题干命题、条件、范围。
- link：通过形式翻译或保守推断得到必然项。

## strength_order (`strength_order`)

- （空列表）
