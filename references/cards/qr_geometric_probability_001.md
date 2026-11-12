# 长度/面积/体积比求概率

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_geometric_probability_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

几何概型

## 方法名称 (`method_name`)

长度/面积/体积比求概率

## 检索标签 (`tags`)

- 几何概型
- 长度比
- 面积比
- 体积比
- 随机点

## 适用条件 (`trigger_conditions`)

- 样本点连续、无法一一计数
- 题干出现随机时刻、随机位置、落在区域内概率

## 不适用条件 (`anti_conditions`)

- 若情况数有限且可列举，优先一般概率

## 解题步骤 (`steps`)

- 确定全部试验区域的长度/面积/体积
- 确定符合事件区域的长度/面积/体积
- 用区域比求概率
- 注意区间端点不影响连续概率

## 公式 (`formulas`)

- P(A)=构成事件A的区域长度/面积/体积 ÷ 试验全部结果区域长度/面积/体积

## 示例 (`examples`)

- 红绿灯例：绿灯25秒，总周期60秒，看见绿灯概率=25/60

## 易错点 (`pitfalls`)

- 把连续区域离散计数
- 分母没有取完整周期或完整区域

## 避免事项 (`forbidden`)

- 不要在各结果不按区域均匀分布时套几何概型

## 来源文件 (`source_file`)

- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生数量关系笔记.pdf
  - pages：
    - 21

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总区域长度/面积/体积
- 符合区域长度/面积/体积
- 是否均匀随机

## 计算策略 (`calculation_policy`)

- mode：measure_ratio
- allow_exact_calculation：true
- preferred_tools：
  - 区域比

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 概率
  - 选项
- must_check：连续均匀随机
