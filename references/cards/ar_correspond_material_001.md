# 原材料-成品关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_correspond_material_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

原材料-成品关系识别法

## 检索标签 (`tags`)

- 对应关系
- 原材料
- 成品
- 材料

## 适用条件 (`trigger_conditions`)

- 题干一个词是材料，另一个词是由该材料制成的物品
- 选项中存在材料-成品搭配

## 不适用条件 (`anti_conditions`)

- A是B的一部分时优先考虑组成关系，不等同于原材料关系

## 解题步骤 (`steps`)

- 判断A是否为制作B的原材料。
- 确认A不是B中的功能部件或组成零件。
- 比较选项是否同为材料到成品方向。
- 若方向相反，也需与题干方向一致才可选。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：木材-木桌被列为原材料对应。

## 易错点 (`pitfalls`)

- 把零件-整体误判为材料-成品。

## 避免事项 (`forbidden`)

- 不得把任意组成物都当作原材料。

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

- term_pair
- option_pairs

## 计算策略 (`calculation_policy`)

- mode：material_product_relation

## 原程序优先级 (`solver_priority`)

21

## 原卡输出约束 (`output_constraints`)

- must_output：
  - material
  - product
  - direction

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-原材料

## secondary_check (`secondary_check`)

- 材料到成品方向
- 区别于组成关系
