# 如果是你会怎么写法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_as_writer_006

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

语境还原

## 方法名称 (`method_name`)

如果是你会怎么写法

## 检索标签 (`tags`)

- 逻辑填空
- 语境还原
- 写作意图

## 适用条件 (`trigger_conditions`)

- 空格处表达人物状态或整体评价
- 选项均可勉强搭配但语境色彩不同

## 不适用条件 (`anti_conditions`)

- 空格有明确语法硬约束时先判语法

## 解题步骤 (`steps`)

- 把自己代入作者，概括这一句想表达的状态。
- 把候选词逐个转换成白话含义。
- 选择最能表达原句画面和态度的词。
- 排除只描述表情、泛泛夸奖或不贴合风险状态的词。
- 带入验证文气是否一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 古籍修复师面对珍贵古籍，重点是极度谨慎，因此用‘如履薄冰’。

## 易错点 (`pitfalls`)

- 被熟悉词吸引
- 选择不能表现工作状态的词

## 避免事项 (`forbidden`)

- 选项只表达一般态度而不回应具体情境

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
    - 26

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- scene_description
- candidate_meanings
- author_tone

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

65

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

- 情境画面
- 心理状态
- 作者意图

## collocation_rules (`collocation_rules`)

- 状态词与人物行为一致
