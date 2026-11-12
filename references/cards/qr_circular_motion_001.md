# 同起点同向追及/背向相遇

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_circular_motion_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

环形运动

## 方法名称 (`method_name`)

同起点同向追及/背向相遇

## 检索标签 (`tags`)

- 环形运动
- 同向追及
- 背向相遇
- 圈长

## 适用条件 (`trigger_conditions`)

- 题干出现环形跑道、圆形路线、同一起点、追上、相遇

## 不适用条件 (`anti_conditions`)

- 非同一位置出发时需先构造同一位置或另列方程

## 解题步骤 (`steps`)

- 同一起点同向出发，追上一次多跑一圈
- 同一起点背向而行，相遇一次路程和一圈
- N次追及对应距离差N圈
- N次相遇对应路程和N圈

## 公式 (`formulas`)

- 同向追及：路程差=N×圈长
- 背向相遇：路程和=N×圈长

## 示例 (`examples`)

- 笔记第31页强调非同一位置出发需构造同一位置出发

## 易错点 (`pitfalls`)

- 把同向和背向混用
- 非同起点直接套N圈

## 避免事项 (`forbidden`)

- 不要忽略圈长单位

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

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 圈长
- 两者速度
- 方向
- 追及/相遇次数
- 出发位置

## 计算策略 (`calculation_policy`)

- mode：lap_count_relative_motion
- allow_exact_calculation：true
- preferred_tools：
  - 速度差
  - 速度和
  - 圈数

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 路程
  - 速度
  - 时间
  - 选项
- must_check：同一位置出发条件
