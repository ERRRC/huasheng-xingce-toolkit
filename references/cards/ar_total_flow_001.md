# 类比推理总体解题流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_total_flow_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

总流程

## 方法名称 (`method_name`)

类比推理总体解题流程

## 检索标签 (`tags`)

- 类比推理
- 总流程
- 大众思维
- 简单思维
- 内在联系

## 适用条件 (`trigger_conditions`)

- 题干呈现词语对、三词组、括号式类比
- 问与题干关系最为相似

## 不适用条件 (`anti_conditions`)

- 题干给出概念定义并问属于/不属于时路由到定义判断

## 解题步骤 (`steps`)

- 先用大众思维、简单思维判断题干词项之间的直接内在联系。
- 优先想“造句子”：选择相似点和题干最多的关系，而不是强行找冷僻常识。
- 先粗分为语义、语法、逻辑、对应、拆词等一级关系。
- 一级辨析选不出时，再进入二级辨析；不要一开始就陷入细枝末节。
- 二级辨析依次检查：感情色彩、程度轻重、词性、主动/被动、种属/组成、矛盾/反对、特指/泛指、关系方向。
- 全同关系必须一点不能差；对应关系尤其要看主体、对象、数量、先后顺序和方式目的。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：资料强调类比题多想词与词本身联系，如猎豹-速度快、蜜蜂-采蜜。

## 易错点 (`pitfalls`)

- 想太复杂，使用冷门知识。
- 只看表面同类词，不看内在关系。

## 避免事项 (`forbidden`)

- 不得为了匹配选项临时编造关系。

## 来源文件 (`source_file`)

- 【判断推理】类比推理.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】类比推理.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 21
    - 22

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_terms
- option_terms
- stem_format

## 计算策略 (`calculation_policy`)

- mode：relation_matching
- first_principle：simple_common_relation

## 原程序优先级 (`solver_priority`)

1

## 原卡输出约束 (`output_constraints`)

- must_output：
  - primary_relation
  - secondary_check
  - chosen_option_reason

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

总流程

## secondary_check (`secondary_check`)

- 大众思维/简单思维
- 一级关系优先
- 一级不够再二级辨析
- 关系方向一致
- 主体与数量一致
