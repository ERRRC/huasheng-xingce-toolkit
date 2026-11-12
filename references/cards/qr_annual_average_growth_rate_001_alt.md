# 年均增长率估算公式及常数记忆

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_annual_average_growth_rate_001_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

年均增长率

## 子题型 (`sub_type`)

近似计算

## 方法名称 (`method_name`)

年均增长率估算公式及常数记忆

## 别名 (`aliases`)

- 年均增速近似

## 检索标签 (`tags`)

- 资料分析
- 年均增长率
- 近似公式

## 适用条件 (`trigger_conditions`)

求一段时间内的年均增长率，选项差距较大需要估算时。

## 不适用条件 (`anti_conditions`)

选项极为接近，需要精确开n次方。

## 所需信息 (`required_inputs`)

- 末期量
- 基期量
- 年份差n

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_logic：利用二项式展开进行近似，或通过背诵常见次方常数快速估算。
- detailed_policy：
  - 近似公式：末期/基期 ≈ 1 + nR
  - 常数记忆：1.05^4 ≈ 1.216, 1.1^4 ≈ 1.46, 1.15^4 ≈ 1.75, 1.2^4 ≈ 2.07

## 原程序优先级 (`solver_priority`)

- tier：fallback
- rank：30
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 利用判定法则确认基期量，计算 末期量/基期量。
- 观察比值，对比记忆常数推测R范围。
- 若无法匹配常数，使用 近似公式 (末期/基期 - 1) / n 估算R。

## 公式 (`formulas`)

- 末期 / 基期 ≈ 1 + nR
- (1+R)^n = 末期 / 基期

## 示例 (`examples`)

-
  - context：计算末期/基期=1.46，n=4的年均增长率
  - action：利用记忆常数 1.1^4 ≈ 1.46，直接选10%附近的选项。

## 易错点 (`pitfalls`)

- 将 末期/基期 直接当成增长率。

## 避免事项 (`forbidden`)

- 考场上硬算高次开方。

## 原卡输出约束 (`output_constraints`)

- 得到年均增长率的估算百分比

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 7

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
