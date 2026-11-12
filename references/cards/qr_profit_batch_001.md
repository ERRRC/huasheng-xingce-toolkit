# 按各批收入相加列总收入方程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_profit_batch_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

经济利润问题

## 子题型 (`sub_type`)

分批销售

## 方法名称 (`method_name`)

按各批收入相加列总收入方程

## 检索标签 (`tags`)

- 分批销售
- 总收入
- 利润率
- 折扣

## 适用条件 (`trigger_conditions`)

- 题干出现第一批、第二批、剩余部分、不同利润率/折扣出售
- 问成本、售价或利润

## 不适用条件 (`anti_conditions`)

- 若商品只有一个销售阶段，直接基础利润公式

## 解题步骤 (`steps`)

- 问什么设什么
- 分别计算每一批收入
- 列“第一批收入+第二批收入+...=总收入”
- 根据成本和利润率转换收入

## 公式 (`formulas`)

- 收入=成本×(1+利润率)=成本+利润
- 总收入=Σ各批收入

## 示例 (`examples`)

- 笔记第17页给出分批销售：第一部分销售收入+第二部分销售收入=总销售收入

## 易错点 (`pitfalls`)

- 批次数量比例漏乘
- 利润率分母仍为各批成本
- 把收入方程写成利润方程

## 避免事项 (`forbidden`)

- 不要把各批利润率直接平均

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

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 各批数量或比例
- 各批售价/利润率/折扣
- 总收入或总利润
- 所求变量

## 计算策略 (`calculation_policy`)

- mode：income_equation
- allow_exact_calculation：true
- preferred_tools：
  - 分批列式
  - 问什么设什么

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 成本
  - 售价
  - 利润
  - 利润率
  - 选项
- must_report：各批收入表达式
