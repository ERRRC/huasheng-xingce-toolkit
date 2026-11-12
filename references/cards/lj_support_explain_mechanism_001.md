# 解释说明式支持法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_support_explain_mechanism_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强

## 子题型 (`sub_type`)

解释机制

## 方法名称 (`method_name`)

解释说明式支持法

## 检索标签 (`tags`)

- 支持类
- 解释说明
- 机制解释
- 原因解释

## 适用条件 (`trigger_conditions`)

- 选项解释为什么论点成立
- 题干结论为某因素不利/有利于某结果
- 选项给出中间机制

## 不适用条件 (`anti_conditions`)

- 题干要求解释矛盾时应调用解释说明题流程，而非普通加强

## 解题步骤 (`steps`)

- 找出题干论点中的因果或作用关系。
- 看选项是否说明该因果关系的中间机制。
- 机制必须能解释结果为什么会发生。
- 若选项只说另一种无关结果，不优先。
- 机制越贴合题干结果，支持力度越强。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 担忧情绪不利于心脏病康复；选项说明严重担忧者血液中含加重心脏病风险的化学物质，解释了影响机制。

## 易错点 (`pitfalls`)

- 机制解释到其他疾病但没解释题干结果
- 只说相关不说为什么

## 避免事项 (`forbidden`)

- 不得把泛化危害当作特定机制

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
    - 11

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- factor
- result
- options

## 计算策略 (`calculation_policy`)

- mode：mechanism_support
- verification：
  - factor_to_mechanism
  - mechanism_to_result

## 原程序优先级 (`solver_priority`)

26

## 原卡输出约束 (`output_constraints`)

- must_output：
  - mechanism
  - target_result
- must_not_output：
  - 用无关后果替代机制

## argument_structure (`argument_structure`)

- claim：某因素导致或影响某结果。
- evidence：题干观察到的相关或结果。
- link：选项补充中间机制增强因果可信度。

## strength_order (`strength_order`)

- 断点搭桥/必要条件：直接补足论据到论点的缺口，力度强
- 自断一臂/排除关键漏洞：排除最主要替代路径，力度强
- 加入论据和事实：直接增加支持事实，力度中强
- 解释说明机制：解释为什么论点可能成立，力度中等
- 举例或类比支持：支持但范围较窄，力度较弱
- 主体或话题不一致：无关
