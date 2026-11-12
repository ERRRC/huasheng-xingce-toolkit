# 尾句承上启下看新信息法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_next_tail_newinfo_001

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

下文推断

## 子题型 (`sub_type`)

尾句新信息

## 方法名称 (`method_name`)

尾句承上启下看新信息法

## 检索标签 (`tags`)

- 下文推断
- 尾句
- 新信息
- 话题延续

## 适用条件 (`trigger_conditions`)

- 题干出现“接下来最可能讲的是”
- 末句出现新概念、未展开对象、时间转折如“过去”

## 不适用条件 (`anti_conditions`)

- 末句只是总结全文且没有新信息
- 选项继续重复上文已谈内容

## 解题步骤 (`steps`)

- 定位最后一句，找新出现且尚未展开的信息。
- 判断末句是承上总结还是启下引出新话题。
- 下文必须延续新信息，不能跳到旧话题或泛化话题。
- 若末句出现“过去没有/此前不足”，下文常接“现在突破/解决办法”。
- 排除上文已经详细讲过的内容。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 社交恐惧症例：尾句说过去没有满意治疗方法，下文应讲现在治疗方法上的突破。

## 易错点 (`pitfalls`)

- 只看文段主题不看尾句新信息
- 把已讲危害继续作为下文

## 避免事项 (`forbidden`)

- 下文选项与尾句关键词不一致

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
    - 14
    - 15

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- last_sentence
- new_terms
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

20

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
