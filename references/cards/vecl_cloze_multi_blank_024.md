# 强提示空优先突破法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_multi_blank_024

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

多空题策略

## 方法名称 (`method_name`)

强提示空优先突破法

## 检索标签 (`tags`)

- 逻辑填空
- 多空题
- 突破口

## 适用条件 (`trigger_conditions`)

- 题目有两个或三个横线
- 某一空附近有强解释或固定搭配

## 不适用条件 (`anti_conditions`)

- 单空题

## 解题步骤 (`steps`)

- 不要从第一空机械开始，先找提示最强的空。
- 提示强度排序：固定搭配 > 明确解释句 > 关联词反向/递进 > 对象特征。
- 用强提示空排除至少一半选项。
- 再用剩余空检验语义、搭配和语法。
- 最后整体带入，避免单空正确但整体不通。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 基层治理题可从第三空‘失去窗口期’入手，先锁定‘积重难返’。

## 易错点 (`pitfalls`)

- 只验证第一个空
- 每个空孤立判断

## 避免事项 (`forbidden`)

- 强提示空未利用

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
- option_word_groups
- strong_clue_blank

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

58

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

- 强提示空
- 解释提示
- 固定搭配

## collocation_rules (`collocation_rules`)

- 多空整体搭配一致
