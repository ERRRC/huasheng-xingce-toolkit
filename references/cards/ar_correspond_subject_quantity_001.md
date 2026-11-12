# 对应关系主体数量核对法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 模块 (`module`)

判断推理-定义判断与类比推理

## 检索标签 (`tags`)

- 类比推理
- 对应关系
- 功能
- 时间顺序
- 方式目的
- 主体数量
- 二级辨析

## 适用条件 (`trigger_conditions`)

- 题干为功能、时间顺序、方式目的、职业场所、工具对象等对应关系
- 多个选项均能造句但关系细节不同

## 不适用条件 (`anti_conditions`)

- 题干只是语义或语法关系时不优先调用

## 解题步骤 (`steps`)

- 先确认对应关系类型：功能、时间顺序、方式目的、职业场所、工具对象等。
- 若为功能，区分主要功能与次要功能。
- 若为时间顺序，先看时间先后，再看主体是否一致、主体数量是否一致。
- 若为方式目的，看通过某种方式是否能达到某种目的，并核对主体是否一致。
- 选项能造句不代表一定正确，还要检查主体、对象、数量和方向。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生判断笔记总结.pdf
  - page：21
  - summary：笔记提示对应关系范围很广，功能看主要/次要功能，时间顺序看时间先后、主体一致和主体数量，方式与目的看方式是否能达成目的。

## 易错点 (`pitfalls`)

- 只要能造句就选择，忽略主体数量或功能主次。
- 把目的关系和因果关系混淆。

## 避免事项 (`forbidden`)

- 不得用牵强造句强行建立关系。

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 21

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_terms
- option_terms
- candidate_correspondence_type

## 计算策略 (`calculation_policy`)

- mode：correspondence_check
- must_check：
  - 主体
  - 对象
  - 数量
  - 方向
  - 主次

## 原程序优先级 (`solver_priority`)

7

## 原卡输出约束 (`output_constraints`)

- must_output：
  - 对应类型
  - 主体数量核对
  - 关系方向

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

对应关系

## secondary_check (`secondary_check`)

- 功能主次
- 时间先后
- 主体一致
- 主体数量一致
- 方式是否达成目的

## 方法 ID (`id`)

ar_correspond_subject_quantity_001

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

对应关系二级辨析

## 方法名称 (`method_name`)

对应关系主体数量核对法
