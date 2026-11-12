# 引申义/象征义识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_semantic_extended_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

语义关系

## 方法名称 (`method_name`)

引申义/象征义识别法

## 检索标签 (`tags`)

- 语义关系
- 引申义
- 象征义
- 常识

## 适用条件 (`trigger_conditions`)

- 题干词语存在古称、代称、象征义或引申含义
- 选项中出现文化常识词

## 不适用条件 (`anti_conditions`)

- 需要极冷僻知识才能解释时，谨慎使用并降低置信度

## 解题步骤 (`steps`)

- 判断题干是否为词语本义与引申义/代称之间的关系。
- 识别选项是否也为同类代称或象征。
- 优先选择大众常识范围内的对应。
- 若多个选项可解释，比较是否同为人/物/抽象意义的代称。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：青衿指学子、读书人；南冠指囚犯。玉盘象征月亮。

## 易错点 (`pitfalls`)

- 引入过深文学常识。
- 把比喻、功能、目的误当作引申义。

## 避免事项 (`forbidden`)

- 不得用生僻解释强行匹配。

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
    - 22

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_terms
- option_terms
- common_cultural_meaning

## 计算策略 (`calculation_policy`)

- mode：extended_meaning
- common_knowledge_only：true

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- must_output：
  - literal_term
  - extended_meaning

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

语义关系-引申义/象征义

## secondary_check (`secondary_check`)

- 代称对象类型一致
- 常识普遍性
- 是否与题干同为象征/代称
