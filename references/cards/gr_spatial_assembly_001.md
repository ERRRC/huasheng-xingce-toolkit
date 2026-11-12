# 积木题分层画图法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_spatial_assembly_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

立体拼合

## 方法名称 (`method_name`)

积木题分层画图法

## 检索标签 (`tags`)

- 立体拼合
- 积木题
- 分层画图
- 分层凑数

## 适用条件 (`trigger_conditions`)

- 题干是多个正方体/积木拼合
- 要求判断缺块或能否拼成目标立体
- 选项为立体块组合

## 不适用条件 (`anti_conditions`)

- 普通六面体折叠题不用
- 透视关系极不清晰时标记不确定

## 解题步骤 (`steps`)

- 先数个数。
- 试拼时优先找特殊块或“占地大”的块，最好横跨所有层级。
- 用分层画图法把立体转为平面层图。
- 必要时用分层凑数法想象0空间。
- 特殊块先拼，再用平面图确定空位。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记立体拼合页给出数个数、试拼、分层画图法、分层凑数法和“特殊块先拼”。

## 易错点 (`pitfalls`)

- 只看外观不数方块
- 上下层关系混乱
- 被遮挡方块漏数

## 避免事项 (`forbidden`)

- 禁止未分层就判断复杂积木题

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 24
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 方块总数
- 每层占位
- 特殊块形状
- 候选空位

## 计算策略 (`calculation_policy`)

- mode：layered_assembly
- count_first：true

## 原程序优先级 (`solver_priority`)

17

## 原卡输出约束 (`output_constraints`)

- must_draw_or_describe_layers：true

## check_order (`check_order`)

- 数个数
- 找特殊块
- 分层画图
- 分层凑数
- 选项验证
