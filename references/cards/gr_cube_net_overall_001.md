# 六面体展开图总流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_cube_net_overall_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

六面体展开图

## 方法名称 (`method_name`)

六面体展开图总流程

## 检索标签 (`tags`)

- 空间重构
- 六面体
- 展开图
- 还原母图
- 特殊展开图

## 适用条件 (`trigger_conditions`)

- 题干为正方体/六面体展开图
- 选项为立体图或另一个展开图
- 需要判断能否折叠

## 不适用条件 (`anti_conditions`)

- 平面图形规律题不使用空间重构
- 立体拼合题不要直接套相对面规则

## 解题步骤 (`steps`)

- 先识别展开图结构，如1-4-1、2-3-1、2-2-2、0-3-3等。
- 先用相对面排除：立体中相对面不能同时出现。
- 再用公共边或公共点验证相邻关系。
- 复杂选项用时针法描边验证方向。
- 特殊展开图原图不重要时，重点盯选项与公共边。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记空间页列出展开图结构、相对面、公共边、公共点、时针画边法。

## 易错点 (`pitfalls`)

- 相对面同时出现未排除
- 公共边方向看反
- 把展开图平面距离当立体相邻

## 避免事项 (`forbidden`)

- 禁止只凭某一个面位置相似就判断可折叠

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

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 展开图结构
- 每个面标记
- 候选立体可见面
- 公共边/公共点

## 计算策略 (`calculation_policy`)

- mode：cube_net_verification
- order：
  - opposite_faces
  - common_edge
  - common_point
  - clockwise_edge

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- must_use_elimination_before_confirming：true

## check_order (`check_order`)

- 结构
- 相对面
- 公共边
- 公共点
- 时针法
- 选项排除
