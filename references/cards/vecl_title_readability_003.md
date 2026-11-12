# 标题可读性与力度法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_title_readability_003

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

标题填入

## 子题型 (`sub_type`)

标题表达

## 方法名称 (`method_name`)

标题可读性与力度法

## 检索标签 (`tags`)

- 标题拟定
- 可读性
- 对策标题
- 问题标题

## 适用条件 (`trigger_conditions`)

- 两个选项都能概括中心
- 文段有鲜明问题或批评态度
- 标题选项含修辞或引号

## 不适用条件 (`anti_conditions`)

- 修辞标题没有覆盖主题
- 题目只要求主旨概括而非标题

## 解题步骤 (`steps`)

- 先确认候选标题都符合文段中心，再比较表达。
- 问题类文段标题应能体现问题或警示，不宜太中性。
- 对策类标题应有明确行动方向，避免空泛口号。
- 含引号或双关的标题只有在准确对应原文问题时才优先。
- 最终仍以准确性优先，趣味性只用于同等内容下比较。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 手游历史例：选项“手游不该‘游戏’历史”比“手游也需要尊重历史”更有针对性和标题感。

## 易错点 (`pitfalls`)

- 为了有趣牺牲准确性
- 标题表达有力但缺少主体

## 避免事项 (`forbidden`)

- 选择与文段情绪相反的标题

## 来源文件 (`source_file`)

- 【言语理解与表达】标题、下文、语句填入、排序.pdf
- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】标题、下文、语句填入、排序.pdf
  - pages：
    - 1
-
  - file：花生言语理解笔记.pdf
  - pages：
    - 12
    - 13

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- candidate_titles
- passage_attitude
- problem_or_solution

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
