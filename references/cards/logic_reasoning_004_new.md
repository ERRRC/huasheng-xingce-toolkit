# 全对全错一对一错秒杀法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_reasoning_004_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

真假推理

## 方法名称 (`method_name`)

全对全错一对一错秒杀法

## 别名 (`aliases`)

- 找出现次数最多

## 检索标签 (`tags`)

- 真假推理
- 全对全错

## 适用条件 (`trigger_conditions`)

题目条件明确说明：三个人每人做两个判断，其中一个人的两个判断全对，一个人的两个判断全错，第三个人的两个判断一对一错。

## 不适用条件 (`anti_conditions`)

并非此固定模式的真假推理

## 所需信息 (`required_inputs`)

- 三个人的六个判断陈述

## 推理策略 (`reasoning_policy`)

- core_logic：找出出现次数最多的词，即为答案。
- detailed_policy：统计三个人所说的话中各个名词出现的频率，出现次数最多的名词即为正确答案。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 确认题目符合“一人全对，一人全错，一人一对一错”的模型特征。
- 统计所有人说的话中，各个核心词汇（如车牌子，人名等）出现的次数。
- 找出出现次数最多的词。
- 该词即为正确答案，直接对应选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - context：甲：“这不是奇瑞，也不是荣威。”乙：“这不是奇瑞，而是红旗。”丙：“这不是红旗，而是奇瑞。”（一人全对一人全错一人一半）
  - action：三人说话中“奇瑞”出现次数最多，因此这辆车是“奇瑞”，选A。

## 易错点 (`pitfalls`)

- 没有验证题目是否完全符合该特定模型

## 避免事项 (`forbidden`)

- 假设法一步步推导浪费时间

## 原卡输出约束 (`output_constraints`)

- 直接定位正确选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 62

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
