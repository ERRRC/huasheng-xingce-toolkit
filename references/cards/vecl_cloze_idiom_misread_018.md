# 望文生义防错卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_idiom_misread_018

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

成语误用

## 方法名称 (`method_name`)

望文生义防错卡

## 检索标签 (`tags`)

- 逻辑填空
- 成语
- 望文生义
- 备查

## 适用条件 (`trigger_conditions`)

- 选项含常见易错成语
- 成语表面意思与真实意思可能不同

## 不适用条件 (`anti_conditions`)

- 选项不含成语

## 解题步骤 (`steps`)

- 检查成语是否属于望文生义高风险。
- 确认成语真实含义、褒贬色彩和适用对象。
- 排除按字面理解才成立的选项。
- 与语境的对象、态度、程度逐项匹配。
- 必要时标记为需要人工复核，不凭印象强选。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 空穴来风指传闻有一定根据，不是毫无根据；文不加点形容文思敏捷，不是没有标点。

## 易错点 (`pitfalls`)

- 按字面解释成语
- 忽略成语常搭配否定形式

## 避免事项 (`forbidden`)

- 使用未确认含义的成语

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 40

## 原卡置信度 (`confidence`)

0.72

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- idiom_options
- context_attitude
- object

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

82

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

- 真实含义
- 褒贬色彩
- 适用对象

## collocation_rules (`collocation_rules`)

- 望其项背常搭配否定
- 汗牛充栋常指藏书
