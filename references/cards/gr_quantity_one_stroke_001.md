# 一笔画与笔画数法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_quantity_one_stroke_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量规律

## 子题型 (`sub_type`)

一笔画

## 方法名称 (`method_name`)

一笔画与笔画数法

## 检索标签 (`tags`)

- 一笔画
- 奇点
- 笔画数
- 连通图

## 适用条件 (`trigger_conditions`)

- 出现五角星、圆相切/相交、田字变形、出头端点、T点、分离图形、特殊字符等
- 图形可视为线条网络
- 题干图形复杂但线条连接明显

## 不适用条件 (`anti_conditions`)

- 图形主要是面数量或元素数量规律时不要强行笔画
- 不连通图形需分部分计算，不能直接用全图奇点

## 解题步骤 (`steps`)

- 先看图形是否连通。
- 数奇点：通常0或2个奇点可一笔画。
- 多笔画时通常按奇点数/2并结合分离部分相加。
- 遇到出头点、T点、交点需严格区分。
- 选项必须满足同样笔画数或变化规律。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 思维导图提示笔画数的提示点为出头、T点、分离、特殊字符；笔记页强调一笔画与奇点。

## 易错点 (`pitfalls`)

- 把端点当交点
- 忽略分离部分
- 多部分图形只看其中一部分

## 避免事项 (`forbidden`)

- 禁止在不连通图形中直接套一笔画结论

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 10
    - 11
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 连通部分数
- 奇点数
- 端点/T点/交点
- 图形分离情况

## 计算策略 (`calculation_policy`)

- mode：stroke_count
- odd_point_rule：true
- component_aware：true

## 原程序优先级 (`solver_priority`)

40

## 原卡输出约束 (`output_constraints`)

- must_count_components：true

## check_order (`check_order`)

- 是否连通
- 数奇点
- 奇点/2
- 分离部分相加
- 选项验证
