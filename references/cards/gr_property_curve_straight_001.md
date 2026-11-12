# 曲直性判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_property_curve_straight_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

属性规律

## 子题型 (`sub_type`)

曲直性

## 方法名称 (`method_name`)

曲直性判断法

## 检索标签 (`tags`)

- 曲直性
- 全曲
- 全直
- 曲直混合
- 直线曲线

## 适用条件 (`trigger_conditions`)

- 图形由明显曲线和直线构成
- 元素组成不同但线条属性明显
- 汉字、数字、字母可按曲直分类

## 不适用条件 (`anti_conditions`)

- 图形组成相同且只是方向变化时不看曲直
- 曲直数量变化复杂时转线数量卡

## 解题步骤 (`steps`)

- 判断整体是全曲、全直还是曲直混合。
- 若整体属性无规律，分别数直线数、曲线数或曲直分开看。
- 观察曲线/直线位置，如内外、上下、左右关系。
- 用选项匹配曲直属性或数量。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记曲直页将属性分为全直、全曲、曲+直，并可进一步数直线/曲线。

## 易错点 (`pitfalls`)

- 把弧线近似当直线
- 只看外轮廓不看内部线条
- 属性与数量混用

## 避免事项 (`forbidden`)

- 禁止未界定曲线/直线标准就计数

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 9
    - 18
    - 19
    - 20
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 曲线数量
- 直线数量
- 曲直位置
- 整体属性

## 计算策略 (`calculation_policy`)

- mode：curve_straight_screening
- count_if_attribute_fails：true

## 原程序优先级 (`solver_priority`)

32

## 原卡输出约束 (`output_constraints`)

- must_separate_attribute_and_quantity：true

## check_order (`check_order`)

- 全曲/全直/曲直
- 曲线数
- 直线数
- 曲直位置
- 选项验证
