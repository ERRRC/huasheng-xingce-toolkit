# 主体限定排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_subject_check_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

主体要素

## 方法名称 (`method_name`)

主体限定排除法

## 检索标签 (`tags`)

- 主体
- 定义要素
- 排除法

## 适用条件 (`trigger_conditions`)

- 定义中出现明确主体，如年轻人、商家、求助者、工作学习者等
- 选项行为主体明显不同

## 不适用条件 (`anti_conditions`)

- 定义没有限定主体，或主体只是泛指对象时，不要强行排除

## 解题步骤 (`steps`)

- 标记定义中的行为主体或适用主体。
- 逐项识别选项中的行为主体。
- 主体不符合时直接排除；主体符合后再看对象和行为。
- 若题问不属于，主体不符的选项优先成为候选答案。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：粉丝滤镜效应限定主体为年轻人，五岁小刚不是年轻人，应排除。

## 易错点 (`pitfalls`)

- 忽略年龄、身份、组织类型等主体限定。

## 避免事项 (`forbidden`)

- 不得在定义限定主体明确时用相似行为替代主体要求。

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

- definition_subject
- option_subjects
- ask_polarity

## 计算策略 (`calculation_policy`)

- mode：element_check
- hard_elimination：true

## 原程序优先级 (`solver_priority`)

3

## 原卡输出约束 (`output_constraints`)

- must_output：
  - definition_subject
  - option_subject
- if_not_match：exclude_or_select_for_not_belong

## definition_elements (`definition_elements`)

- 主体：必须匹配
- 客体/对象：后续检查
- 条件：null
- 方式：null
- 目的：null
- 结果：null
- 特殊要求：null

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
