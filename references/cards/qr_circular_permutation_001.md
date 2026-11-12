# 环形固定一位后排列

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_circular_permutation_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

环形排列

## 方法名称 (`method_name`)

环形固定一位后排列

## 检索标签 (`tags`)

- 环形排列
- 圆桌
- 围坐
- 圆周排列

## 适用条件 (`trigger_conditions`)

- 题干出现圆桌、围成一圈、环形排列

## 不适用条件 (`anti_conditions`)

- 若有固定座位编号或起点明确，可能转为线性排列

## 解题步骤 (`steps`)

- 将环形旋转等价的情况视为同一种
- 固定一个元素作参照
- 其余n-1个元素全排列
- 若有相邻等限制再叠加捆绑/插空

## 公式 (`formulas`)

- n个不同元素环形排列数=A_(n-1)^(n-1)=(n-1)!

## 示例 (`examples`)

- 5人坐一桌吃饭，共A_4^4种坐法

## 易错点 (`pitfalls`)

- 把环形排列按n!计算
- 忽略圆桌旋转等价

## 避免事项 (`forbidden`)

- 不要在座位有编号且不旋转等价时套(n-1)!

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
    - 23

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 元素数量
- 座位是否有编号
- 是否旋转等价
- 附加限制

## 计算策略 (`calculation_policy`)

- mode：fix_one_then_permute
- allow_exact_calculation：true
- preferred_tools：
  - 环形排列

## 原程序优先级 (`solver_priority`)

20

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 概率
  - 选项
- must_check：是否旋转等价
