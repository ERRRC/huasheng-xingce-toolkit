# 字母图形规律法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_letter_symbol_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

特殊题型

## 子题型 (`sub_type`)

字母类

## 方法名称 (`method_name`)

字母图形规律法

## 检索标签 (`tags`)

- 字母
- 对称性
- 曲直性
- 开闭性
- 字母顺序
- 字母本身算法

## 适用条件 (`trigger_conditions`)

- 题干主体为英文字母
- 字母形态或字母表顺序可能成规律

## 不适用条件 (`anti_conditions`)

- 字母只是选项标签时不得纳入规律
- 无字母本身规律证据时先按图形属性解

## 解题步骤 (`steps`)

- 先看字母图形属性：对称、曲直、开闭。
- 再看数量：面、点、线、素等。
- 最后看特殊：字母表顺序、字母本身算法。
- 选项需同时满足图形属性或字母序列规律。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记字母页将字母属性、数量和特殊字母表规律列为观察点。

## 易错点 (`pitfalls`)

- 把选项A/B/C/D当题干字母
- 字母顺序规律证据不足时乱用
- 忽略大小写字形差异

## 避免事项 (`forbidden`)

- 禁止使用选项标签作为规律依据

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 20
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 字母字符
- 大小写样式
- 字母表位置
- 封闭面/曲直/对称属性

## 计算策略 (`calculation_policy`)

- mode：letter_shape_first_then_alphabet
- alphabet_rule_requires_sequence：true

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- must_not_use_answer_labels：true

## check_order (`check_order`)

- 对称
- 曲直
- 开闭
- 数量
- 字母表顺序/算法
- 选项验证
