# 基期量直接公式法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_abx_base_direct_001

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

基期量

## 子题型 (`sub_type`)

已知现期量B和增长率R求基期A

## 方法名称 (`method_name`)

基期量直接公式法

## 检索标签 (`tags`)

- ABRX
- 基期量
- 前期量
- 现期量
- 增长率

## 适用条件 (`trigger_conditions`)

- 题干给出现期量B和同比增长率R，问上年、去年、前期、基期量
- 题干出现‘比上年增长/下降R%’，问题问上一时期的量

## 不适用条件 (`anti_conditions`)

- 题目要求隔年前期时，应先处理间隔增长率
- 题目只比较大小且选项差距很大时，可用估算或415份数法替代精算

## 解题步骤 (`steps`)

- 识别现期量B与增长率R
- 增长为正时用A=B/(1+R)，下降为负时用A=B/(1-R的绝对值)
- 若R接近常用分数，转化为份数估算
- 结合选项差距决定精算、直除或估算

## 公式 (`formulas`)

- A = B / (1 + R)
- X = B - A = B - B/(1+R)
- 也可记为：A = B - X = X/R

## 示例 (`examples`)

- 思维导图示例：政府债券8996亿元、同比增长约68.37%，用假设分配或415份数法估算前期。
- 笔记页ABRX类将‘直接求前期’列为基期A第一类公式。

## 易错点 (`pitfalls`)

- 把现期量B误当基期量A
- 增长率下降时分母应小于1，不可机械写1+R正数
- 选项差距大时过度精算浪费时间

## 避免事项 (`forbidden`)

- 未区分增长和下降就写1+R
- 把增长率百分点变化当作增长率本身

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

- 现期量B
- 增长率R
- 目标基期时间
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
- 结果通常输出为百分数%
- 不得把百分点变化直接当作增长率
- 结果单位应与材料原量单位一致
- 下降率参与分母时要保留负向关系
