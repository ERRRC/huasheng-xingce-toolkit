# 正难则反（全部减不符）

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_perm_comb_reverse_002_new

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

逆向思维

## 方法名称 (`method_name`)

正难则反（全部减不符）

## 别名 (`aliases`)

- 逆向思维法
- 排除法

## 检索标签 (`tags`)

- 至少
- 否定词
- 排列组合

## 适用条件 (`trigger_conditions`)

题目中出现“至少”、“否定词（如不、没）”等提示语，或者正面情况非常复杂时

## 不适用条件 (`anti_conditions`)

正面情况很少，直接计算更容易时

## 所需信息 (`required_inputs`)

- 全部可能情况数
- 不符合条件的情况数

## 推理策略 (`reasoning_policy`)

- core_logic：从特殊入手，全部情况数减去不符合条件的情况数。
- detailed_policy：当正面求解情况分类过多时，考虑计算总情况数，然后减去对立面（即完全不符合要求）的情况数。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：80
- fallback_method_ids：
  - qr_perm_comb_basic_001

## 解题步骤 (`steps`)

- 识别题目中的“至少”或否定提示词
- 计算在不考虑该限制条件下的总情况数
- 计算完全违背该限制条件（即不符情况）的情况数
- 将总情况数减去不符情况数得到答案

## 公式 (`formulas`)

- 符合条件的法 = 全部可能的方法 - 不符合条件的方法

## 示例 (`examples`)

-
  - context：4名女性中有1位是副院长，要求副院长不去甲乡，且去丁乡的是女性
  - action：采用“全部 - 不符”法。全部去丁乡是女性的情况数为216，副院长去甲乡的情况数为18，答案为216-18=198

## 易错点 (`pitfalls`)

- 找错对立面情况
- 漏算部分限制条件

## 避免事项 (`forbidden`)

- 正面分类太多仍强行分类计算，导致耗时极长易错

## 原卡输出约束 (`output_constraints`)

- 输出一个合法的整数情况数

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 2

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
