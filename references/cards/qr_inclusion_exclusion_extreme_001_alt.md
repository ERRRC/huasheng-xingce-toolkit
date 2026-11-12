# 容斥问题极值分析 (至少至多判断)

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_inclusion_exclusion_extreme_001_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

特殊考点

## 子题型 (`sub_type`)

容斥极值

## 方法名称 (`method_name`)

容斥问题极值分析 (至少至多判断)

## 别名 (`aliases`)

- 容斥极值
- 占比重叠极值

## 检索标签 (`tags`)

- 资料分析
- 容斥问题
- 交集极值

## 适用条件 (`trigger_conditions`)

题目给出部分占比，询问两属性重叠（交集）的'至少'或'至多'或'一定有'情况。

## 不适用条件 (`anti_conditions`)

已知具体交集数值的普通容斥题。

## 所需信息 (`required_inputs`)

- 集合A占比
- 集合B占比

## 推理策略 (`reasoning_policy`)

- core_logic：基于集合相斥和包含原理求交集极值。
- detailed_policy：
  - 1. 占比和超过100%，必然存在交集。
  - 2. 求'至多'，则让大集合完全包含小集合，交集极值即为小集合占比 min(A, B)。
  - 3. 求'至少'，则让两集合尽量相斥，交集极值 = A + B - 100%。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：15
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 提取两个群体占比A和B。
- 求至多交集，直接选A和B中较小者。
- 求至少交集，计算A+B-100%。

## 公式 (`formulas`)

- 至多交集 = min(A, B)
- 至少交集 = A + B - 100%

## 示例 (`examples`)

-
  - context：男生占50%，南方同学占80%。问至多有多少南方男生？至少有多少南方男生？
  - action：至多：50%（80%包含50%）。至少：80%+50%-100% = 30%。

## 易错点 (`pitfalls`)

- 至多和至少使用的公式记混。

## 避免事项 (`forbidden`)

- 认为两个占比独立，使用A×B来求交集。

## 原卡输出约束 (`output_constraints`)

- 得出重叠比例的极值

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 8

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
