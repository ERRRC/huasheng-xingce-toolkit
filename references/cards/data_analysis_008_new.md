# ABRX核心公式：增长率与增长量

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

data_analysis_008_new

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

ABRX类

## 子题型 (`sub_type`)

增长率与增长量计算

## 方法名称 (`method_name`)

ABRX核心公式：增长率与增长量

## 别名 (`aliases`)

- 求增长率
- 求增长量
- 间隔增长率
- 比值增长率
- 乘积增长率

## 检索标签 (`tags`)

- 增长率
- 增长量
- 间隔增长率
- 比值增长率
- 乘积增长率
- ABRX

## 适用条件 (`trigger_conditions`)

题目要求计算某指标的增长率、增长量，或者跨年份的间隔增长率，以及平均数/比重的增长率（比值/乘积形式）

## 不适用条件 (`anti_conditions`)

- （空列表）

## 所需信息 (`required_inputs`)

- 相关期的数值
- 部分与整体的增长率

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_method：匹配题目类型，套用相应的增长率或增长量公式

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 一般增长率：R = X / A
- 2. 间隔增长率：R间 = R1 + R2 + R1*R2 (注意可能有逆运用)
- 3. 比值增长率（平均数增长率）：符合 A = B/C 的形式。公式：Ra = (Rb - Rc) / (1 + Rc)。记忆口诀：比值倍数 = 比值增长率 + 1。询前每后敢分母
- 4. 乘积增长率：符合 A = B*C 的形式（如B*C有实际含义，或B*C表示占比）。公式：Ra = Rb + Rc + Rb*Rc
- 5. 求增长量：直接求X = B - A = A*R。若选项有一定差距且R较大，用415份数法；R较小用假设分配法或 X ≈ B*R；若选项差距小，用代入法或直除。

## 公式 (`formulas`)

- R = X / A
- R间 = R1 + R2 + R1*R2
- Ra = (Rb - Rc) / (1 + Rc)
- Ra = Rb + Rc + Rb*Rc
- X = B - A = A*R

## 示例 (`examples`)

-
  - context：2015年同比增长8.2%，2014年下降0.8个百分点，求2015年较2013年增长率
  - action：R1=8.2%, R2=9%。R间 = 9% + 8.2% + 9%*8.2% = 17.2% + 0.8% = 18%
-
  - context：已知R间 = 3.9%，R2=2.4%，求R1
  - action：逆用公式：3.9% = R1 + 2.4% + R1*2.4%，解得 R1 < 1.5%

## 易错点 (`pitfalls`)

- 间隔增长率计算漏掉 R1*R2 项
- 比值增长率分母 (1+Rc) 搞错符号

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 计算得出准确的百分比或绝对变化量

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 146
- 147

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
