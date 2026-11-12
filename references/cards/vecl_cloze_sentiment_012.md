# 褒贬色彩匹配法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_sentiment_012

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

感情色彩

## 方法名称 (`method_name`)

褒贬色彩匹配法

## 检索标签 (`tags`)

- 逻辑填空
- 感情色彩
- 褒贬

## 适用条件 (`trigger_conditions`)

- 文段含真假莫辨、甚至、损害、狂热、灰色产业等评价词
- 选项褒贬色彩不同

## 不适用条件 (`anti_conditions`)

- 选项都是中性词，需看搭配或程度

## 解题步骤 (`steps`)

- 判断作者对对象的态度：肯定、否定、担忧、中性。
- 给候选词标注褒义、贬义、中性。
- 优先排除色彩方向相反的词。
- 再看词义侧重和搭配。
- 带入确认语气一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 网红食品例：文段带否定态度，‘趋之若鹜’偏贬义，能反映作者态度。

## 易错点 (`pitfalls`)

- 把褒义词用于批评语境
- 只看词义不看态度

## 避免事项 (`forbidden`)

- 感情色彩与文段态度相反

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
    - 24

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- author_attitude_markers
- candidate_sentiment

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

71

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

- 感情色彩
- 作者态度
- 评价词

## collocation_rules (`collocation_rules`)

- 褒贬与对象一致
