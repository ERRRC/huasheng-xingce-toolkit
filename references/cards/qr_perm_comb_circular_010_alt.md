# 圆桌/环形排列法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_perm_comb_circular_010_alt

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

环形排列

## 方法名称 (`method_name`)

圆桌/环形排列法

## 别名 (`aliases`)

- 圆桌排列
- 环形排列

## 检索标签 (`tags`)

- 圆桌
- 环形
- 围成一圈

## 适用条件 (`trigger_conditions`)

题目明确描述元素“围成一圈”或“在圆桌上就餐”等形成闭环的排列情况

## 不适用条件 (`anti_conditions`)

线性排列（排成一排）

## 所需信息 (`required_inputs`)

- 围成一圈的总元素个数

## 推理策略 (`reasoning_policy`)

- core_logic：环形排列与线性排列不同，由于可以旋转，n个不同元素做环形排列，共有 A_{n-1}^{n-1} 种排法。
- detailed_policy：将其中的一个元素位置固定作为参照物，剩下的n-1个元素进行线性的全排列，即(n-1)!

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：90
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 确认场景为无固定座次编号的圆桌/环形排列
- 找出独立参与环形排列的大元素个数n
- 应用公式计算排列数 (n-1)!
- 若有捆绑元素，还需在其内部计算线性全排列，再相乘

## 公式 (`formulas`)

- 环形排列数 = A_{n-1}^{n-1} = (n-1)!

## 示例 (`examples`)

-
  - context：10个座位的圆桌就餐，5对夫妇相邻而坐的概率
  - action：总情况为10个元素环形排列A(9,9)。5对夫妇捆绑后变为5个元素环形排列A(4,4)，夫妇内部A(2,2)^5

## 易错点 (`pitfalls`)

- 将圆桌排列等同于排成一排的全排列A(n,n)
- 圆桌有明确且固定的座位编号时（例如东南西北座），此时相当于线排

## 避免事项 (`forbidden`)

- 对于无差异的环形位置依然使用A(n,n)计算总数

## 原卡输出约束 (`output_constraints`)

- 输出合法整数或概率

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 4

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
