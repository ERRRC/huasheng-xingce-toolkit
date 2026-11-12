# 可重复排列公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_perm_comb_repeated_011_alt

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

重复排列

## 方法名称 (`method_name`)

可重复排列公式

## 别名 (`aliases`)

- 密码问题
- 重复选取

## 检索标签 (`tags`)

- 可重复
- 每次独立
- 密码

## 适用条件 (`trigger_conditions`)

题目要求进行多次选取或排列，且每次选取后元素放回，或各个位置的选择互相独立不受之前影响

## 不适用条件 (`anti_conditions`)

不放回抽取，元素只能使用一次

## 所需信息 (`required_inputs`)

- 每次可选的元素种类数
- 选取/排列的次数

## 推理策略 (`reasoning_policy`)

- core_logic：n个不同元素，可重复地取m次，每一次都有n种选择，共有 n^m 种情形。
- detailed_policy：分析每个步骤的选项池是否受到上一步影响，若不受影响则直接使用乘法原理连乘。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：80
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 确定总共需要进行m次选择（即m个步骤）
- 确认每次选择时面临的独立选项种类数为n
- 利用乘法原理直接计算 n的m次方

## 公式 (`formulas`)

- 重复排列数 = n^m

## 示例 (`examples`)

-
  - context：6个年级选6个科技馆，仅有2个年级选A馆
  - action：先挑2个年级选A馆C(6,2)=15，剩余4个年级每个年级都有5种选择（不能是A），即5×5×5×5=625种

## 易错点 (`pitfalls`)

- 将重复取样当做不放回取样使用A(n,m)
- 分不清底数和指数谁是谁

## 避免事项 (`forbidden`)

- 选项不互斥时使用加法原理

## 原卡输出约束 (`output_constraints`)

- 输出合法整数

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 4

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
