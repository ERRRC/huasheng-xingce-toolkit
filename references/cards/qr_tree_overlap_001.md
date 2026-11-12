# 两次植树最大公约数求无需移动棵数

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_tree_overlap_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

植树重合

## 方法名称 (`method_name`)

两次植树最大公约数求无需移动棵数

## 检索标签 (`tags`)

- 植树重合
- 最大公约数
- 无需移动
- 间隔

## 适用条件 (`trigger_conditions`)

- 题干出现原来按某间隔植树，改按另一间隔，问重合/无需移动数量

## 不适用条件 (`anti_conditions`)

- 若只有一次植树，不用本卡

## 解题步骤 (`steps`)

- 求出两次植树的间隔数
- 求两次间隔数的最大公约数
- 根据两端植树情况确定无需移动棵数
- 注意端点是否重合

## 公式 (`formulas`)

- 无需移动树木数量=最大公约数-1+两端情况

## 示例 (`examples`)

- 思维导图第8页给出三步：求间隔数、求最大公约数、考虑两端植树情况

## 易错点 (`pitfalls`)

- 端点情况漏加
- 把间隔长度和间隔数混为一谈

## 避免事项 (`forbidden`)

- 不要在两次端点不一致时直接套公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 8

## 原卡置信度 (`confidence`)

0.86

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 原间隔
- 新间隔
- 总长
- 两端是否植树

## 计算策略 (`calculation_policy`)

- mode：gcd_overlap
- allow_exact_calculation：true
- preferred_tools：
  - 最大公约数
  - 端点修正

## 原程序优先级 (`solver_priority`)

36

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 重合棵数
  - 移动棵数
  - 选项
- must_check：两端情况
