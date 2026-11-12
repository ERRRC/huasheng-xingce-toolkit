# 无中生有排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_none_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

无中生有

## 方法名称 (`method_name`)

无中生有排除法

## 检索标签 (`tags`)

- 无中生有
- 过度引申
- 原文无依据

## 适用条件 (`trigger_conditions`)

- 选项提出原文未涉及的概念、关系、原因、影响或对策
- 选项看似合理但无法从文段结构推出

## 不适用条件 (`anti_conditions`)

- 选项是对中心句的合理同义转换

## 解题步骤 (`steps`)

- 将选项拆成主体、动作、关系、结果
- 逐一回原文找依据
- 任一核心成分无依据则排除
- 注意合理常识不能替代原文依据

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：书院例中“文明传承”不是文段直接表达，被判为无中生有。
  - lesson：主旨意图题也不能脱离原文常识发挥。

## 易错点 (`pitfalls`)

- 用生活常识补全原文没有的内容
- 把可能对策当作者意图

## 避免事项 (`forbidden`)

- 选择原文未出现且不能结构推出的内容

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：evidence_check
- focus_rule：所有核心成分必须有原文依据或可由结构直接推出

## option_elimination (`option_elimination`)

-
  - type：无中生有
  - rule：原文未涉及且无法结构推出的选项排除

## 所需信息 (`required_inputs`)

- 选项核心成分
- 原文依据句
- 是否可由结构推出

## 计算策略 (`calculation_policy`)

- mode：evidence_trace
- allow_world_knowledge_substitution：false

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
