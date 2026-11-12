# 并列句组捆绑法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_pair_binding_020

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

并列捆绑

## 方法名称 (`method_name`)

并列句组捆绑法

## 检索标签 (`tags`)

- 语句排序
- 捆绑
- 并列提示

## 适用条件 (`trigger_conditions`)

- 若干句内容同类，存在也/同时/另外等并列词
- 选项对这些句子顺序不同

## 不适用条件 (`anti_conditions`)

- 句子间有明显因果或转折而非并列

## 解题步骤 (`steps`)

- 识别同类并列句组。
- 看并列标志词，如“也”通常不放并列组首句。
- 按语义从一般到补充、从无标记到有标记排列。
- 把并列组作为整体放入文段结构中。
- 通读验证并列组前后衔接。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 读书排序例：①⑥③为并列论证，③有“也”，应放在并列组后部。

## 易错点 (`pitfalls`)

- 把并列句拆散
- 忽略‘也’的补充位置

## 避免事项 (`forbidden`)

- 有补充标志的句子放在并列首句

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
    - 18
    - 19

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- candidate_parallel_sentences
- parallel_markers
- candidate_orders

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

47

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 也/同时/此外
- 同类内容
- 并列组整体移动

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
