# 尾句总结对策法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_last_sentence_003

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

尾句判断

## 方法名称 (`method_name`)

尾句总结对策法

## 检索标签 (`tags`)

- 语句排序
- 尾句判断
- 总结
- 对策

## 适用条件 (`trigger_conditions`)

- 候选尾句中出现“因此/所以/可见/应当/必须”等
- 选项尾句不同

## 不适用条件 (`anti_conditions`)

- 结论句后还有明显解释或例证未放置

## 解题步骤 (`steps`)

- 寻找总结词或对策词。
- 判断该句是否概括前文或提出最终做法。
- 若是总结/对策句，优先放尾句。
- 检查前文是否已经铺垫其结论对象。
- 排除把例子或定义放在尾句的排序。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 生态红线例：①“因此”引出总结和对策，大概率为尾句。

## 易错点 (`pitfalls`)

- 只看到“因此”就放尾，不检查前文铺垫

## 避免事项 (`forbidden`)

- 总结句前没有对应论证

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

- candidate_last_sentences
- conclusion_markers
- policy_markers

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

42

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 因此/所以
- 总结句
- 对策句
- 前文铺垫

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
