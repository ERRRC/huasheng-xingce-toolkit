# 样本无效削弱法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_invalid_sample_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

样本不代表总体

## 方法名称 (`method_name`)

样本无效削弱法

## 检索标签 (`tags`)

- 样本不代表总体
- 调查样本
- 样本无效
- 削弱

## 适用条件 (`trigger_conditions`)

- 题干用某机构/某渠道/部分样本推出总体结论
- 选项指出样本遗漏主要群体或样本来源偏差

## 不适用条件 (`anti_conditions`)

- 题干只是讨论该样本内部结论时不适用

## 解题步骤 (`steps`)

- 识别题干样本来源和结论总体。
- 检查样本是否覆盖结论所指总体。
- 寻找选项是否指出大量总体成员未进入样本。
- 若样本来源偏差会改变比例或结论，强削弱。
- 排除只指出个别反例但不影响代表性的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 闪婚离婚例题中，仅调查法院审理案件，但协议离婚占总量70%，样本不能代表总体离婚情况。

## 易错点 (`pitfalls`)

- 只说最快离婚不是闪婚，不能代表总体
- 忽略样本来源和结论范围差异

## 避免事项 (`forbidden`)

- 不得用样本内比例直接推广总体

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

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- sample_source
- target_population
- sample_result
- options

## 计算策略 (`calculation_policy`)

- mode：sample_validity_check
- verification：
  - sample_scope
  - target_scope
  - coverage_gap

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- must_output：
  - sample_scope
  - target_population
  - representativeness_issue
- must_not_output：
  - 忽视样本外总体

## argument_structure (`argument_structure`)

- claim：样本结果可推出总体原因或总体比例。
- evidence：某样本调查结果。
- link：若样本不代表总体，结论不可靠。

## strength_order (`strength_order`)

- 样本遗漏主要总体或来源严重偏差：强
- 个别反例：弱
- 样本内补充事实：视是否影响代表性
- 无关背景：无效
