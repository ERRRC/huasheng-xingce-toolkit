# 如果/只要/所有都前推后翻译法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_translation_if_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

结论推出

## 子题型 (`sub_type`)

假言命题

## 方法名称 (`method_name`)

如果/只要/所有都前推后翻译法

## 检索标签 (`tags`)

- 翻译推理
- 假言命题
- 前推后

## 适用条件 (`trigger_conditions`)

- 如果A那么B
- 只要A就B
- 若A则B
- 所有A都B

## 不适用条件 (`anti_conditions`)

- 出现只有A才B时不要用前推后，应使用后推前

## 解题步骤 (`steps`)

- 将如果、只要、若、所有都的前半句作为前件 A。
- 将后半句作为后件 B。
- 写成 A→B。
- 验证选项是否为 A→B 或 ¬B→¬A。
- 排除 B→A 与 ¬A→¬B。

## 公式 (`formulas`)

- 如果A那么B：A→B
- 只要A就B：A→B
- 所有A都B：A→B

## 示例 (`examples`)

- 如果发生通货膨胀，那么人民就会遭受损失：通货膨胀→遭受损失。

## 易错点 (`pitfalls`)

- 把所有A都B翻译成B→A
- 把肯后当作有效推理

## 避免事项 (`forbidden`)

- 不得忽略否定词
- 不得把原命题与逆命题混同

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

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- conditional_text
- options

## 计算策略 (`calculation_policy`)

- mode：symbolic_logic
- verification：
  - translate
  - contrapositive
  - reject converse/inverse

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- must_output：
  - A
  - B
  - A_to_B
  - option_check
- must_not_output：
  - 把必要条件词混入本规则

## argument_structure (`argument_structure`)

- claim：判断选项是否由假言命题推出。
- evidence：题干如果/只要/所有都结构。
- link：前推后与逆否等价。

## strength_order (`strength_order`)

- （空列表）
