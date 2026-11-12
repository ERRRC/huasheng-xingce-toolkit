# 主体词与主题词锁定法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_subject_word_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

主体词

## 方法名称 (`method_name`)

主体词与主题词锁定法

## 检索标签 (`tags`)

- 主体词
- 主题词
- 范围一致
- 高频词

## 适用条件 (`trigger_conditions`)

- 首句或多句反复出现同一对象
- 选项主语差异明显
- 文段围绕某一对象展开说明或议论

## 不适用条件 (`anti_conditions`)

- 背景对象不是答案主体
- 选项主体词明显不同

## 解题步骤 (`steps`)

- 圈首句主语、反复出现的高频词和核心对象
- 检查重点句是否仍围绕该主体
- 优先保留主体一致且覆盖重点关系的选项
- 排除主语替换、范围扩大/缩小或只抓背景对象的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：美术馆温湿度控制例强调文段主语为“温湿度控制”，选项必须体现该主题。
  - lesson：主体词不一致，即使看似合理也不能选。

## 易错点 (`pitfalls`)

- 把背景对象当成文段主语
- 用选项中的熟悉概念替代文段主体

## 避免事项 (`forbidden`)

- 只看选项观点不核对主体词

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 9
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

- type：subject_tracking
- focus_rule：主体一致是进入备选的底线，主题词+观点/对策才是答案

## option_elimination (`option_elimination`)

-
  - type：偷换概念
  - rule：选项主语与文段核心主语不一致则优先排除
-
  - type：范围错位
  - rule：选项只覆盖背景对象或局部对象时排除

## 所需信息 (`required_inputs`)

- 首句主语
- 高频词
- 重点句主语
- 选项主语

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

3

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
