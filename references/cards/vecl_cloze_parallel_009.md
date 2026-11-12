# 并列同向与结构一致法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_parallel_009

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

并列提示

## 方法名称 (`method_name`)

并列同向与结构一致法

## 检索标签 (`tags`)

- 逻辑填空
- 并列
- 同义对应
- 结构一致

## 适用条件 (`trigger_conditions`)

- 出现和、与、同时、一面、另一面、顿号并列等
- 空格与并列词相邻

## 不适用条件 (`anti_conditions`)

- 并列词实际表达转折或对比时需改用反向规则

## 解题步骤 (`steps`)

- 识别并列双方的语义方向：同向、反向还是列举。
- 同向并列时，候选词应与旁边词语意义相近或同类。
- 反向并列时，候选词应与对应词形成对照。
- 检查词性和结构是否一致。
- 排除搭配不当或状态词误作动作词。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 公共议题例：第一空应与‘和衷共济’同向，第二空与‘置身事外’形成常见并列表达。

## 易错点 (`pitfalls`)

- 只看并列词不看语义方向
- 词性结构不一致

## 避免事项 (`forbidden`)

- 并列双方语义不协调

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
    - 24

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- parallel_terms
- semantic_direction
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

68

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

- 并列提示
- 同向对应
- 反向并列

## collocation_rules (`collocation_rules`)

- 并列项词性一致
- 常见搭配保持
