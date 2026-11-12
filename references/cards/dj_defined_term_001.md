# 抓住被定义词法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_defined_term_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

关键词拆解

## 方法名称 (`method_name`)

抓住被定义词法

## 检索标签 (`tags`)

- 被定义词
- 关键词拆解
- 核心特征

## 适用条件 (`trigger_conditions`)

- 定义名称本身含有明显语义，如“垂直搜索引擎”“亲情经济”“工具性求助”
- 选项与定义细节接近但概念本质不同

## 不适用条件 (`anti_conditions`)

- 被定义词为高度抽象、名称不能直接提示核心特征时，不可只靠名称判断

## 解题步骤 (`steps`)

- 先读被定义词名称，标出名称中最关键的一两个词。
- 判断这些词为何被用作定义之名，推测其最核心特征。
- 回到定义文本验证核心特征。
- 选项代入时优先排除与名称核心特征不符的项。
- 最后再核对定义中的主体、对象、特殊要求。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：“垂直搜索引擎”必须同时体现搜索引擎与专业领域搜索；购物网站、央视网站、图书馆网站均不符合搜索引擎核心。

## 易错点 (`pitfalls`)

- 只看定义句中的局部词，不看定义名称。
- 把平台、网站、查询行为误等同于搜索引擎。

## 避免事项 (`forbidden`)

- 不得脱离定义文本，只凭名称想象含义。

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

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- defined_term
- definition_text
- options

## 计算策略 (`calculation_policy`)

- mode：semantic_core_extraction
- first_pass：defined_term

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- must_output：
  - defined_term_core
  - option_core_mismatch

## definition_elements (`definition_elements`)

- 被定义词：核心入口
- 主体：null
- 客体/对象：null
- 条件：null
- 方式：null
- 目的：null
- 结果：null
- 特殊要求：null

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
