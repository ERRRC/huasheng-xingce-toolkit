# 文氏图范畴分析法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_category_analysis_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

分析推理

## 子题型 (`sub_type`)

范畴分析

## 方法名称 (`method_name`)

文氏图范畴分析法

## 检索标签 (`tags`)

- 范畴分析
- 文氏图
- 集合关系

## 适用条件 (`trigger_conditions`)

- 题干有所有、有些、某些、没有、不确定
- 涉及多个类别范围关系

## 不适用条件 (`anti_conditions`)

- 如果只是条件箭头关系，优先翻译推理

## 解题步骤 (`steps`)

- 识别每个概念集合。
- 根据所有/有些/没有画包含、相交或不相交关系。
- 不确定区域不能强行推出。
- 逐项检查选项是否在所有可能图形中都成立。
- 只选必然成立的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记范畴分析页提示一个小二画圈法，所有画实圈，有些画不确定圈，不确定区间在纸上。

## 易错点 (`pitfalls`)

- 把有些区域画成全部
- 把不确定区域当确定
- 漏掉多个可能图形

## 避免事项 (`forbidden`)

- 不得从图上一种画法推出唯一关系

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 18

## 原卡置信度 (`confidence`)

0.82

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- category_statements
- options

## 计算策略 (`calculation_policy`)

- mode：venn_analysis
- verification：
  - draw_sets
  - mark_certain_uncertain
  - test_options

## 原程序优先级 (`solver_priority`)

36

## 原卡输出约束 (`output_constraints`)

- must_output：
  - set_relations
  - certainty_status
- must_not_output：
  - 将不确定区确定化

## argument_structure (`argument_structure`)

- claim：选项是否由范畴关系必然推出。
- evidence：题干集合关系。
- link：用文氏图保留所有可能关系。

## strength_order (`strength_order`)

- （空列表）
