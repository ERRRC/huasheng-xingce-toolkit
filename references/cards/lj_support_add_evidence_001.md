# 新增事实数据支持法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_support_add_evidence_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强

## 子题型 (`sub_type`)

加入论据和事实

## 方法名称 (`method_name`)

新增事实数据支持法

## 检索标签 (`tags`)

- 支持类
- 加入论据
- 事实支持
- 数据支持

## 适用条件 (`trigger_conditions`)

- 选项给出新事实、数据、研究结果
- 结论需要更多事实证明

## 不适用条件 (`anti_conditions`)

- 新事实与论点主体或话题不一致时不适用

## 解题步骤 (`steps`)

- 确认论点需要证明的方向。
- 判断选项新增事实是否与论点同向。
- 检查新增事实是否直接覆盖论点主体或关键范围。
- 优先选择数据更具体、范围更贴合的选项。
- 若新增事实只是背景或反向事实，排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 银河系宜居星球例题中，红矮星数量、类地行星、水和大气层构成新增事实支持。

## 易错点 (`pitfalls`)

- 数据看似大但分母范围不一致
- 新增事实只证明可能性很弱

## 避免事项 (`forbidden`)

- 不得把无关统计数字当作支持

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

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- existing_evidence
- option_facts

## 计算策略 (`calculation_policy`)

- mode：evidence_addition
- prefer：
  - 具体数据
  - 同主体
  - 同话题
- avoid：
  - 离题事实

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- must_output：
  - added_fact
  - how_it_supports
- must_not_output：
  - 只复述数据

## argument_structure (`argument_structure`)

- claim：需要被事实支撑的结论。
- evidence：题干已有事实。
- link：新增事实扩大或增强结论成立基础。

## strength_order (`strength_order`)

- 断点搭桥/必要条件：直接补足论据到论点的缺口，力度强
- 自断一臂/排除关键漏洞：排除最主要替代路径，力度强
- 加入论据和事实：直接增加支持事实，力度中强
- 解释说明机制：解释为什么论点可能成立，力度中等
- 举例或类比支持：支持但范围较窄，力度较弱
- 主体或话题不一致：无关
