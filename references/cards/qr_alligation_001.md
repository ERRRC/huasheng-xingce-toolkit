# 已知3个浓度求两部分量之比

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_alligation_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

浓度问题

## 子题型 (`sub_type`)

十字相乘

## 方法名称 (`method_name`)

已知3个浓度求两部分量之比

## 检索标签 (`tags`)

- 十字相乘
- 盐水
- 浓度混合
- 已知3r

## 适用条件 (`trigger_conditions`)

- 两部分浓度和混合浓度均已知
- 问两部分溶液量之比或配比

## 不适用条件 (`anti_conditions`)

- 未知浓度超过一个，或混合后有蒸发/加水导致总量变化复杂时，优先溶质守恒方程

## 解题步骤 (`steps`)

- 将两个原浓度写在十字两端，混合浓度写中间
- 交叉相减取正差
- 差值对应对方溶液量之比
- 必要时再结合总量求各部分量

## 公式 (`formulas`)

- 若浓度A、浓度B混合为R，则A液质量:B液质量=|B-R|:|A-R|

## 示例 (`examples`)

- 笔记第9页强调只要能表示成A/B形式的比例关系，均可能是类浓度问题

## 易错点 (`pitfalls`)

- 比值方向写反
- 没有确认混合浓度介于两原浓度之间

## 避免事项 (`forbidden`)

- 不要在非两端混合模型中硬套十字相乘

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 6
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 9

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 高浓度
- 低浓度
- 混合浓度
- 总量或比例目标

## 计算策略 (`calculation_policy`)

- mode：shortcut_formula
- allow_exact_calculation：true
- preferred_tools：
  - 十字相乘
  - 比例换算

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 比例
  - 质量
  - 选项
- must_check：混合浓度应在两原浓度之间
