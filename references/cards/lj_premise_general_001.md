# 前提假设没它不行检验法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_premise_general_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

前提假设

## 子题型 (`sub_type`)

前提总原则

## 方法名称 (`method_name`)

前提假设没它不行检验法

## 检索标签 (`tags`)

- 前提假设
- 没它不行
- 必要条件

## 适用条件 (`trigger_conditions`)

- 需要补充的前提是
- 上述结论成立还需基于
- 以下哪项是前提
- 假设是

## 不适用条件 (`anti_conditions`)

- 问最能支持时不要把所有支持项都当作前提

## 解题步骤 (`steps`)

- 先找论点、论据和论证缺口。
- 对每个选项做否定代入：如果否定该选项，结论是否无法成立。
- 若没有该选项论证必然断裂，则是前提。
- 若选项只是让结论更好但不必需，则不是最优前提。
- 优先选择连接断点、补充漏洞、保证可行性的选项。

## 公式 (`formulas`)

- 前提判定：选没它不行，不选有它更好

## 示例 (`examples`)

- 火星冰原例题中，沸石、硫化物和黏土仅在冰川下火山活动后产生，补足从矿物到冰下火山的前提。

## 易错点 (`pitfalls`)

- 把强支持误当必要前提
- 否定代入时否定错范围
- 选了只重复论点的选项

## 避免事项 (`forbidden`)

- 不得选有它更好但没它仍可成立的选项

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
    - 12

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- evidence
- options

## 计算策略 (`calculation_policy`)

- mode：assumption_test
- test：negate_option_then_argument_breaks

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- must_output：
  - negation_test
  - premise_type
- must_not_output：
  - 把普通支持项当作前提

## argument_structure (`argument_structure`)

- claim：题干结论。
- evidence：题干论据。
- link：前提是论据推出论点不可缺少的条件。

## strength_order (`strength_order`)

- 没它不行的断点搭桥/必要条件：最强
- 补充直接证据缺失或关键漏洞：强
- 能与不能/可行性条件：强
- 有它更好但没它仍可成立：不是前提
- 主体话题无关：排除
