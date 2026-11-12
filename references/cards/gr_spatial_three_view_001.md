# 立体三视图还原法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_spatial_three_view_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

三视图

## 方法名称 (`method_name`)

立体三视图还原法

## 检索标签 (`tags`)

- 三视图
- 主视图
- 左视图
- 俯视图
- 遮挡

## 适用条件 (`trigger_conditions`)

- 题干给出立体图或三视图
- 选项要求判断主视/左视/俯视
- 存在被遮挡部分

## 不适用条件 (`anti_conditions`)

- 平面规律题不使用
- 没有视角信息时不能强行推断

## 解题步骤 (`steps`)

- 观察到的视图都是平面图。
- 某些斜线或斜面可能被压平，注意透视压缩。
- 原图有线就有线，原图没线就没线。
- 被遮挡部分在对应视图中不可见。
- 用选项比对轮廓、线条和遮挡关系。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记三视图页列出“观察到的视图都是平面图”“原图有线就有线，原图没线就没线”“被遮挡看不见”。

## 易错点 (`pitfalls`)

- 把看不见的遮挡线画出来
- 把斜线透视关系看错
- 忽略视角方向

## 避免事项 (`forbidden`)

- 禁止把隐藏线当可见线

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 23
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 观察方向
- 立体轮廓
- 可见线条
- 遮挡关系

## 计算策略 (`calculation_policy`)

- mode：orthographic_projection_check
- hidden_lines_not_counted：true

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- must_respect_visibility：true

## check_order (`check_order`)

- 视角
- 轮廓
- 线条
- 遮挡
- 选项验证
