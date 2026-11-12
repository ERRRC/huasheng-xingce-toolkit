# 主旨意图题结构优先总流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_total_flow_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

总流程

## 方法名称 (`method_name`)

主旨意图题结构优先总流程

## 检索标签 (`tags`)

- 总流程
- 结构分析
- 主旨概括
- 意图判断
- 标题填入

## 适用条件 (`trigger_conditions`)

- 题干问主要说明/意在说明/旨在强调/中心意思/最适合做标题
- 片段阅读需要概括文段主旨或作者意图

## 不适用条件 (`anti_conditions`)

- （空列表）

## 解题步骤 (`steps`)

- 题干先判题型：主旨概括、意图判断、标题填入、中心理解
- 通读文段，先切分结构：引出话题/问题、分析论证、观点或对策
- 圈定主体词和高频主题词，排除主语不一致选项
- 优先找作者观点、对策、结论；若无观点对策，再概括问题或原因
- 用选项排除表检查：出处不对、片面、无中生有、偷换概念、绝对化、杂糅
- 标题题再检查是否简洁、醒目、准确覆盖主题

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：思维导图反复以“引出话题/问题-分析-观点/对策”为核心结构分析主旨意图。
  - lesson：先结构后选项，不直接凭语感。

## 易错点 (`pitfalls`)

- 看到首句主题词就直接选首句同义项
- 忽略转折、因此、只有才等重点标志
- 选项主语与文段主语不一致

## 避免事项 (`forbidden`)

- 未完成结构划分前直接作答
- 只根据某个高频词匹配选项

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
    - 9
    - 11
    - 13
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：global_flow
- focus_rule：观点/对策优先；无观点对策时概括问题、原因或并列整体
- signal_words：
  - 但是
  - 然而
  - 因此
  - 所以
  - 为此
  - 只有...才
  - 应
  - 需要
- structure_order：
  - 引出话题/问题
  - 分析论证
  - 观点/对策
  - 选项验证

## option_elimination (`option_elimination`)

-
  - type：通用排除
  - rule：排除出处不对、主语不一致、片面、无中生有、绝对化和杂糅项

## 所需信息 (`required_inputs`)

- 题干问法
- 完整文段
- 四个选项
- 关联词
- 主体词/主题词
- 文段尾句

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

1

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
