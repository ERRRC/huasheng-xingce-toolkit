# 反向构造相交最小/最大

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_inclusion_exclusion_extreme_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

容斥问题

## 子题型 (`sub_type`)

容斥最值

## 方法名称 (`method_name`)

反向构造相交最小/最大

## 检索标签 (`tags`)

- 容斥最值
- 反向构造
- 相交最小
- 相交最大

## 适用条件 (`trigger_conditions`)

- 题干问至少有多少、最多有多少、相交部分最少/最多
- 集合数量给出但交集未知

## 不适用条件 (`anti_conditions`)

- 若题干给出完整交集数量，直接一般容斥计算

## 解题步骤 (`steps`)

- 明确要求最大还是最小
- 要相交部分尽量小，则反向尽量相斥
- 用总量限制判断是否必然重叠
- 构造极端情形后给出边界值

## 公式 (`formulas`)

- 最小交集通常由总需求超过总体容量的溢出部分确定

## 示例 (`examples`)

- 思维导图第6页给出“反向构造：要想相交部分尽量小，则反向尽量相斥”

## 易错点 (`pitfalls`)

- 未构造最不利或最极端情况
- 把“可能”当“必然”

## 避免事项 (`forbidden`)

- 不要在没有总量边界时断言最值

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
    - 11

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总量
- 各集合规模
- 所求交集类型
- 最大/最小目标

## 计算策略 (`calculation_policy`)

- mode：construct_extreme
- allow_exact_calculation：true
- preferred_tools：
  - 反向构造
  - 容量溢出

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最小值
  - 最大值
  - 选项
- must_report：极端构造方向
