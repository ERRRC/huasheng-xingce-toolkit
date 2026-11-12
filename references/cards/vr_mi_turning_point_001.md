# 转折后重点法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_turning_point_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

转折关系

## 方法名称 (`method_name`)

转折后重点法

## 检索标签 (`tags`)

- 转折
- 但是
- 然而
- 不过
- 重点句

## 适用条件 (`trigger_conditions`)

- 出现但是/然而/不过/可是/实际上等转折词
- 转折前后观点方向不同
- 转折后给出问题、观点或对策

## 不适用条件 (`anti_conditions`)

- 转折后只是让步补充且文段另有结论

## 解题步骤 (`steps`)

- 标记转折词
- 判断转折后内容是问题、观点还是对策
- 以后半句或转折后层次为重点
- 若转折后再出现因此/对策，继续以后续对策为重点

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：线上教学例：转折引出教师不再是知识垄断者，随后给出开放供给对策。
  - lesson：转折后若接对策，最终答案落在对策。

## 易错点 (`pitfalls`)

- 选转折前背景
- 只看到转折后第一句而忽略后续对策

## 避免事项 (`forbidden`)

- 把“但是/然而”之前内容作为答案主体

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 4
    - 6
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：turning_point
- focus_rule：转折之后优先；若转折后继续推出对策，则对策优先
- signals：
  - 但是
  - 然而
  - 不过
  - 可是
  - 其实

## option_elimination (`option_elimination`)

-
  - type：出处不对
  - rule：转折前内容通常为背景或让步，除非后文反复确认，否则排除

## 所需信息 (`required_inputs`)

- 转折词
- 转折前内容
- 转折后重点
- 后续因果/对策标志

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

7

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
