# 下定义选项慎选法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_definition_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

下定义选项

## 方法名称 (`method_name`)

下定义选项慎选法

## 检索标签 (`tags`)

- 下定义
- A是B
- 中性表达
- 无态度

## 适用条件 (`trigger_conditions`)

- 选项形式为“A是B”或客观定义
- 文段实际强调问题、对策、观点或态度

## 不适用条件 (`anti_conditions`)

- 文段目的就是解释概念或定义

## 解题步骤 (`steps`)

- 判断文段是否真在下定义
- 若文段重点为对策/观点，排除中性定义项
- 若文段目的就是解释概念或定义，则可保留
- 与其他选项比较是否体现态度和重点

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：户外活动预防近视例中，下定义式或分析式选项不如对策项。
  - lesson：对策文段不能选无态度定义项。

## 易错点 (`pitfalls`)

- 定义项看似准确但没有体现作者重点
- 把说明对象的概念解释当中心

## 避免事项 (`forbidden`)

- 对策文段选择纯定义项

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

- type：definition_option_check
- focus_rule：只有文段确为定义说明时才选定义项；议论对策文段不选中性定义

## option_elimination (`option_elimination`)

-
  - type：下定义误选
  - rule：A是B式选项未体现观点/对策时排除

## 所需信息 (`required_inputs`)

- 选项表达形式
- 文段结构类型
- 是否有作者态度/对策

## 计算策略 (`calculation_policy`)

- mode：option_form_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

25

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
