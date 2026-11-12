# 全同关系识别法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_logic_equivalence_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

逻辑关系

## 方法名称 (`method_name`)

全同关系识别法

## 检索标签 (`tags`)

- 逻辑关系
- 全同
- 别称
- 同一事物

## 适用条件 (`trigger_conditions`)

- 两个词指向同一对象或同一地区/事物的不同名称
- 选项有别称关系

## 不适用条件 (`anti_conditions`)

- 只是近义词但指代对象不同，不是全同

## 解题步骤 (`steps`)

- 判断A与B是否完全指同一对象。
- 排除近义但非同一对象的词。
- 检查选项是否也是别称/简称/旧称/俗称关系。
- 比较对象类别是否一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：牛油果-鳄梨、桂-广西为全同关系示例。

## 易错点 (`pitfalls`)

- 把近义误判为全同。

## 避免事项 (`forbidden`)

- 不得将相似概念当作全同。

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

- mode：identity_alias_check

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- must_output：
  - alias_or_same_object

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

逻辑关系-全同

## secondary_check (`secondary_check`)

- 是否同一对象
- 是否别称
- 是否与近义区分
