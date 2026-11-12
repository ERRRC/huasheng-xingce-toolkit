# 命题形式与读取顺序卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_question_form_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

图推总流程

## 子题型 (`sub_type`)

命题形式识别

## 方法名称 (`method_name`)

命题形式与读取顺序卡

## 检索标签 (`tags`)

- 一组图
- 两组图
- 九宫格
- 分组分类
- 立体类
- 读取顺序

## 适用条件 (`trigger_conditions`)

- 题干呈现一行或两行图形
- 九宫格中缺一格
- 要求分组分类
- 出现立体展开/截面/三视图

## 不适用条件 (`anti_conditions`)

- 不要在未确定读取顺序时直接套数量递推

## 解题步骤 (`steps`)

- 一组图：从左往右观察，必要时看间隔或奇偶项。
- 两组图：第一组找规律，第二组对应套用。
- 九宫格：横行、竖列、米字或中心特殊均可尝试。
- 分组分类：先找共性，再找差异，优先考虑三三分组。
- 立体类：从展开图、截面图、三视图、立体拼合分类进入专项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记页将一组图、两组图、九宫格、分组分类、立体类分别列为命题形式。

## 易错点 (`pitfalls`)

- 九宫格只横看不竖看
- 分组分类只看相似不看差异
- 立体题用平面位置规律硬解

## 避免事项 (`forbidden`)

- 禁止跳过命题形式直接给答案

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 3
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 题干布局
- 空缺位置
- 是否有选项
- 是否要求分组/分类

## 计算策略 (`calculation_policy`)

- mode：form_first_routing
- try_orders：
  - row
  - column
  - diagonal
  - grouping
  - spatial

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- must_report_reading_order：true

## check_order (`check_order`)

- 先判断一组/两组/九宫格/分组/空间
- 再确定读取方向
- 最后进入对应规律卡
