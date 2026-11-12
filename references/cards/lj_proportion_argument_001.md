# 比例类论证分母校验法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_proportion_argument_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

比例类

## 方法名称 (`method_name`)

比例类论证分母校验法

## 检索标签 (`tags`)

- 比例类
- 率
- 分子分母
- 数字比较
- 削弱

## 适用条件 (`trigger_conditions`)

- 题干用人数/数量/死亡人数/销量等绝对数比较后推出风险、威胁、概率或比例结论
- 出现比例、率、占比、更多、更少

## 不适用条件 (`anti_conditions`)

- 题干已经给出同一分母下的比例时，不要再质疑分母缺失

## 解题步骤 (`steps`)

- 识别论点是否在比较率或风险。
- 拆出分子：题干直接比较的数量。
- 寻找分母：总体人数、患者人数、样本总数、机会总数。
- 若题干只比较分子而未比较分母，优先找指出分母差异的选项。
- 正确选项常用比例或数字补充，说明绝对数比较不能推出比例结论。

## 公式 (`formulas`)

- 率=分子/分母
- 只比分子不能推出率大小

## 示例 (`examples`)

- MERS例题中，普通感冒死亡人数多于MERS死亡人数，但普通感冒患者远多于MERS患者，不能推出普通感冒更能威胁生命安全。

## 易错点 (`pitfalls`)

- 只看死亡人数等绝对数
- 忽略患者总数
- 把绝对数多当风险高

## 避免事项 (`forbidden`)

- 不得在无分母信息时直接比较风险大小

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
    - 13

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- numerator_a
- numerator_b
- denominator_a
- denominator_b
- claim_rate_comparison
- options

## 计算策略 (`calculation_policy`)

- mode：ratio_check
- prefer：
  - 分母差异
  - 率的直接比较
- avoid：
  - 单纯分子比较

## 原程序优先级 (`solver_priority`)

17

## 原卡输出约束 (`output_constraints`)

- must_output：
  - numerator
  - denominator
  - rate_issue
- must_not_output：
  - 用绝对数直接判断比例

## argument_structure (`argument_structure`)

- claim：由绝对数推出比例/风险/威胁大小。
- evidence：题干给出的分子数量比较。
- link：若分母不同，分子大小不能推出比例大小。

## strength_order (`strength_order`)

- 直接指出分母差异导致率无法比较：强削弱
- 直接给出相反比例：更强
- 只说明原因不同或有重叠个体：弱或无关
- 只补充绝对数：通常无效
