# 先抽后抽概率相同

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_lottery_probability_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

抽奖概率

## 方法名称 (`method_name`)

先抽后抽概率相同

## 检索标签 (`tags`)

- 抽奖
- 抓阄
- 先后顺序
- 中奖概率

## 适用条件 (`trigger_conditions`)

- 题干问第几个人抽中、先抽后抽公平性

## 不适用条件 (`anti_conditions`)

- 若抽后放回或概率变化规则不同，需要按具体规则计算

## 解题步骤 (`steps`)

- 判断每个人是否对称
- 若无放回但每人只抽一次且奖项固定，则每个人中奖概率相同
- 直接用奖项数/人数

## 公式 (`formulas`)

- 每人中奖概率=中奖纸条数/总人数

## 示例 (`examples`)

- 5人抓阄只有1张中奖，第2个人抽中概率=1/5

## 易错点 (`pitfalls`)

- 误认为后抽概率一定变小
- 没有区分是否已知前面抽奖结果

## 避免事项 (`forbidden`)

- 若已知前面已抽中或未抽中，不能再用对称概率

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总人数
- 中奖数量
- 是否已知前序结果
- 是否放回

## 计算策略 (`calculation_policy`)

- mode：symmetry
- allow_exact_calculation：true
- preferred_tools：
  - 对称性

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 概率
  - 选项
- must_check：是否已知前序结果
