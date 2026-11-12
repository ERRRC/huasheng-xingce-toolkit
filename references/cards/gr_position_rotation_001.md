# 旋转角度与方向法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_position_rotation_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

位置规律

## 子题型 (`sub_type`)

旋转

## 方法名称 (`method_name`)

旋转角度与方向法

## 检索标签 (`tags`)

- 旋转
- 顺时针
- 逆时针
- 角度

## 适用条件 (`trigger_conditions`)

- 元素组成相同
- 图形整体或局部方向连续变化
- 每幅图只是转向变化

## 不适用条件 (`anti_conditions`)

- 图形存在镜像翻转时不要误判旋转
- 角度不稳定且元素位置改变复杂时先结合平移

## 解题步骤 (`steps`)

- 确认旋转主体是整体还是局部。
- 判断方向：顺时针或逆时针。
- 判断角度：恒定、递增或递减。
- 将候选选项旋转回题干位置进行比对。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记位置页标注旋转从方向和角度两方面观察。

## 易错点 (`pitfalls`)

- 把翻转后的镜像误当旋转
- 未判断旋转中心

## 避免事项 (`forbidden`)

- 禁止不看镜像关系就认定为旋转

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 5
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 旋转主体
- 旋转中心
- 方向
- 角度序列

## 计算策略 (`calculation_policy`)

- mode：rotation_sequence
- angle_pattern：
  - constant
  - increasing
  - decreasing

## 原程序优先级 (`solver_priority`)

13

## 原卡输出约束 (`output_constraints`)

- must_distinguish_flip_from_rotation：true

## check_order (`check_order`)

- 主体
- 中心
- 方向
- 角度
- 镜像排除
- 选项验证
