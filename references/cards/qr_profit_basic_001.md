# 成本、售价、利润率基础公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_profit_basic_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

经济利润问题

## 子题型 (`sub_type`)

单件与多件销售

## 方法名称 (`method_name`)

成本、售价、利润率基础公式

## 检索标签 (`tags`)

- 利润
- 成本
- 售价
- 折扣
- 利润率

## 适用条件 (`trigger_conditions`)

- 题干出现成本、售价、定价、折扣、利润、利润率
- 问单件或总利润

## 不适用条件 (`anti_conditions`)

- 若题干涉及多批销售收入相加，优先分批销售利润方程

## 解题步骤 (`steps`)

- 先明确成本、定价、实际售价、利润率
- 按单件或数量乘积建立总收入/总成本/总利润
- 折扣题先把定价转换为实际售价
- 求所问变量

## 公式 (`formulas`)

- 利润=售价-成本
- 利润率=利润/成本
- 售价=成本×(1+利润率)
- 实际售价=定价×折扣
- 总利润=数量×单件利润

## 示例 (`examples`)

- 笔记第17页强调“利润问题一般可用方程法，算售价可用赋值法”

## 易错点 (`pitfalls`)

- 利润率分母错用售价
- 折扣未转化为实际售价
- 数量乘漏

## 避免事项 (`forbidden`)

- 不要把利润率当利润金额

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 17

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 成本
- 售价或定价
- 折扣
- 利润率
- 数量

## 计算策略 (`calculation_policy`)

- mode：formula_equation
- allow_exact_calculation：true
- preferred_tools：
  - 成本赋值
  - 方程法

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 利润
  - 售价
  - 成本
  - 利润率
  - 选项
- unit_check：利润率统一为小数或百分数
