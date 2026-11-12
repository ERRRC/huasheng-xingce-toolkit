# 车身长不可忽略

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_train_bridge_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

火车过桥

## 方法名称 (`method_name`)

车身长不可忽略

## 检索标签 (`tags`)

- 火车过桥
- 桥长
- 车身长
- 过完全桥

## 适用条件 (`trigger_conditions`)

- 题干出现火车过桥、完全通过、车头上桥到车尾下桥

## 不适用条件 (`anti_conditions`)

- 若火车看作质点或题干说明忽略车长，不加车身长

## 解题步骤 (`steps`)

- 判断是完全过桥还是车头到达
- 完全过桥路程=桥长+车身长
- 完全在桥上路程=桥长-车身长
- 用路程=速度×时间求解

## 公式 (`formulas`)

- 完全过桥：桥长+车身长=速度×时间
- 完全在桥上：桥长-车身长=速度×时间

## 示例 (`examples`)

- 笔记第32页配图区分火车完全过桥和完全在桥上

## 易错点 (`pitfalls`)

- 忘加车身长
- 把车头到桥尾当完全过桥

## 避免事项 (`forbidden`)

- 不要在桥长小于车身长时使用完全在桥上公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 3
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 32

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 桥长
- 车身长
- 速度
- 时间
- 通过类型

## 计算策略 (`calculation_policy`)

- mode：effective_distance
- allow_exact_calculation：true
- preferred_tools：
  - 有效路程判断

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 长度
  - 速度
  - 时间
  - 选项
- must_check：过桥类型
