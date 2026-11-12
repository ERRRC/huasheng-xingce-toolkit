# 构成对比实验变量控制法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_compare_experiment_construct_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强削弱

## 子题型 (`sub_type`)

对比实验

## 方法名称 (`method_name`)

构成对比实验变量控制法

## 检索标签 (`tags`)

- 对比实验
- 构成对比
- 实验变量
- 归因类

## 适用条件 (`trigger_conditions`)

- 题干需要构造或评价对比实验
- 两个组或两个时期进行比较
- 选项说明实验组与对照组差异

## 不适用条件 (`anti_conditions`)

- 没有组间比较时不适用

## 解题步骤 (`steps`)

- 确定实验目标：要证明哪个因素A影响结果B。
- 设置实验组有A，对照组无A或A较弱。
- 保持其他条件尽量一致。
- 比较结果B是否不同。
- 加强选项应说明除A外条件一致；削弱选项应说明存在其他系统差异。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记中构成对比实验例题通过支持/质疑两类选项判断实验因素是否真正导致结果。

## 易错点 (`pitfalls`)

- 只比较结果不控制其他条件
- 将多个变量同时变化仍归因于单一变量

## 避免事项 (`forbidden`)

- 不得把非控制实验当严格因果证明

## 来源文件 (`source_file`)

- 花生判断笔记总结.pdf
- 【判断推理】质疑类.pdf

## 来源页码 (`source_page`)

-
  - file：花生判断笔记总结.pdf
  - pages：
    - 6
-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.82

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- group_a
- group_b
- target_variable
- outcome
- controlled_variables

## 计算策略 (`calculation_policy`)

- mode：contrast_experiment_design
- verification：
  - single_variable_difference
  - controlled_conditions

## 原程序优先级 (`solver_priority`)

33

## 原卡输出约束 (`output_constraints`)

- must_output：
  - target_variable
  - control_status
- must_not_output：
  - 把多变量差异归因于单变量

## argument_structure (`argument_structure`)

- claim：A导致B。
- evidence：实验组和对照组差异。
- link：只有控制其他变量才能把B归因于A。

## strength_order (`strength_order`)

- 明确控制其他变量且仅A不同：强加强
- 指出另一个变量也不同：强削弱
- 无法判断组间差异：不选或弱
- 无关变量：无效
