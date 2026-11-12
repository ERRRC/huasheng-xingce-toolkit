# 循环赛、淘汰赛与轮空规则

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_competition_schedule_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

比赛问题

## 子题型 (`sub_type`)

场次轮次轮空

## 方法名称 (`method_name`)

循环赛、淘汰赛与轮空规则

## 检索标签 (`tags`)

- 比赛场次
- 循环赛
- 淘汰赛
- 轮空
- 已赛未赛

## 适用条件 (`trigger_conditions`)

- 题干出现单循环、双循环、淘汰赛、轮空、比赛场次、轮次、已赛未赛

## 不适用条件 (`anti_conditions`)

- 若问几局几胜概率，调用比赛类概率卡

## 解题步骤 (`steps`)

- 单循环用C(n,2)，双循环乘2
- 淘汰赛决出冠军共淘汰n-1队，故n-1场
- 轮次接近2^k时约k轮；奇数队伍当轮有1队轮空
- 已赛/未赛可用连线法，完成比赛数=该点发出射线数

## 公式 (`formulas`)

- 单循环场次=C_n^2
- 双循环场次=2C_n^2
- 淘汰赛决冠军场次=n-1

## 示例 (`examples`)

- 笔记第27页列出淘汰赛、单循环赛和双循环赛公式

## 易错点 (`pitfalls`)

- 淘汰赛误按组合数算
- 轮空次数未逐轮判断

## 避免事项 (`forbidden`)

- 不要把循环赛和淘汰赛场次公式混用

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

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 队伍数
- 赛制
- 是否主客场双循环
- 是否问轮空/轮次
- 已赛关系

## 计算策略 (`calculation_policy`)

- mode：competition_formula
- allow_exact_calculation：true
- preferred_tools：
  - 组合数
  - 淘汰数
  - 连线法

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 场次
  - 轮次
  - 轮空次数
  - 选项
- must_report：赛制类型
