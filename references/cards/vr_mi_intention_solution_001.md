# 意图判断对策优先法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_intention_solution_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

意图判断

## 子题型 (`sub_type`)

意图判断

## 方法名称 (`method_name`)

意图判断对策优先法

## 检索标签 (`tags`)

- 意图判断
- 旨在强调
- 意在说明
- 对策

## 适用条件 (`trigger_conditions`)

- 题干问“意在说明/旨在强调/重在说明/想表达”
- 文段出现问题、观点、对策或作者态度

## 不适用条件 (`anti_conditions`)

- 选项脱离文段问题过度引申

## 解题步骤 (`steps`)

- 识别作者要解决的问题或表达的观点
- 有对策选对策
- 无对策但有观点选观点
- 有问题无对策，可选问题或合理对策，但必须贴合题干
- 排除中性背景项和出处不对项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：思维导图明确：原文有对策选对策，有作者观点选观点，有问题可选问题也可选对策。
  - lesson：意图题不是简单概括材料，而是抓作者表达目的。

## 易错点 (`pitfalls`)

- 把背景知识当意图
- 选择过度引申的无中生有对策

## 避免事项 (`forbidden`)

- 脱离原文问题自拟对策

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：intention
- focus_rule：对策>观点>问题>背景；但对策必须来自原文或直接对应问题

## option_elimination (`option_elimination`)

-
  - type：过度引申
  - rule：原文无依据且不能直接解决问题的选项排除

## 所需信息 (`required_inputs`)

- 题干问法
- 问题句
- 观点句
- 对策句
- 选项倾向

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

5

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
