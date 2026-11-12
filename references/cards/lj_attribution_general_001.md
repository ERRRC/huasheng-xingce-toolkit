# 归因论证识别与攻击总法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_attribution_general_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

归因论证

## 方法名称 (`method_name`)

归因论证识别与攻击总法

## 检索标签 (`tags`)

- 归因类
- 因果关系
- 质疑削弱
- 对比实验

## 适用条件 (`trigger_conditions`)

- 题干由现象推出原因
- 研究者认为A导致B
- 归因于、得益于、因为、影响、导致

## 不适用条件 (`anti_conditions`)

- 纯条件推出题不适用；没有因果或原因结论时不优先

## 解题步骤 (`steps`)

- 识别结果 B 和题干声称的原因 A。
- 判断结构：对比实验归因、一般归因、直接根本原因、对策隐含归因。
- 优先检查是否存在另有他因、因果倒置、否定此因、根/表原因、样本或实验问题。
- 若是对比实验，先检查分组是否正确、初始状态是否一致、是否缺对照组。
- 比较选项力度，选择最直接破坏A导致B的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 焦虑影响任务质量、运动时间越多成绩越高、凉茶销量增长得益于保健效用提升均属于归因论证。

## 易错点 (`pitfalls`)

- 把相关关系当因果
- 忽略实验分组差异
- 选项只谈背景不攻击因果链

## 避免事项 (`forbidden`)

- 不得把只说明相关的选项当作因果证明

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
    - 3
    - 4
    - 5
    - 7

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claimed_cause
- observed_effect
- experiment_groups
- comparison_basis
- options

## 计算策略 (`calculation_policy`)

- mode：causal_attack
- sequence：
  - cause_effect_extract
  - structure_classify
  - attack_type_match
  - strength_compare

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- must_output：
  - cause
  - effect
  - attribution_type
  - weakening_path
- must_not_output：
  - 把相关性当因果

## argument_structure (`argument_structure`)

- claim：A是B的原因或A导致B。
- evidence：题干观察到A与B相关、同时出现或实验组差异。
- link：从相关/差异推出因果，需要排除其他解释。

## strength_order (`strength_order`)

- 因果倒置/另有他因/否定此因直接击中原因：强
- 实验初始状态或对照组问题：强
- 样本无效：强
- 只说明A与B相关：不能削弱，甚至可能支持
- 无关背景：无效
