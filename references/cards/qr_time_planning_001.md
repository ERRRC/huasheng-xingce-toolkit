# 等待时间最少与煎饼共用时间

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_time_planning_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

统筹规划问题

## 子题型 (`sub_type`)

时间统筹

## 方法名称 (`method_name`)

等待时间最少与煎饼共用时间

## 检索标签 (`tags`)

- 时间统筹
- 等待时间
- 煎饼问题
- 安排顺序

## 适用条件 (`trigger_conditions`)

- 题干问排队、等待时间总和、煎饼、烙饼、最短完成时间

## 不适用条件 (`anti_conditions`)

- 若每个任务不能并行或无等待时间目标，只做普通加总

## 解题步骤 (`steps`)

- 若目标是总等待时间最少，短任务优先
- 煎饼类题注意正反面时间可以共用
- 统筹最后几张饼的制作顺序

## 公式 (`formulas`)

- 两张饼铛煎三张饼：正正、正反、反反

## 示例 (`examples`)

- 思维导图第5页标注该题型为了解内容，但给出核心思路

## 易错点 (`pitfalls`)

- 把总完成时间和总等待时间混为一谈
- 煎饼问题没有利用并行

## 避免事项 (`forbidden`)

- 不要在任务间有前置依赖时简单按短任务优先

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5

## 原卡置信度 (`confidence`)

0.82

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 任务时长
- 人数或设备数
- 是否可并行
- 目标是等待时间还是完成时间

## 计算策略 (`calculation_policy`)

- mode：schedule_reasoning
- allow_exact_calculation：true
- preferred_tools：
  - 短任务优先
  - 并行统筹

## 原程序优先级 (`solver_priority`)

45

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 时间
  - 顺序
  - 选项
- must_disambiguate：
  - 等待时间总和
  - 完成总时长
