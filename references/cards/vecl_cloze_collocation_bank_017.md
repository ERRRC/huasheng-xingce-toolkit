# 近义词习惯搭配备查卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_collocation_bank_017

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

搭配积累

## 方法名称 (`method_name`)

近义词习惯搭配备查卡

## 检索标签 (`tags`)

- 实词辨析
- 习惯搭配
- 近义词

## 适用条件 (`trigger_conditions`)

选项中出现近义实词，且横线前后有明确的修饰对象、宾语或主语时

## 不适用条件 (`anti_conditions`)

横线前后缺乏明确搭配对象，或者考查重点在于词的感情色彩而非搭配时

## 解题步骤 (`steps`)

- 提取横线前后的核心词（如主语、宾语、被修饰语）
- 将选项中的近义词逐一代入，判断是否符合日常习惯搭配
- 直接排除搭配不当或不符合固定用法的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - context：横线后宾语为‘法令/制度’
  - action：选用‘废除’，排除‘废黜’
-
  - context：横线后宾语为‘关系/条件/生活’
  - action：选用‘改善’，排除‘改进’

## 易错点 (`pitfalls`)

- 忽略横线前后的中心语，主观臆断词语搭配
- 将被修饰语的定语误认为中心语进行搭配

## 避免事项 (`forbidden`)

- 破坏习惯搭配

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 38
    - 39
    - 40

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- object_after_blank
- candidate_words
- context_logic

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

81

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

- 搭配对象
- 语义范围

## collocation_rules (`collocation_rules`)

- 改进工作/方法/技术
- 改善关系/条件/生活
- 履行承诺/职责/条约
- 执行任务/计划/命令

## 推理策略 (`reasoning_policy`)

- core_logic：依据现代汉语的语言习惯和固定搭配对象来排除不当选项
- detailed_policy：常见固定搭配如：废除（法令/制度/条约），废黜（王位/特权）；改进（工作/方法/技术），改善（关系/条件/生活）；弥补（缺陷/损失/弱点），填补（空缺/亏空/缺额）；继承（传统/遗志/财产），秉承（理念/宗旨/原则）；缜密（心思/分析/研究），周密（计划/布局/安排）；侵占（财产/公款/领土），侵犯（权益/领海/领空）等。
