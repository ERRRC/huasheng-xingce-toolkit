# 作者意图与对象特征法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_intent_object_005

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

对象特征

## 方法名称 (`method_name`)

作者意图与对象特征法

## 检索标签 (`tags`)

- 逻辑填空
- 对象特征
- 作者意图
- 宏观把握

## 适用条件 (`trigger_conditions`)

- 词语选择取决于对象性质或作者评价
- 文段描述人物/事物状态

## 不适用条件 (`anti_conditions`)

- 存在明确固定搭配或关联词直接定位时先用其他规则

## 解题步骤 (`steps`)

- 跳出局部字面，判断作者想表达的总体意思。
- 明确被描述对象的属性、状态和现实特征。
- 候选词要符合该对象的自然属性。
- 排除看似能搭配但不符合对象特征的词。
- 带入后检查是否能表达作者态度。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 放归野外的动物需要‘合适’栖息地；‘安全’不贴合放归野外的目的。

## 易错点 (`pitfalls`)

- 只按字面搭配选词
- 忽略对象本身不可能具备的属性

## 避免事项 (`forbidden`)

- 使用与对象现实属性冲突的词

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
    - 22
    - 26

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- described_object
- object_features
- author_intent

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

64

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

- 对象属性
- 作者态度
- 现实合理性

## collocation_rules (`collocation_rules`)

- 词语对象适配
- 语义符合现实语境
