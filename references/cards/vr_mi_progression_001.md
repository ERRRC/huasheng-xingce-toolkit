# 递进后重点法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_progression_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

递进关系

## 方法名称 (`method_name`)

递进后重点法

## 检索标签 (`tags`)

- 递进
- 甚至
- 更
- 不仅而且
- 不但而且

## 适用条件 (`trigger_conditions`)

- 出现不仅/不但/甚至/更/尤其等递进标志
- 后项比前项语义更重或范围更深

## 不适用条件 (`anti_conditions`)

- 递进后只是局部例子或修饰

## 解题步骤 (`steps`)

- 识别递进标志
- 以前后项中程度更深、结论性更强的一项为重点
- 若递进后仍属举例或分析，应回到整体结构验证
- 选项需覆盖递进后核心而不是只覆盖前项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生言语理解笔记.pdf
  - page：4
  - summary：笔记把递进关系列入片段阅读常见关联词，要求结合结构判断重点。
  - lesson：递进不是单独秒杀，仍要与文段结构合并判断。

## 易错点 (`pitfalls`)

- 只凭“甚至/更”机械选后半句
- 忽略后项可能只是局部分析

## 避免事项 (`forbidden`)

- 不做结构验证就把递进后词语当答案

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 4

## 原卡置信度 (`confidence`)

0.78

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：progression
- focus_rule：递进后通常更重要，但必须接受整体结构复核
- signals：
  - 不仅
  - 不但
  - 甚至
  - 更
  - 尤其

## option_elimination (`option_elimination`)

-
  - type：片面
  - rule：只覆盖递进前项、未覆盖递进后核心的选项排除

## 所需信息 (`required_inputs`)

- 递进关联词
- 前项内容
- 后项内容
- 后项是否为观点/对策

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
