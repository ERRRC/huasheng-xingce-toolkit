# LCM*n+x枚举法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_remainder_enum_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

余数问题

## 子题型 (`sub_type`)

无特征余数

## 方法名称 (`method_name`)

LCM*n+x枚举法

## 检索标签 (`tags`)

- 余数
- 枚举
- 最小公倍数

## 适用条件 (`trigger_conditions`)

- 多个余数条件但不满足余同、和同、差同
- 选项给出具体整数

## 不适用条件 (`anti_conditions`)

- 若满足特征余数口诀，优先调用qr_remainder_formula_001

## 解题步骤 (`steps`)

- 求除数最小公倍数M
- 设数为M*n+x
- 从一个余数条件生成候选x
- 逐个检验其他余数条件
- 再结合范围求答案

## 公式 (`formulas`)

- x=M*n+最小满足条件的x0

## 示例 (`examples`)

- 除6余5、除7余8，可设42n+x，枚举得到x=29，表达式42n+29

## 易错点 (`pitfalls`)

- 把不满足特征的题强行套口诀
- 只检验一个余数条件

## 避免事项 (`forbidden`)

- 不要忽略题目给出的上下界或最小值要求

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 7
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 5

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 除数列表
- 余数列表
- 范围
- 选项

## 计算策略 (`calculation_policy`)

- mode：enumeration
- allow_exact_calculation：true
- preferred_tools：
  - LCM
  - 候选枚举
  - 逐条件验证

## 原程序优先级 (`solver_priority`)

28

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 整数
  - 表达式
  - 选项
