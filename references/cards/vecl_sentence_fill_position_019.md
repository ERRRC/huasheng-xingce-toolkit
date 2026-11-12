# 横线位置功能判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_sentence_fill_position_019

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句填入

## 子题型 (`sub_type`)

横线位置功能

## 方法名称 (`method_name`)

横线位置功能判断法

## 检索标签 (`tags`)

- 语句填入
- 位置功能
- 段首段中段尾

## 适用条件 (`trigger_conditions`)

- 语句填入横线位于开头/中间/结尾
- 需要判断句子作用

## 不适用条件 (`anti_conditions`)

- 横线只是词语空缺

## 解题步骤 (`steps`)

- 横线在开头：优先总领全文、引出话题或提出观点。
- 横线在中间：重点承上启下，既接前文又引后文。
- 横线在结尾：优先总结全文、提出结论或对策。
- 结合关联词、代词、话题一致验证。
- 排除只满足一侧、不满足另一侧的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 古籍例横线在中间，既承接保护与利用不冲突，又引出影印扫描等做法。

## 易错点 (`pitfalls`)

- 只看横线后一侧
- 不判断位置功能

## 避免事项 (`forbidden`)

- 中间句只承上不启下

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】标题、下文、语句填入、排序.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 16
    - 17
-
  - file：【言语理解与表达】标题、下文、语句填入、排序.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- blank_position
- pre_context
- post_context
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

29

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- 段首总领
- 段中承上启下
- 段尾总结
- 两侧衔接

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
