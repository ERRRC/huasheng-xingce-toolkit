# 不符合定义项排除流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_elimination_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

排除法

## 方法名称 (`method_name`)

不符合定义项排除流程

## 检索标签 (`tags`)

- 排除法
- 主体不符
- 对象不符
- 条件不符

## 适用条件 (`trigger_conditions`)

- 选项数量固定，且每项均可与定义元素比对
- 需要快速定位唯一符合/不符合项

## 不适用条件 (`anti_conditions`)

- 题干问最能概括、最能推出时不是定义判断排除流程

## 解题步骤 (`steps`)

- 按问法确定要保留符合项还是不符合项。
- 第一轮排除主体或对象明显错误项。
- 第二轮排除特殊要求、条件、方式不满足项。
- 第三轮比较剩余选项与被定义词核心含义的贴合度。
- 输出时说明排除理由，不只给答案。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：垂直搜索引擎题排除不是搜索引擎的网站/购物行为，再保留百度音乐。

## 易错点 (`pitfalls`)

- 排除理由不是定义依据，而是个人常识判断。

## 避免事项 (`forbidden`)

- 不得凭选项熟悉度选择。

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

- ask_polarity
- definition_elements_extracted
- options

## 计算策略 (`calculation_policy`)

- mode：ordered_elimination
- element_order：
  - 问法
  - 被定义词
  - 主体
  - 对象
  - 特殊要求
  - 方式/目的/结果

## 原程序优先级 (`solver_priority`)

8

## 原卡输出约束 (`output_constraints`)

- must_output：
  - elimination_reasons
- format：option_by_option

## definition_elements (`definition_elements`)

- 主体：优先排除
- 客体/对象：优先排除
- 条件：次级排除
- 方式：次级排除
- 目的：次级排除
- 结果：次级排除
- 特殊要求：优先排除

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
