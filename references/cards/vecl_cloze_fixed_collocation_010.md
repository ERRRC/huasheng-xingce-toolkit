# 固定用法优先法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_fixed_collocation_010

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

固定搭配

## 方法名称 (`method_name`)

固定用法优先法

## 检索标签 (`tags`)

- 逻辑填空
- 固定搭配
- 近义词搭配

## 适用条件 (`trigger_conditions`)

- 选项中存在明显固定短语
- 空格前后形成常见搭配

## 不适用条件 (`anti_conditions`)

- 固定搭配与语境冲突时不能机械套用

## 解题步骤 (`steps`)

- 识别空格前后是否构成固定搭配。
- 优先验证固定搭配是否与文段主题一致。
- 若搭配成立且语境无冲突，可作为强排除依据。
- 对多空题，固定搭配可先锁定一个空，再验证其他空。
- 注意近义词搭配对象差异。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- ‘奉为圭臬’为固定搭配，可直接帮助锁定选项。

## 易错点 (`pitfalls`)

- 知道固定搭配但忽略语境
- 把近义词强行套进固定搭配

## 避免事项 (`forbidden`)

- 破坏固定搭配

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
    - 38
    - 39
    - 40

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- pre_blank_words
- post_blank_words
- candidate_words

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

69

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

- 固定短语提示
- 搭配对象

## collocation_rules (`collocation_rules`)

- 奉为圭臬
- 履行承诺/执行任务
- 制定政策/制订方案
- 严谨思维/严密防守
