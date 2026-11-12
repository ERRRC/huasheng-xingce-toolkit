# 实验初始状态一致性检查法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_experiment_initial_state_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强削弱

## 子题型 (`sub_type`)

对比实验

## 方法名称 (`method_name`)

实验初始状态一致性检查法

## 检索标签 (`tags`)

- 对比实验
- 初始状态
- 实验控制
- 加强削弱

## 适用条件 (`trigger_conditions`)

- 题干是实验组与对照组比较
- 选项涉及实验前两组差异是否大
- 问加强或削弱实验结论

## 不适用条件 (`anti_conditions`)

- 非实验类归因不优先使用

## 解题步骤 (`steps`)

- 识别实验组、对照组、处理变量和结果变量。
- 检查实验前两组初始状态是否一致。
- 若要加强实验结论，选项应说明实验前差异不大。
- 若要削弱实验结论，选项可指出实验前两组已存在关键差异。
- 实验前差异必须能影响结果变量。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 小鼠认知实验中，实验前两组小鼠个体差异不大，可加强外界刺激改变大脑结构和能力的结论。

## 易错点 (`pitfalls`)

- 实验后差异不能证明实验前一致
- 与结果无关的初始差异力度弱

## 避免事项 (`forbidden`)

- 不得把实验后的结果差异当作初始状态控制

## 来源文件 (`source_file`)

- 【判断推理】质疑类.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 4

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- experimental_group
- control_group
- treatment
- outcome
- initial_state_info
- options

## 计算策略 (`calculation_policy`)

- mode：experiment_control_check
- verification：
  - pre_experiment_state
  - relevance_to_outcome

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- must_output：
  - groups
  - initial_state_check
- must_not_output：
  - 用实验后信息替代初始信息

## argument_structure (`argument_structure`)

- claim：处理变量A导致结果差异B。
- evidence：实验组与对照组结果不同。
- link：初始状态一致才能把差异归因于处理变量。

## strength_order (`strength_order`)

- 实验前关键差异不大：强加强
- 实验前关键差异明显：强削弱
- 实验后差异：不能控制初始状态
- 无关差异：弱或无效
