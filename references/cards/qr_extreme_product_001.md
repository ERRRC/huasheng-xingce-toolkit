# 总平均固定下的十字相乘极值

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_extreme_product_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

最值问题

## 子题型 (`sub_type`)

乘积最值

## 方法名称 (`method_name`)

总平均固定下的十字相乘极值

## 检索标签 (`tags`)

- 乘积最值
- 平均分
- 十字相乘
- 极端构造

## 适用条件 (`trigger_conditions`)

- 题干给出总体平均，问某类人数最多/最少，个体值有上下限

## 不适用条件 (`anti_conditions`)

- 若没有总和/平均约束，不走乘积最值

## 解题步骤 (`steps`)

- 将问题转成a1×b1+a2×b2=总和
- 要使a1最多，b1尽量接近总体平均，b2尽量远离总体平均
- 用十字相乘或方程求人数边界
- 按整数修正

## 公式 (`formulas`)

- a1*b1+a2*b2=总和
- 十字思想：人数比与距离平均值的差值成反比

## 示例 (`examples`)

- 30人平均70分，不及格最多：不及格取59，及格取100，59x+100(30-x)=2100，x最多21

## 易错点 (`pitfalls`)

- 极端值选择方向反了
- 解出小数后取整方向错误

## 避免事项 (`forbidden`)

- 不要用普通平均直接四舍五入

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

- 总体平均
- 总人数
- 目标类别上下限
- 另一类别上下限

## 计算策略 (`calculation_policy`)

- mode：extreme_assignment
- allow_exact_calculation：true
- preferred_tools：
  - 十字相乘
  - 方程法

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最大人数
  - 最小人数
  - 选项
- must_check：取值上下限和整数取整
