# 加减同异与去同去异法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_style_add_sub_same_diff_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

样式规律

## 子题型 (`sub_type`)

加减同异

## 方法名称 (`method_name`)

加减同异与去同去异法

## 检索标签 (`tags`)

- 加减同异
- 去同存异
- 去异存同
- 叠加

## 适用条件 (`trigger_conditions`)

- 相邻图有线条或元素叠加关系
- 两图合成第三图
- 相同部分可能保留或消失

## 不适用条件 (`anti_conditions`)

- 元素没有对应位置关系时不要强行做加减
- 黑白块题应先按黑白运算专项核对

## 解题步骤 (`steps`)

- 对齐相邻图形。
- 判断运算方式：直接相加、相减、去同存异、去异存同。
- 在每个相同位置或相同线段上验证运算。
- 用选项替入，看是否能完成同样运算。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记样式规律页将加减同异列为样式规律，并提示同位置线条重复出现。

## 易错点 (`pitfalls`)

- 未对齐图形就运算
- 只验证一处线条
- 把位置移动误认为叠加

## 避免事项 (`forbidden`)

- 禁止未说明运算规则就说“叠加”

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 6
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 对应位置
- 重合部分
- 差异部分
- 行列关系

## 计算策略 (`calculation_policy`)

- mode：boolean_shape_operation
- ops：
  - add
  - subtract
  - same_keep
  - same_remove
  - different_keep
  - different_remove

## 原程序优先级 (`solver_priority`)

21

## 原卡输出约束 (`output_constraints`)

- must_define_operation：true

## check_order (`check_order`)

- 对齐
- 找相同
- 找不同
- 确定保留/删除
- 选项代入
