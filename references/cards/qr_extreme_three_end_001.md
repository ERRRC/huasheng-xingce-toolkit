# 两端同向极端构造

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_extreme_three_end_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

最值问题

## 子题型 (`sub_type`)

三端最值

## 方法名称 (`method_name`)

两端同向极端构造

## 检索标签 (`tags`)

- 三端最值
- 混合
- 浓度
- 极端构造

## 适用条件 (`trigger_conditions`)

- 三种水平/浓度/温度混合，问某一端最多或最少

## 不适用条件 (`anti_conditions`)

- 若只有两端混合，优先十字相乘

## 解题步骤 (`steps`)

- 把三端想成热水、温水、冷水混合
- 要某一端最多，则另一端也尽量多，中间尽量少
- 要某一端最少，则另一端也尽量少
- 列方程求目标量

## 公式 (`formulas`)

- 总量守恒；加权平均守恒

## 示例 (`examples`)

- 80%、50%、20%各100g配50%盐水100g，80%最多时50%取0，设80%为x，0.8x+0.2(100-x)=50，x=50

## 易错点 (`pitfalls`)

- 中间量没有取极端
- 两端方向理解反

## 避免事项 (`forbidden`)

- 不要在三端容量限制未检查时给答案

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 4
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 19

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 三端数值
- 各端容量限制
- 目标总量
- 目标平均/浓度
- 所求端最多/最少

## 计算策略 (`calculation_policy`)

- mode：extreme_construct_then_equation
- allow_exact_calculation：true
- preferred_tools：
  - 极端构造
  - 加权平均

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最大量
  - 最小量
  - 选项
- must_report：中间端取值策略
