# 每位独立选择n^m

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_repeated_permutation_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

重复排列

## 方法名称 (`method_name`)

每位独立选择n^m

## 检索标签 (`tags`)

- 重复排列
- 独立选择
- 密码
- 号码

## 适用条件 (`trigger_conditions`)

- 题干描述每个位置可重复选择、各位互不干扰
- 电话号码、密码、编号后几位

## 不适用条件 (`anti_conditions`)

- 若元素不能重复，改用排列或组合

## 解题步骤 (`steps`)

- 确认每个位置选择数是否相同
- 确认各位置选择相互独立且可重复
- 按每位选择数相乘
- 若每位均n种且m位，则n^m

## 公式 (`formulas`)

- m个位置，每位n种可重复选择：n^m

## 示例 (`examples`)

- 电话号码后3位每位0-9，共10^3种

## 易错点 (`pitfalls`)

- 忘记0是否可作为首位
- 把可重复当不可重复

## 避免事项 (`forbidden`)

- 不要在不能重复的抽取问题中套n^m

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 1
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 23

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 位置数m
- 每位可选数量
- 是否可重复
- 首位限制

## 计算策略 (`calculation_policy`)

- mode：independent_multiplication
- allow_exact_calculation：true
- preferred_tools：
  - 乘法原理
  - 幂

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 选项
- must_check：是否允许重复和首位0
