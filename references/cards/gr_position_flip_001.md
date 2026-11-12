# 翻转轴与镜像识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_position_flip_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

位置规律

## 子题型 (`sub_type`)

翻转

## 方法名称 (`method_name`)

翻转轴与镜像识别法

## 检索标签 (`tags`)

- 翻转
- 横轴对称
- 竖轴对称
- 中心对称
- 镜像

## 适用条件 (`trigger_conditions`)

- 元素组成相同
- 相邻图呈镜像关系
- 横向或纵向左右互换/上下互换明显

## 不适用条件 (`anti_conditions`)

- 图形只是角度转动且非镜像时不要看翻转
- 内部标识不支持镜像时须排除

## 解题步骤 (`steps`)

- 判断两图是否横轴对称、竖轴对称或中心对称。
- 横轴对称对应上下翻，竖轴对称对应左右翻。
- 中心对称通常可视为旋转180度。
- 用不对称标记点验证是否真的翻转。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记位置页将两图横轴对称、竖轴对称、中心对称分别对应不同翻转判断。

## 易错点 (`pitfalls`)

- 对称图形本身看不出翻转，需找不对称标记
- 把180度旋转和上下/左右翻混用

## 避免事项 (`forbidden`)

- 禁止只看外轮廓对称就忽略内部方向

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

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 镜像轴
- 内部标记
- 翻转前后方向

## 计算策略 (`calculation_policy`)

- mode：mirror_check
- use_asymmetric_marker：true

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- must_verify_internal_orientation：true

## check_order (`check_order`)

- 横轴
- 竖轴
- 中心
- 内部标记
- 选项镜像验证
