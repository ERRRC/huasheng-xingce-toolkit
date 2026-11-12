# 有更具体选项时优选具体法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_one_compare_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项比较

## 子题型 (`sub_type`)

优选具体

## 方法名称 (`method_name`)

有更具体选项时优选具体法

## 检索标签 (`tags`)

- 选项比较
- 具体优先
- 一个比较

## 适用条件 (`trigger_conditions`)

- 两个选项都能大致体现中心
- 其中一个更贴合文段具体问题或主体，另一个较宽泛

## 不适用条件 (`anti_conditions`)

- 具体项只对应细节而非中心

## 解题步骤 (`steps`)

- 先确认两个选项都没有硬伤
- 比较主体是否更贴合文段
- 比较是否体现问题/态度/对策
- 在不偏离原文的前提下优选更具体贴合项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：斑马线之争例中，比起泛谈交通出行，倡导礼让斑马线更贴合文段具体问题。
  - lesson：具体优先的前提是具体项不偏离中心。

## 易错点 (`pitfalls`)

- 把过度具体的局部项误认为更好
- 泛项和具体项都不核对主体

## 避免事项 (`forbidden`)

- 具体项只对应细节时强行优选

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.87

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：option_comparison
- focus_rule：无硬伤且都对应中心时，优选更贴合具体问题的选项

## option_elimination (`option_elimination`)

-
  - type：过宽泛
  - rule：在有贴合具体问题的正确项时，泛泛表述排除

## 所需信息 (`required_inputs`)

- 两个候选选项
- 文段具体问题
- 主体词
- 选项覆盖度

## 计算策略 (`calculation_policy`)

- mode：compare_surviving_options
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
