# 造句法：工具-对象-场所对应

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_sentence_tool_object_place_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

造句法：工具-对象-场所对应

## 检索标签 (`tags`)

- 造句法
- 工具与对象
- 职业与场所
- 物品对象地点

## 适用条件 (`trigger_conditions`)

- 题干为三词关系，词间关系不直观
- 可能涉及物品、对象、地点、动作

## 不适用条件 (`anti_conditions`)

- 题干两词已能明确一级关系时，造句法作为复核而非首选

## 解题步骤 (`steps`)

- 用自然句把题干词语串联起来。
- 标注每个词在句子中的角色：地点、物品/工具、对象、动作等。
- 对选项造同结构句。
- 选择句法角色和语义角色都一致的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：点唱机-歌曲-歌厅：在歌厅用点唱机点播歌曲。

## 易错点 (`pitfalls`)

- 造句过于牵强。
- 只保证能造句，不保证角色一致。

## 避免事项 (`forbidden`)

- 不得为每个选项临时造不同句式。

## 来源文件 (`source_file`)

- 【判断推理】类比推理.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】类比推理.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 21

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_terms
- option_terms

## 计算策略 (`calculation_policy`)

- mode：sentence_role_mapping
- same_sentence_pattern_required：true

## 原程序优先级 (`solver_priority`)

25

## 原卡输出约束 (`output_constraints`)

- must_output：
  - stem_sentence
  - role_mapping
  - option_sentence_match

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-造句

## secondary_check (`secondary_check`)

- 地点/工具/对象角色一致
- 句式一致
- 不能牵强造句
