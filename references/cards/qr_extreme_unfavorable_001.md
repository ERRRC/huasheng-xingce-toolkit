# 构造最不利保证n人满足

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_extreme_unfavorable_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

最值问题

## 子题型 (`sub_type`)

最不利问题

## 方法名称 (`method_name`)

构造最不利保证n人满足

## 检索标签 (`tags`)

- 最不利
- 抽屉原理
- 保证
- 至少

## 适用条件 (`trigger_conditions`)

- 题干出现至少要取多少、才能保证、一定有、最坏情况

## 不适用条件 (`anti_conditions`)

- 若问的是可能性而非保证性，不走最不利

## 解题步骤 (`steps`)

- 构造不满足要求的最大情况
- 识别正常抽屉和小抽屉
- 若有不符合情况先去掉或单独计入
- 最后加1保证满足

## 公式 (`formulas`)

- 至少人数=正常抽屉数×(n-1)+小抽屉数量+1；有不符合情况应先加入最不利

## 示例 (`examples`)

- 毕业生专业例：3名延迟毕业为不符合，至少3+5+5×3+1=24

## 易错点 (`pitfalls`)

- 忘记“小抽屉”容量不足
- 未把不符合情况计入最不利

## 避免事项 (`forbidden`)

- 不要把“至少可能”当“至少保证”

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 4
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 19

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 抽屉类别数量
- 每类容量
- 目标n
- 不符合情况数量

## 计算策略 (`calculation_policy`)

- mode：worst_case_plus_one
- allow_exact_calculation：true
- preferred_tools：
  - 抽屉原理
  - 极端构造

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 至少数量
  - 选项
- must_report：最不利构造
