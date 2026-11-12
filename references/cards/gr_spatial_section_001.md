# 立体截面图判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_spatial_section_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

截面图

## 方法名称 (`method_name`)

立体截面图判断法

## 检索标签 (`tags`)

- 截面图
- 六面体
- 圆柱体
- 圆锥体
- 截面形状

## 适用条件 (`trigger_conditions`)

- 题干给出立体图并问截面形状
- 出现六面体、圆柱、圆锥等常见立体
- 选项为平面截面图

## 不适用条件 (`anti_conditions`)

- 展开图折叠题不使用截面法
- 复杂切割无法从资料确认时标记不确定

## 解题步骤 (`steps`)

- 六面体可截出三角形、四边形、五边形、六边形，注意不能截出直角梯形、正五边形等限制。
- 圆柱体可截出圆形、矩形、椭圆、抛物线与桶形等，注意资料标注无法截出梯形。
- 圆锥体可截出圆形、椭圆、抛物线、双曲线及三角形，注意资料标注无法截出四边形。
- 用“能否经过对应面/边/顶点”验证选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记截面图页列出六面体、圆柱体、圆锥体可截出的图形及若干红色注意事项。

## 易错点 (`pitfalls`)

- 把圆锥斜截误判为四边形
- 忽略截面必须连续穿过立体
- 复杂选项硬猜

## 避免事项 (`forbidden`)

- 禁止资料未支持的截面形状直接判断为可截出

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 22
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.89

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 立体类型
- 切割方向
- 截面候选形状
- 经过的面/边/顶点

## 计算策略 (`calculation_policy`)

- mode：known_section_shape_filter
- unsupported_shape_to_uncertain：true

## 原程序优先级 (`solver_priority`)

15

## 原卡输出约束 (`output_constraints`)

- must_state_solid_type：true

## check_order (`check_order`)

- 立体类型
- 常见可截形状
- 资料限制项
- 选项排除
