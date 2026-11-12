# 常见几何体截面图总结

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_graphic_002_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

图形推理

## 子题型 (`sub_type`)

立体图形

## 方法名称 (`method_name`)

常见几何体截面图总结

## 别名 (`aliases`)

- 截面图

## 检索标签 (`tags`)

- 图推
- 立体截面
- 几何体

## 适用条件 (`trigger_conditions`)

题目要求判断给定立体图形的可能或不可能截面

## 不适用条件 (`anti_conditions`)

不涉及截面的图形推理

## 所需信息 (`required_inputs`)

- 基础立体几何体

## 推理策略 (`reasoning_policy`)

- core_logic：熟记常见几何体能切出和不能切出的截面形状。
- detailed_policy：长方体可以切出四边形、三角形、梯形、六边形，但切不出正方形（一般指非正方体的长方体，或者图示特殊情况）。圆柱体可切出圆、矩形、酒桶型、半椭圆、椭圆。圆锥体可切出圆形、三角形、椭圆、半椭圆。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：90
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 识别给定的立体几何体类型（如长方体、圆柱、圆锥）。
- 回忆该几何体对应的可能截面形状。
- 比对选项，排除不可能的截面形状。
- 注意截面图一定要注意有没有实线，有坑。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 将酒桶型误认为椭圆
- 认为长方体（非正方体）能切出正方形截面
- 忽略截面图内部的实线特征

## 避免事项 (`forbidden`)

- 主观臆造截面形状

## 原卡输出约束 (`output_constraints`)

- 输出截面图正确选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 60

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false
