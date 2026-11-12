# 前提类断点搭桥法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_premise_bridge_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

前提假设

## 子题型 (`sub_type`)

断点搭桥

## 方法名称 (`method_name`)

前提类断点搭桥法

## 检索标签 (`tags`)

- 前提假设
- 断点搭桥
- 论证缺口

## 适用条件 (`trigger_conditions`)

- 论据中的概念与论点中的概念不同
- 问需要补充的前提
- 选项连接两个概念

## 不适用条件 (`anti_conditions`)

- 选项只增强某个概念但没有连接两端时不适用

## 解题步骤 (`steps`)

- 抽取论据核心 A。
- 抽取论点核心 B。
- 确认题干没有说明 A 与 B 的关系。
- 寻找选项是否声明 A 能推出或指向 B。
- 否定该桥梁后若论证断裂，则选该项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 火星平顶山丘矿物质→早期冰原和火山活动；前提需说明这类矿物质与冰川下火山活动的唯一或关键联系。

## 易错点 (`pitfalls`)

- 桥梁不够唯一但题干要求必要条件时需谨慎
- 只解释背景不连接结论

## 避免事项 (`forbidden`)

- 不得自行补充桥梁

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

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- evidence_keyword
- claim_keyword
- options

## 计算策略 (`calculation_policy`)

- mode：premise_bridge
- test：negate_bridge

## 原程序优先级 (`solver_priority`)

19

## 原卡输出约束 (`output_constraints`)

- must_output：
  - A
  - B
  - bridge
  - negation_effect
- must_not_output：
  - 用无关事实替代桥梁

## argument_structure (`argument_structure`)

- claim：B成立。
- evidence：A事实。
- link：需要A与B之间的桥梁。

## strength_order (`strength_order`)

- 没它不行的断点搭桥/必要条件：最强
- 补充直接证据缺失或关键漏洞：强
- 能与不能/可行性条件：强
- 有它更好但没它仍可成立：不是前提
- 主体话题无关：排除
