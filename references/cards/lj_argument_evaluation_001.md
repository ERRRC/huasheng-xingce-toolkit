# 评价论证结构定位法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_argument_evaluation_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

评价论证

## 子题型 (`sub_type`)

评价论证

## 方法名称 (`method_name`)

评价论证结构定位法

## 检索标签 (`tags`)

- 评价论证
- 论证强弱
- 断点
- 漏洞

## 适用条件 (`trigger_conditions`)

- 评价上述论证
- 下列哪项最能评价
- 论证是否成立取决于
- 为使论证有效需要考察

## 不适用条件 (`anti_conditions`)

- 问最能支持/削弱/解释时应转入对应题型，不停留在评价

## 解题步骤 (`steps`)

- 抽取论点、论据和论证关系。
- 找出论证成立依赖的关键变量或断点。
- 评价类选项通常应能决定该断点是否成立。
- 若选项回答后会影响论证强弱，则为有效评价项。
- 排除只补充背景、只重复题干、不能改变论证强弱的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 评价论证可复用一般论证的论点-论据-断点拆解与主体话题一致原则。

## 易错点 (`pitfalls`)

- 把评价题直接当加强题
- 选择只能单向支持但不能检验关键断点的选项

## 避免事项 (`forbidden`)

- 不得新增题干没有的评价标准

## 来源文件 (`source_file`)

- 【判断推理】支持、前提假设、比例、解释说明.pdf
- 【判断推理】质疑类.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】支持、前提假设、比例、解释说明.pdf
  - pages：
    - 1
-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 8
    - 11

## 原卡置信度 (`confidence`)

0.78

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- claim
- evidence
- gap
- options

## 计算策略 (`calculation_policy`)

- mode：argument_evaluation
- verification：
  - identify_gap
  - option_tests_gap

## 原程序优先级 (`solver_priority`)

38

## 原卡输出约束 (`output_constraints`)

- must_output：
  - evaluated_gap
  - why_option_evaluates
- must_not_output：
  - 把评价项直接说成前提而不说明检验作用

## argument_structure (`argument_structure`)

- claim：被评价的论点。
- evidence：题干论据。
- link：评价项应检验论据能否推出论点的关键条件。

## strength_order (`strength_order`)

- 能检验关键断点且回答不同会改变论证强弱：强
- 只能单向支持或削弱但不检验断点：中等
- 背景事实：弱
- 无关：排除
