# 一般平均值法则与技巧

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_general_average_001_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

平均数

## 子题型 (`sub_type`)

一般平均值计算

## 方法名称 (`method_name`)

一般平均值法则与技巧

## 别名 (`aliases`)

- 均前后做分母

## 检索标签 (`tags`)

- 资料分析
- 平均数
- 计算技巧

## 适用条件 (`trigger_conditions`)

题目要求计算平均数，出现'平均'、'每'等字眼。

## 不适用条件 (`anti_conditions`)



## 所需信息 (`required_inputs`)

- 分子指标数据
- 分母指标数据

## 推理策略 (`reasoning_policy`)

- core_logic：明确谁除以谁。口诀：'均'字前后做分母，'平均每'也是'每'后做分母。
- detailed_policy：
  - 时间平均要注意平年闰年（闰年能被400整除或被4整除但不被100整除）。

## 计算策略 (`calculation_policy`)

- core_logic：除法转化为乘法，先约分；关注有效数字，忽略量级。
- detailed_policy：
  - (A/B) ÷ (C/D) = (A×D) / (B×C)，先观察能否约分。
  - 不管题目问'每X万'，先算出'每1'的有效数字，通过有效数字直接匹配选项。

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：20
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 利用口诀确定分母。
- 列出计算式。
- 如果是除法算式可先转换形式约分。
- 计算前几位有效数字并选择选项。

## 公式 (`formulas`)

- (A/B) ÷ (C/D) = (A×D) / (B×C)

## 示例 (`examples`)

-
  - context：求每实现100万元的物流额，运输费用平均约多少万元？（运输费5.6，物流额213.5）
  - action：列式 5.6/213.5，直接计算得约26（有效数字），找到带26的选项，忽略'100万'的数量级换算。

## 易错点 (`pitfalls`)

- 分子分母搞反
- 被数量级和单位迷惑导致计算缓慢

## 避免事项 (`forbidden`)

- 带入过多的0进行死算

## 原卡输出约束 (`output_constraints`)

- 得出正确的首两位或首三位有效数字

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 7

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
