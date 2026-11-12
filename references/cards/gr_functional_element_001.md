# 功能元素标记位置法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_functional_element_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量/位置规律

## 子题型 (`sub_type`)

功能元素

## 方法名称 (`method_name`)

功能元素标记位置法

## 检索标签 (`tags`)

- 功能元素
- 标记点
- 标记线
- 标记面
- 标记角
- 相对位置

## 适用条件 (`trigger_conditions`)

- 图中出现黑点、箭头、小圆点、小线段等标记
- 标记与主体图形的相对位置变化
- 需要判断标记位于点/线/面/角

## 不适用条件 (`anti_conditions`)

- 没有独立标记元素时不要使用
- 标记本身参与普通移动规律时先看位置规律

## 解题步骤 (`steps`)

- 识别功能元素类型：点、线、面、角或特殊标记。
- 判断标记与主体的位置：上/下/左/右/内/外。
- 判断标记所依附对象：交点、直线/曲线、最大/最小面、直角/锐角/钝角等。
- 用选项验证标记的对象和相对位置。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记功能元素页按相对位置、标记点、标记线、标记面、标记角和特殊关系整理。

## 易错点 (`pitfalls`)

- 只看标记位置不看依附对象
- 把标记当普通元素数个数
- 忽略内外关系

## 避免事项 (`forbidden`)

- 禁止不说明功能元素作用对象

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 16
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 功能元素位置
- 主体图形结构
- 依附对象
- 内外/上下/左右关系

## 计算策略 (`calculation_policy`)

- mode：marker_relation
- requires_anchor_object：true

## 原程序优先级 (`solver_priority`)

47

## 原卡输出约束 (`output_constraints`)

- must_identify_anchor：true

## check_order (`check_order`)

- 找标记
- 看相对位置
- 看依附对象
- 看变化规律
- 选项验证
