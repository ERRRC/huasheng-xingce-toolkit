# 415份数法求基期与变化量

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

data_analysis_005_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

速算技巧

## 子题型 (`sub_type`)

415份数法

## 方法名称 (`method_name`)

415份数法求基期与变化量

## 别名 (`aliases`)

- 份数法

## 检索标签 (`tags`)

- 份数法
- 增长量
- 基期量
- 百分数转分数

## 适用条件 (`trigger_conditions`)

已知本期量和增长率，求基期量或变化量（增长量），且增长率可以近似转化为简单的分数 1/n 或 a/b

## 不适用条件 (`anti_conditions`)

增长率极小（<5%）或无法转化为简单分数

## 所需信息 (`required_inputs`)

- 本期量
- 增长率

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_method：将增长率转化为分数 a/b，将本期量看作 a+b 份，基期量看作 b 份，变化量看作 a 份

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：90
- fallback_method_ids：
  - data_analysis_006

## 解题步骤 (`steps`)

- 1. 将增长率 R 化成相近的分数 a/b
- 2. 设定基期对应的份数为 b，变化量（增长量）为 a，则本期量的份数为 a+b
- 3. 根据 本期量具体数值 / (a+b) 求得『一份量』
- 4. 根据一份量的大小和求知目标（基期或变化量）对应的份数，计算最终结果
- 5. 误差控制：估大则一份变大、估小则一份变小。若增长率为负数，变化量也为负数，变为减法。

## 公式 (`formulas`)

- R ≈ a/b
- 本期量份数 = a+b
- 基期量份数 = b
- 变化量份数 = a

## 示例 (`examples`)

-
  - context：本期B=328，增长率R=49.8%，求变化量X和基期A
  - action：R ≈ 1/2。则变化量A:X:B = 2:1:3。X = (328/3)*1 ≈ 109，A = 328 - 109 = 219

## 易错点 (`pitfalls`)

- 增长率为负时，本期量份数算错（应为b-a）
- 未进行误差修正

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 求出近似的基期或增长量

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 145

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
