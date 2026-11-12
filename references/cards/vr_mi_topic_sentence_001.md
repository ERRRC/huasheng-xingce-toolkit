# 主题句定位法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_topic_sentence_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

主题句

## 方法名称 (`method_name`)

主题句定位法

## 检索标签 (`tags`)

- 主题句
- 观点句
- 对策句
- 重点句

## 适用条件 (`trigger_conditions`)

- 文段存在明确观点、对策、结论句
- 出现因此/所以/为此/可见/应该/需要等标志
- 尾句或转折后出现作者态度

## 不适用条件 (`anti_conditions`)

- 主题句只是例子或背景说明

## 解题步骤 (`steps`)

- 先定位关联词后的句子
- 判断该句是观点、对策还是结论
- 核对前后内容是否为该句服务
- 选项优先选择主题句的同义替换，而非原文局部复述

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生言语理解笔记.pdf
  - page：6
  - summary：笔记将常见引出方式后接“观点/对策”作为中心理解重点。
  - lesson：主题句通常由结构位置和关联词共同确定。

## 易错点 (`pitfalls`)

- 把例子或背景句当主题句
- 只选原文某句话而没有概括全文结构

## 避免事项 (`forbidden`)

- 忽略论证服务于观点的层级关系

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

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：topic_sentence
- focus_rule：观点句/对策句优先；例子、背景、分析通常服务于主题句
- signals：
  - 因此
  - 所以
  - 为此
  - 应该
  - 需要
  - 关键
  - 基础
  - 前提

## option_elimination (`option_elimination`)

-
  - type：出处不对
  - rule：来自背景、例子、分析且未上升到主题句的选项排除

## 所需信息 (`required_inputs`)

- 关联词
- 观点/对策句
- 例证句
- 选项同义替换程度

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

4

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
