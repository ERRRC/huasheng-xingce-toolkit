# 增长量公式与方法选择

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_growth_amount_001

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

增长量

## 子题型 (`sub_type`)

直接求增长量X

## 方法名称 (`method_name`)

增长量公式与方法选择

## 检索标签 (`tags`)

- 增长量
- X
- ABRX
- 415份数法
- 假设分配法
- 直除

## 适用条件 (`trigger_conditions`)

- 题干问增长量、增加多少、减少多少、多多少、少多少
- 给出现期量B和增长率R，或基期量A和增长率R
- 选项单位与原量单位相同

## 不适用条件 (`anti_conditions`)

- 题干问增长率时不可把增长量当答案
- 问比重差或百分点变化时不属于增长量

## 解题步骤 (`steps`)

- 若A和R明确，用X=A×R；若B和R明确，用X=B×R/(1+R)
- 先看选项差距：差距大则估算，差距小则直除或代入
- R≥10%且能靠近分数时优先考虑415份数法
- R<10%时可用假设分配法；R≤5%或非常小，可近似X≈B×R
- 增长率为负时注意增长量为负，下降量取绝对值

## 公式 (`formulas`)

- X = B - A = A×R
- X = B×R/(1+R)
- R≤5%且粗略判断时：X≈B×R

## 示例 (`examples`)

- 思维导图ABRX页直接求X分支提示：R在分数附近用415份数法，假设分配法用于估算，极少数可用B×R代替A×R。
- 笔记ABRX页列出计算方法选择：选项有一定差距时R≥10%靠分数考虑415，R<10%用假设分配，R非常小近似X≈BR。

## 易错点 (`pitfalls`)

- 用B×R作为精确增长量，忽略分母1+R
- 题干问减少量却把负号带入选项
- 增长率很大时仍用近似导致误差过大

## 避免事项 (`forbidden`)

- 选项接近时使用粗略近似
- 不判断增长率正负就直接求正数

## 来源文件 (`source_file`)

- 【花生十三】资料分析思维导图.pdf
- 花生资料分析笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】资料分析思维导图.pdf
  - pages：
    - 1
-
  - file：花生资料分析笔记.pdf
  - pages：
    - 7

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 现期量B或基期量A
- 增长率R
- 题目所求增长量/减少量
- 选项单位

## 计算策略 (`calculation_policy`)

- default：先识别ABRX/分式结构，再套用对应公式；能估则估，必要时直除。
- precision：按选项差距决定估算、截位或精算
- allowed：
  - 公式法
  - 截位直除
  - 分数化估算
- avoid：
  - 未审题直接代数值
  - 把百分点当百分数
- verify：
  - 时间口径
  - 主体口径
  - 单位口径

## 原程序优先级 (`solver_priority`)

- tier：core_formula
- rank：10
- fallback_method_ids：
  - da_415_parts_001
  - da_assumption_allocation_001
  - da_truncate_division_001

## 原卡输出约束 (`output_constraints`)

- 输出前必须核对时间、主体、单位
- 若为选择题，优先给出最接近选项
- 结果单位应与原始数量单位一致
- 减少量可输出正值并说明方向
