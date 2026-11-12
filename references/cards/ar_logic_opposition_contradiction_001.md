# 反对/矛盾二级辨析法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_logic_opposition_contradiction_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

逻辑关系-并列

## 方法名称 (`method_name`)

反对/矛盾二级辨析法

## 检索标签 (`tags`)

- 逻辑关系
- 并列
- 反对
- 矛盾
- 二级辨析

## 适用条件 (`trigger_conditions`)

- 题干两词互斥或相反
- 选项同时出现反对与矛盾关系

## 不适用条件 (`anti_conditions`)

- 只是语义近反义但非概念集合关系时，不必套用矛盾/反对

## 解题步骤 (`steps`)

- 先判断A与B是否互斥。
- 若非A即B、没有第三者，则为矛盾关系。
- 若有第三种可能，则为反对关系。
- 选项必须与题干同为矛盾或同为反对。
- 再检查词性和概念层级是否一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：两栖动物-哺乳动物为反对；城市-农村为矛盾。资料将矛盾和反对区别列为三难点。

## 易错点 (`pitfalls`)

- 把反对当矛盾，忽略第三者。

## 避免事项 (`forbidden`)

- 不得只因两个词不同就判并列。

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

- concept_pair
- option_pairs

## 计算策略 (`calculation_policy`)

- mode：mutual_exclusion_check
- third_possibility_test：true

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- must_output：
  - relation_is_contradiction_or_opposition
  - third_possibility

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

逻辑关系-反对/矛盾

## secondary_check (`secondary_check`)

- 有无第三者
- 非A即B测试
- 概念层级一致
