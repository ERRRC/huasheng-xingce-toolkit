# 时间轴与逻辑顺序法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vecl_order_time_logic_007

## 模块 (`module`)

言语理解-语句表达与逻辑填空

## 题型 (`question_type`)

语句排序

## 子题型 (`sub_type`)

时间与逻辑顺序

## 方法名称 (`method_name`)

时间轴与逻辑顺序法

## 检索标签 (`tags`)

- 语句排序
- 时间顺序
- 逻辑顺序

## 适用条件 (`trigger_conditions`)

- 句中有长期以来、后来、目前、如今、此前等时间词
- 材料呈发展过程

## 不适用条件 (`anti_conditions`)

- 时间词只是例子内部时间，不支配全文结构

## 解题步骤 (`steps`)

- 抽取所有时间标记并排序。
- 先按时间轴排出大框架。
- 再用指代、转折、尾首相连补局部关系。
- 若时间轴与逻辑结构冲突，以文段主线为准并重新验证。
- 通读检查是否符合认知顺序：先背景、后变化、再结论。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 玛雅文明例：“长期以来”早于“目前”，可先排除以“目前”开头的选项。

## 易错点 (`pitfalls`)

- 只按时间词机械排序而忽略指代
- 把现在例子放在理论前

## 避免事项 (`forbidden`)

- 时间顺序倒置且无倒叙提示

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
    - 18
    - 19

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- time_markers
- candidate_orders
- logical_markers

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_intuition_only：false
- must_trace_text_evidence：true

## 原程序优先级 (`solver_priority`)

46

## 原卡输出约束 (`output_constraints`)

- answer_basis：必须给出文段/语境中的结构依据或搭配依据
- avoid：
  - 只凭语感
  - 只看单个字面相似词
  - 无来源扩展知识

## ordering_clues (`ordering_clues`)

- 长期以来/后来/目前/如今
- 先总后分
- 先背景后结论

## coherence_checks (`coherence_checks`)

- （空列表）

## semantic_clues (`semantic_clues`)

- （空列表）

## collocation_rules (`collocation_rules`)

- （空列表）
