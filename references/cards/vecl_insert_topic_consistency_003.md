# 话题一致与多主体概括法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_insert_topic_consistency_003

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句填入

## 子题型 (`sub_type`)

话题一致

## 方法名称 (`method_name`)

话题一致与多主体概括法

## 检索标签 (`tags`)

- 语句填入
- 话题一致
- 多主体
- 总领

## 适用条件 (`trigger_conditions`)

- 后文列举多个主体或方面
- 选项主题词存在差异

## 不适用条件 (`anti_conditions`)

- 后文只是单一主体的递进说明

## 解题步骤 (`steps`)

- 确定后文共同话题，而不是每一句的局部对象。
- 识别后文列举的主体数量和身份。
- 横线句应概括这些主体及共同动作。
- 排除话题过宽、目标错误、无中生有的选项。
- 验证横线句与后文第一句的衔接是否自然。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 游戏监管例：制作方、政府、家长三方都出现，横线应对应三方形成合力，而非泛说游戏发展。

## 易错点 (`pitfalls`)

- 把“游戏发展”误当“游戏监管”
- 遗漏某一主体

## 避免事项 (`forbidden`)

- 横线句只覆盖一个主体

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

- following_subjects
- common_topic
- options

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

32

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- （空列表）

## coherence_checks (`coherence_checks`)

- 主体覆盖
- 话题一致
- 无新增目标

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
