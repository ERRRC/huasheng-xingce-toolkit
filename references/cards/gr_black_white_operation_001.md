# 黑白块同位置运算法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_black_white_operation_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

样式规律

## 子题型 (`sub_type`)

黑白运算

## 方法名称 (`method_name`)

黑白块同位置运算法

## 检索标签 (`tags`)

- 黑白运算
- 黑白块
- 同位置比较
- 加减同异

## 适用条件 (`trigger_conditions`)

- 图形由黑白格/黑白块组成
- 每幅图格子结构一致
- 黑白数量或位置随行列变化

## 不适用条件 (`anti_conditions`)

- 格子结构不一致或无同位置可比时不优先黑白运算
- 黑块数量完全相同且整体平移明显时先看平移

## 解题步骤 (`steps`)

- 先确认所有图格位一致。
- 按同一位置比较黑白状态。
- 尝试黑+黑、黑+白、白+黑、白+白对应结果。
- 用一整行或一整列建立运算表，再用另一行/列验证。
- 选项必须在所有格位上满足同一运算。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记页在样式规律与黑白块页均强调“对相同位置的黑白块进行运算”。

## 易错点 (`pitfalls`)

- 只比较黑块数量，不逐格运算
- 行列运算方向混乱
- 用不同运算解释不同格位

## 避免事项 (`forbidden`)

- 禁止在格位不一致时做黑白运算

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 6
    - 17
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 格位结构
- 每格黑白状态
- 行列运算方向

## 计算策略 (`calculation_policy`)

- mode：cellwise_boolean
- require_same_grid：true
- derive_operation_from_known_rows：true

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- must_apply_same_operation_all_cells：true

## check_order (`check_order`)

- 同格位
- 建运算表
- 用另一组验证
- 代入选项
