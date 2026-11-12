# 交叉关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_logic_cross_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

逻辑关系-圈圈关系

## 方法名称 (`method_name`)

交叉关系识别法

## 检索标签 (`tags`)

- 逻辑关系
- 交叉
- 圈圈关系

## 适用条件 (`trigger_conditions`)

- 两个概念部分重合：有的A是B，有的B是A
- 选项中出现类别交叉关系

## 不适用条件 (`anti_conditions`)

- 若所有A都是B则为种属，不是交叉；若A是B一部分则为组成

## 解题步骤 (`steps`)

- 判断是否存在A∩B且A不完全属于B、B不完全属于A。
- 用“有的A是B，有的B是A”测试。
- 排除种属、组成、全同关系。
- 比较选项是否也为交叉关系。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：川菜与凉菜可作交叉关系示例。

## 易错点 (`pitfalls`)

- 把交叉误判为并列或种属。

## 避免事项 (`forbidden`)

- 不得只因两个词都属于食物/物品就判交叉。

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

- concept_A
- concept_B
- option_concepts

## 计算策略 (`calculation_policy`)

- mode：set_relation
- test：some_A_are_B_and_some_B_are_A

## 原程序优先级 (`solver_priority`)

15

## 原卡输出约束 (`output_constraints`)

- must_output：
  - set_relation_test

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

逻辑关系-交叉

## secondary_check (`secondary_check`)

- 有的A是B
- 有的B是A
- 非种属
- 非组成
