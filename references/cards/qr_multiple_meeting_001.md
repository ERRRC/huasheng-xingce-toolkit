# 第N次相遇走2N-1个全程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_multiple_meeting_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

多次相遇

## 方法名称 (`method_name`)

第N次相遇走2N-1个全程

## 检索标签 (`tags`)

- 多次相遇
- 全程
- 两端出发
- 单岸型
- 双岸型

## 适用条件 (`trigger_conditions`)

- 题干出现第几次相遇、两端出发、往返、多次相遇点距离

## 不适用条件 (`anti_conditions`)

- 环形同起点问题优先环形运动；非两端往返模型需谨慎

## 解题步骤 (`steps`)

- 判断两端出发往返模型
- 第N次相遇路程和为(2N-1)个全程
- 若给两次相遇点到同一边距离，用单岸公式
- 若到两边距离，用双岸公式
- 代入求全程或速度关系

## 公式 (`formulas`)

- 第N次相遇路程和=(2N-1)S
- 单岸型：S=(3S1+S2)/2
- 双岸型：S=3S1-S2

## 示例 (`examples`)

- 相遇1、2、3、4次分别走1、3、5、7个全程

## 易错点 (`pitfalls`)

- 单岸和双岸判错
- 把第N次相遇写成2N个全程

## 避免事项 (`forbidden`)

- 不要在不是两端往返的题中直接使用单岸/双岸公式

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

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 相遇次数N
- 全程或相遇点距离
- 是否同岸/双岸
- 速度关系

## 计算策略 (`calculation_policy`)

- mode：meeting_count_formula
- allow_exact_calculation：true
- preferred_tools：
  - 奇数全程
  - 单岸双岸公式

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 全程
  - 速度
  - 距离
  - 选项
- must_check：单岸/双岸归类
