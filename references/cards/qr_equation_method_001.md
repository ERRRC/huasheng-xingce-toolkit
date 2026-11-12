# 和差倍比与问什么设什么

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_equation_method_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

方程问题

## 子题型 (`sub_type`)

普通方程

## 方法名称 (`method_name`)

和差倍比与问什么设什么

## 检索标签 (`tags`)

- 方程法
- 和差倍比
- 代入排除
- 比例

## 适用条件 (`trigger_conditions`)

- 题干出现和、差、倍、比、共、剩余、增加减少
- 未知量关系明确

## 不适用条件 (`anti_conditions`)

- 若可用整除、尾数或选项直接秒杀，应优先快速筛选；若变量过多再考虑不定方程

## 解题步骤 (`steps`)

- 优先用条件中的倍数、比例或特性筛选选项
- 找等量关系，问什么设什么
- 根据题意列方程或方程组
- 结合选项代入验证

## 公式 (`formulas`)

- 常见等量关系：总量=部分之和；A/B=给定比例；变化后量=原量±变化量

## 示例 (`examples`)

- 笔记第7页强调“先排除、再列式”，普通方程可用代入法与特性法减少计算

## 易错点 (`pitfalls`)

- 直接设多个未知数导致方程冗余
- 忽略题干中的整数、倍数、奇偶限制

## 避免事项 (`forbidden`)

- 不要脱离题干关系凭直觉配平

## 来源文件 (`source_file`)

- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生数量关系笔记.pdf
  - pages：
    - 7

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 未知量
- 等量关系
- 比例或倍数关系
- 整数限制
- 选项

## 计算策略 (`calculation_policy`)

- mode：option_filter_then_equation
- allow_exact_calculation：true
- preferred_tools：
  - 代入排除
  - 方程法
  - 比例法

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 数值
  - 选项
- must_report：核心等量关系
