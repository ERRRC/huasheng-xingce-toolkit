# 逻辑对应关系定位法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_cloze_logic_correspondence_004

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

逻辑填空

## 子题型 (`sub_type`)

逻辑对应

## 方法名称 (`method_name`)

逻辑对应关系定位法

## 检索标签 (`tags`)

- 逻辑填空
- 逻辑对应
- 解释提示
- 后文提示

## 适用条件 (`trigger_conditions`)

- 横线前后有明显解释、结果、例证或并列对应
- 多空题某一空有强提示句

## 不适用条件 (`anti_conditions`)

- 文段缺少提示信息，只能依靠词义与搭配

## 解题步骤 (`steps`)

- 不要找表面字面对应，先确定语句之间的逻辑关系。
- 寻找横线后解释句、结果句或关键词。
- 从提示最强的空切入。
- 选词要能与提示句形成同义、反义、因果或程度对应。
- 带入其余空验证整体一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- ‘失去改革最佳窗口期’提示问题长期不解决且难以回转，对应‘积重难返’。

## 易错点 (`pitfalls`)

- 看到相同字就选
- 没有判断提示句与空格的关系

## 避免事项 (`forbidden`)

- 只做字面重复

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

- context_before_after_blank
- logical_markers
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

63

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

- 解释提示
- 结果提示
- 因果对应
- 反义对应

## collocation_rules (`collocation_rules`)

- 提示词与候选词语义方向一致
