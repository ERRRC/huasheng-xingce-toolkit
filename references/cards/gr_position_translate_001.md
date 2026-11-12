# 平移与移动路径法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_position_translate_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

位置规律

## 子题型 (`sub_type`)

平移

## 方法名称 (`method_name`)

平移与移动路径法

## 检索标签 (`tags`)

- 平移
- 移动
- 路径
- 宫格
- 方向

## 适用条件 (`trigger_conditions`)

- 元素组成相同
- 某个元素在不同位置出现
- 题干呈宫格或有明确路径

## 不适用条件 (`anti_conditions`)

- 元素数量变化明显
- 相邻图存在叠加/消失/新增时不优先看平移

## 解题步骤 (`steps`)

- 确定移动主体：整体轮廓、小元素、空白、顶点/交点或线条。
- 确定移动路径：直线、顺/逆时针、横向、纵向、内外圈。
- 记录每一步移动格数或位置变化。
- 在选项中模拟下一步位置。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记位置规律页列出有序移动、单独移动、循环移动、移动路径和特殊图形。

## 易错点 (`pitfalls`)

- 移动主体选错
- 九宫格中只看横向不看纵向
- 忽略空白或交点也可能是移动主体

## 避免事项 (`forbidden`)

- 禁止只因为位置变化就忽略其他元素是否同步变化

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

- 移动主体
- 图形坐标/格位
- 移动方向
- 移动步长

## 计算策略 (`calculation_policy`)

- mode：simulate_translation
- path_candidates：
  - linear
  - clockwise
  - counterclockwise
  - inner_outer
  - row_column

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- must_name_moving_element：true

## check_order (`check_order`)

- 找主体
- 找路径
- 找步长
- 验证选项
