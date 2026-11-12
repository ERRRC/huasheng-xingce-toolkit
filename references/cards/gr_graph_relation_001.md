# 图形间相离相交关系法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_graph_relation_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量/属性规律

## 子题型 (`sub_type`)

图形间关系

## 方法名称 (`method_name`)

图形间相离相交关系法

## 检索标签 (`tags`)

- 图形间关系
- 相离
- 相交于点
- 相交于线
- 相交于面

## 适用条件 (`trigger_conditions`)

- 题干由两个或多个图形组合
- 图形之间接触、相交、重叠明显
- 交点、公共线、重叠面变化

## 不适用条件 (`anti_conditions`)

- 单个图形内部规律明显时不优先图形间关系
- 组合关系不稳定且数量规律更清晰时后置

## 解题步骤 (`steps`)

- 判断图形之间是相离、相交于点、相交于线还是相交于面。
- 若相交于线，观察接触线数量、长短或位置。
- 若相交于面，观察重叠面的形状、属性或数量。
- 用选项验证组合关系是否一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记图形间关系页列出相离、相交于点、相交于线、相交于面。

## 易错点 (`pitfalls`)

- 把接触点当重叠面
- 忽略公共边长短
- 只看单个图形不看组合关系

## 避免事项 (`forbidden`)

- 禁止在图形明显相交时只做单体属性判断

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 15
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 图形个数
- 相对位置
- 接触点/线/面
- 重叠区域

## 计算策略 (`calculation_policy`)

- mode：inter_shape_relation
- relation_types：
  - disjoint
  - point_contact
  - line_contact
  - area_overlap

## 原程序优先级 (`solver_priority`)

46

## 原卡输出约束 (`output_constraints`)

- must_state_relation_type：true

## check_order (`check_order`)

- 相离
- 交点
- 交线
- 交面
- 形状/位置
- 选项验证
