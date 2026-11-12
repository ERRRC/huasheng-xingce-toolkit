# 一般增长率公式法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_growth_rate_general_001

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

增长率

## 子题型 (`sub_type`)

一般增长率

## 方法名称 (`method_name`)

一般增长率公式法

## 检索标签 (`tags`)

- 增长率
- ABRX
- R=X/A
- 增速

## 适用条件 (`trigger_conditions`)

- 题干问增长率、增速、同比增长百分之几
- 给出基期量A和增长量X，或给出现期B与基期A

## 不适用条件 (`anti_conditions`)

- 题干问平均数增长率、人均增长率等比值增长率时，调用比值增长率卡片
- 题干问比重变化时，不可当一般增长率处理

## 解题步骤 (`steps`)

- 确定基期量A、现期量B、增长量X
- 优先使用R=X/A；也可用(B-A)/A
- 选项差距大时截位直除，差距小时保留足够有效位

## 公式 (`formulas`)

- R = X / A = (B - A) / A

## 示例 (`examples`)

- 笔记ABRX页将一般增长率记为R=X/A。
- 思维导图ABRX页LED产业示例直接用X/A求增长率。

## 易错点 (`pitfalls`)

- 把增长量X除以现期量B
- 把百分点变化当成增长率
- 忽视单位导致X和A口径不同

## 避免事项 (`forbidden`)

- 未确认谁是基期量就计算
- 平均数增长率题套R=X/A

## 来源文件 (`source_file`)

- 【花生十三】资料分析思维导图.pdf
- 花生资料分析笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】资料分析思维导图.pdf
  - pages：
    - 1
-
  - file：花生资料分析笔记.pdf
  - pages：
    - 7

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 基期量A
- 现期量B或增长量X
- 选项是否为百分数

## 计算策略 (`calculation_policy`)

- default：先识别ABRX/分式结构，再套用对应公式；能估则估，必要时直除。
- precision：按选项差距决定估算、截位或精算
- allowed：
  - 公式法
  - 截位直除
  - 分数化估算
- avoid：
  - 未审题直接代数值
  - 把百分点当百分数
- verify：
  - 时间口径
  - 主体口径
  - 单位口径

## 原程序优先级 (`solver_priority`)

- tier：core_formula
- rank：10
- fallback_method_ids：
  - da_truncate_division_001
  - da_common_pitfalls_001

## 原卡输出约束 (`output_constraints`)

- 输出前必须核对时间、主体、单位
- 若为选择题，优先给出最接近选项
- 结果通常输出为百分数%
- 不得把百分点变化直接当作增长率
