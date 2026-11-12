# 隔年前期先求间隔增长率法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_abx_base_interval_002

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

基期量

## 子题型 (`sub_type`)

隔年前期量

## 方法名称 (`method_name`)

隔年前期先求间隔增长率法

## 检索标签 (`tags`)

- ABRX
- 基期量
- 间隔增长率
- 隔年前期

## 适用条件 (`trigger_conditions`)

- 题干要求求隔年、两年前、与2014年相比的前期量
- 题干给出连续两期增长率或增长率相对前一年提高/下降若干百分点

## 不适用条件 (`anti_conditions`)

- 若直接给出目标前期值，不必计算间隔增长率
- 若只问两期增长率本身，调用间隔增长率卡片

## 解题步骤 (`steps`)

- 先根据相邻两期增长率求总间隔增长率R间
- 再把现期量B代入A=B/(1+R间)
- 若R间接近常用分数，可用415份数法或假设分配法估算

## 公式 (`formulas`)

- R间 = R1 + R2 + R1×R2
- A隔年 = B / (1 + R间)

## 示例 (`examples`)

- 笔记例题先由R1、R2算出2015年较2013年的间隔增长率，再求2013年收入。
- 思维导图ABRX页把‘隔年前期’放在前期A分支，并提示先求隔年增长率。

## 易错点 (`pitfalls`)

- 遗漏R1×R2项
- 把‘增速下降百分点’直接当负增长率
- 年份方向反了，导致用错基期

## 避免事项 (`forbidden`)

- 不求R间就直接连除或乱乘
- 将百分点变化误当作量的增减

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
    - 8

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 现期量B
- 相邻两期增长率R1/R2或等价信息
- 目标隔年前期时间
- 选项差距

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
  - da_growth_rate_interval_002
  - da_abx_base_direct_001

## 原卡输出约束 (`output_constraints`)

- 输出前必须核对时间、主体、单位
- 若为选择题，优先给出最接近选项
- 结果单位应与材料原量单位一致
- 下降率参与分母时要保留负向关系
