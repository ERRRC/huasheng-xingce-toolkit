# 功能关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_correspond_function_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系

## 方法名称 (`method_name`)

功能关系识别法

## 检索标签 (`tags`)

- 对应关系
- 功能关系
- 用途

## 适用条件 (`trigger_conditions`)

- 题干一个词是物品/主体，另一个词是其功能
- 选项存在工具或物品与功能关系

## 不适用条件 (`anti_conditions`)

- 目的关系、使用对象关系或场所关系更明确时，不要只判功能

## 解题步骤 (`steps`)

- 判断A的主要功能是否为B。
- 检查选项是否也为物品-功能或功能-物品。
- 比较功能是否为主要功能而非偶然用途。
- 核对方向。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：灭火器-灭火被列为功能关系。

## 易错点 (`pitfalls`)

- 把目的、结果、对象误判为功能。

## 避免事项 (`forbidden`)

- 不得用偶然用途替代主要功能。

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

- mode：function_relation

## 原程序优先级 (`solver_priority`)

19

## 原卡输出约束 (`output_constraints`)

- must_output：
  - function_owner
  - function

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系-功能

## secondary_check (`secondary_check`)

- 主要功能/次要功能
- 主体是否一致
- 对象是否一致
- 数量是否一致
