# 数字图形规律法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_digit_symbol_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

特殊题型

## 子题型 (`sub_type`)

数字类

## 方法名称 (`method_name`)

数字图形规律法

## 检索标签 (`tags`)

- 数字
- 对称性
- 曲直性
- 开闭性
- 封闭面
- 数字本身

## 适用条件 (`trigger_conditions`)

- 题干主体为阿拉伯数字
- 数字形态或数字大小/运算可能成规律

## 不适用条件 (`anti_conditions`)

- 数字只是标号或选项序号时不得纳入规律
- 图形规律已明显时不强行用数字本身运算

## 解题步骤 (`steps`)

- 先看图形属性：对称性、曲直性、开闭性。
- 再看封闭面数量。
- 再看数字本身：大小比较、排序或运算。
- 若出现数字组合，验证每一位或整体是否同规律。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记数字页列出数字的对称性、曲直性、开闭性、封闭面数量和数字本身特殊。

## 易错点 (`pitfalls`)

- 把题号当题干数字
- 数字本身运算与图形属性混淆
- 封闭面数量看漏8有两个面

## 避免事项 (`forbidden`)

- 禁止用选项序号参与规律

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 19
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 数字字符
- 封闭面数量
- 曲直属性
- 大小/顺序/运算关系

## 计算策略 (`calculation_policy`)

- mode：digit_shape_first_then_numeric
- numeric_operation_last：true

## 原程序优先级 (`solver_priority`)

23

## 原卡输出约束 (`output_constraints`)

- must_confirm_digits_are_stimuli：true

## check_order (`check_order`)

- 对称
- 曲直
- 开闭
- 封闭面
- 数字本身
- 选项验证
