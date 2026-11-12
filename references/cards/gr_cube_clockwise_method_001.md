# 时针画边法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_cube_clockwise_method_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

时针法

## 方法名称 (`method_name`)

时针画边法

## 检索标签 (`tags`)

- 时针法
- 空间重构
- 方向验证
- 公共边

## 适用条件 (`trigger_conditions`)

- 展开图和选项均有方向性图案
- 公共边验证仍不足以排除
- 需要判断面内图案方向是否一致

## 不适用条件 (`anti_conditions`)

- 没有方向性标记时不优先使用
- 相对面已排除唯一选项时可不使用

## 解题步骤 (`steps`)

- 结合选项描画一个面。
- 找一个特殊面的唯一点或唯一边。
- 顺时针方向描述标号或图案顺序。
- 题干与选项对应面方向不一致则排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记空间页“顺时针画边法”提示结合选项描面、找特殊面的唯一点或边、顺时针描述标号。

## 易错点 (`pitfalls`)

- 起点不一致
- 顺逆方向混乱
- 面对应错位

## 避免事项 (`forbidden`)

- 禁止在未确定对应面的情况下用时针法

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 21
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 特殊面
- 唯一点/边
- 图案方向
- 选项可见面

## 计算策略 (`calculation_policy`)

- mode：clockwise_orientation_check
- requires_anchor：true

## 原程序优先级 (`solver_priority`)

13

## 原卡输出约束 (`output_constraints`)

- must_use_same_anchor_point：true

## check_order (`check_order`)

- 选特殊面
- 定锚点/边
- 顺时针读序
- 选项比对
