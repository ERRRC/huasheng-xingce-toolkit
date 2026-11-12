# 乘法截位与拆分技巧

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

data_analysis_003_new

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

速算技巧

## 子题型 (`sub_type`)

乘法速算

## 方法名称 (`method_name`)

乘法截位与拆分技巧

## 别名 (`aliases`)

- 截位相乘法
- 小分互换
- 乘法拆分

## 检索标签 (`tags`)

- 乘法速算
- 截位相乘
- 小分互换
- 乘法拆分

## 适用条件 (`trigger_conditions`)

遇到大数相乘、带百分数的乘法计算

## 不适用条件 (`anti_conditions`)

选项差距极小，必须精确到最后一位

## 所需信息 (`required_inputs`)

- 待相乘的两个数字
- 选项差距

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_method：截取两位有效数字进行乘法，或者将百分数转换为分数/拆分为常见百分数之和

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：80
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 截位相乘法：截取前2位数字，观察第3位。若第3位均<=2，则全舍；若均>=8，则全进；其他情况一进一舍
- 2. 小分互换：记住常见分数与百分数的转换关系，将百分数和分母互换位置
- 3. 乘法拆分：把乘数拆成常见的百分数相乘，再相加减

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - context：278.3 * 4695
  - action：截位相乘：第三位分别是8和9，全进，约等于 280 * 4700
-
  - context：592 * 97%
  - action：乘法拆分：592 * (100% - 3%) = 592 - 17.76 ≈ 574

## 易错点 (`pitfalls`)

- 截位时进舍规则使用错误导致误差过大
- 小分互换时分数记忆错误

## 避免事项 (`forbidden`)

- 未观察选项差距直接截位

## 原卡输出约束 (`output_constraints`)

- 快速得出近似值并选出正确选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 144

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
