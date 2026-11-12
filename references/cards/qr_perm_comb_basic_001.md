# 有序为排列、无序为组合，分类加法分步乘法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_perm_comb_basic_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

基础排列组合

## 方法名称 (`method_name`)

有序为排列、无序为组合，分类加法分步乘法

## 检索标签 (`tags`)

- 排列
- 组合
- 加法原理
- 乘法原理
- 至少
- 全部减不符

## 适用条件 (`trigger_conditions`)

- 题干出现安排、选择、分配、排队、方案数、至少、不能、符合条件数

## 不适用条件 (`anti_conditions`)

- 若每个元素独立重复选择，优先重复排列；若概率题需再除以所有情况

## 解题步骤 (`steps`)

- 判断有序还是无序：有顺序用排列，无顺序用组合
- 分类完成一件事用加法
- 分步完成一件事用乘法
- 有“至少/不能”等否定提示时考虑全部减不符
- 从特殊元素或特殊位置入手

## 公式 (`formulas`)

- A_n^m=n!/(n-m)!
- C_n^m=n!/[m!(n-m)!]
- 至少2个的反面为0个或1个

## 示例 (`examples`)

- 笔记第21页维修任务例用组合处理完成次数不同的情况

## 易错点 (`pitfalls`)

- 把分类和分步混用
- “至少”的反面写错
- 未判断是否有序

## 避免事项 (`forbidden`)

- 不要在未明确样本空间时直接把方案数当概率

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
    - 21

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 元素总数n
- 选取个数m
- 是否有序
- 限制条件
- 是否求概率

## 计算策略 (`calculation_policy`)

- mode：classify_then_count
- allow_exact_calculation：true
- preferred_tools：
  - 排列
  - 组合
  - 加法原理
  - 乘法原理
  - 补集法

## 原程序优先级 (`solver_priority`)

8

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 概率
  - 选项
- must_report：有序/无序判断
