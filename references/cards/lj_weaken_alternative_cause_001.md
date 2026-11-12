# 另有他因削弱法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_alternative_cause_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

另有他因

## 方法名称 (`method_name`)

另有他因削弱法

## 检索标签 (`tags`)

- 质疑削弱
- 归因类
- 另有他因

## 适用条件 (`trigger_conditions`)

- 题干声称A导致B
- 选项提出另一个因素C也能导致B
- 对比实验中分组除了A还有其他差异

## 不适用条件 (`anti_conditions`)

- 选项提出的C不能解释B或与题干结果无关时不适用

## 解题步骤 (`steps`)

- 抽取题干原因 A 与结果 B。
- 寻找选项是否提出其他原因 C。
- 判断 C 是否能独立解释 B。
- 若 C 与A同时存在或更能解释结果，则削弱 A导致B。
- 对比实验中优先看C是否为两组差异因素。

## 公式 (`formulas`)

- A→B 被 C→B 削弱

## 示例 (`examples`)

- 焦虑实验例题中，高焦虑组实验前对任务不熟悉，也可导致错误率高，构成另有他因。

## 易错点 (`pitfalls`)

- C只是背景差异但不能解释结果
- C其实是A的结果而非替代原因

## 避免事项 (`forbidden`)

- 不得把无关差异当他因

## 来源文件 (`source_file`)

- 【判断推理】质疑类.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 5
    - 7

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claimed_cause_A
- effect_B
- alternative_cause_C
- options

## 计算策略 (`calculation_policy`)

- mode：alternative_cause
- verification：
  - C_explains_B
  - C_independent_from_A
  - fits_evidence

## 原程序优先级 (`solver_priority`)

11

## 原卡输出约束 (`output_constraints`)

- must_output：
  - alternative_cause
  - why_it_explains_effect
- must_not_output：
  - 把任何差异都当他因

## argument_structure (`argument_structure`)

- claim：A导致B。
- evidence：题干观察到A与B共同出现或组间差异。
- link：选项提出C导致B，从而A未必是原因。

## strength_order (`strength_order`)

- C能完全解释B且排斥A：最强
- C能部分解释B：中强
- C只是相关背景：弱
- C不能解释B：无关
