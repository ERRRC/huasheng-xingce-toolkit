# 缺少对照组/对照不当检查法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_experiment_missing_control_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

对比实验

## 方法名称 (`method_name`)

缺少对照组/对照不当检查法

## 检索标签 (`tags`)

- 对比实验
- 对照组
- 实验设计
- 削弱

## 适用条件 (`trigger_conditions`)

- 题干实验缺少必要比较
- 两批测试者处理不同但无法隔离变量
- 选项指出应有对照或两组不可比

## 不适用条件 (`anti_conditions`)

- 题干已有严格对照且只问解释现象时不适用

## 解题步骤 (`steps`)

- 识别实验希望证明的处理变量。
- 检查是否存在合适对照组隔离该变量。
- 若缺少对照组或对照组处理不同太多，则实验结论可信度下降。
- 若选项说明两组健康、心理等基础状况接近，可反驳对实验可信度的质疑。
- 选择最能说明变量是否被隔离的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 睡眠实验中，两批测试者健康状况和心理素质原本接近，可反驳因对照问题提出的质疑。

## 易错点 (`pitfalls`)

- 只比较结果不比较控制变量
- 把两组不同处理混成一个原因

## 避免事项 (`forbidden`)

- 不得忽视实验设计中的变量隔离问题

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

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- treatment_variable
- control_variable
- groups
- outcome
- options

## 计算策略 (`calculation_policy`)

- mode：control_group_check
- verification：
  - isolate_variable
  - group_comparability

## 原程序优先级 (`solver_priority`)

15

## 原卡输出约束 (`output_constraints`)

- must_output：
  - control_issue
  - impact_on_claim
- must_not_output：
  - 把所有组间差异都当作有效削弱

## argument_structure (`argument_structure`)

- claim：某处理导致某结果。
- evidence：两组实验结果不同。
- link：需要合适对照排除其他变量。

## strength_order (`strength_order`)

- 指出缺失关键对照：强削弱
- 说明关键初始条件接近：强加强/反驳质疑
- 只谈非关键指标：弱
- 实验后结果重复：无效
