# 图表查找四大坑

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_chart_reading_pitfalls_001_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

易错点提取

## 子题型 (`sub_type`)

图表查找

## 方法名称 (`method_name`)

图表查找四大坑

## 别名 (`aliases`)

- 图表易错点

## 检索标签 (`tags`)

- 资料分析
- 读图
- 易错点
- 坑点

## 适用条件 (`trigger_conditions`)

从图表（表格、柱状图等）中提取数据进行任何计算时。

## 不适用条件 (`anti_conditions`)



## 所需信息 (`required_inputs`)

- 图表时间范围
- 图例
- 单位

## 推理策略 (`reasoning_policy`)

- core_logic：防止因粗心导致的找数错误，需对图表的边缘信息保持高度敏感。
- detailed_policy：
  - 1. 注意起始、结束年份、月份，尤其是年均或累计。
  - 2. 避开'合计'或'总计'行。
  - 3. 警惕第一年的增量，若无前一年数据则无法计算增量。
  - 4. 留意数据单位（万、亿、%等）。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：precheck
- rank：5
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 读题干时圈出时间和单位。
- 去图表中核对时间是否完全吻合。
- 扫描图表排除合计行干扰。
- 确认基期量是否存在。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - context：图表给2011-2015年数据，问2011-2015年每年增量均超过100的年份有几个
  - action：注意材料中如果没有2010年数据，2011年增量未知，不能纳入统计。

## 易错点 (`pitfalls`)

- 把合计数据当成个体项
- 单位未对齐直接计算
- 累计值当成当月值

## 避免事项 (`forbidden`)

- 不看表头和单位直接找数字

## 原卡输出约束 (`output_constraints`)

- 准确找到目标数据

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 6

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
