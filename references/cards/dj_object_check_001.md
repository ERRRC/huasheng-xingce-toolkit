# 对象限定排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_object_check_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

客体/对象要素

## 方法名称 (`method_name`)

对象限定排除法

## 检索标签 (`tags`)

- 对象
- 客体
- 崇拜对象
- 定义要素

## 适用条件 (`trigger_conditions`)

- 定义含有行为指向对象，如崇拜的对象、求助对象、商业活动对象等
- 选项有行为但对象缺失或对象错误

## 不适用条件 (`anti_conditions`)

- 定义只描述行为过程，没有明确对象限制时，不要硬套对象检查

## 解题步骤 (`steps`)

- 标出定义中行为作用的对象。
- 识别选项中实际被看待、被求助、被作用的对象。
- 对象缺失、对象类型错误或对象关系不成立时排除。
- 对象符合后再检查方式和目的。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：粉丝滤镜效应要求看待自己崇拜的对象；只爱看战争剧没有崇拜对象。

## 易错点 (`pitfalls`)

- 把兴趣对象误判为崇拜对象。
- 把工具使用误判为求助他人。

## 避免事项 (`forbidden`)

- 不得把选项中任意相关名词当作定义对象。

## 来源文件 (`source_file`)

- 【判断推理】定义判断.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】定义判断.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 20

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- definition_object
- option_objects
- object_relation

## 计算策略 (`calculation_policy`)

- mode：element_check
- hard_elimination：true

## 原程序优先级 (`solver_priority`)

4

## 原卡输出约束 (`output_constraints`)

- must_output：
  - definition_object
  - option_object_match

## definition_elements (`definition_elements`)

- 主体：先检查
- 客体/对象：必须匹配
- 条件：null
- 方式：null
- 目的：null
- 结果：null
- 特殊要求：null

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
