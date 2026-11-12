# 定义判断三看选项设置法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 模块 (`module`)

判断推理-定义判断与类比推理

## 检索标签 (`tags`)

- 定义判断
- 选项设置
- 属于不属于
- 有效信息
- 防陷阱

## 适用条件 (`trigger_conditions`)

- 定义判断题进入选项比对阶段
- 选项相近、题干信息较多、不确定哪个要素是核心

## 不适用条件 (`anti_conditions`)

- 题目为类比词项关系题时不调用
- 题干没有明确定义时不调用

## 解题步骤 (`steps`)

- 看提问：先圈出“属于/不属于/符合/不符合”，这是最大陷阱。
- 看题干：识别有效信息，优先找准关键词、关键句。
- 看选项：不要因某一个表面特点就排除某项，要关注“被定义词”中不包含的信息。
- 若选项均相近，回到被定义词的本质解释和核心条件，而不是扩大定义范围。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生判断笔记总结.pdf
  - page：20
  - summary：笔记将定义判断选项设置拆为看提问、看题干、看选项，并强调“属于/不属于”是最大陷阱。

## 易错点 (`pitfalls`)

- 把不属于题看成属于题。
- 只凭选项中某个相似特点就判定。
- 忽略定义名称本身没有包含的信息。

## 避免事项 (`forbidden`)

- 不得仅凭关键词重合判定选项。
- 不得把题干未包含的信息补入定义。

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 20

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- ask_polarity
- defined_term
- definition_text
- options

## 计算策略 (`calculation_policy`)

- mode：option_elimination
- first_step：ask_polarity
- hard_checks：
  - 被定义词
  - 关键词
  - 关键句

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- must_output：
  - 问法方向
  - 核心定义信息
  - 每个选项排除理由
- avoid：
  - 只输出答案字母

## definition_elements (`definition_elements`)

- 问法：必须先读
- 被定义词：必须检查
- 主体：按题干检查
- 客体/对象：按题干检查
- 条件：按题干检查
- 方式：按题干检查
- 目的：按题干检查
- 结果：按题干检查

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）

## 方法 ID (`id`)

dj_option_setting_001

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

选项设置

## 方法名称 (`method_name`)

定义判断三看选项设置法
