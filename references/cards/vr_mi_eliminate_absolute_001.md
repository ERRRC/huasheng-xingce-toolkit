# 绝对化选项排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_absolute_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

绝对化选项

## 方法名称 (`method_name`)

绝对化选项排除法

## 检索标签 (`tags`)

- 绝对化
- 最高级
- 比较级
- 最
- 全部

## 适用条件 (`trigger_conditions`)

- 选项出现最、最高、唯一、所有、完全、一定等绝对化或强比较表达
- 原文没有同等强度依据

## 不适用条件 (`anti_conditions`)

- 原文明确出现同等程度的绝对或比较表达

## 解题步骤 (`steps`)

- 标记选项绝对化词
- 回原文查找是否有明确支持
- 若原文无支持或只表达一般趋势，排除
- 若原文明确有最高级或比较关系，再保留

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：乡愁例中“最好精神慰藉”“最基本、最普遍情感”因原文没有“最”而排除。
  - lesson：绝对化必须有原文强支撑。

## 易错点 (`pitfalls`)

- 觉得选项语气强就像主旨
- 忽略原文只是在并列或举例

## 避免事项 (`forbidden`)

- 原文无最高级依据时选择绝对化项

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

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：option_modality_check
- focus_rule：选项强度不得超过原文

## option_elimination (`option_elimination`)

-
  - type：绝对化
  - rule：最高级、唯一、全部、完全等无原文支持时排除

## 所需信息 (`required_inputs`)

- 选项程度词
- 原文对应程度
- 是否有明确比较/最高级依据

## 计算策略 (`calculation_policy`)

- mode：modality_strength_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

23

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
