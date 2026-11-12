# 先判题型后结构化求解流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_total_flow_001

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

综合流程

## 子题型 (`sub_type`)

语句表达与逻辑填空总流程

## 方法名称 (`method_name`)

先判题型后结构化求解流程

## 检索标签 (`tags`)

- 总流程
- 题型路由
- 结构优先
- 语境优先

## 适用条件 (`trigger_conditions`)

- 出现标题/下文/填入/排序/横线填词等题干形式

## 不适用条件 (`anti_conditions`)

- （空列表）

## 解题步骤 (`steps`)

- 先读题干形式：标题类看是否要求标题；下文类看是否问接下来讲什么；填入类看横线位置；排序类看句号编号；逻辑填空看横线词语。
- 语句表达类先做结构判断：首尾句、话题、转折/因果/并列、指代、时间顺序。
- 逻辑填空类先做语境定位：横线前后提示、关联词、感情色彩、程度、搭配、语法。
- 验证选项：排除话题不一致、出处不对、片面、无中生有、语法不通、搭配不当。
- 无法确定时回到原文结构，不用常识强行补全。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 综合路由：看到“最适合做标题”优先调用标题卡；看到“接下来最可能讲”优先调用下文卡；看到编号句子优先调用排序卡。

## 易错点 (`pitfalls`)

- 把标题题当普通主旨题但忽略标题可读性；把逻辑填空当近义词替换题而不看语境。

## 避免事项 (`forbidden`)

- 未识别题型直接选答案
- 只凭语感选择成语
- 排序题不验证首尾和捆绑关系

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】标题、下文、语句填入、排序.pdf
- 【言语理解与表达】逻辑填空.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 2
    - 12
    - 14
    - 16
    - 18
    - 22
    - 24
    - 26
-
  - file：【言语理解与表达】标题、下文、语句填入、排序.pdf
  - pages：
    - 1
-
  - file：【言语理解与表达】逻辑填空.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- question_stem
- passage_or_sentences
- options
- blank_positions
- sentence_numbers

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

1

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
