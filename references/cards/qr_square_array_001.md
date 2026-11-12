# 最外层边长平方与层人数公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_square_array_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

方阵问题

## 方法名称 (`method_name`)

最外层边长平方与层人数公式

## 检索标签 (`tags`)

- 方阵
- 正方形方阵
- 层数
- 最外层
- 空心方阵

## 适用条件 (`trigger_conditions`)

- 题干出现方阵、每边人数、最外层、相邻两层、地砖方阵

## 不适用条件 (`anti_conditions`)

- 若不是方阵或边长不相等，需改用几何或方程

## 解题步骤 (`steps`)

- 默认方阵为正方形
- 总人数=最外层每边人数平方
- 层数=最外层边长÷2
- 每层人数=每边人数×4-4
- 相邻两层人数差为8

## 公式 (`formulas`)

- 方阵总人数=最外层每边人数^2
- 每层人数=每边人数×4-4
- 相邻两层人数差=8

## 示例 (`examples`)

- 笔记第26页地砖例用(x+1)^2-x^2关系求缺少地砖数

## 易错点 (`pitfalls`)

- 忘记四个角重复计算要减4
- 把矩形阵列当方阵

## 避免事项 (`forbidden`)

- 没有明确方阵时不要默认正方形

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 8
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 26

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 每边人数或总人数
- 层数
- 是否最外层
- 是否空心

## 计算策略 (`calculation_policy`)

- mode：formula_lookup
- allow_exact_calculation：true
- preferred_tools：
  - 方阵公式
  - 平方数判断

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 人数
  - 层数
  - 方阵边长
  - 选项
- must_check：是否正方形方阵
