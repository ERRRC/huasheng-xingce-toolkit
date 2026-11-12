# 总分/分总结构总句优先法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_total_part_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

总分/分总

## 方法名称 (`method_name`)

总分/分总结构总句优先法

## 检索标签 (`tags`)

- 总分
- 分总
- 概括
- 总句

## 适用条件 (`trigger_conditions`)

- 文段先总说后分述，或先分述后总括
- 分述部分围绕同一总观点展开

## 不适用条件 (`anti_conditions`)

- 分述之间没有共同总主题

## 解题步骤 (`steps`)

- 识别总句位置
- 判断分述内容是否围绕总句举例/展开
- 答案选择总句的概括或同义替换
- 排除只对应某一分述层次的片面选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：钞票制作例为总分结构，重点是钞票制作各环节要求严格。
  - lesson：总分结构不能选分述中的单一技术或艺术点。

## 易错点 (`pitfalls`)

- 选分述中最显眼的细节
- 把一个分论点当全文主旨

## 避免事项 (`forbidden`)

- 只覆盖分述某一层面

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 6
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

- type：total_part
- focus_rule：总句重要；分句用于解释总句
- structure：
  - 总
  - 分

## option_elimination (`option_elimination`)

-
  - type：片面
  - rule：只对应分述部分的选项排除

## 所需信息 (`required_inputs`)

- 总句
- 分述层次
- 各层是否同一主题
- 选项覆盖度

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

11

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
