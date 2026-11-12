# 因果结构重点判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_causality_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

因果关系

## 方法名称 (`method_name`)

因果结构重点判断法

## 检索标签 (`tags`)

- 因果
- 原因类
- 果因
- 因此
- 因为

## 适用条件 (`trigger_conditions`)

- 文段出现因为/由于/所以/因此/根源在于/这是因为
- 文段重在解释原因或由原因推出结论

## 不适用条件 (`anti_conditions`)

- 选项给出文段没有的解决方案

## 解题步骤 (`steps`)

- 判断结构是因→果还是果→因
- 若文段重点表述原因，选原因概括
- 若因此推出观点或对策，选观点/对策
- 排除只描述结果或只抓次要原因的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：智慧城市发展缓慢例：问题根源在于数据孤岛，文段主要讲原因。
  - lesson：原因类文段答案要体现“为什么”。

## 易错点 (`pitfalls`)

- 把结果当主旨
- 把文段未提出的解决方案当答案

## 避免事项 (`forbidden`)

- 看到原因就一律选对策

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 6
    - 7
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：causal
- focus_rule：果因结构重在原因；因果推出对策时重在结论/对策
- signals：
  - 因为
  - 由于
  - 因此
  - 所以
  - 根源在于
  - 这是因为

## option_elimination (`option_elimination`)

-
  - type：无中生有
  - rule：原因类文段未给对策时，具体解决方案选项排除

## 所需信息 (`required_inputs`)

- 因果标志
- 原因内容
- 结果内容
- 是否有对策句

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

9

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
