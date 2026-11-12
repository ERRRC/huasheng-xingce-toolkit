# 图推选项验证流程卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_option_verification_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

选项验证

## 子题型 (`sub_type`)

选项验证流程

## 方法名称 (`method_name`)

图推选项验证流程卡

## 检索标签 (`tags`)

- 选项验证
- 排除法
- 反向验证
- 防猜

## 适用条件 (`trigger_conditions`)

- 已发现候选规律
- 选项中有多个看似相近答案
- 空间题、数量题或黑白运算题需要排除

## 不适用条件 (`anti_conditions`)

- 题干规律尚未形成时不要直接以选项倒推唯一答案

## 解题步骤 (`steps`)

- 先用题干已有图形验证候选规律至少两处。
- 再把每个选项代入空缺位置。
- 优先排除违反硬规则的选项，如相对面同时出现、格位运算不一致、数量口径不一致。
- 若多个选项满足，回到总流程寻找第二规律或更高优先级特征。
- 若规律不唯一，标记需要复核而不是强答。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 空间展开图笔记多处强调结合选项、相对面排除、公共边和时针法验证。

## 易错点 (`pitfalls`)

- 只用一个局部特征排除
- 多个选项都满足时强行选
- 不同选项使用不同规则

## 避免事项 (`forbidden`)

- 禁止没有题干规律就只看选项相似度

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 3
    - 4
    - 21
    - 22
    - 24
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 候选规律
- 全部选项
- 硬性排除条件
- 是否存在多解

## 计算策略 (`calculation_policy`)

- mode：option_driven_validation_after_rule
- no_rule_no_guess：true

## 原程序优先级 (`solver_priority`)

8

## 原卡输出约束 (`output_constraints`)

- must_compare_all_options：true
- if_multiple_match_return_need_review：true

## check_order (`check_order`)

- 题干验证
- 选项代入
- 硬规则排除
- 多解回退
- 输出答案
