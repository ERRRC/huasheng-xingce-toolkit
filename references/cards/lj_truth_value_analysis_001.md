# 真假分析矛盾-假设-代入法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_truth_value_analysis_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

分析推理

## 子题型 (`sub_type`)

真假分析

## 方法名称 (`method_name`)

真假分析矛盾-假设-代入法

## 检索标签 (`tags`)

- 真假分析
- 矛盾关系
- 假设法
- 代入法

## 适用条件 (`trigger_conditions`)

- 题干出现几人说真话/假话
- 只有一真/一假
- 问谁说真话或结论

## 不适用条件 (`anti_conditions`)

- 单纯论证加强削弱题不适用

## 解题步骤 (`steps`)

- 找矛盾：先看两句话是否一真一假。
- 找条件：根据题干真话/假话数量确定剩余话真假。
- 若无明显矛盾，使用假设法逐一代入。
- 代入选项或人物陈述，检查是否满足真假数量。
- 保留唯一满足条件的结果。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记分析类页面列出真假分析，强调看真假话和平衡关系。

## 易错点 (`pitfalls`)

- 没有先找矛盾就盲目假设
- 假设后忘记验证所有陈述

## 避免事项 (`forbidden`)

- 不得只验证一个条件就下结论

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 17
    - 18

## 原卡置信度 (`confidence`)

0.84

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- statements
- truth_count
- options

## 计算策略 (`calculation_policy`)

- mode：constraint_reasoning
- sequence：
  - find_contradictions
  - assign_truth_values
  - verify_all

## 原程序优先级 (`solver_priority`)

34

## 原卡输出约束 (`output_constraints`)

- must_output：
  - truth_assignment
  - verification
- must_not_output：
  - 只凭直觉判断真假

## argument_structure (`argument_structure`)

- claim：确定某个陈述或选项真假。
- evidence：所有人物陈述和真假数量约束。
- link：通过矛盾关系或假设代入满足约束。

## strength_order (`strength_order`)

- （空列表）
