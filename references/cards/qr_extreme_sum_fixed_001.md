# 总和固定下问某部分最多/最少

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_extreme_sum_fixed_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

最值问题

## 子题型 (`sub_type`)

和定最值

## 方法名称 (`method_name`)

总和固定下问某部分最多/最少

## 检索标签 (`tags`)

- 和定最值
- 排名
- 抽屉原理
- 平均值

## 适用条件 (`trigger_conditions`)

- 题干给出总和固定，问某一部分最多/最少、第一名最少、最后一名最多

## 不适用条件 (`anti_conditions`)

- 若存在二次函数或乘积形式，优先函数最值/乘积最值

## 解题步骤 (`steps`)

- 判断各部分是否允许相等
- 不能相等时：问某部分最多则其他尽量少，问某部分最少则其他尽量多，并满足排名
- 可能相等时：第一名最少/最后一名最多可用抽屉平均值
- 问什么设什么列总量方程

## 公式 (`formulas`)

- 总量=目标部分+其他部分之和

## 示例 (`examples`)

- 10个球分3人，最多的人最少拿4；若三人均不等，设x+x-1+x-2=10，x最小取5

## 易错点 (`pitfalls`)

- 忽略排名要求
- 小数结果未向符合题意的整数方向取整

## 避免事项 (`forbidden`)

- 不要在部分可相等与不可相等未判断时套平均值

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 4
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 19

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总和
- 部分数量
- 是否可相等
- 排名要求
- 所求最多/最少

## 计算策略 (`calculation_policy`)

- mode：construct_extreme
- allow_exact_calculation：true
- preferred_tools：
  - 抽屉平均
  - 问什么设什么

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最大值
  - 最小值
  - 选项
- must_check：整数取整方向
