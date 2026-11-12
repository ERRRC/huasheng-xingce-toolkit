# 图推分三轮处理策略

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_exam_pacing_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

图推总流程

## 子题型 (`sub_type`)

考场策略

## 方法名称 (`method_name`)

图推分三轮处理策略

## 检索标签 (`tags`)

- 考场策略
- 时间分配
- 放弃策略

## 适用条件 (`trigger_conditions`)

- 一组图推题数量较多
- 短时间看不出规律
- 需要避免卡题

## 不适用条件 (`anti_conditions`)

- 单题已经明显可解时不需要拖到下一轮

## 解题步骤 (`steps`)

- 第一轮用3-4分钟先解决3-5道简单题。
- 判断模块做完后用2-3分钟回看剩余题。
- 涂卡阶段再利用直觉回看难题，不因个别图推拖慢整体速度。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 资料建议10道图推分三次做，避免在难题上浪费过多时间。

## 易错点 (`pitfalls`)

- 连续盯一题超过合理时间
- 因图推影响整个判断模块节奏

## 避免事项 (`forbidden`)

- 禁止在没有新观察角度时反复硬看同一题

## 来源文件 (`source_file`)

- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总题量
- 当前用时
- 已解题数
- 剩余题目数量

## 计算策略 (`calculation_policy`)

- mode：time_boxed_solving
- allow_skip：true
- max_initial_time_minutes_for_10_questions：3-4

## 原程序优先级 (`solver_priority`)

5

## 原卡输出约束 (`output_constraints`)

- must_not_overfit_single_hard_item：true

## check_order (`check_order`)

- 先做明显题
- 回看剩余题
- 最后涂卡阶段再补看
