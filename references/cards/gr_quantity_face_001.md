# 封闭面数量与面属性法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_quantity_face_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量规律

## 子题型 (`sub_type`)

面

## 方法名称 (`method_name`)

封闭面数量与面属性法

## 检索标签 (`tags`)

- 面
- 封闭空间
- 部分面
- 最大面
- 面形状
- 面积

## 适用条件 (`trigger_conditions`)

- 图形有明显封闭区域
- 出现分割图、图形内部格子或多个面
- 同时可数面/线/点时封闭面突出

## 不适用条件 (`anti_conditions`)

- 图形没有封闭空间时不要数面
- 开闭性只是状态而非数量时不要混淆

## 解题步骤 (`steps`)

- 先数封闭面的总数。
- 若总数无规律，再看某一类面：三角形面、四边形面、多边形面或相同形状面。
- 单个大面可看最大面形状、面积、属性或与外框相似关系。
- 选项必须满足同一类面规则。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记面页分为两有面、部分面、单个面，并提示最大面的形状、面积、属性等。

## 易错点 (`pitfalls`)

- 把开放区域当面
- 重复数重叠区域
- 面数、线数、点数同时出现时选择混乱

## 避免事项 (`forbidden`)

- 禁止在开口图形中强行数封闭面

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 13
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 封闭区域
- 面形状
- 最大面/最小面
- 内部外部分割

## 计算策略 (`calculation_policy`)

- mode：face_count_then_face_property
- closed_region_required：true

## 原程序优先级 (`solver_priority`)

44

## 原卡输出约束 (`output_constraints`)

- must_count_closed_regions_only：true

## check_order (`check_order`)

- 总面数
- 某类面数
- 最大/最小面
- 面属性
- 选项验证
