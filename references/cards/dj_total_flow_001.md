# 定义判断总体理解流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

dj_total_flow_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

定义判断

## 子题型 (`sub_type`)

总流程

## 方法名称 (`method_name`)

定义判断总体理解流程

## 检索标签 (`tags`)

- 定义判断
- 总流程
- 理解优先
- 整体把握

## 适用条件 (`trigger_conditions`)

- 题干给出一个或多个概念定义
- 问下列属于/不属于/符合/不符合定义的是

## 不适用条件 (`anti_conditions`)

- 题目要求比较两个词语关系时优先路由到类比推理
- 题干没有完整定义、只让判断结论能否推出时不调用本卡

## 解题步骤 (`steps`)

- 先看问法，明确是“属于”还是“不属于”，不属于题最大陷阱是把符合定义的例子当答案。
- 抓住被定义词，先根据概念名称判断本质解释和核心方向。
- 整体理解定义所指的人、事或现象，必要时联系生活常识，但必须回到题干验证。
- 识别有效信息：主体、客体/对象、条件、方式、目的、结果、特殊要求。
- 看选项时不要因某一特点就排除，重点关注被定义词中“不包含”的信息。
- 技巧题可用同构选项同时排除、对比枚举型逐一定义对应、涉及时间变化时核对前后状态。
- 最终输出每个选项的符合/不符合要素，不允许只给答案。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：垂直搜索引擎题通过被定义词中的“搜索引擎”和“某一行业/专业”定位正确选项。
-
  - source：【判断推理】定义判断.pdf
  - page：1
  - summary：闭环思维不属于题中，错误选项多是符合定义的例子，可借例子理解定义。

## 易错点 (`pitfalls`)

- 只见树木不见森林：把定义拆成过多碎片，反而忽略被定义词本身。
- 属于/不属于方向看反。
- 把生活常识中的相似现象误当成定义项。
- 题干另有相近概念或相似焦点时，抓手常藏在本质解释或延伸解释里。
- 有限枚举时可做抓手，无限枚举不可当抓手。

## 避免事项 (`forbidden`)

- 不得只按单个关键词命中就判定正确。
- 不得在没有题干依据时添加定义外条件。

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

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- question_stem
- defined_term
- definition_text
- ask_polarity
- options

## 计算策略 (`calculation_policy`)

- mode：qualitative_matching
- priority：understand_defined_term_first
- allow_external_common_sense：only_if_consistent_with_definition

## 原程序优先级 (`solver_priority`)

1

## 原卡输出约束 (`output_constraints`)

- must_output：
  - ask_polarity
  - core_definition
  - elimination_reason
- avoid：
  - keyword_only_answer

## definition_elements (`definition_elements`)

- 主体：可选但优先检查
- 客体/对象：可选但优先检查
- 条件：按题干明示
- 方式：按题干明示
- 目的：按题干明示
- 结果：按题干明示
- 特殊要求：必须保留
- 被定义词：优先检查
- 问法：必须先读

## relation_type (`relation_type`)

null

## secondary_check (`secondary_check`)

- （空列表）
