# 因果倒置削弱法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_weaken_reverse_causation_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

削弱

## 子题型 (`sub_type`)

因果倒置

## 方法名称 (`method_name`)

因果倒置削弱法

## 检索标签 (`tags`)

- 质疑削弱
- 因果倒置
- 归因类

## 适用条件 (`trigger_conditions`)

- 题干由A与B相关推出A导致B
- 选项说明B导致A
- 时间先后可能相反

## 不适用条件 (`anti_conditions`)

- 题干已有明确时间先后且A先于B时，因果倒置力度下降

## 解题步骤 (`steps`)

- 抽取题干因果：A导致B。
- 检查题干是否只证明相关，没有证明时间先后。
- 寻找选项是否说明B导致A。
- 若B导致A能解释题干现象，则强削弱。
- 注意时间先后：若选项与时间事实冲突则排除。

## 公式 (`formulas`)

- 题干：A→B；削弱：B→A

## 示例 (`examples`)

- 运动时间越多成绩越高例题中，可能是学习成绩好的孩子有更多自由活动时间，而非运动提高成绩。

## 易错点 (`pitfalls`)

- 忽略时间先后
- 把共同相关误作倒置

## 避免事项 (`forbidden`)

- 不得在题干明确A先发生时强行倒置

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
    - 5

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- cause_A
- effect_B
- temporal_order
- options

## 计算策略 (`calculation_policy`)

- mode：reverse_causation
- verification：
  - original_causal_direction
  - reverse_direction
  - time_consistency

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- must_output：
  - original_direction
  - reversed_direction
  - time_check
- must_not_output：
  - 无时间依据时断言倒置一定成立

## argument_structure (`argument_structure`)

- claim：A导致B。
- evidence：A与B正相关。
- link：选项提出B才是A的原因。

## strength_order (`strength_order`)

- 直接说明B导致A且符合时间：强
- 只说明B与A相关：弱
- 与时间先后矛盾：排除
