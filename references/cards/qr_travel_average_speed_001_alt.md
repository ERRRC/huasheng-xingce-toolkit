# 等距离平均速度公式法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_travel_average_speed_001_alt

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

等距离平均速度

## 方法名称 (`method_name`)

等距离平均速度公式法

## 别名 (`aliases`)

- 往返平均速度
- 上下坡平均速度

## 检索标签 (`tags`)

- 行程问题
- 平均速度
- 等距离
- 往返

## 适用条件 (`trigger_conditions`)

题目描述在两段相等的路程（如往返跑、上下坡距离相等、半路折返）中，分别以不同的速度v1和v2行驶，要求计算全程的平均速度。

## 不适用条件 (`anti_conditions`)

两段路程距离不相等，或求的是算术平均速度而非调和平均速度。

## 所需信息 (`required_inputs`)

- 第一段等距离路程的速度v1
- 第二段等距离路程的速度v2

## 推理策略 (`reasoning_policy`)

- core_logic：等距离情况下，平均速度并不是两速度的算术平均值，而是调和平均数，即总路程除以总时间得出。
- detailed_policy：

## 计算策略 (`calculation_policy`)

- shortcuts：直接代入等距离平均速度公式，无需设路程为未知数；定性判断平均速度必然略小于算术平均数(v1+v2)/2，可直接排除过大选项。

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - qr_travel_ordinary_001

## 解题步骤 (`steps`)

- 1. 确认两段路程是否严格相等（如上坡与下坡距离相同、去程与回程距离相同）。
- 2. 提取出两段路程对应的行驶速度v1和v2。
- 3. 直接代入公式 v_bar = 2*v1*v2 / (v1 + v2) 计算出平均速度。
- 4. 结合总时间计算单程或往返总路程。

## 公式 (`formulas`)

- $\bar{v} = \frac{2 v_1 v_2}{v_1 + v_2}$
- $\bar{v} < \frac{v_1 + v_2}{2}$ (若v1和v2大小不同)

## 示例 (`examples`)

-
  - context：平路速度9km/h，上坡6km/h，下坡18km/h，往返总共用时1小时，求家距学校多远？
  - action：上下坡距离相等，应用公式计算上下坡的平均速度：2×6×18 / (6+18) = 9km/h。由于平路速度也是9km/h，可知全程平均速度皆为9km/h。单程距离 = (9 × 1) / 2 = 4.5km。

## 易错点 (`pitfalls`)

- 错把平均速度算作 (v1+v2)/2。
- 求出往返总路程后，忘记除以2得到单程距离。

## 避免事项 (`forbidden`)

- 在距离不等的情况下错误使用该公式。

## 原卡输出约束 (`output_constraints`)

- 输出平均速度数值，或以此求出的距离数值

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 2

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
