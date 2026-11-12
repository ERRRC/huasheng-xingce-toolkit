# 工程/运输/经济统筹的低耗优先法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_planning_optimal_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

统筹规划问题

## 子题型 (`sub_type`)

最优方案

## 方法名称 (`method_name`)

工程/运输/经济统筹的低耗优先法

## 检索标签 (`tags`)

- 统筹规划
- 最优方案
- 运输统筹
- 经济统筹
- 工程统筹

## 适用条件 (`trigger_conditions`)

- 题干要求最省、最少、最优、如何安排、统筹
- 有多种方案可选

## 不适用条件 (`anti_conditions`)

- 若题干只问单一公式计算，不走统筹规划

## 解题步骤 (`steps`)

- 工程统筹比较各部分效率，先分工再合作
- 运输统筹比较耗能，优先低耗能且尽量不空载
- 经济统筹比较单价，优先低单价且尽量不浪费
- 最后剩余部分多方案比较

## 公式 (`formulas`)

- 无固定公式，核心为单位效率/单位成本比较

## 示例 (`examples`)

- 思维导图第5页列出工程、运输、经济统筹的优先原则

## 易错点 (`pitfalls`)

- 只贪心前半段，忘记最后剩余部分需要比较
- 忽略空载或浪费

## 避免事项 (`forbidden`)

- 不要在局部最优无法保证全局最优时不验证剩余部分

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 方案列表
- 单位成本或效率
- 容量限制
- 剩余部分规则

## 计算策略 (`calculation_policy`)

- mode：compare_unit_efficiency
- allow_exact_calculation：true
- preferred_tools：
  - 单位比较
  - 剩余枚举

## 原程序优先级 (`solver_priority`)

32

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最优方案
  - 最小成本
  - 最短时间
  - 选项
- must_report：优先选择依据
