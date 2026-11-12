# 直接证据缺失补洞法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_premise_fill_gap_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

前提假设

## 子题型 (`sub_type`)

补充漏洞

## 方法名称 (`method_name`)

直接证据缺失补洞法

## 检索标签 (`tags`)

- 前提假设
- 补充漏洞
- 间接证据

## 适用条件 (`trigger_conditions`)

- 题干说直接证据缺失
- 只能通过间接证据推测
- 结论强调某证据尤为重要

## 不适用条件 (`anti_conditions`)

- 证据已经充足且只是要求加强时不优先

## 解题步骤 (`steps`)

- 识别题干中承认的证据缺口。
- 判断结论是否依赖该缺口成立。
- 选项应补充为什么在当前情境下直接证据确实缺失或间接证据不可替代。
- 做否定代入：如果直接证据并不缺失，结论重要性会下降。
- 选择能堵住该缺口的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 足迹化石例题中，前寒武纪到寒武纪转折时期保留下来的实体化石十分稀少，补充了直接证据缺失漏洞。

## 易错点 (`pitfalls`)

- 把证据更多误作证据更重要
- 只比较价值不补充缺失原因

## 避免事项 (`forbidden`)

- 不得把结论本身改写成前提

## 来源文件 (`source_file`)

- 【判断推理】支持、前提假设、比例、解释说明.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】支持、前提假设、比例、解释说明.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 12

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- evidence_gap
- claim
- options

## 计算策略 (`calculation_policy`)

- mode：gap_filling
- test：if_gap_absent_claim_weakens

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- must_output：
  - gap
  - filled_condition
- must_not_output：
  - 将研究价值表述当作前提

## argument_structure (`argument_structure`)

- claim：某间接证据尤为重要。
- evidence：直接证据缺失时只能通过间接证据推测。
- link：必须证明该时期直接证据确实缺失。

## strength_order (`strength_order`)

- 没它不行的断点搭桥/必要条件：最强
- 补充直接证据缺失或关键漏洞：强
- 能与不能/可行性条件：强
- 有它更好但没它仍可成立：不是前提
- 主体话题无关：排除
