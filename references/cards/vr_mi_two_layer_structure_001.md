# 二层结构主次判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_two_layer_structure_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

中心理解

## 子题型 (`sub_type`)

二层结构

## 方法名称 (`method_name`)

二层结构主次判断法

## 检索标签 (`tags`)

- 二层结构
- 转折
- 并列
- 因果
- 背景知识

## 适用条件 (`trigger_conditions`)

- 文段由两大层组成，如背景+新发现、问题+原因、观点+解释
- 第一层和第二层存在主次或承接关系

## 不适用条件 (`anti_conditions`)

- 无法划分主次的平行并列结构

## 解题步骤 (`steps`)

- 先把文段分成两个大层
- 判断第二层是否为新发现、观点、问题原因或对策
- 优先选择主层内容
- 排除只抓次层铺垫或过度具体的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：蓝离散星例先介绍背景，后提出研究团队的新发现。
  - lesson：背景知识引出后，新发现是重点。

## 易错点 (`pitfalls`)

- 把背景知识当答案
- 选项只对应第一层铺垫

## 避免事项 (`forbidden`)

- 不划分大层次直接看选项

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

0.92

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：two_layer
- focus_rule：二层结构中后层若是新发现/观点/对策，后层优先；若后层解释原因，则概括原因

## option_elimination (`option_elimination`)

-
  - type：出处不对
  - rule：只来自铺垫层的选项排除

## 所需信息 (`required_inputs`)

- 第一层内容
- 第二层内容
- 两层关系
- 选项对应层次

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

13

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
