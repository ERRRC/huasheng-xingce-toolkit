# 公共边验证法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_cube_common_edge_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

公共边

## 方法名称 (`method_name`)

公共边验证法

## 检索标签 (`tags`)

- 公共边
- 展开图
- 相邻面
- L型画边法

## 适用条件 (`trigger_conditions`)

- 相对面排除后仍有多个候选
- 选项涉及两个或三个相邻面
- 面上有方向性图案

## 不适用条件 (`anti_conditions`)

- 相对面已经能唯一排除时可不展开深入
- 公共边无法确定时使用公共点或时针法

## 解题步骤 (`steps`)

- 在平面图中构成直角的两条边通常是公共边。
- 一列/一行连着4个面时，最两侧的两条边可对应公共边。
- 3+1的L型同方向两条边可作为公共边。
- 沿公共边检查面上图案方向是否与选项一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记空间页列出平面图中构成直角的两条边、一列/一行连着4个面、3+1的L型同方向两条边等公共边判断。

## 易错点 (`pitfalls`)

- 公共边找错导致方向反判
- 两个面的公共边唯一性忽略
- 只看面不看边

## 避免事项 (`forbidden`)

- 禁止不标公共边就判断图案方向

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 21
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.89

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 相邻面
- 候选公共边
- 图案方向
- 选项对应边

## 计算策略 (`calculation_policy`)

- mode：common_edge_trace
- requires_edge_marking：true

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- must_mark_edge_before_compare：true

## check_order (`check_order`)

- 找公共边
- 标方向
- 折叠对应
- 选项比较
