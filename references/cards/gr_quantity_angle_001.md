# 角数量与角类型法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_quantity_angle_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量规律

## 子题型 (`sub_type`)

角

## 方法名称 (`method_name`)

角数量与角类型法

## 检索标签 (`tags`)

- 角
- 直角
- 锐角
- 钝角
- 扇形中心角

## 适用条件 (`trigger_conditions`)

- 图形有明显折线或三角结构
- 出现直角、锐角、钝角可比较
- 角度呈递增递减

## 不适用条件 (`anti_conditions`)

- 大量交点但角定义不清时先谨慎
- 图形为封闭面且面数更明显时可后置

## 解题步骤 (`steps`)

- 先确定角的类型：总角、直角、锐角、钝角。
- 只数小于180度的角，且通常需由相交线段形成。
- 图形外部角一般不数，除非题干规律明确。
- 用选项验证角数或角度变化。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记角页提示一眼小于180度的角、直角/钝角/锐角、扇形中心角递增递减等。

## 易错点 (`pitfalls`)

- 把180度直线当角
- 图形外角乱数
- 交点处多角漏数

## 避免事项 (`forbidden`)

- 禁止未说明数哪类角就直接给数量

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 12
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 角类型
- 线段交点
- 内角/外角
- 角度序列

## 计算策略 (`calculation_policy`)

- mode：angle_count
- less_than_180_rule：true

## 原程序优先级 (`solver_priority`)

43

## 原卡输出约束 (`output_constraints`)

- must_state_angle_type：true

## check_order (`check_order`)

- 总角/直角/锐角/钝角
- 计数口径
- 逐图计数
- 选项验证
