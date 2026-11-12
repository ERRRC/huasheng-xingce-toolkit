# 常见无关选项排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_irrelevant_options_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

无关选项

## 方法名称 (`method_name`)

常见无关选项排除法

## 检索标签 (`tags`)

- 无关选项
- 主体一致
- 话题一致
- 偷换概念

## 适用条件 (`trigger_conditions`)

- 选项看似合理但主体或话题不同
- 加强/削弱题出现泛泛背景事实
- 选项只重复题干

## 不适用条件 (`anti_conditions`)

- 选项直接命中断点或因果链时不要误排除

## 解题步骤 (`steps`)

- 检查主体是否与论点主体相同。
- 检查话题是否与论证话题相同。
- 检查选项是否只讲背景、只重复题干、只换了概念。
- 检查选项是否能改变论据到论点的关系。
- 不能改变论证关系的选项，标为无关或力度弱。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 支持类笔记强调主体一致、话题一致、贴合题干；一般质疑也要求主体一致、话题一致。

## 易错点 (`pitfalls`)

- 把常识正确当作逻辑相关
- 把题干复述当加强
- 把范围不同的事实当证据

## 避免事项 (`forbidden`)

- 不得选择主体不一致、话题不一致的选项

## 来源文件 (`source_file`)

- 【判断推理】支持、前提假设、比例、解释说明.pdf
- 【判断推理】质疑类.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】支持、前提假设、比例、解释说明.pdf
  - pages：
    - 1
-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 8
    - 11

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim_subject
- claim_topic
- option_subject
- option_topic

## 计算策略 (`calculation_policy`)

- mode：irrelevance_filter
- verification：
  - subject_match
  - topic_match
  - argument_effect

## 原程序优先级 (`solver_priority`)

6

## 原卡输出约束 (`output_constraints`)

- must_output：
  - relevance_label
  - reason
- must_not_output：
  - 把常识正确性当相关性

## argument_structure (`argument_structure`)

- claim：题干论点。
- evidence：题干论据。
- link：选项必须影响论据与论点关系才相关。

## strength_order (`strength_order`)

- 命中断点/因果链：有效
- 同主体同话题但只背景：弱
- 主体或话题不一致：无关
- 偷换概念：排除
