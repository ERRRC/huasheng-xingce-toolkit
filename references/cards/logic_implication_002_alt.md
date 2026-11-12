# 假言命题翻译与逆否推理

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_implication_002_alt

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

翻译推理

## 方法名称 (`method_name`)

假言命题翻译与逆否推理

## 别名 (`aliases`)

- 前推后
- 后推前
- 逆否定理

## 检索标签 (`tags`)

- 假言命题
- 如果那么
- 只有才
- 除非否则

## 适用条件 (`trigger_conditions`)

题干中出现'如果...那么...','只要...就...','只有...才...','除非...否则不...'等表示条件关系的关联词。

## 不适用条件 (`anti_conditions`)

没有条件关联词的直言命题或日常推理。

## 所需信息 (`required_inputs`)

- 条件命题

## 推理策略 (`reasoning_policy`)

- core_logic：充分条件（如果A那么B）前推后：A->B；必要条件（只有A才B）后推前：B->A；除非A否则不B：B->A（或非A->非B）。逆否原则：A->B 等价于 非B->非A。
- detailed_policy：识别关联词提取逻辑式。应用'肯前必肯后，否后必否前，否前肯后无必然联系'进行推理。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：15
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 识别关联词，确定是充分条件还是必要条件。
- 2. 翻译为A->B的标准形式。
- 3. 结合已知条件，应用逆否定理（肯前肯后，否后否前）得出结论。

## 公式 (`formulas`)

- 如果A那么B => A->B
- 只有A才B => B->A
- 除非A否则不B => B->A
- A->B = 非B->非A

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 混淆充分条件和必要条件，导致箭头画反。
- 犯'否前推否后'或'肯后推肯前'的逻辑错误。

## 避免事项 (`forbidden`)

- 无条件肯定后件来推断肯定前件。

## 原卡输出约束 (`output_constraints`)

- 输出推导出的逻辑必然结果。

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 50

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
