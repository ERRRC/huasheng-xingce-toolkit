# 无论据有结论反驳结论法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_general_no_premise_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

一般质疑

## 方法名称 (`method_name`)

无论据有结论反驳结论法

## 检索标签 (`tags`)

- 质疑削弱
- 无论据有结论
- 反驳结论

## 适用条件 (`trigger_conditions`)

- 题干只有观点或结论，没有明显论据
- 问能够削弱上述观点
- 选项直接说明结论相反

## 不适用条件 (`anti_conditions`)

- 题干有明确论据和结论时，应优先攻击论据到结论的关系

## 解题步骤 (`steps`)

- 判断题干是否无明显论据，只有结论。
- 把结论抽象为 A。
- 寻找选项是否给出有理由的非 A。
- 若选项直接证明结论不成立，优先选择。
- 排除仅重复题干、只解释题干或无关事实。

## 公式 (`formulas`)

- 本质：A 与 ¬A

## 示例 (`examples`)

- 普通感冒药不真正治疗感冒；选项若说明吃药可加速治愈，即反驳结论。

## 易错点 (`pitfalls`)

- 题干有论据时仍只反驳结论，可能力度不如拆论证
- 无理由反对不算削弱

## 避免事项 (`forbidden`)

- 不得选择没有理由的反向表述

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
    - 8
    - 9

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- options

## 计算策略 (`calculation_policy`)

- mode：direct_refutation
- verification：
  - claim_A
  - option_not_A_with_reason

## 原程序优先级 (`solver_priority`)

28

## 原卡输出约束 (`output_constraints`)

- must_output：
  - claim
  - refuting_fact
- must_not_output：
  - 无理由说反对

## argument_structure (`argument_structure`)

- claim：题干唯一或主要观点A。
- evidence：无明显论据或论据很弱。
- link：削弱通过给出有理由的¬A。

## strength_order (`strength_order`)

- 直接否定论证核心因果/条件/断点：最强
- 提出另有他因或因果倒置且贴合结果：强
- 指出实验初始状态、缺少对照组、样本无效：强
- 肯定论据但说明得不出结论：中强
- 少数质疑论据：较弱
- 主体或话题无关：无效
