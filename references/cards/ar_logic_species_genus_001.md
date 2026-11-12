# 种属关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_logic_species_genus_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

逻辑关系-包含

## 方法名称 (`method_name`)

种属关系识别法

## 检索标签 (`tags`)

- 逻辑关系
- 种属关系
- 包含
- 特指泛指

## 适用条件 (`trigger_conditions`)

- A是B的一种
- 可表达为所有A都是B

## 不适用条件 (`anti_conditions`)

- A只是B的一部分时是组成关系，不是种属

## 解题步骤 (`steps`)

- 用“A是B的一种/所有A都是B”测试题干。
- 区分特指与泛指：苏格拉底-人类属于特指个体到类，公交车-汽车属于泛指类别到类。
- 排除组成关系。
- 检查选项是否同为种属，且特指/泛指层级一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：资料强调种属与组成区别：A是B为种属；苏格拉底-人类、公交车-汽车为示例。

## 易错点 (`pitfalls`)

- 把轮胎-汽车误判为种属。
- 忽略特指/泛指差异。

## 避免事项 (`forbidden`)

- 不得把组成部分说成一种。

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

- mode：set_inclusion
- test：all_A_are_B

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- must_output：
  - species_genus_direction
  - specific_or_generic

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

逻辑关系-种属

## secondary_check (`secondary_check`)

- A是B的一种
- 特指/泛指一致
- 不是组成关系
