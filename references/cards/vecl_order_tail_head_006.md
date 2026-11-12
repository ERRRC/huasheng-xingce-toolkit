# 尾首重复词相连法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_tail_head_006

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

尾首相连

## 方法名称 (`method_name`)

尾首重复词相连法

## 检索标签 (`tags`)

- 语句排序
- 尾首相连
- 重复词

## 适用条件 (`trigger_conditions`)

- 某句末尾词与另一句开头词重复或解释
- 选项中存在固定相邻差异

## 不适用条件 (`anti_conditions`)

- 重复词只是同一主题高频词，不构成承接

## 解题步骤 (`steps`)

- 找每句句尾的核心名词、观点名、理论名。
- 在其他句子开头或主体中找直接承接。
- 优先形成相邻组合。
- 结合时间顺序或结构验证组合位置。
- 排除重复词不构成解释关系的伪捆绑。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 玛雅文明例：⑥句尾提“扶桑国”，②句解释扶桑国，应⑥②相连。

## 易错点 (`pitfalls`)

- 所有同话题词都当尾首相连
- 忽略时间线

## 避免事项 (`forbidden`)

- 强行捆绑无解释关系的同词句

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

- sentence_end_terms
- sentence_start_terms
- candidate_orders

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

45

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 句尾关键词
- 句首复现
- 解释承接
- 相邻组合

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
