# 否定此因削弱法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_not_this_cause_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

并非此因

## 方法名称 (`method_name`)

否定此因削弱法

## 检索标签 (`tags`)

- 质疑削弱
- 否定此因
- 归因类

## 适用条件 (`trigger_conditions`)

- 题干说A结果得益于/源于原因B
- 选项说明真正原因是D或B不适合解释
- 销量增长、效果提升等归因

## 不适用条件 (`anti_conditions`)

- 选项只是说明还有其他品牌/情况，但不能排除题干原因时力度较弱

## 解题步骤 (`steps`)

- 识别题干把结果归因于原因B。
- 检查选项是否直接说明结果由另一个原因D造成。
- 判断D是否比B更贴合结果。
- 若D排斥B或说明B不是原因，则强削弱。
- 若D只可能并存但不排斥B，力度下降。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- A凉茶销量增长例题中，消费者购买是因为口味宜人、包装时尚，而非保健效用提升。

## 易错点 (`pitfalls`)

- 另一个原因不能解释主要结果
- 选项只说明行业整体增长但未排除该品牌原因

## 避免事项 (`forbidden`)

- 不得把普通另有现象当成否定此因

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
    - 5

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- result
- claimed_reason
- replacement_reason
- options

## 计算策略 (`calculation_policy`)

- mode：not_this_cause
- verification：
  - replacement_reason_explains_result
  - claimed_reason_weakened

## 原程序优先级 (`solver_priority`)

13

## 原卡输出约束 (`output_constraints`)

- must_output：
  - claimed_reason
  - replacement_reason
- must_not_output：
  - 把并存原因当排他原因

## argument_structure (`argument_structure`)

- claim：B是结果A的原因。
- evidence：B与结果A同时增长或相关。
- link：选项说明结果由D导致，B未必是原因。

## strength_order (`strength_order`)

- 直接说明D才是购买/结果原因：强
- 行业整体同向变化：中强
- B仍可能有效但不是唯一原因：中等
- 无关市场信息：无效
