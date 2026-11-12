# 尾句观点/对策重点法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_end_sentence_focus_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

意图判断

## 子题型 (`sub_type`)

尾句重点

## 方法名称 (`method_name`)

尾句观点/对策重点法

## 检索标签 (`tags`)

- 尾句
- 后对策
- 后观点
- 总结句

## 适用条件 (`trigger_conditions`)

- 尾句出现因此、所以、应该、需要、只有才、结论性判断
- 前文为铺垫、分析、举例或问题

## 不适用条件 (`anti_conditions`)

- 尾句只是例子、补充材料或并列末项

## 解题步骤 (`steps`)

- 检查尾句是否为观点/对策/结论
- 若尾句只是补充例子，不作为重点
- 若尾句重复或升华前文观点，优先选择尾句同义替换
- 核对尾句主语与全文主题一致

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：文段常以末尾对策或观点收束，思维导图强调原文有对策选对策、观点选观点。
  - lesson：尾句重点必须由结构功能决定，不是所有尾句都重点。

## 易错点 (`pitfalls`)

- 所有题都机械看尾句
- 尾句为例子或补充说明时误选

## 避免事项 (`forbidden`)

- 不判断尾句功能就当中心

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 4
    - 6
    - 7
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.87

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：ending_focus
- focus_rule：尾句为观点/对策/结论时优先；尾句为例证补充时不优先
- signals：
  - 因此
  - 所以
  - 这说明
  - 可见
  - 应
  - 需要

## option_elimination (`option_elimination`)

-
  - type：功能误判
  - rule：只对应尾句例子或补充细节的选项排除

## 所需信息 (`required_inputs`)

- 尾句文本
- 尾句功能
- 前文功能
- 选项对应位置

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

15

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
