# 插板法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_same_elements_distribution_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

相同元素分配

## 方法名称 (`method_name`)

插板法

## 检索标签 (`tags`)

- 插板法
- 相同元素
- 分配
- 至少一个

## 适用条件 (`trigger_conditions`)

- 题干出现相同小球、相同任务、相同物品分给若干人
- 每人至少一个或可构造至少一个

## 不适用条件 (`anti_conditions`)

- 元素不同不能用插板法；若每人要求不同下限，要先构造后再插板

## 解题步骤 (`steps`)

- 确认元素相同
- 确认每个对象至少一个；若没有要求，构造为n+m个元素分给m人且每人至少一个
- 若每人至少k个，先预分k-1个，使其变成至少一个
- 在空位中插板

## 公式 (`formulas`)

- n个相同元素分给m人每人至少1个：C_(n-1)^(m-1)
- 无至少要求：C_(n+m-1)^(m-1)

## 示例 (`examples`)

- 9个相同小球分给3人至少1个：C_8^2；无要求：C_11^2；每人至少2个：C_5^2

## 易错点 (`pitfalls`)

- 元素不同误用插板
- 没有构造“每人至少一个”
- 下限预分数量错误

## 避免事项 (`forbidden`)

- 不要对不同元素分配使用插板法

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

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 相同元素总数
- 分配对象数
- 每个对象下限
- 是否允许0

## 计算策略 (`calculation_policy`)

- mode：stars_and_bars
- allow_exact_calculation：true
- preferred_tools：
  - 构造至少一个
  - 插板法

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 分法数
  - 选项
- must_check：元素相同
