# 捆绑法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_adjacent_bundle_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

相邻问题

## 方法名称 (`method_name`)

捆绑法

## 检索标签 (`tags`)

- 相邻
- 挨着
- 捆绑法
- 内部排序

## 适用条件 (`trigger_conditions`)

- 题干要求若干元素必须相邻、连续、挨着

## 不适用条件 (`anti_conditions`)

- 若要求不相邻，改用插空法；若相邻元素内部固定顺序，应减少内部排序

## 解题步骤 (`steps`)

- 将必须相邻的元素捆成一个整体
- 把整体与其他元素一起排列
- 判断捆内元素是否需要内部排序
- 两部分结果相乘

## 公式 (`formulas`)

- 总数=A_(新元素数)^(新元素数) × 捆内排列数

## 示例 (`examples`)

- 5人排成1列，甲乙丙必须一起：甲乙丙合为1个元素，总元素3个，A_3^3×A_3^3

## 易错点 (`pitfalls`)

- 忘记捆内排序
- 总元素个数未减少

## 避免事项 (`forbidden`)

- 不要对内部顺序已固定的捆再乘内部排列

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 1
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 22

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 需相邻元素集合
- 其他元素数量
- 内部是否有序
- 整体排列方式

## 计算策略 (`calculation_policy`)

- mode：bundle_then_permute
- allow_exact_calculation：true
- preferred_tools：
  - 捆绑法

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 概率
  - 选项
- must_report：捆内是否排序
