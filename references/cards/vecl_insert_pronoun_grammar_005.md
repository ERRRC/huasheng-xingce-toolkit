# 主语语法与指代一致法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_insert_pronoun_grammar_005

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句填入

## 子题型 (`sub_type`)

主语语法指代

## 方法名称 (`method_name`)

主语语法与指代一致法

## 检索标签 (`tags`)

- 语句填入
- 代词指代
- 语法
- 主语一致

## 适用条件 (`trigger_conditions`)

- 横线后出现“它/这/其”等代词
- 选项主语不同
- 横线前后语法衔接明显

## 不适用条件 (`anti_conditions`)

- 没有代词且选项均为完整总领句

## 解题步骤 (`steps`)

- 检查横线后代词指代对象，横线句必须提供清晰先行词。
- 检查选项主语是否能承接后文谓语。
- 判断横线前后是否构成因果、转折、总结。
- 排除指代空缺、语法不顺、主语漂移的选项。
- 带入后读完整句验证自然度。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 植物油例：后文“它最适合温度不太高的烹饪”，横线中应有能被“它”指代的植物油。

## 易错点 (`pitfalls`)

- 选项本身正确但后文代词无所指
- 主语换成动作导致语法不通

## 避免事项 (`forbidden`)

- 让代词指代不明

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
    - 16
    - 17

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- pronouns_after_blank
- candidate_subjects
- sentence_grammar

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

34

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- 代词先行词明确
- 主谓宾通顺
- 上下文逻辑一致

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
