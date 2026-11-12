# 转折前后反向定位法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_transition_007

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

转折提示

## 方法名称 (`method_name`)

转折前后反向定位法

## 检索标签 (`tags`)

- 逻辑填空
- 转折
- 关联词
- 反向提示

## 适用条件 (`trigger_conditions`)

- 出现但、然而、不过、却等转折词
- 转折前后描述对象相同但结论相反

## 不适用条件 (`anti_conditions`)

- 转折词只连接轻微补充，不构成语义反向

## 解题步骤 (`steps`)

- 定位转折词，确定转折后重点。
- 转折前空格往往与转折后形成相反或对照。
- 先填转折后约束更强的空，再回推前文。
- 排除同向词、程度不符词。
- 带入验证前后确实形成转折。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 内外太阳系例：转折后说成分相似，转折前应表达最初差异大。

## 易错点 (`pitfalls`)

- 只看到‘但’不分析转折方向
- 候选词语义同向

## 避免事项 (`forbidden`)

- 转折前后语义一致

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
    - 24

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- transition_marker
- before_after_semantics
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

66

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

- 转折提示
- 反向对应

## collocation_rules (`collocation_rules`)

- 前后词义方向相反或形成对比
