# 插空法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_nonadjacent_insert_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

不相邻问题

## 方法名称 (`method_name`)

插空法

## 检索标签 (`tags`)

- 不相邻
- 不能连续
- 插空法
- 空位

## 适用条件 (`trigger_conditions`)

- 题干要求某些元素不能相邻、不能连续

## 不适用条件 (`anti_conditions`)

- 若要求必须相邻，使用捆绑法；若空位不足，应判断为无解或用补集法

## 解题步骤 (`steps`)

- 先排列无位置限制元素
- 数出形成的空位，两端是否算空位需按题意判断
- 将不相邻元素插入不同空位
- 判断插入元素是否有序
- 相乘得到结果

## 公式 (`formulas`)

- m个已排元素形成m+1个含两端空位，不含两端则m-1个

## 示例 (`examples`)

- 5人排队甲乙不能相邻：先排另3人A_3^3，形成4空，甲乙有序插入A_4^2

## 易错点 (`pitfalls`)

- 两端空位是否可用判断错误
- 插入元素顺序漏乘或多乘

## 避免事项 (`forbidden`)

- 不要先排受限制元素再数空

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

- 不相邻元素数量
- 其他元素数量
- 是否允许端点
- 插入元素是否有序

## 计算策略 (`calculation_policy`)

- mode：arrange_then_insert
- allow_exact_calculation：true
- preferred_tools：
  - 插空法

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 概率
  - 选项
- must_check：空位数量足够
