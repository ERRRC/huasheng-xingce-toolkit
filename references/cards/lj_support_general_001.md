# 支持题主体话题一致原则

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_support_general_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强

## 子题型 (`sub_type`)

支持加强类

## 方法名称 (`method_name`)

支持题主体话题一致原则

## 检索标签 (`tags`)

- 支持类
- 加强
- 主体一致
- 话题一致

## 适用条件 (`trigger_conditions`)

- 最能支持上述结论
- 最能加强上述观点
- 以下哪项为真最能支持

## 不适用条件 (`anti_conditions`)

- 问需要补充的前提时优先前提假设流程
- 题干要求解释矛盾时优先解释说明流程

## 解题步骤 (`steps`)

- 先找论点和论据。
- 检查选项主体是否与论点主体一致。
- 检查选项话题是否与论证话题一致。
- 优先选择能贴合论据到论点关系的选项。
- 若多个选项都相关，按是否直接补断点或直接增加事实比较力度。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 银河系宜居星球例题中，加入恒星数量、红矮星比例、类地行星与水和大气事实可支持结论。

## 易错点 (`pitfalls`)

- 选项只谈背景但不服务论点
- 主体一致但话题偏离
- 把削弱项误认为补充事实

## 避免事项 (`forbidden`)

- 不得选择与题干主体不一致的泛泛常识

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

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- evidence
- options

## 计算策略 (`calculation_policy`)

- mode：strengthen
- prefer：
  - 主体一致
  - 话题一致
  - 贴合论证缺口
- avoid：
  - 无关背景
  - 只重复题干

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- must_output：
  - support_type
  - strength_reason
- must_not_output：
  - 只说选项正确不说明增强点

## argument_structure (`argument_structure`)

- claim：题干要被加强的结论。
- evidence：题干给出的支持性事实。
- link：选项应增强论据到论点的可接受度。

## strength_order (`strength_order`)

- 断点搭桥/必要条件：直接补足论据到论点的缺口，力度强
- 自断一臂/排除关键漏洞：排除最主要替代路径，力度强
- 加入论据和事实：直接增加支持事实，力度中强
- 解释说明机制：解释为什么论点可能成立，力度中等
- 举例或类比支持：支持但范围较窄，力度较弱
- 主体或话题不一致：无关
