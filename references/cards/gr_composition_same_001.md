# 组成相同优先看位置规律

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_composition_same_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

组成判断

## 子题型 (`sub_type`)

元素组成相同

## 方法名称 (`method_name`)

组成相同优先看位置规律

## 检索标签 (`tags`)

- 组成相同
- 位置规律
- 平移
- 旋转
- 翻转

## 适用条件 (`trigger_conditions`)

- 每幅图的元素种类和数量基本相同
- 图形只是位置、方向或角度变化
- 图形轮廓完全一致或仅摆放不同

## 不适用条件 (`anti_conditions`)

- 元素数量或种类明显变化时不要优先看位置
- 出现加减叠加痕迹时转样式规律

## 解题步骤 (`steps`)

- 核对每图元素种类与数量是否一致。
- 若一致，优先看平移路径、旋转角度、翻转轴向。
- 在九宫格中按行列分别验证位置变化是否一致。
- 用选项逐一模拟下一步位移/旋转/翻转。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 解题思维页标注“元素组成相同→位置规律”。

## 易错点 (`pitfalls`)

- 把相似图误判为相同图
- 只看整体，不看内部小元素的移动

## 避免事项 (`forbidden`)

- 禁止组成不同还强行套平移

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 4
    - 5
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 每个图形中的元素种类
- 元素数量
- 元素相对位置
- 方向角度

## 计算策略 (`calculation_policy`)

- mode：position_first
- verify_by：simulate_transform

## 原程序优先级 (`solver_priority`)

3

## 原卡输出约束 (`output_constraints`)

- must_confirm_same_components：true

## check_order (`check_order`)

- 元素种类
- 元素数量
- 移动路径
- 方向/角度
- 选项模拟
