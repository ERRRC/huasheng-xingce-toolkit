# 加强/削弱力度比较通用规则

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_strength_order_compare_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

力度比较

## 方法名称 (`method_name`)

加强/削弱力度比较通用规则

## 检索标签 (`tags`)

- 力度比较
- 加强力度
- 削弱力度
- 无关选项

## 适用条件 (`trigger_conditions`)

- 多个选项都看似相关
- 问最能加强/最能削弱
- 需要比较选项力度

## 不适用条件 (`anti_conditions`)

- 只有一个选项贴合题干时无需复杂排序

## 解题步骤 (`steps`)

- 先排除主体不一致、话题不一致、偷换概念的无关项。
- 再判断选项作用对象：论点、论据、论证关系、背景事实。
- 直接作用于论证关系的选项通常强于只作用于论据背景的选项。
- 因果题中，因果倒置、另有他因、否定此因通常强于泛泛相关。
- 前提题中，没它不行强于有它更好。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 支持题中断点搭桥通常强于普通事实；削弱题中A且非B反例强于只质疑少数论据。

## 易错点 (`pitfalls`)

- 相关不等于有力度
- 忽略问法导致把解释项当加强项

## 避免事项 (`forbidden`)

- 不得用选项字数长短判断力度
- 不得选主体不一致项

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
    - 12

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- evidence
- gap
- candidate_options

## 计算策略 (`calculation_policy`)

- mode：strength_ranking
- verification：
  - relevance
  - target_of_attack_or_support
  - directness

## 原程序优先级 (`solver_priority`)

5

## 原卡输出约束 (`output_constraints`)

- must_output：
  - ranked_options
  - reason_for_top_choice
- must_not_output：
  - 只说某项更强但不说明强在哪里

## argument_structure (`argument_structure`)

- claim：被加强/削弱的论点。
- evidence：论据与论证关系。
- link：力度取决于选项作用位置和直接程度。

## strength_order (`strength_order`)

- 直接补/拆论证关系
- 直接支持/反驳论点
- 关键事实或必要条件
- 一般相关事实
- 背景常识或无关项
