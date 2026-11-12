# 符合情况/所有可能情况

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_probability_basic_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

一般概率

## 方法名称 (`method_name`)

符合情况/所有可能情况

## 检索标签 (`tags`)

- 概率
- 样本空间
- 符合情况
- 所有情况

## 适用条件 (`trigger_conditions`)

- 题干问概率、可能性、随机、抽到、恰好、至少

## 不适用条件 (`anti_conditions`)

- 若样本空间难以直接计数但可转化面积或长度，优先几何概型

## 解题步骤 (`steps`)

- 先明确随机试验和样本空间
- 数符合要求的情况
- 数所有可能情况
- 概率=符合情况/所有可能情况
- 能用补集时先算反面

## 公式 (`formulas`)

- P=符合要求的情况数/所有可能的情况数

## 示例 (`examples`)

- 排列组合概率本质仍是考察排列组合知识点

## 易错点 (`pitfalls`)

- 样本空间前后口径不一致
- 符合情况和所有情况的有序/无序口径不同

## 避免事项 (`forbidden`)

- 不要把未等可能的情况当等可能

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
    - 21

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 随机对象
- 总情况数
- 符合条件数
- 是否等可能

## 计算策略 (`calculation_policy`)

- mode：count_ratio
- allow_exact_calculation：true
- preferred_tools：
  - 排列组合计数
  - 补集法

## 原程序优先级 (`solver_priority`)

9

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 概率
  - 选项
- must_report：分子分母口径一致
