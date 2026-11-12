# 样式/数量/位置遍历法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_style_traversal_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

样式规律

## 子题型 (`sub_type`)

遍历

## 方法名称 (`method_name`)

样式/数量/位置遍历法

## 检索标签 (`tags`)

- 遍历
- 样式规律
- 重复出现
- 行列次数

## 适用条件 (`trigger_conditions`)

- 相同元素重复出现
- 每行每列元素种类或数量可能相同
- 九宫格或两组图中有元素循环

## 不适用条件 (`anti_conditions`)

- 图形组成完全不同且无重复元素时不要优先遍历
- 有明显移动主体时先看位置

## 解题步骤 (`steps`)

- 列出每行/每列出现过的元素、样式或位置。
- 检查缺失项是否为某一类元素、某一数量或某一位置。
- 对九宫格按行列分别尝试。
- 选项必须补足缺失遍历项且不破坏已有次数。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记样式规律页列出样式遍历、数量遍历、位置遍历。

## 易错点 (`pitfalls`)

- 只看样式不看位置
- 把重复次数看错
- 没有逐行逐列核对

## 避免事项 (`forbidden`)

- 禁止只凭“像缺什么”选项，必须列出缺失项

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

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 各行/列元素清单
- 样式类别
- 出现次数
- 空缺位置

## 计算策略 (`calculation_policy`)

- mode：set_completion
- verify_by：row_column_frequency

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- must_list_missing_item：true

## check_order (`check_order`)

- 列元素清单
- 看每行
- 看每列
- 找缺失
- 选项补足
