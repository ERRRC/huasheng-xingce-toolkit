# 比较类/区别比较类选项验证法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_compare_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

比较类选项

## 方法名称 (`method_name`)

比较类/区别比较类选项验证法

## 检索标签 (`tags`)

- 比较类
- 区别比较
- 双主语

## 适用条件 (`trigger_conditions`)

- 选项使用比较、高于、区别、优势、不同等表达
- 文段没有把两个对象放在平等篇幅比较
- 或文段确实双主语对比

## 不适用条件 (`anti_conditions`)

- 文段确实围绕两个对象平等比较展开

## 解题步骤 (`steps`)

- 检查文段是否双主语且篇幅地位接近
- 若不是双主语比较结构，排除比较类选项
- 若文段重点就是区别比较，则可选概括二者区别的选项
- 比较选项必须对应文段比较维度

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：城墙例中“文化价值高于商业价值”属于文段未比较内容；综述与元科普例则可选区别项。
  - lesson：比较类选项只有在文段真实比较时才能选。

## 易错点 (`pitfalls`)

- 看到两个概念就选比较
- 比较维度原文没有

## 避免事项 (`forbidden`)

- 文段非双主语比较时选择比较项

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：comparison_option_check
- focus_rule：双主语地位平等才可选区别比较类；否则多为无中生有或挑文段

## option_elimination (`option_elimination`)

-
  - type：比较无据
  - rule：原文没有平等比较或比较维度时排除

## 所需信息 (`required_inputs`)

- 比较对象A
- 比较对象B
- 文段篇幅比例
- 比较维度

## 计算策略 (`calculation_policy`)

- mode：comparison_validity_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

27

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
