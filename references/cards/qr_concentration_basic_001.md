# 浓度基础公式与溶质守恒

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_concentration_basic_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

浓度问题

## 子题型 (`sub_type`)

溶质不变

## 方法名称 (`method_name`)

浓度基础公式与溶质守恒

## 检索标签 (`tags`)

- 浓度
- 溶质
- 溶液
- 溶剂
- 混合

## 适用条件 (`trigger_conditions`)

- 题干出现浓度、溶质、溶液、加水、蒸发、混合
- 材料强调溶质不变

## 不适用条件 (`anti_conditions`)

- 若两种溶液浓度和混合浓度均已知且问量之比，优先十字相乘

## 解题步骤 (`steps`)

- 定义溶质、溶剂、溶液
- 用浓度=溶质/溶液建立关系
- 混合时列“各部分溶质之和=混合溶液溶质”
- 加水或蒸发时抓住溶质不变

## 公式 (`formulas`)

- 浓度=溶质/溶液
- 溶液=溶质+溶剂
- Σ(溶液量×浓度)=混合溶液量×混合浓度

## 示例 (`examples`)

- 笔记第9页例题通过浓度变化，利用溶质质量不变建立方程

## 易错点 (`pitfalls`)

- 把溶剂当溶液
- 加水后误认为溶质也变化
- 浓度百分数未转小数计算

## 避免事项 (`forbidden`)

- 不要忽略混合前后溶液总量是否变化

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 6
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 9

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 初始浓度
- 初始溶液量或溶质量
- 加水/蒸发/混合量
- 目标浓度

## 计算策略 (`calculation_policy`)

- mode：conservation_equation
- allow_exact_calculation：true
- preferred_tools：
  - 溶质守恒
  - 方程法

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 质量
  - 浓度
  - 比例
  - 选项
- unit_check：浓度单位统一为小数或百分数
