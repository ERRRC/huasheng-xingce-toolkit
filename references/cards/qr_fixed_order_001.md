# 全排列除以特定元素全排列

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_fixed_order_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

定序问题

## 方法名称 (`method_name`)

全排列除以特定元素全排列

## 检索标签 (`tags`)

- 定序
- 顺序固定
- 先后顺序
- 拜访顺序

## 适用条件 (`trigger_conditions`)

- 题干要求若干元素保持固定先后顺序，但不要求相邻

## 不适用条件 (`anti_conditions`)

- 若要求相邻且顺序固定，应和捆绑法结合

## 解题步骤 (`steps`)

- 先按全排列处理所有相关元素
- 找出被限定相对顺序的元素个数k
- 除以这k个元素的全排列k!
- 若有多个独立定序组分别处理

## 公式 (`formulas`)

- 定序方案数=全排列数/k!

## 示例 (`examples`)

- 笔记第22页：甲乙相邻用捆绑，丙要在丁前、戊要在己前，用除以A_3^3等方式处理

## 易错点 (`pitfalls`)

- 把定序误认为固定位置
- 没有除以定序元素的全排列

## 避免事项 (`forbidden`)

- 不要在元素位置已固定时再除定序排列

## 来源文件 (`source_file`)

- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生数量关系笔记.pdf
  - pages：
    - 22

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总元素数量
- 定序元素集合
- 是否相邻
- 其他限制

## 计算策略 (`calculation_policy`)

- mode：permute_then_divide_order
- allow_exact_calculation：true
- preferred_tools：
  - 定序除法

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 选项
- must_report：被固定相对顺序的元素个数
