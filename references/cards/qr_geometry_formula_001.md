# 常用长度、面积、体积公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_geometry_formula_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

几何问题

## 子题型 (`sub_type`)

几何计算与构造

## 方法名称 (`method_name`)

常用长度、面积、体积公式

## 检索标签 (`tags`)

- 几何
- 面积
- 体积
- 周长
- 弧长
- 扇形

## 适用条件 (`trigger_conditions`)

- 题干出现图形面积、周长、体积、弧长、扇形、圆、三角形、长方体

## 不适用条件 (`anti_conditions`)

- 若问最大最小，先结合几何最值性质；若问最短路径，调用最短距离

## 解题步骤 (`steps`)

- 识别图形类型
- 代入对应长度/面积/体积公式
- 对组合图形进行分割或补形
- 统一单位并计算

## 公式 (`formulas`)

- 圆周长=2πr
- 弧长=nπr/180
- S圆=πr^2
- S扇形=nπr^2/360=lr/2
- V柱体=Sh
- V锥体=1/3Sh
- V球=4/3πr^3

## 示例 (`examples`)

- 笔记第29页列出平面图形和立体图形公式表

## 易错点 (`pitfalls`)

- 扇形弧长公式与面积公式混淆
- 锥体体积忘乘1/3
- 组合图形未分割

## 避免事项 (`forbidden`)

- 不要在图形条件不足时强行套公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 2
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 29

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 图形类型
- 边长/半径/高/角度/弧长
- 单位
- 所求量

## 计算策略 (`calculation_policy`)

- mode：formula_lookup
- allow_exact_calculation：true
- preferred_tools：
  - 分割补形
  - 公式代入

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 长度
  - 面积
  - 体积
  - 选项
- unit_check：长度/面积/体积单位区分
