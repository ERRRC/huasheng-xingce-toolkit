# 出处不对排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_source_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

出处不对

## 方法名称 (`method_name`)

出处不对排除法

## 检索标签 (`tags`)

- 选项分析
- 出处
- 背景
- 例子
- 分析

## 适用条件 (`trigger_conditions`)

- 选项内容来自背景、例子、分析、转折前或因此前
- 该信息不是文段重点层

## 不适用条件 (`anti_conditions`)

- 该出处本身就是总句、观点句或对策句

## 解题步骤 (`steps`)

- 定位选项出处
- 判断出处功能：背景/例子/分析/让步/观点
- 若出处不是重点层且未概括全文，排除
- 若选项为重点层同义替换，保留

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生言语理解笔记.pdf
  - page：11
  - summary：选项分析页列出“背景、例子、分析不能选”“但是、因此之前不能选”等出处规则。
  - lesson：选项出处必须对应文段重点层。

## 易错点 (`pitfalls`)

- 选原文出现过但不是重点的句子
- 将例子里的具体对象当主题

## 避免事项 (`forbidden`)

- 认为“原文出现过”就一定正确

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

- type：option_source_check
- focus_rule：选项必须出自重点层或概括全文，非重点出处不能选

## option_elimination (`option_elimination`)

-
  - type：出处不对
  - rule：背景、例子、分析、转折前、因此前的非重点信息排除

## 所需信息 (`required_inputs`)

- 选项关键词
- 原文对应句
- 对应句结构功能

## 计算策略 (`calculation_policy`)

- mode：map_option_to_source
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
