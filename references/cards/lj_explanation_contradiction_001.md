# 看似矛盾现象合理解释法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_explanation_contradiction_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

解释说明

## 子题型 (`sub_type`)

矛盾解释

## 方法名称 (`method_name`)

看似矛盾现象合理解释法

## 检索标签 (`tags`)

- 解释说明
- 矛盾现象
- 合理事实

## 适用条件 (`trigger_conditions`)

- 最能解释上述现象
- 最能解释上述矛盾
- 为什么出现这种情况
- 看似矛盾

## 不适用条件 (`anti_conditions`)

- 问法为加强/削弱且没有矛盾双方时不适用

## 解题步骤 (`steps`)

- 找出题干中看似矛盾的两个事实 A 与 B。
- 不要急于支持或削弱结论，而是寻找能同时容纳 A 和 B 的理由。
- 选项应是题干未提及但合理、容易被忽略的事实。
- 理由不能像借口，越能让人接受越好。
- 排除只解释一边或与矛盾无关的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 养生节目试播好评但正式播出收视率低，播出时间较晚、大多数老人已休息可同时解释两方面。

## 易错点 (`pitfalls`)

- 只解释正式播出差但不解释试播好
- 把加强结论当解释矛盾
- 选项过于牵强

## 避免事项 (`forbidden`)

- 不得把矛盾题做成支持题
- 不得选择只能解释一半的选项

## 来源文件 (`source_file`)

- 【判断推理】支持、前提假设、比例、解释说明.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】支持、前提假设、比例、解释说明.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 13

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- phenomenon_a
- phenomenon_b
- options

## 计算策略 (`calculation_policy`)

- mode：explain_paradox
- verification：
  - covers_A
  - covers_B
  - reasonable_fact

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- must_output：
  - contradiction_pair
  - explanation
- must_not_output：
  - 把解释项说成加强项

## argument_structure (`argument_structure`)

- claim：解释题通常没有要证明的论点，而是存在A与B两事实冲突。
- evidence：题干给出的两侧现象。
- link：选项提供第三事实，使A和B可同时成立。

## strength_order (`strength_order`)

- 同时解释矛盾双方：最强
- 只解释一方：弱
- 解释与题干无关现象：无关
- 与题干事实冲突：排除
