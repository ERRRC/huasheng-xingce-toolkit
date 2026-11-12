# 背景知识引出新发现法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_background_new_discovery_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

主旨概括

## 子题型 (`sub_type`)

背景-新发现

## 方法名称 (`method_name`)

背景知识引出新发现法

## 检索标签 (`tags`)

- 背景知识
- 新发现
- 研究发现
- 出处判断

## 适用条件 (`trigger_conditions`)

- 前半段介绍概念、背景、既有认识
- 后半段出现研究团队/首次发现/根据发现等新信息
- 题干问意在说明或主要说明

## 不适用条件 (`anti_conditions`)

- 新发现只是例子，不是文段中心

## 解题步骤 (`steps`)

- 识别背景介绍边界
- 找新发现或新观点句
- 答案应体现新发现主体和内容
- 排除背景定义、背景原因、旧知识选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：蓝离散星例中背景解释蓝离散星，重点是年轻星团中观测到不同寻常的蓝离散星。
  - lesson：新发现优先于背景定义。

## 易错点 (`pitfalls`)

- 选概念定义项
- 选背景中的旧知识

## 避免事项 (`forbidden`)

- 把“介绍概念”误认为“文段意图”

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.91

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：background_new_finding
- focus_rule：背景服务于新发现，新发现为重点
- signals：
  - 研究团队
  - 发现
  - 首次
  - 根据发现

## option_elimination (`option_elimination`)

-
  - type：出处不对
  - rule：来自背景定义的选项排除

## 所需信息 (`required_inputs`)

- 背景句
- 新发现句
- 研究主体
- 发现对象

## 计算策略 (`calculation_policy`)

- mode：structure_first
- allow_pure_language_feel：false
- must_analyze_relation_words：true
- must_check_subject_consistency：true
- prefer_author_view_or_strategy：true

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
