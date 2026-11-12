# 必要条件关系表对策法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_necessary_condition_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

意图判断

## 子题型 (`sub_type`)

必要条件

## 方法名称 (`method_name`)

必要条件关系表对策法

## 检索标签 (`tags`)

- 必要条件
- 只有才
- 关键
- 基础
- 前提
- 对策

## 适用条件 (`trigger_conditions`)

- 出现只有...才、除非、关键、基础、前提、必须、需要等
- 必要条件承载作者主张或解决路径

## 不适用条件 (`anti_conditions`)

- 必要条件只是客观定义，不是作者对策

## 解题步骤 (`steps`)

- 识别必要条件标志
- 判断必要条件指向哪一项措施或条件
- 将必要条件部分视作对策重点
- 选项必须保留必要条件的主体和方向

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：食品谣言治理例用“才能真正建立信心”提示对策，重点在健全举报平台和机制。
  - lesson：只有才结构中，“只有”部分常为对策条件。

## 易错点 (`pitfalls`)

- 把结果句当对策
- 把必要条件关系方向读反

## 避免事项 (`forbidden`)

- 忽略“只有/前提/基础”等必要条件标志

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

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：necessary_condition_solution
- focus_rule：必要条件词通常引出解决问题的关键条件
- signals：
  - 只有...才
  - 关键
  - 基础
  - 前提
  - 必须
  - 需要

## option_elimination (`option_elimination`)

-
  - type：方向错误
  - rule：把必要条件与结果倒置的选项排除

## 所需信息 (`required_inputs`)

- 必要条件标志
- 条件项
- 结果项
- 选项是否保留方向

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

8

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
