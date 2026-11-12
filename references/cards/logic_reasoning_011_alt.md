# 常用逻辑关系40组通式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_reasoning_011_alt

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

翻译推理

## 方法名称 (`method_name`)

常用逻辑关系40组通式

## 别名 (`aliases`)

- 逻辑推理公式
- 形式逻辑必备

## 检索标签 (`tags`)

- 翻译推理
- 形式逻辑
- 命题转化

## 适用条件 (`trigger_conditions`)

题目涉及假言命题、联言命题、选言命题的翻译与推理，需要寻找矛盾、等价或推出关系

## 不适用条件 (`anti_conditions`)

日常推理，无逻辑关联词

## 所需信息 (`required_inputs`)

- 包含逻辑关联词的题干命题

## 推理策略 (`reasoning_policy`)

- core_logic：熟练运用前推后、后推前、否后推否前及摩根定律等进行命题的等价转换与矛盾求取。
- detailed_policy：充分条件前推后（如果A那么B -> A->B）；必要条件后推前（只有A才B -> B->A，除非A否则B -> -B->A）。矛盾关系找反面（A且B矛盾为-A或-B）；等价关系逆否命题（A->B等价于-B->-A）；推出关系递推法（A->B, B->C 则 A->C）。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：100
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 识别题干中的逻辑关联词（如果...那么，只有...才，除非...否则，所有，有的，且，或）。
- 将其翻译为标准逻辑表达式（如 A->B）。
- 根据题目问法，求其矛盾命题、等价命题或进行递推推导。
- 对照选项，选出符合逻辑公式的答案。

## 公式 (`formulas`)

- 如果A，那么B = A -> B
- 只有A，才B = B -> A
- 除非A，否则B = -B -> A
- 所有A都是B = A -> B
- 有的A是B = 有的A -> B
- A或B且-(A且B) = 要么A，要么B
- A是B的充分条件 = A -> B
- A是B的必要条件 = B -> A
- 某个A是B 矛盾 某个A不是B
- 所有A都是B 矛盾 有的A不是B
- A且B 矛盾 -A或-B
- A或B 矛盾 -A且-B
- A -> B 矛盾 A且-B
- 所有A都是B 反对 所有A都不是B
- 有的A是B 反反对 有的A不是B
- A -> B 等价 -A或B
- -(A且B) 等价 -A或-B
- -(A或B) 等价 -A且-B
- A -> B 等价 -B -> -A
- A且B -> A(B) -> A或B
- A -> -A, 则 -A 为真

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 除非A否则B翻译错方向（应为-B->A）
- 将必要条件当做充分条件

## 避免事项 (`forbidden`)

- 代入个人主观常识进行推理

## 原卡输出约束 (`output_constraints`)

- 输出符号化翻译结果或正确选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 66
- 67

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
