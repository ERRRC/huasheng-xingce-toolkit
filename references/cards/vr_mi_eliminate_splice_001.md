# 杂糅拼凑选项排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_splice_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

杂糅选项

## 方法名称 (`method_name`)

杂糅拼凑选项排除法

## 检索标签 (`tags`)

- 杂糅
- 拼凑
- 不同语句拼接

## 适用条件 (`trigger_conditions`)

- 选项中若干词都来自原文，但组合关系不是原文中心关系
- 选项主体或动作拼接了不同层次内容

## 不适用条件 (`anti_conditions`)

- 选项虽包含多个信息但结构关系与中心一致

## 解题步骤 (`steps`)

- 拆分选项成若干信息块
- 分别定位原文出处
- 检查这些信息在原文是否属于同一结构层级和同一逻辑关系
- 若只是拼凑不同句子且不成中心，排除

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：音乐教育例中，部分选项把教师、真善美、主旨等分散信息拼凑，主体和对策均不准确。
  - lesson：原文词语都出现不等于结构关系正确。

## 易错点 (`pitfalls`)

- 看到多个原文词就误以为概括全面
- 忽略选项内部关系与原文不同

## 避免事项 (`forbidden`)

- 不检查选项内部逻辑关系

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

- type：spliced_option_check
- focus_rule：正确项应概括中心关系，不是拼凑原文词

## option_elimination (`option_elimination`)

-
  - type：杂糅
  - rule：来自不同结构层的词语拼接且不构成中心关系时排除

## 所需信息 (`required_inputs`)

- 选项信息块
- 每块出处
- 原文结构层级
- 中心关系

## 计算策略 (`calculation_policy`)

- mode：decompose_option_then_map
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

26

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
