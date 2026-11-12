# 肯定论据否定结论法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_evidence_conclusion_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

一般质疑

## 方法名称 (`method_name`)

肯定论据否定结论法

## 检索标签 (`tags`)

- 质疑削弱
- 有论据有结论
- 论证缺口

## 适用条件 (`trigger_conditions`)

- 题干有事实/论据并推出结论
- 选项承认论据但说明结论不成立
- 虽然...但是...所以不...

## 不适用条件 (`anti_conditions`)

- 严格条件命题题应调用A且非B削弱规则

## 解题步骤 (`steps`)

- 划分论据 A 与结论 B。
- 保持论据 A 成立。
- 寻找选项是否补充事实说明即使 A 成立也不能推出 B。
- 用句式检验：虽然 A，但是选项，所以不一定 B。
- 选择最直接击中论据到结论缺口的选项。

## 公式 (`formulas`)

- 削弱本质：A 且 ¬B

## 示例 (`examples`)

- 贫铀弹例题：虽粉尘150米内沉降，但风可吹到40公里外，因此仍可能影响士兵健康。

## 易错点 (`pitfalls`)

- 只反驳论据但不影响结论
- 只提出可能性但不贴合题干

## 避免事项 (`forbidden`)

- 不得忽视题干已经给出的论据

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
    - 10

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- evidence
- claim
- options

## 计算策略 (`calculation_policy`)

- mode：evidence_conclusion_attack
- test：although_A_but_not_B

## 原程序优先级 (`solver_priority`)

29

## 原卡输出约束 (`output_constraints`)

- must_output：
  - evidence_A
  - claim_B
  - why_A_not_lead_to_B
- must_not_output：
  - 单纯攻击无关事实

## argument_structure (`argument_structure`)

- claim：由论据A推出结论B。
- evidence：题干事实A。
- link：选项构造A成立但B不成立，切断推出。

## strength_order (`strength_order`)

- 直接否定论证核心因果/条件/断点：最强
- 提出另有他因或因果倒置且贴合结果：强
- 指出实验初始状态、缺少对照组、样本无效：强
- 肯定论据但说明得不出结论：中强
- 少数质疑论据：较弱
- 主体或话题无关：无效
