# 去掉完整周期看余数

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_cycle_mod_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

周期循环问题

## 子题型 (`sub_type`)

周期余数

## 方法名称 (`method_name`)

去掉完整周期看余数

## 检索标签 (`tags`)

- 周期
- 循环
- 余数
- 最小公倍数

## 适用条件 (`trigger_conditions`)

- 题干出现每隔、每几天、循环、轮流、周期、星期循环
- 问第N次/第N天状态

## 不适用条件 (`anti_conditions`)

- 若周期不是固定的，不能直接取余

## 解题步骤 (`steps`)

- 确定循环周期T
- 用N除以T看余数
- 余数为0时对应周期末项
- 两个周期共同出现时取最小公倍数

## 公式 (`formulas`)

- 第N天状态=第(N mod T)天状态；余0按第T天处理
- 共同周期=LCM(T1,T2)

## 示例 (`examples`)

- 第18天，18÷7余4，第18天星期与第4天一样

## 易错点 (`pitfalls`)

- 混淆“每5天”和“每隔5天”（后者实际周期为6天）
- 余数为0误判成第0项

## 避免事项 (`forbidden`)

- 不要在非等周期场景下机械取余

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
    - 13

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 周期长度
- 目标序号或天数
- 初始状态
- 多个周期时各周期长度

## 计算策略 (`calculation_policy`)

- mode：modulo
- allow_exact_calculation：true
- preferred_tools：
  - 取余
  - LCM

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 状态
  - 日期
  - 星期
  - 选项
- must_check：每N天/每隔N天区别
