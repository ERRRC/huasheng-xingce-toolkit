# 主谓宾语法检查法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_grammar_013

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

语法正确

## 方法名称 (`method_name`)

主谓宾语法检查法

## 检索标签 (`tags`)

- 逻辑填空
- 语法
- 词性
- 主谓宾

## 适用条件 (`trigger_conditions`)

- 候选词词性不同
- 空格位置要求动词/形容词/名词
- 句子主谓宾明显

## 不适用条件 (`anti_conditions`)

- 词性都相同且语法都通时需看语义

## 解题步骤 (`steps`)

- 先判断空格所需词性。
- 检查候选词能否与主语、宾语构成合法搭配。
- 排除形容词误作动词、被动词误作主动词等语法错误。
- 再比较语义和色彩。
- 多空题每个空都要语法通顺。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- ‘诗人济慈所___’需要动词，‘愤怒’是形容词，不能填。

## 易错点 (`pitfalls`)

- 只看词义忽略词性
- 语法通顺但语义不符未继续验证

## 避免事项 (`forbidden`)

- 词性错误的选项

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

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- blank_syntax_role
- candidate_pos
- subject_object

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

72

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

- 语法角色
- 词性

## collocation_rules (`collocation_rules`)

- 主谓宾搭配合法
- 被动/主动一致
