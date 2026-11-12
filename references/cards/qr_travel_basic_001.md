# 路程=速度×时间与比例法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_travel_basic_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

普通行程

## 方法名称 (`method_name`)

路程=速度×时间与比例法

## 检索标签 (`tags`)

- 行程
- 速度
- 时间
- 路程
- 比例法
- 单位换算

## 适用条件 (`trigger_conditions`)

- 题干出现速度、路程、时间、提前到达、晚到、提速降速

## 不适用条件 (`anti_conditions`)

- 若涉及相遇追及则调用相遇追及；若涉及流水则调用流水行船

## 解题步骤 (`steps`)

- 统一单位
- 用S=vt建立关系
- 路程一定时速度与时间反比
- 速度或时间一定时路程与另一变量正比
- 用比例差和实际量建立对应关系

## 公式 (`formulas`)

- S=v*t
- m/s转km/h乘3.6；km/h转m/s除以3.6

## 示例 (`examples`)

- 笔记第31页例题用提速前后速度比得到时间比，再由提前时间求原定时间和距离

## 易错点 (`pitfalls`)

- 单位未统一
- 路程一定时误用正比
- 提前时间与用时差混淆

## 避免事项 (`forbidden`)

- 不要在路程不等时套反比时间关系

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 3
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 31

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 速度
- 时间
- 路程
- 单位
- 变化前后关系

## 计算策略 (`calculation_policy`)

- mode：ratio_or_equation
- allow_exact_calculation：true
- preferred_tools：
  - 比例法
  - 方程法
  - 单位换算

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 路程
  - 速度
  - 时间
  - 选项
- unit_check：速度单位统一
