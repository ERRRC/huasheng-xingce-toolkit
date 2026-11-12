# 必要条件式支持法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_support_necessary_condition_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强

## 子题型 (`sub_type`)

必要条件

## 方法名称 (`method_name`)

必要条件式支持法

## 检索标签 (`tags`)

- 支持类
- 必要条件
- 基础条件

## 适用条件 (`trigger_conditions`)

- 选项说明结论成立必须具备的条件
- 题干问得出结论的依据
- 没有该条件结论不能成立

## 不适用条件 (`anti_conditions`)

- 问'需要补充的前提'时优先前提假设卡，但本卡可作为支持判断

## 解题步骤 (`steps`)

- 识别论点成立所依赖的条件。
- 判断选项是否是没有它就不能成立的条件。
- 该条件若为真，应使论点更可能成立。
- 与普通事实支持比较时，必要条件通常更强。
- 排除只是有帮助但非必要的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 丹尼索瓦人能在高海拔区域生活，适应高海拔基因片段可作为结论依据。

## 易错点 (`pitfalls`)

- 把充分条件当必要条件
- 条件只相关但不是必须

## 避免事项 (`forbidden`)

- 不得把'有它更好'误判为'没它不行'

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
    - 11
    - 12

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- dependency_condition
- options

## 计算策略 (`calculation_policy`)

- mode：necessary_condition_support
- test：remove_option_then_claim_fails

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- must_output：
  - necessary_condition
  - remove_test
- must_not_output：
  - 把弱相关条件标成必要条件

## argument_structure (`argument_structure`)

- claim：某结论成立。
- evidence：题干提出证据或现象。
- link：选项提供结论成立不可缺少的条件。

## strength_order (`strength_order`)

- 断点搭桥/必要条件：直接补足论据到论点的缺口，力度强
- 自断一臂/排除关键漏洞：排除最主要替代路径，力度强
- 加入论据和事实：直接增加支持事实，力度中强
- 解释说明机制：解释为什么论点可能成立，力度中等
- 举例或类比支持：支持但范围较窄，力度较弱
- 主体或话题不一致：无关
