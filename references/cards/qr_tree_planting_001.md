# 两端/一端/环形/两端不植树公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_tree_planting_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

植树问题

## 方法名称 (`method_name`)

两端/一端/环形/两端不植树公式

## 检索标签 (`tags`)

- 植树
- 间隔
- 路长
- 两端植树
- 环形

## 适用条件 (`trigger_conditions`)

- 题干出现植树、路灯、标记点、间隔相等、两端是否种

## 不适用条件 (`anti_conditions`)

- 若是两次植树重合棵数，调用重合棵数方法

## 解题步骤 (`steps`)

- 先求间隔数=路长÷间隔
- 两端植树：棵数=间隔数+1
- 一端植树或环形：棵数=间隔数
- 两端不植树：棵数=间隔数-1
- 道路两侧植树时最后乘2

## 公式 (`formulas`)

- 两端植树：总长=间隔×(棵数-1)
- 一端/环形：总长=间隔×棵数
- 两端不植树：总长=间隔×(棵数+1)

## 示例 (`examples`)

- 笔记第27页环形跑道100个标记点，跑半圈经过51个标记点

## 易错点 (`pitfalls`)

- 忘记道路两侧乘2
- 两端植树和环形植树公式混淆

## 避免事项 (`forbidden`)

- 不要在间隔不等时直接套公式

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
    - 27

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 路长
- 间隔
- 是否两端植树
- 是否环形
- 是否两侧

## 计算策略 (`calculation_policy`)

- mode：interval_count
- allow_exact_calculation：true
- preferred_tools：
  - 间隔公式

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 棵数
  - 间隔
  - 路长
  - 选项
- must_check：端点情况和是否两侧
