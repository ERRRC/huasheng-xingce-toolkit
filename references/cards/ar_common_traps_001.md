# 类比推理常见误判防错卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_common_traps_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

常见陷阱

## 方法名称 (`method_name`)

类比推理常见误判防错卡

## 检索标签 (`tags`)

- 陷阱
- 常识干扰
- 关系混淆
- 二级辨析

## 适用条件 (`trigger_conditions`)

- 类比推理任意题最终复核
- 选项均有一定联系但难以取舍

## 不适用条件 (`anti_conditions`)

- 非类比推理题不调用

## 解题步骤 (`steps`)

- 检查是否用冷门常识代替大众常识。
- 检查是否把种属与组成混淆。
- 检查是否把矛盾与反对混淆。
- 检查是否把特指与泛指混淆。
- 检查是否把因果、功能、目的、时间顺序混淆。
- 检查是否只看词性或字数，未看内在关系。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：资料强调类比三难点和大众思维、简单思维。

## 易错点 (`pitfalls`)

- 关系牵强也强行对应。

## 避免事项 (`forbidden`)

- 不得输出未通过二级辨析的答案。

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
    - 22

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- candidate_answer
- stem_relation
- option_relation

## 计算策略 (`calculation_policy`)

- mode：final_verification
- must_run_after_candidate：true

## 原程序优先级 (`solver_priority`)

99

## 原卡输出约束 (`output_constraints`)

- must_output：
  - trap_check_result

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

防错复核

## secondary_check (`secondary_check`)

- 大众思维
- 简单思维
- 种属/组成
- 矛盾/反对
- 特指/泛指
- 方向一致
