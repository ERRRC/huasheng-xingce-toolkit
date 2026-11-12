# 对称性与对称轴法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_property_symmetry_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

属性规律

## 子题型 (`sub_type`)

对称性

## 方法名称 (`method_name`)

对称性与对称轴法

## 检索标签 (`tags`)

- 对称性
- 轴对称
- 中心对称
- 对称轴数量
- 对称轴方向

## 适用条件 (`trigger_conditions`)

- 图形呈规整形状
- 出现Z/S/风车/太极/平行四边形等中心对称提示
- 正三角形、田字、五角星、正六边形等提示对称轴

## 不适用条件 (`anti_conditions`)

- 图形组成相同且明显移动时不要先看对称
- 对称性无稳定规律时转数量或位置

## 解题步骤 (`steps`)

- 判断是否轴对称、中心对称或二者兼具。
- 统计对称轴数量是否恒定、递增递减或运算。
- 判断对称轴方向是否不变或依次变化。
- 必要时观察对称轴是否经过点、线、面或与图形关系平行/垂直。
- 用选项验证对称类型和轴数方向。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 思维导图提示中心对称图形如Z、S、风车、太极、平行四边形；正三角形、田、五角星、正六边形分别提示3、4、5、6条对称轴。

## 易错点 (`pitfalls`)

- 把近似对称当严格对称
- 只看轴数不看方向
- 忽略中心对称

## 避免事项 (`forbidden`)

- 禁止凭视觉感觉不画轴就判断复杂图形对称

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 7
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 图形轮廓
- 内部结构
- 候选对称轴
- 中心点

## 计算策略 (`calculation_policy`)

- mode：symmetry_classification
- axis_count_required：true

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- must_state_symmetry_type：true

## check_order (`check_order`)

- 轴对称
- 中心对称
- 轴数
- 轴方向
- 轴与图形关系
- 选项验证
