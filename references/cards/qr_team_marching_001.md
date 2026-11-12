# 队头到队尾的相对速度

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_team_marching_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

队伍行进

## 方法名称 (`method_name`)

队头到队尾的相对速度

## 检索标签 (`tags`)

- 队伍行进
- 队伍长度
- 队头
- 队尾
- 通信员

## 适用条件 (`trigger_conditions`)

- 题干出现队伍行进、从队尾到队头、再返回队尾、队长

## 不适用条件 (`anti_conditions`)

- 若没有队伍整体移动，按普通相遇追及处理

## 解题步骤 (`steps`)

- 队头到队尾或队尾到队头都使用相对速度
- 队头到队尾：队伍长度=(人速+队伍速度)×时间
- 队尾到队头：队伍长度=(人速-队伍速度)×时间
- 结合往返总时间列方程

## 公式 (`formulas`)

- 队伍长度=(人速+队伍速度)t 或 (人速-队伍速度)t

## 示例 (`examples`)

- 笔记第32页列出队伍行进公式

## 易错点 (`pitfalls`)

- 相对速度符号用反
- 把队伍长度当总路程

## 避免事项 (`forbidden`)

- 不要忽略队伍本身在移动

## 来源文件 (`source_file`)

- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生数量关系笔记.pdf
  - pages：
    - 32

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 队伍速度
- 人速度
- 队伍长度
- 方向
- 时间

## 计算策略 (`calculation_policy`)

- mode：relative_speed
- allow_exact_calculation：true
- preferred_tools：
  - 速度和差
  - 方程法

## 原程序优先级 (`solver_priority`)

32

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 队伍长度
  - 速度
  - 时间
  - 选项
- must_report：队头/队尾方向
