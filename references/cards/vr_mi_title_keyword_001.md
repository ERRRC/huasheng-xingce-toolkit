# 标题关键词覆盖法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_title_keyword_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

标题填入

## 子题型 (`sub_type`)

标题关键词

## 方法名称 (`method_name`)

标题关键词覆盖法

## 检索标签 (`tags`)

- 标题
- 关键词
- 主体词
- 醒目

## 适用条件 (`trigger_conditions`)

- 标题选项中主题词差异明显
- 文段有清晰核心对象和观点

## 不适用条件 (`anti_conditions`)

- 标题主体词与文段核心不一致

## 解题步骤 (`steps`)

- 提取文段核心主体词
- 检查标题是否包含或准确替代主体词
- 检查标题是否覆盖文段态度或重点
- 优先选择既准确又简洁的标题

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生言语理解笔记.pdf
  - page：13
  - summary：标题拟定页强调正确选项要与文段核心关键词相关，并避免与文段不符的标题。
  - lesson：标题不能只追求概括大范围，要抓文段核心对象。

## 易错点 (`pitfalls`)

- 标题范围大但主题词不准
- 标题只对应文段的例子

## 避免事项 (`forbidden`)

- 选择文艺化但核心词缺失的标题

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 13

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：title_keyword
- focus_rule：核心主题词必须保留，标题同时体现中心态度

## option_elimination (`option_elimination`)

-
  - type：偷换概念
  - rule：标题主体词与文段核心主体不一致则排除
-
  - type：范围过大/过小
  - rule：标题过宽或只概括局部时排除

## 所需信息 (`required_inputs`)

- 核心主题词
- 标题主语
- 标题修饰方向
- 文段中心

## 计算策略 (`calculation_policy`)

- mode：keyword_and_structure_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
