# 包含全篇关键词法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_insert_keyword_002

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句填入

## 子题型 (`sub_type`)

关键词覆盖

## 方法名称 (`method_name`)

包含全篇关键词法

## 检索标签 (`tags`)

- 语句填入
- 关键词
- 因果衔接

## 适用条件 (`trigger_conditions`)

- 横线前出现原因或限制，横线后承接“因此/本文尝试/所以”
- 选项覆盖关键词程度不同

## 不适用条件 (`anti_conditions`)

- 关键词只是例子或背景，不是主线

## 解题步骤 (`steps`)

- 抽取横线前后的核心限定词。
- 横线句必须回应这些限定词，不能漏掉关键维度。
- 若前文说已有研究缺少A、局限B，则横线往往补“从A角度研究非B对象”。
- 排除只满足部分关键词的选项。
- 带入确认与后文语义不冲突。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 族群研究例：前文说没有从经济层面、范围仅限欧洲，横线应体现经济层面和非欧洲对象。

## 易错点 (`pitfalls`)

- 只命中一个关键词就选
- 忽略“尝试”表示新角度

## 避免事项 (`forbidden`)

- 重复前人已做过的范围

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

- key_constraints_before_blank
- options
- post_blank_context

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

31

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- 关键词完整性
- 新旧信息衔接
- 前后逻辑一致

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
