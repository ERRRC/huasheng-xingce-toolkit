# 等距离/等时间平均速度及A=B*C迁移

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_average_number_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

平均数问题

## 子题型 (`sub_type`)

调和与算术平均

## 方法名称 (`method_name`)

等距离/等时间平均速度及A=B*C迁移

## 检索标签 (`tags`)

- 平均数
- 平均速度
- 调和平均数
- 算术平均数

## 适用条件 (`trigger_conditions`)

- 题干出现平均速度、平均单价、等距离、等时间
- A=B*C且A相等

## 不适用条件 (`anti_conditions`)

- 若两段路程不相等，不能直接用等距离调和平均数；若时间不相等，不能直接用算术平均

## 解题步骤 (`steps`)

- 先判断等距离还是等时间
- 等距离用调和平均数
- 等时间用算术平均数
- 识别总售价=单价×数量等迁移模型

## 公式 (`formulas`)

- 等距离平均速度=2v1v2/(v1+v2)
- 等时间平均速度=(v1+v2)/2
- 调和平均数≤算术平均数

## 示例 (`examples`)

- 两件商品总售价相等时，平均单价也可用调和平均数思想

## 易错点 (`pitfalls`)

- 把等距离和等时间混用
- 把调和平均数误认为普通平均

## 避免事项 (`forbidden`)

- 条件不是等距离或A相等时禁止直接套调和平均

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 3
    - 7
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 31

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 两段速度或单价
- 路程是否相等
- 时间是否相等
- A=B*C中的固定量

## 计算策略 (`calculation_policy`)

- mode：condition_check_then_formula
- allow_exact_calculation：true
- preferred_tools：
  - 调和平均
  - 算术平均

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 速度
  - 平均值
  - 选项
- must_check：等距离/等时间条件
