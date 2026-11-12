# 定义判断常见陷阱防错卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_common_traps_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

常见陷阱

## 方法名称 (`method_name`)

定义判断常见陷阱防错卡

## 检索标签 (`tags`)

- 陷阱
- 不属于
- 主体错误
- 对象错误
- 特殊要求

## 适用条件 (`trigger_conditions`)

- 定义判断任意题均可作为最终复核
- 选项看似贴近但存在细节差异

## 不适用条件 (`anti_conditions`)

- 非定义判断题不用调用

## 解题步骤 (`steps`)

- 检查是否把属于/不属于读反。
- 检查主体是否被替换。
- 检查对象是否缺失或对象关系错误。
- 检查特殊要求是否被忽略。
- 检查是否把另一个定义类别误当成目标定义。
- 检查是否机械关键词匹配而忽略整体含义。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：粉丝滤镜效应示例体现主体、对象两个陷阱；亲情经济体现特殊要求陷阱。

## 易错点 (`pitfalls`)

- 只看关键词命中。
- 用生活常识扩大定义范围。

## 避免事项 (`forbidden`)

- 不得在最终答案中省略对陷阱的复核。

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

- candidate_answer
- definition_text
- ask_polarity
- options

## 计算策略 (`calculation_policy`)

- mode：final_verification
- must_run_after_candidate：true

## 原程序优先级 (`solver_priority`)

99

## 原卡输出约束 (`output_constraints`)

- must_output：
  - trap_check_result

## definition_elements (`definition_elements`)

- 问法：最终复核
- 主体：最终复核
- 客体/对象：最终复核
- 条件：最终复核
- 方式：最终复核
- 目的：最终复核
- 结果：最终复核
- 特殊要求：最终复核

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
