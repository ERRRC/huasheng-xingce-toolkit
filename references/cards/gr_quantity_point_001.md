# 点数量与交点类型法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_quantity_point_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量规律

## 子题型 (`sub_type`)

点

## 方法名称 (`method_name`)

点数量与交点类型法

## 检索标签 (`tags`)

- 点
- 交点
- 切点
- 出头点
- 曲直交点
- 内部交点

## 适用条件 (`trigger_conditions`)

- 线条相交较多
- 出现切点、圆相交、出头线、网格或交叉结构
- 题干强调点状关系

## 不适用条件 (`anti_conditions`)

- 图形没有明显交叉或切点时不要优先数点
- 面或笔画提示更强时后置

## 解题步骤 (`steps`)

- 先确定要数哪类点：交点、切点、出头点、内部交点、外框交点等。
- 统一计数口径，不同图必须按同一类点计数。
- 注意出头点是端点，不是交点。
- 用数量恒定、递增递减、加减等关系验证选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记点页列出曲直交点、内部交点、圆内交点、外框交点、切点、出头点等。

## 易错点 (`pitfalls`)

- 计数口径变化
- 出头点和交点混淆
- 漏数重叠处

## 避免事项 (`forbidden`)

- 禁止为了匹配选项临时更换点的定义

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 11
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 点类型
- 交叉位置
- 切点/端点
- 图形内部外部

## 计算策略 (`calculation_policy`)

- mode：point_type_count
- definition_fixed：true

## 原程序优先级 (`solver_priority`)

41

## 原卡输出约束 (`output_constraints`)

- must_state_point_type：true

## check_order (`check_order`)

- 选点类型
- 统一口径
- 逐图计数
- 找规律
- 选项验证
