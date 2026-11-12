# 主旨概括整体覆盖法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_main_summary_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

主旨概括

## 方法名称 (`method_name`)

主旨概括整体覆盖法

## 检索标签 (`tags`)

- 主旨概括
- 主要内容
- 整体覆盖

## 适用条件 (`trigger_conditions`)

- 题干问“主要内容/主旨/概括最准确”
- 文段以说明或议论为主

## 不适用条件 (`anti_conditions`)

- 选项带有无依据意图推断

## 解题步骤 (`steps`)

- 识别文段结构
- 确定主干信息：主体+核心观点/问题/原因/对策
- 选覆盖主干且不偏不漏的选项
- 排除细节项、背景项、例子项、片面项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：书院例用总分结构说明教育与文化传播功能，正确项为整体概括。
  - lesson：主旨概括要“主体+核心内容”完整。

## 易错点 (`pitfalls`)

- 选细节最熟悉的选项
- 忽略并列结构中的另一半

## 避免事项 (`forbidden`)

- 以关键词命中代替整体覆盖

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：main_summary
- focus_rule：主体+核心内容完整覆盖；不作过度意图推断

## option_elimination (`option_elimination`)

-
  - type：片面
  - rule：只覆盖一个分支或一个例子的选项排除

## 所需信息 (`required_inputs`)

- 主体词
- 结构类型
- 中心层
- 选项覆盖度

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
