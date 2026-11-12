# 速度和/速度差公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_meeting_chasing_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

相遇追及

## 方法名称 (`method_name`)

速度和/速度差公式

## 检索标签 (`tags`)

- 相遇
- 追及
- 速度和
- 速度差
- 距离差

## 适用条件 (`trigger_conditions`)

- 题干出现相向而行、相遇、追上、领先、落后、距离差

## 不适用条件 (`anti_conditions`)

- 环形多次相遇/追及优先调用环形运动或多次相遇

## 解题步骤 (`steps`)

- 相遇问题找相遇点，用速度和×时间=相遇距离
- 追及问题找距离差，用速度差×时间=追及距离
- 必要时画线段图表示相对位置
- 结合比例或方程求解

## 公式 (`formulas`)

- 相遇距离=(v1+v2)t
- 追及距离=(v1-v2)t

## 示例 (`examples`)

- 笔记第31页强调“相遇要找相遇点，追及要知距离差”

## 易错点 (`pitfalls`)

- 把速度和与速度差用反
- 追及距离不是总路程而是距离差

## 避免事项 (`forbidden`)

- 不要在同向但没有追及关系时套速度差

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
    - 31

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 两者速度
- 方向
- 时间
- 初始距离或距离差
- 目标事件

## 计算策略 (`calculation_policy`)

- mode：relative_motion
- allow_exact_calculation：true
- preferred_tools：
  - 线段图
  - 速度和/差

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 距离
  - 速度
  - 时间
  - 选项
- must_report：相遇/追及类型
