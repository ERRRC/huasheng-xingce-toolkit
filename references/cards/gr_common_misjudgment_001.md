# 图推常见误判点清单

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_common_misjudgment_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

易错点

## 子题型 (`sub_type`)

常见误判

## 方法名称 (`method_name`)

图推常见误判点清单

## 检索标签 (`tags`)

- 易错点
- 误判
- 防错
- 规则冲突

## 适用条件 (`trigger_conditions`)

- 图推题出现多个可能规律
- 题干图形复杂或选项相似
- AI解题器需要防止乱猜

## 不适用条件 (`anti_conditions`)

- 单一明确规律且选项唯一时只需简短复核

## 解题步骤 (`steps`)

- 先防组成误判：相同/相似/不同不要混。
- 防数量口径误判：点、线、角、面、素必须先定义计数对象。
- 防空间误判：相对面、公共边、时针法不能混用。
- 防黑白块误判：黑数相同时先看平移，格位一致才做运算。
- 防特殊符号误判：不要把选项标签当题干字母/数字。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 资料多处以“注意”“提示”形式强调出头点不是交点、相对面不能同时出现、复杂选项很难切出等。

## 易错点 (`pitfalls`)

- 为了匹配答案临时换规则
- 遇到难题强行输出确定答案

## 避免事项 (`forbidden`)

- 禁止编造未在资料中出现的冷门规律

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 4
    - 10
    - 11
    - 12
    - 17
    - 21
    - 22
    - 23
    - 24
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 候选规律列表
- 计数口径
- 选项排除记录

## 计算策略 (`calculation_policy`)

- mode：anti_hallucination_checklist
- requires_rule_consistency：true

## 原程序优先级 (`solver_priority`)

9

## 原卡输出约束 (`output_constraints`)

- must_report_uncertainty_if_rule_not_unique：true

## check_order (`check_order`)

- 组成判断
- 计数口径
- 空间关系
- 黑白格位
- 符号身份
- 多解复核
