# A且非B削弱条件命题法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_strict_conditional_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

严谨逻辑关系

## 方法名称 (`method_name`)

A且非B削弱条件命题法

## 检索标签 (`tags`)

- 质疑削弱
- 必要条件
- 充分条件
- A且非B

## 适用条件 (`trigger_conditions`)

- 结论含只有/必须/所有/如果等严谨逻辑关系
- 论证推出A→B
- 选项给出A成立但B不成立

## 不适用条件 (`anti_conditions`)

- 普通因果归因没有严格条件关系时，不要机械套用A且非B

## 解题步骤 (`steps`)

- 将题干结论翻译为 A→B。
- 寻找选项是否给出 A 且 ¬B。
- 若存在 A 且 ¬B，则直接反驳条件命题。
- 若选项只是另有原因但不构成反例，力度低于A且非B。
- 注意只有A才B先翻译为B→A，再寻找B且¬A。

## 公式 (`formulas`)

- 质疑 A→B：A∧¬B
- 质疑只有A才B：B∧¬A

## 示例 (`examples`)

- 经理任期目标责任制例题：若未实行责任制也能增长更快，则反驳只有实行责任制才能增长。

## 易错点 (`pitfalls`)

- 条件方向翻译错误
- 用¬A且B攻击错命题

## 避免事项 (`forbidden`)

- 不得不翻译就找反例

## 来源文件 (`source_file`)

- 【判断推理】质疑类.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 8
    - 10
    - 14

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- conditional_claim
- translated_form
- options

## 计算策略 (`calculation_policy`)

- mode：conditional_counterexample
- verification：
  - translate_condition
  - find_counterexample

## 原程序优先级 (`solver_priority`)

27

## 原卡输出约束 (`output_constraints`)

- must_output：
  - translated_claim
  - counterexample
- must_not_output：
  - 条件方向错误

## argument_structure (`argument_structure`)

- claim：严格条件结论。
- evidence：题干支持该条件结论的事实。
- link：用反例打破必要或充分关系。

## strength_order (`strength_order`)

- A且非B/B且非A精确反例：最强
- 另有原因但不构成反例：中等
- 只质疑个别论据：较弱
- 无关事实：无效
