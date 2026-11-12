# ABRX核心公式：基期与现期

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

data_analysis_007_new

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

ABRX类

## 子题型 (`sub_type`)

基期与现期计算

## 方法名称 (`method_name`)

ABRX核心公式：基期与现期

## 别名 (`aliases`)

- 求基期
- 求现期
- 求隔年基期

## 检索标签 (`tags`)

- 基期
- 现期
- 隔年基期
- ABRX

## 适用条件 (`trigger_conditions`)

题目中已知现期求基期，或已知基期求现期

## 不适用条件 (`anti_conditions`)

- （空列表）

## 所需信息 (`required_inputs`)

- 本期量B
- 增长率R
- 增长量X
- 基期量A
- 年份差

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_method：利用基本公式及变形求解

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 直接求前期（基期）：A = B / (1+R) = B - X = X / R
- 2. 求隔年前期：先用公式求出隔年增长率，再求隔年前期
- 3. 求前期差值：分别求出A1和A2，然后进行做差判断
- 4. 假设增量求现期：先求出X的具体值，列出对应不等式：当年的量 + n年*增量x
- 5. 假设增速求现期：B = A + A*R，依次求出后一年，一般2到3次即可

## 公式 (`formulas`)

- A = B / (1+R)
- A = B - X
- A = X / R
- B = A * (1+R)
- B = A + A*R

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 求隔年基期时忘记考虑间隔增长率的复利效应

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 得出基期或现期的具体数值

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 146

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
