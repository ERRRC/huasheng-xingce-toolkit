# 增量比较法 (大大则大)

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_increment_comparison_001_new

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

大小比较

## 子题型 (`sub_type`)

增量比较

## 方法名称 (`method_name`)

增量比较法 (大大则大)

## 别名 (`aliases`)

- 大大则大
- 一大一小看倍数

## 检索标签 (`tags`)

- 资料分析
- 增量比较
- 大大则大

## 适用条件 (`trigger_conditions`)

已知多个对象的现期量B和正的增长率R，比较它们的增量X大小。

## 不适用条件 (`anti_conditions`)

增长率为负数或相差极大需精确计算的情境。

## 所需信息 (`required_inputs`)

- 现期量B
- 增长率R

## 推理策略 (`reasoning_policy`)

- core_logic：增量 X = B × (R / (1+R))。现期量大且增长率大的，增量必定大。
- detailed_policy：
  - 规则1：B越大，R越大，则增量X越大（大大则大）。
  - 规则2：一大一小看倍数。若B1是B2的n倍，而R2是R1的n倍以上时，两者增量才可能相等。所以比较倍数差别的悬殊程度。

## 计算策略 (`calculation_policy`)

- core_logic：增长率超过10%的判断。
- detailed_policy：
  - 方法①：R = (B-A)/A = X/A > 10%。
  - 方法②：A + 0.1A < B。

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：15
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 提取对象的现期量B和增长率R。
- 若某对象的B和R均大于另一个对象，直接得出前者增量更大的结论。
- 若一对象B大，另一对象R大，观察倍数关系决定增量大小。

## 公式 (`formulas`)

- X = B × (R / (1+R))
- X = A × R = (B / (1+R)) × R

## 示例 (`examples`)

-
  - context：比较A(B=1000, R=10%)和B(B=800, R=5%)的增量大小
  - action：因为A的现期量和增长率都大于B，根据'大大则大'，A的增量一定大于B的增量。

## 易错点 (`pitfalls`)

- 增长率为负数时盲目套用大大则大。

## 避免事项 (`forbidden`)

- 直接对所有数据使用增量公式强行计算。

## 原卡输出约束 (`output_constraints`)

- 得出增量的大小顺序

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 6

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
