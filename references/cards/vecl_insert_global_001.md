# 语句填入整体通篇法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_insert_global_001

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句填入

## 子题型 (`sub_type`)

整体首句/通篇

## 方法名称 (`method_name`)

语句填入整体通篇法

## 检索标签 (`tags`)

- 语句填入
- 整体理解
- 首句
- 总领句

## 适用条件 (`trigger_conditions`)

- 横线在段首或段中关键位置
- 后文多句共同解释横线

## 不适用条件 (`anti_conditions`)

- 横线只承担局部衔接且前后有明确代词/关联词

## 解题步骤 (`steps`)

- 先判断横线位置：段首多为总领，段中多为承上启下，段尾多为总结。
- 通读全段，确定横线要概括的后文范围。
- 若横线在首句，选项必须能统领后文各主体/分论点。
- 排除只覆盖后文某一分支的选项。
- 带入后检查语义是否自然、逻辑是否完整。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 游戏监管例：后文分别谈开发团队、政府、家长，首句应概括三方形成合力。

## 易错点 (`pitfalls`)

- 只看横线后一两句导致片面
- 首句选项无总领能力

## 避免事项 (`forbidden`)

- 首句引入后文没有展开的新概念

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
    - 16
    - 17

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- blank_position
- following_sentences
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- 位置功能检查
- 后文覆盖检查
- 主题词一致检查
- 带入通顺检查

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
