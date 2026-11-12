# 定义关键词查找抓手法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 模块 (`module`)

判断推理-定义判断与类比推理

## 检索标签 (`tags`)

- 定义判断
- 关键词
- 抓手
- 必要条件
- 否定条件
- 枚举

## 适用条件 (`trigger_conditions`)

- 定义文本较长，难以确定核心条件
- 题干出现名词本质解释、延伸解释、逻辑关联语气词、必要条件、否定条件或枚举结构

## 不适用条件 (`anti_conditions`)

- 定义很短且核心要素清晰时，不必过度拆解
- 无限枚举或开放式举例不能单独作为抓手

## 解题步骤 (`steps`)

- 先找题干既有定义名词的本质解释和延伸解释。
- 若定义中出现逻辑关联语气转折，尤其形成对比色彩，优先作为抓手。
- 若出现必要性条件型语句，将其视为强约束。
- 若出现否定性条件型语句，将其视为强排除条件。
- 若定义用有限枚举界定概念，可作为抓手；若是无限枚举，只能作为辅助理解。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生判断笔记总结.pdf
  - page：20
  - summary：关键词查找技巧列出本质解释/延伸解释、逻辑关联语气转折、必要性条件、否定性条件、有限枚举等抓手。

## 易错点 (`pitfalls`)

- 把普通修饰词当成强条件。
- 把无限枚举当作穷尽条件。
- 看不到否定条件导致反选。

## 避免事项 (`forbidden`)

- 不得把开放式例举改写为封闭式定义。

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 20

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- definition_text
- defined_term
- options

## 计算策略 (`calculation_policy`)

- mode：keyword_anchor
- strong_anchors：
  - 本质解释
  - 转折
  - 必要条件
  - 否定条件
  - 有限枚举

## 原程序优先级 (`solver_priority`)

3

## 原卡输出约束 (`output_constraints`)

- must_output：
  - 抓手类型
  - 抓手原句或概括
  - 选项命中情况

## definition_elements (`definition_elements`)

- 关键词/关键句：核心
- 条件：强约束
- 否定条件：强排除
- 有限枚举：可作抓手

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）

## 方法 ID (`id`)

dj_keyword_lookup_001

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

关键词查找

## 方法名称 (`method_name`)

定义关键词查找抓手法
