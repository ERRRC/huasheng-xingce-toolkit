# 具体类选项验证法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_specific_option_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

具体类选项

## 方法名称 (`method_name`)

具体类选项验证法

## 检索标签 (`tags`)

- 具体类
- 一二三四
- 具体方法
- 具体意义

## 适用条件 (`trigger_conditions`)

- 选项表述为具体方法、具体措施、具体意义、具体原因
- 文段是否实际列举多个具体方面需要验证

## 不适用条件 (`anti_conditions`)

- 文段没有具体方法或具体意义展开

## 解题步骤 (`steps`)

- 检查文段是否有一二三四五式具体展开
- 若没有具体展开，具体类选项多为无中生有或过度具体
- 若文段按时间或多方面列举具体方法，可保留具体类概括
- 具体类选项必须覆盖全部具体层次

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：公文保密例按朝代列举多种方法，可选“历代公文保密方法”。
  - lesson：具体类选项必须由文段具体展开支撑。

## 易错点 (`pitfalls`)

- 文段只有原因或问题，却选“如何解决”具体类选项
- 具体类选项只覆盖一项

## 避免事项 (`forbidden`)

- 文段未给具体方法时选择具体解决方案

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：specific_option_check
- focus_rule：具体类选项需要文段有多点具体展开作支撑

## option_elimination (`option_elimination`)

-
  - type：无中生有
  - rule：文段无具体方法列表时，具体对策类选项排除

## 所需信息 (`required_inputs`)

- 选项是否具体类
- 文段是否列举具体层次
- 具体层次数量

## 计算策略 (`calculation_policy`)

- mode：specificity_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

29

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
