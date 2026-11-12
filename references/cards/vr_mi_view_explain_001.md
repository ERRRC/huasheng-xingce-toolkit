# 观点—解释/论证结构解题法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_view_explain_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

观点-解释

## 方法名称 (`method_name`)

观点—解释/论证结构解题法

## 检索标签 (`tags`)

- 观点
- 解释说明
- 论证
- 重复论点

## 适用条件 (`trigger_conditions`)

- 文段先给出观点或对策，后文用例子、原因、说明重复证明
- 题干问主要说明/重在说明/意在强调

## 不适用条件 (`anti_conditions`)

- 后文不是服务前文观点，而是转折提出新观点

## 解题步骤 (`steps`)

- 先找观点或对策句
- 把后文解释、例证、原因视为支撑材料
- 选择观点句同义概括
- 排除来自例子、背景或分析细节的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：民间盗墓与地方政府破土开棺例：对策之后用论证说明危害。
  - lesson：论证服务于对策，答案落在对策。

## 易错点 (`pitfalls`)

- 选解释材料中的具体危害
- 将论证细节上升为主旨

## 避免事项 (`forbidden`)

- 把例证句当中心句

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 6
    - 7
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

- type：view_explanation
- focus_rule：观点/对策是中心，解释说明和例子不直接入选
- structure：
  - 观点/对策
  - 解释说明/论证

## option_elimination (`option_elimination`)

-
  - type：出处不对
  - rule：来自论证例子的具体信息通常不能选

## 所需信息 (`required_inputs`)

- 观点句
- 论证句
- 例证内容
- 选项是否为观点同义替换

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

6

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
