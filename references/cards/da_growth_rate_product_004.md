# 乘积增长率公式法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_growth_rate_product_004

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

增长率

## 子题型 (`sub_type`)

乘积增长率

## 方法名称 (`method_name`)

乘积增长率公式法

## 检索标签 (`tags`)

- 乘积增长率
- A=B×C
- 占比
- 增长率

## 适用条件 (`trigger_conditions`)

- 题干中的目标量可拆成B×C
- 题干给出一个总量增长率和占比变化/占比增长率，要求目标量增长率
- 资料中存在‘整体×占比=部分’关系

## 不适用条件 (`anti_conditions`)

- B×C只是单位换算且无增长率时不作为增长率题处理
- 若C是比重差的百分点变化而不是增长率，需要先转换或改用比重类方法

## 解题步骤 (`steps`)

- 确认目标量A=B×C是否有实际含义或表示占比关系
- 识别B、C各自增长率Rb、Rc
- 代入Ra=Rb+Rc+RbRc；若增长率较小可先估算Rb+Rc，再校验乘积项

## 公式 (`formulas`)

- Ra = Rb + Rc + Rb×Rc

## 示例 (`examples`)

- 思维导图ABRX页将乘积增长率分为‘B×C有实际含义’和‘B×C表示占比’两类，并给出乘积公式。
- 笔记页在增长率R部分把乘积增长率列为第四类。

## 易错点 (`pitfalls`)

- 漏掉Rb×Rc
- 误把占比提高的百分点当成占比增长率
- 未判断B×C是否真能表达目标量

## 避免事项 (`forbidden`)

- 只用Rb+Rc作最终答案且选项接近
- 把比重差直接代入Rc

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

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 两个因子B/C的增长率Rb/Rc
- 目标量A=B*C是否成立
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
  - da_truncate_division_001

## 原卡输出约束 (`output_constraints`)

- 输出前必须核对时间、主体、单位
- 若为选择题，优先给出最接近选项
- 结果通常输出为百分数%
- 不得把百分点变化直接当作增长率
