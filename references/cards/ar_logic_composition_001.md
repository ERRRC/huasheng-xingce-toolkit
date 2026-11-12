# 组成关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_logic_composition_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

逻辑关系-包含

## 方法名称 (`method_name`)

组成关系识别法

## 检索标签 (`tags`)

- 逻辑关系
- 组成关系
- 部分整体

## 适用条件 (`trigger_conditions`)

- A是B的一部分
- 题干存在零件-整体、成员-整体关系

## 不适用条件 (`anti_conditions`)

- 若A是B的一种，应转入种属关系

## 解题步骤 (`steps`)

- 用“A是B的一部分”测试题干。
- 确认A与B不是同类层级，而是部分与整体。
- 检查选项是否也为部分-整体，且方向一致。
- 若选项为一种-类别，排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：轮胎-汽车为组成关系。

## 易错点 (`pitfalls`)

- 种属与组成混淆是类比三难点之一。

## 避免事项 (`forbidden`)

- 不得把部分整体关系写成所有A都是B。

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

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- concept_A
- concept_B
- option_concepts

## 计算策略 (`calculation_policy`)

- mode：part_whole_relation

## 原程序优先级 (`solver_priority`)

13

## 原卡输出约束 (`output_constraints`)

- must_output：
  - part_whole_direction

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

逻辑关系-组成

## secondary_check (`secondary_check`)

- A是B的一部分
- 方向一致
- 区别于种属
