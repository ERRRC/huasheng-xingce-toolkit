# 线数量与线组关系法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_quantity_line_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量规律

## 子题型 (`sub_type`)

线

## 方法名称 (`method_name`)

线数量与线组关系法

## 检索标签 (`tags`)

- 线
- 直线
- 曲线
- 平行线组
- 线段数量
- 线位置

## 适用条件 (`trigger_conditions`)

- 图形由明显线段或曲线组成
- 出现两个三角形、平行线、垂线等提示
- 属性看不出但线数量有变化

## 不适用条件 (`anti_conditions`)

- 图形面数量提示更明显时先数面
- 线条有重合或分割不清时需标注不确定

## 解题步骤 (`steps`)

- 确定数直线、曲线、线段总数还是特殊线组。
- 必要时分开数横/竖/斜或平行线组。
- 观察线数是否恒定、递增递减、加减或分组。
- 选项线数和线组关系必须同规律。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 曲直页涉及线段数量、曲线数量、方向位置；思维导图也提示平行线组数。

## 易错点 (`pitfalls`)

- 把一条直线被交点分成多段后口径混乱
- 忽略内部线条
- 漏数重合线

## 避免事项 (`forbidden`)

- 禁止不同图中采用不同分段口径

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 9
    - 12
    - 15
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 线条类型
- 是否分段
- 平行/垂直关系
- 内部外部线条

## 计算策略 (`calculation_policy`)

- mode：line_count_or_relation
- keep_segmentation_consistent：true

## 原程序优先级 (`solver_priority`)

42

## 原卡输出约束 (`output_constraints`)

- must_define_line_unit：true

## check_order (`check_order`)

- 数什么线
- 是否分段
- 是否分组
- 是否平行/垂直
- 选项验证
