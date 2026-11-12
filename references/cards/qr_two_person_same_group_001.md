# 先固定一人再看另一人

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_two_person_same_group_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

两人同组概率

## 方法名称 (`method_name`)

先固定一人再看另一人

## 检索标签 (`tags`)

- 两人同组
- 同排
- 同车
- 同班
- 概率

## 适用条件 (`trigger_conditions`)

- 题干问两个人在同一组/同一排/同一辆车的概率

## 不适用条件 (`anti_conditions`)

- 若组容量不等或存在复杂限制，需先明确分母空间

## 解题步骤 (`steps`)

- 先让第一人任意选择位置
- 统计剩余位置总数
- 统计第二人与第一人同组的可选位置数
- 概率=同组位置数/剩余总位置数

## 公式 (`formulas`)

- P=同组剩余位置数/总剩余位置数

## 示例 (`examples`)

- 5排座位每排8人，小李坐定后，小王剩39位，同排7位，概率7/39

## 易错点 (`pitfalls`)

- 把第一人的位置也计入第二人可选位置
- 组容量不等时直接套等组公式

## 避免事项 (`forbidden`)

- 不要先复杂全排列导致口径错误

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
    - 24

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总位置数
- 每组容量
- 第一人固定后剩余总位置
- 同组剩余位置

## 计算策略 (`calculation_policy`)

- mode：fix_one_person
- allow_exact_calculation：true
- preferred_tools：
  - 条件概率直算

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 概率
  - 选项
- must_report：先固定一人
