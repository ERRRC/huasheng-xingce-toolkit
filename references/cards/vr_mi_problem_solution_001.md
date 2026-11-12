# 问题—对策结构解题法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_problem_solution_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

意图判断

## 子题型 (`sub_type`)

问题-对策

## 方法名称 (`method_name`)

问题—对策结构解题法

## 检索标签 (`tags`)

- 问题
- 对策
- 意图判断
- 主旨意图

## 适用条件 (`trigger_conditions`)

- 文段指出现实问题/不足/困境/风险
- 后文出现应、需要、必须、为此、只有才、关键、基础等对策标志
- 题干问意在说明/旨在强调/重在说明

## 不适用条件 (`anti_conditions`)

- 选项对策无法解决文段问题
- 选项对策主语与问题主体不一致

## 解题步骤 (`steps`)

- 先明确问题是什么
- 定位直接对策、禁止性对策或必要条件对策
- 判断对策是否能针对问题
- 选择对策的同义替换；没有对策选能体现问题的选项，但优先级低于对策

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：传统文化“活起来”例：先指出现实问题，再用“只有...才...”给出对策。
  - lesson：意图题中对策优先于问题描述。

## 易错点 (`pitfalls`)

- 选问题项不选对策项
- 选择不能解决文段问题的伪对策
- 对策主语与问题主语不一致

## 避免事项 (`forbidden`)

- 原文已有对策仍只选问题或背景

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

0.96

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：problem_solution
- focus_rule：原文有对策选对策；对策必须针对前文问题
- signals：
  - 应
  - 需要
  - 必须
  - 为此
  - 只有...才
  - 关键
  - 基础
  - 前提
  - 如果不

## option_elimination (`option_elimination`)

-
  - type：伪对策
  - rule：选项虽像对策但不能解决文段问题或主语不一致，排除
-
  - type：问题项弱于对策项
  - rule：有对策时仅陈述问题的选项优先排除

## 所需信息 (`required_inputs`)

- 问题句
- 对策句
- 对策主语
- 选项对策是否针对问题

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
