# 组成相似优先看样式规律

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_composition_similar_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

组成判断

## 子题型 (`sub_type`)

元素组成相似

## 方法名称 (`method_name`)

组成相似优先看样式规律

## 检索标签 (`tags`)

- 组成相似
- 遍历
- 加减同异
- 黑白运算
- 样式规律

## 适用条件 (`trigger_conditions`)

- 图形轮廓或元素有明显相似关系
- 局部线条、阴影、空白、黑白块重复出现
- 相邻图之间存在叠加、去同、去异迹象

## 不适用条件 (`anti_conditions`)

- 元素完全一致且只变位置时先看位置
- 元素差异过大且无叠加关系时先看属性/数量

## 解题步骤 (`steps`)

- 观察相同元素是否在行列中遍历出现。
- 检查相邻图是否存在加、减、去同、去异。
- 若是黑白格或黑白块，按同位置运算验证。
- 验证选项是否能由相同样式规则推出。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记将“元素组成相似”归入样式规律，并列遍历、加减同异、黑白运算。

## 易错点 (`pitfalls`)

- 只凭外观相似而忽略行列遍历
- 未按同一位置比较黑白块

## 避免事项 (`forbidden`)

- 禁止将样式题强行数点线面

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 4
    - 6
    - 17
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 相同元素或相似元素
- 阴影/空白/黑白状态
- 相邻图对应位置

## 计算策略 (`calculation_policy`)

- mode：style_rule_first
- compare_basis：same_position_or_same_element

## 原程序优先级 (`solver_priority`)

4

## 原卡输出约束 (`output_constraints`)

- must_identify_style_operation：true

## check_order (`check_order`)

- 是否遍历
- 是否加减同异
- 是否黑白运算
- 是否选项唯一
