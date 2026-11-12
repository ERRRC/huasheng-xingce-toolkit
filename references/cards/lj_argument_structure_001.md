# 论点-论据-论证方式拆解法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_argument_structure_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

论证结构

## 方法名称 (`method_name`)

论点-论据-论证方式拆解法

## 检索标签 (`tags`)

- 论点
- 论据
- 论证方式
- 评价论证

## 适用条件 (`trigger_conditions`)

- 题干有事实+结论
- 问最能支持/削弱/前提/评价上述论证
- 题干出现调查、实验、研究、数据后给出观点

## 不适用条件 (`anti_conditions`)

- 只有纯条件推出且无论证评价问法时，优先翻译推理

## 解题步骤 (`steps`)

- 定位论点：找因此、所以、由此、认为、推测、说明等结论标志。
- 定位论据：找前置事实、数据、实验、调查、比较结果。
- 识别论证方式：是否存在因果归因、比例比较、样本推总体、对比实验、条件推出、解释矛盾。
- 标记断点：论据到论点之间缺少的桥梁就是加强/前提的核心，也是削弱的攻击点。
- 选项验证：只接受能作用于论点、论据或断点的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 数学学习机例题：论据是拥有学习机人数最多的班成绩最好，论点是学习机提高成绩，断点是是否实际利用学习机学习数学。

## 易错点 (`pitfalls`)

- 把背景信息当论点
- 把选项里的新信息当题干事实
- 论点和论据主体不一致时不标记断点

## 避免事项 (`forbidden`)

- 不得用选项重写题干结论后再判断
- 不得忽视论据到论点的中间跳跃

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

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- argument_text
- question_stem
- options

## 计算策略 (`calculation_policy`)

- mode：structure_extraction
- prefer：
  - 结论标志词
  - 主体一致
  - 话题一致
- avoid：
  - 从选项倒推题型

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- must_output：
  - claim
  - evidence
  - link_type
  - gap
- must_not_output：
  - 不说明论据与论点的关系

## argument_structure (`argument_structure`)

- claim：题干最终要证明的判断。
- evidence：题干已经给出的事实或数据。
- link：论据能否推出论点；若不能，中间缺口即断点。

## strength_order (`strength_order`)

- 直接补断点/拆断点
- 直接支持/反驳论点
- 补充背景事实
- 无关主体或无关话题
