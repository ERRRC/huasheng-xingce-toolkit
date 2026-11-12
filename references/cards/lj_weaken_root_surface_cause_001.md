# 根本原因与表面原因转化法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_root_surface_cause_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

根表原因

## 方法名称 (`method_name`)

根本原因与表面原因转化法

## 检索标签 (`tags`)

- 质疑削弱
- 根本原因
- 表面原因
- 归因类

## 适用条件 (`trigger_conditions`)

- 题干或反对者提出两个不同原因解释同一结果
- 问削弱反对者或原观点
- 选项说明一个原因导致另一个原因

## 不适用条件 (`anti_conditions`)

- 只有单一原因且无根表关系时不适用

## 解题步骤 (`steps`)

- 列出原观点原因A、反对者原因B、共同结果C。
- 判断题干问削弱哪一方。
- 若要削弱反对者B，可找A导致B，说明B只是中间机制或表层原因。
- 若要削弱原观点A，可找B导致A或A只是伴随现象。
- 选项必须连接两个原因，而不只是支持某个原因。

## 公式 (`formulas`)

- A→B→C 可说明B不是根本原因

## 示例 (`examples`)

- 哮喘例题中，消极情绪会提高迷走神经兴奋性并降低交感神经反应性，即原观点原因可导致反对者原因。

## 易错点 (`pitfalls`)

- 只说明A能诱发疾病但没连接B
- 把共同结果的两个原因当互斥

## 避免事项 (`forbidden`)

- 不得忽略题干问削弱的是原观点还是反对者观点

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
    - 7

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- original_reason
- opposing_reason
- effect
- target_viewpoint
- options

## 计算策略 (`calculation_policy`)

- mode：root_surface_cause
- verification：
  - which_view_to_weaken
  - cause_between_causes

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- must_output：
  - root_cause
  - surface_cause
  - target_weakened
- must_not_output：
  - 攻击错对象

## argument_structure (`argument_structure`)

- claim：某一方认为B是结果C的原因。
- evidence：另一方认为A是结果C的原因。
- link：若A导致B，则B可能只是表层原因，A为根本原因。

## strength_order (`strength_order`)

- 直接建立A→B→C链条：强
- 只支持A或B本身：中等
- 只说明A/B普遍存在：弱
- 无关疾病或无关结果：无效
