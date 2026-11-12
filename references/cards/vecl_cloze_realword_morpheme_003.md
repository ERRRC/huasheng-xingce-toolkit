# 实词不同字组词法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_realword_morpheme_003

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

实词辨析

## 方法名称 (`method_name`)

实词不同字组词法

## 检索标签 (`tags`)

- 逻辑填空
- 实词辨析
- 组词法
- 词义侧重

## 适用条件 (`trigger_conditions`)

- 选项为近义实词
- 词语差异集中在一个字
- 空格需要动词或名词搭配

## 不适用条件 (`anti_conditions`)

- 成语题或关联词题

## 解题步骤 (`steps`)

- 拆分近义词不同字，分别组词理解侧重。
- 判断语境需要主动动作、被动接收、结果状态还是过程动作。
- 检查词语与宾语/主语的搭配。
- 排除语义侧重不符的词。
- 若多空题，优先从最容易辨析的实词入手。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 采集/搜集偏主动，收集可表示被动接收；车辆系统记录数据更适合‘收集’。

## 易错点 (`pitfalls`)

- 把“采集、收集、搜集、汇集”混用
- 忽略动作主动/被动差别

## 避免事项 (`forbidden`)

- 只凭日常相似度选择

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
    - 29
    - 30
    - 31
    - 32
    - 33
    - 34
    - 35
    - 36
    - 37

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- word_options
- morpheme_differences
- subject_object_relation

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

62

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

- 主动/被动
- 过程/结果
- 词义侧重

## collocation_rules (`collocation_rules`)

- 动宾搭配
- 主语施事能力
- 固定对象搭配
