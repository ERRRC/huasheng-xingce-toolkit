# 递进程度加重法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_progressive_008

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

递进提示

## 方法名称 (`method_name`)

递进程度加重法

## 检索标签 (`tags`)

- 逻辑填空
- 递进
- 程度轻重
- 关联词

## 适用条件 (`trigger_conditions`)

- 出现既不能、也不能、更不能、不仅、甚至等递进标志

## 不适用条件 (`anti_conditions`)

- 并列结构无程度递进

## 解题步骤 (`steps`)

- 标出递进链条中的每一层。
- 后一个空的程度或危害通常要重于前一个空。
- 第一空要与前文形成对应，第二空要体现进一步加重。
- 排除程度倒置或语义重复的选项。
- 带入验证递进关系自然。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 教育孩子例：既不能放纵不管，也不能越俎代庖，更不能揠苗助长。

## 易错点 (`pitfalls`)

- 忽略‘更不能’导致程度不升反降
- 把同义词并列当递进

## 避免事项 (`forbidden`)

- 递进层级错乱

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

- progressive_markers
- degree_scale
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

67

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

- 递进提示
- 程度加重
- 反义对应

## collocation_rules (`collocation_rules`)

- 递进前后语义层级递升
