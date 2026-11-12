# 总分话题结束反向续写法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_next_topic_finished_002

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

下文推断

## 子题型 (`sub_type`)

话题结束

## 方法名称 (`method_name`)

总分话题结束反向续写法

## 检索标签 (`tags`)

- 下文推断
- 话题结束
- 反向续写
- 整体文段

## 适用条件 (`trigger_conditions`)

- 上文已经完整介绍某一面
- 尾句没有新信息但首句设置问题或对比空间

## 不适用条件 (`anti_conditions`)

- 尾句有明确新信息时优先尾句法

## 解题步骤 (`steps`)

- 判断当前文段是否已经把某个话题讲完。
- 若已讲完“有A”的情况，考虑下文可能讲“无A/另一类A”。
- 从首句设问或全文主线寻找未被展开的另一面。
- 排除继续重复已结束话题的选项。
- 选择与全文话题保持一致但推进到新分支的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 古代城市城墙例：上文讲有城墙的都城，下文更可能讲没有城墙的中国古代城市。

## 易错点 (`pitfalls`)

- 误以为任何下文都看尾句
- 没有判断文段话题是否已经结束

## 避免事项 (`forbidden`)

- 选择上文已介绍过的作用、原因或例子

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

- passage_topic
- covered_aspects
- uncovered_aspects
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

21

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
