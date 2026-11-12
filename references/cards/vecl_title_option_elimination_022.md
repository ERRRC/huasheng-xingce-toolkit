# 标题题干扰项排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_title_option_elimination_022

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

标题填入

## 子题型 (`sub_type`)

标题干扰项

## 方法名称 (`method_name`)

标题题干扰项排除法

## 检索标签 (`tags`)

- 标题拟定
- 干扰项
- 片面
- 无中生有

## 适用条件 (`trigger_conditions`)

- 标题选项包含初衷、由来、意义、作用等不同角度
- 选项覆盖范围差异明显

## 不适用条件 (`anti_conditions`)

- 所有选项均为同一角度，仅需比较语言优劣

## 解题步骤 (`steps`)

- 标记选项来源：过去目的、现在作用、局部句、整体原因。
- 排除只对应一段或一句的片面标题。
- 排除文段未提及的新概念或过度拔高标题。
- 排除主题词不一致的标题。
- 在剩余项中选最能统摄全文的标题。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 桥头堡题中‘初衷’只对应过去目的，‘名字由来’只对应一句，均片面。

## 易错点 (`pitfalls`)

- 标题看似精炼但只覆盖局部
- 被抽象词迷惑

## 避免事项 (`forbidden`)

- 选片面标题

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

- option_scope_map
- passage_sections
- topic_words

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

13

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
