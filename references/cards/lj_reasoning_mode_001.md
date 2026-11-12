# 演绎/归纳/类比推理识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_reasoning_mode_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

逻辑基本知识

## 方法名称 (`method_name`)

演绎/归纳/类比推理识别法

## 检索标签 (`tags`)

- 推理方式
- 演绎推理
- 归纳推理
- 类比推理

## 适用条件 (`trigger_conditions`)

- 问所犯逻辑错误最相似
- 问推理方式最相近
- 题干给出论证模式而非具体真假

## 不适用条件 (`anti_conditions`)

- 问加强削弱力度时不优先用推理方式识别

## 解题步骤 (`steps`)

- 演绎推理：从一般规则到个体结论，常见三段论。
- 归纳推理：从部分样本概括总体，注意不完全归纳。
- 类比推理：两个对象在某些方面相似，推出其他方面相似。
- 比较题干与选项的结构，不比较具体内容是否真实。
- 优先选逻辑错误或推理路径相同的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 五岳归来不看山与桂林山水甲天下都属于不完全归纳式表达。

## 易错点 (`pitfalls`)

- 用常识判断选项真假
- 只看主题相似不看推理结构

## 避免事项 (`forbidden`)

- 不得把内容相似当作推理方式相同

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

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- argument_text
- options

## 计算策略 (`calculation_policy`)

- mode：structure_matching
- verification：
  - general_to_particular
  - particular_to_general
  - analogy_mapping

## 原程序优先级 (`solver_priority`)

35

## 原卡输出约束 (`output_constraints`)

- must_output：
  - reasoning_type
  - matching_basis
- must_not_output：
  - 仅按题材选择

## argument_structure (`argument_structure`)

- claim：识别题干推理方式。
- evidence：题干论证路径。
- link：与选项做结构匹配。

## strength_order (`strength_order`)

- （空列表）
