# 余同取余、和同加和、差同减差

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_remainder_formula_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

余数问题

## 子题型 (`sub_type`)

特征余数

## 方法名称 (`method_name`)

余同取余、和同加和、差同减差

## 检索标签 (`tags`)

- 余数
- 口诀
- 最小公倍数
- 周期

## 适用条件 (`trigger_conditions`)

- 多个除数和余数条件
- 题干出现除以A余B、除以C余D

## 不适用条件 (`anti_conditions`)

- 余数之间没有“余同/和同/差同”特征时，优先转LCM*n+x枚举

## 解题步骤 (`steps`)

- 检查余数条件是否满足余同、和同或差同
- 求除数最小公倍数M
- 写出被除数表达式M*n+常数
- 结合范围或选项求解

## 公式 (`formulas`)

- 余同取余：x=M*n+r
- 和同加和：若除数+余数相同，x=M*n+和
- 差同减差：若除数-余数相同，x=M*n-差

## 示例 (`examples`)

- 除4余3、除6余3、除7余3，M=84，表达式为84n+3

## 易错点 (`pitfalls`)

- 未先判断口诀特征就硬套
- 忘记还要满足范围条件

## 避免事项 (`forbidden`)

- 不满足特征时不要编造口诀常数

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

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 除数列表
- 余数列表
- 范围条件或选项

## 计算策略 (`calculation_policy`)

- mode：formula_then_filter
- allow_exact_calculation：true
- preferred_tools：
  - LCM
  - 口诀表达式
  - 范围代入

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 整数
  - 表达式
  - 选项
