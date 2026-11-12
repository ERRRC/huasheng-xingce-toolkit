# 假设分配法求基期与增长量

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

data_analysis_006_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

速算技巧

## 子题型 (`sub_type`)

假设分配法

## 方法名称 (`method_name`)

假设分配法求基期与增长量

## 别名 (`aliases`)

- 分配法
- 画树法

## 检索标签 (`tags`)

- 假设分配法
- 增长量
- 基期
- 小增长率

## 适用条件 (`trigger_conditions`)

已知本期量和增长率求增长量，尤其当增长率R较小（<10%）或难以使用份数法时

## 不适用条件 (`anti_conditions`)

选项差距极小，需要极高精度

## 所需信息 (`required_inputs`)

- 本期量B
- 增长率R

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_method：将本期量拆分为大数和小数，大数精确计算，小数近似计算，最后相加得出增长量X

## 原程序优先级 (`solver_priority`)

- tier：fallback
- rank：70
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 确定被分配数（本期量B）和增长率R
- 2. 画出分配树，将本期量B拆分为A1和A2（通常A1是一个整百整千好算的数），对应X拆分为X1和X2
- 3. 对大数部分A1，精确计算X1 = A1 * R
- 4. 对小数部分A2，直接近似 X2 ≈ A2 * R（误差可忽略）
- 5. 最终结果：基期A = A1 + A2，增长量X = X1 + X2
- 6. 如果只求最后一步修正，当R<20%时，X ≈ B*R；R在25%左右，A:X=4:1...依此类推，最后进行修正

## 公式 (`formulas`)

- X ≈ B * R (当R较小时)

## 示例 (`examples`)

-
  - context：B=1350, R=19%
  - action：将1350拆分为1000和350（350再拆为150和200等），1000对应的X为190，剩余部分近似计算，最后汇总相加得出X

## 易错点 (`pitfalls`)

- 分配时大数和小数拆分不合理，导致后续计算依然繁琐
- 忽略了R较大时 X ≈ B*R 的巨大误差

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 计算得出高精度的增长量X

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 145

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
