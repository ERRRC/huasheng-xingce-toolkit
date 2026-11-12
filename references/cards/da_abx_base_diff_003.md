# 前期差值比较法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_abx_base_diff_003

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

基期量

## 子题型 (`sub_type`)

前期差值

## 方法名称 (`method_name`)

前期差值比较法

## 检索标签 (`tags`)

- ABRX
- 前期差值
- 基期差
- 比较

## 适用条件 (`trigger_conditions`)

- 题干问两个对象在上年、去年、前期相差多少
- 题干给出现期量与增长率，需要比较A1-A2

## 不适用条件 (`anti_conditions`)

- 只问单个前期量时优先用基期量直接公式法
- 选项为趋势判断时不必求精确差值

## 解题步骤 (`steps`)

- 分别识别两个对象的现期量B1、B2及增长率R1、R2
- 分别估算前期A1、A2
- 计算A1-A2并根据选项差距确定精度

## 公式 (`formulas`)

- A1 - A2 = B1/(1+R1) - B2/(1+R2)

## 示例 (`examples`)

- 思维导图ABRX页在‘前期A’下列出‘前期差值’，示例用假设分配估算两项前期量后相减。

## 易错点 (`pitfalls`)

- 直接用现期差替代前期差
- 两个对象增长率不同却只用一个折扣
- 差值正负方向写反

## 避免事项 (`forbidden`)

- 未分别求A1、A2就做差
- 把增长量差当作前期差

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

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 两个对象的现期量B1/B2
- 两个对象的增长率R1/R2
- 需要比较的前期差值方向或数值

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
  - da_abx_base_direct_001
  - da_truncate_division_001

## 原卡输出约束 (`output_constraints`)

- 输出前必须核对时间、主体、单位
- 若为选择题，优先给出最接近选项
- 结果单位应与材料原量单位一致
- 下降率参与分母时要保留负向关系
