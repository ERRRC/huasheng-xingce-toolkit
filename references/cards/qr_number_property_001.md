# 倍数、整除与余数特性

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_number_property_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

数论与计算

## 子题型 (`sub_type`)

数的特性

## 方法名称 (`method_name`)

倍数、整除与余数特性

## 检索标签 (`tags`)

- 倍数
- 整除
- 最小公倍数
- 最大公约数
- 余数

## 适用条件 (`trigger_conditions`)

- 题干出现整除、倍数、余数、最小公倍数、最大公约数
- 选项多为整数且可被特定数筛选

## 不适用条件 (`anti_conditions`)

- 若题干要求排列种数或几何面积，不应仅按数的特性路由

## 解题步骤 (`steps`)

- 先找倍数或整除限制
- 用最小公倍数统一周期或除数
- 用最大公约数处理重合间隔、植树重合等问题
- 结合选项代入排除

## 公式 (`formulas`)

- 若a、b均能被x整除，则a+b、a-b也能被x整除
- 若x=ay/b且a/b为最简分数，x、y为整数，则x是a的倍数，y是b的倍数

## 示例 (`examples`)

- 笔记中“约数特性”示例用最小公倍数和余数筛选可行值

## 易错点 (`pitfalls`)

- 把“能整除”误当成“只能等于”；忘记最简分数条件

## 避免事项 (`forbidden`)

- 不要在未知量非整数时套整除性质

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 7
    - 8
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 5
    - 7

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 整除条件
- 倍数条件
- 未知量是否为整数
- 选项

## 计算策略 (`calculation_policy`)

- mode：option_filter_first
- allow_exact_calculation：true
- preferred_tools：
  - 整除筛选
  - LCM/GCD
  - 代入排除

## 原程序优先级 (`solver_priority`)

26

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 整数
  - 选项
- must_check：未知量整数性
