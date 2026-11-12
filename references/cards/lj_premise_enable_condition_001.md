# 可行性前提法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_premise_enable_condition_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

前提假设

## 子题型 (`sub_type`)

能与不能

## 方法名称 (`method_name`)

可行性前提法

## 检索标签 (`tags`)

- 前提假设
- 能与不能
- 可行性条件

## 适用条件 (`trigger_conditions`)

- 题干说某人因未发生某事而焦虑/反应
- 问陷入烦恼所需假设
- 选项涉及技术能否实现、条件能否满足

## 不适用条件 (`anti_conditions`)

- 选项只是说明别人行为习惯，不解决能不能的问题时不优先

## 解题步骤 (`steps`)

- 识别题干行为或心理反应依赖的前提条件。
- 判断如果该条件不存在，题干反应是否不会发生。
- 选择能保证该条件可实现的选项。
- 否定该选项后若论证失效，则为前提。
- 排除只解释个别情况但不影响可行性的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 秒回焦虑例题中，当前技术能实现即时通信是人们期待秒回并焦虑的前提。

## 易错点 (`pitfalls`)

- 把可能解释原因当成必要可行性
- 选项解释未秒回但不说明能不能秒回

## 避免事项 (`forbidden`)

- 不得选只说明忙或遗漏的选项作为必要前提

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

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- expected_action
- feasibility_condition
- options

## 计算策略 (`calculation_policy`)

- mode：feasibility_assumption
- test：if_not_possible_then_reaction_unreasonable

## 原程序优先级 (`solver_priority`)

21

## 原卡输出约束 (`output_constraints`)

- must_output：
  - feasibility_condition
  - negation_test
- must_not_output：
  - 把替代解释当必要条件

## argument_structure (`argument_structure`)

- claim：某心理或行为反应成立。
- evidence：题干描述期待某行为发生。
- link：必须先具备该行为能够发生的条件。

## strength_order (`strength_order`)

- 没它不行的断点搭桥/必要条件：最强
- 补充直接证据缺失或关键漏洞：强
- 能与不能/可行性条件：强
- 有它更好但没它仍可成立：不是前提
- 主体话题无关：排除
