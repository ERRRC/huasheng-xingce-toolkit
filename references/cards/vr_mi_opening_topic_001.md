# 开门见山引出话题结构

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_opening_topic_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

开门见山

## 方法名称 (`method_name`)

开门见山引出话题结构

## 检索标签 (`tags`)

- 开门见山
- 引出话题
- 问题-分析-对策

## 适用条件 (`trigger_conditions`)

- 首句直接提出核心话题或问题
- 后文围绕该话题分析并可能给出对策

## 不适用条件 (`anti_conditions`)

- 后文完全转向其他主体

## 解题步骤 (`steps`)

- 识别首句话题
- 继续看后文是否出现分析或对策
- 若后文给出对策，答案必须体现具体做法或对策方向
- 若后文只是解释说明，则概括首句话题及后文共同核心

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：地方政府债务风险例：首句引出话题，后文分析风险并给出多主体对策。
  - lesson：有对策时选对策，不停留在风险话题本身。

## 易错点 (`pitfalls`)

- 只选“话题是什么”，没有体现后文对策或观点
- 把开头引出的背景当作答案

## 避免事项 (`forbidden`)

- 把首句同义项机械当答案

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 4
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：opening_topic
- focus_rule：首句定范围，后文定重点；若出现对策，重点落在对策
- structure：
  - 开门见山话题
  - 分析论证
  - 观点/对策

## option_elimination (`option_elimination`)

-
  - type：出处不完整
  - rule：仅复述首句而未覆盖后文重点的选项排除

## 所需信息 (`required_inputs`)

- 首句话题
- 后文结构
- 是否存在对策
- 选项是否体现对策

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
