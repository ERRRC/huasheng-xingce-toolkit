# 年均增长量基期判定法则

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_annual_average_growth_amount_001_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

年均增长量

## 子题型 (`sub_type`)

基期判断

## 方法名称 (`method_name`)

年均增长量基期判定法则

## 别名 (`aliases`)

- 年均增量计算

## 检索标签 (`tags`)

- 资料分析
- 年均增长量
- 基期选择

## 适用条件 (`trigger_conditions`)

计算一段时期的年均增长量。

## 不适用条件 (`anti_conditions`)

求年均增长率。

## 所需信息 (`required_inputs`)

- 末期量
- 可选的基期量
- 年份

## 推理策略 (`reasoning_policy`)

- core_logic：确定计算年份差和基期量。
- detailed_policy：
  - 严谨算法：基期往前推一年。若问2020-2022，推为2019基期，年份差为3。
  - 不严谨算法：基期不推。问2020-2022，按2020基期，年份差为2。
  - 结论原则：材料能找到前一年数据，且推了之后选项有答案，必须推（严谨）。找不到就不推。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：10
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 确定题目所问的时间段。
- 检查材料中是否存在起始年的前一年数据。
- 若有且选项匹配，使用(末期-前一年)/跨度 进行计算。
- 若无，使用(末期-起始年)/跨度 计算。

## 公式 (`formulas`)

- 年均增长量 = (末期量 - 基期量) / n

## 示例 (`examples`)

-
  - context：问2020年-2022年平均增长量，图表中含有2019年数据。
  - action：采用严谨算法：(2022年数据 - 2019年数据) / 3。

## 易错点 (`pitfalls`)

- 选错基期年份
- 年份差n算错

## 避免事项 (`forbidden`)

- 无论何种情况都统一用末年减初年除以相减的年数

## 原卡输出约束 (`output_constraints`)

- 准确计算出年均增加的具体数值

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 7

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
