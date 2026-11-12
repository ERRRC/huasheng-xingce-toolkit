# 逻辑填空语境优先总流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_total_001

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

总流程

## 方法名称 (`method_name`)

逻辑填空语境优先总流程

## 检索标签 (`tags`)

- 逻辑填空
- 总流程
- 语境
- 搭配

## 适用条件 (`trigger_conditions`)

- 题干出现横线填词、依次填入、最恰当的一项

## 不适用条件 (`anti_conditions`)

- 题目是语句填入而非词语填空

## 解题步骤 (`steps`)

- 先判断空格数量和位置，不急于比较选项。
- 定位每个空前后的语境提示：解释、转折、递进、并列、因果、反向。
- 比较选项词义、感情色彩、程度轻重、固定搭配和语法。
- 优先从约束最强的空入手排除。
- 将剩余选项全部带入，验证整段语义和风格一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 多空题可从最有提示的第三空入手，如“失去窗口期”对应长期难以解决。

## 易错点 (`pitfalls`)

- 先看选项不看语境
- 把近义词当完全等同
- 只验证一个空

## 避免事项 (`forbidden`)

- 只凭熟悉成语选择
- 不带入全文验证

## 来源文件 (`source_file`)

- 【言语理解与表达】逻辑填空.pdf
- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】逻辑填空.pdf
  - pages：
    - 1
-
  - file：花生言语理解笔记.pdf
  - pages：
    - 22
    - 24
    - 26

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- blank_contexts
- candidate_words
- options
- sentence_structure

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

60

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

- 解释提示
- 转折提示
- 递进提示
- 并列提示
- 反向提示
- 对象特征

## collocation_rules (`collocation_rules`)

- 固定搭配优先
- 主谓宾搭配必须通顺
- 多空需整体一致
