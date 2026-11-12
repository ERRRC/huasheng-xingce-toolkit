# 并列结构整体概括法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_parallel_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

并列结构

## 方法名称 (`method_name`)

并列结构整体概括法

## 检索标签 (`tags`)

- 并列
- 大并列
- A且B
- 时间轴

## 适用条件 (`trigger_conditions`)

- 文段多层并列，可能按时间、地区、人物、方面展开
- 没有明显单一对策或转折重点
- 选项中存在A且B或历程概括

## 不适用条件 (`anti_conditions`)

- 文段存在总句或转折重点时不优先按并列处理

## 解题步骤 (`steps`)

- 划分并列层次
- 找并列项共同主题
- 若是时间并列，优先概括为发展历程
- 选择能覆盖所有并列项的选项
- 排除只说其中一项的片面选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：信息加密例按古时候、现代、后来、如今展开，答案概括发展历程。
  - lesson：大并列要整体概括，不能只选最后一项。

## 易错点 (`pitfalls`)

- 只选并列中的某一个层次
- 误把时间轴最后阶段当全文主旨

## 避免事项 (`forbidden`)

- 并列项未合并概括就作答

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 7
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：parallel
- focus_rule：并列无主次时整体概括；时间并列常对应历程类
- signals：
  - 同时
  - 此外
  - 一方面...另一方面
  - 古时候/现代/如今

## option_elimination (`option_elimination`)

-
  - type：片面
  - rule：只覆盖一个并列项的选项排除

## 所需信息 (`required_inputs`)

- 并列标志
- 并列项数量
- 共同主题
- 选项是否覆盖全部并列项

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
