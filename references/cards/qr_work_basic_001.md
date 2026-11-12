# 工作总量=效率×时间与赋值法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_work_basic_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

工程问题

## 子题型 (`sub_type`)

基础工程

## 方法名称 (`method_name`)

工作总量=效率×时间与赋值法

## 检索标签 (`tags`)

- 工程问题
- 效率
- 时间
- 工作总量
- 赋值法

## 适用条件 (`trigger_conditions`)

- 题干出现完成一项工作、甲乙合作、单独完成、效率比、工作量

## 不适用条件 (`anti_conditions`)

- 若题干含草每天生长，优先牛吃草；若含流水速度，优先行程流水

## 解题步骤 (`steps`)

- 若已知时间，设工作总量为各时间最小公倍数
- 根据总量/时间求效率
- 若已知效率比，直接赋值效率
- 多人合作时效率相加，再由总量求时间

## 公式 (`formulas`)

- 工作总量=效率×时间
- 合作效率=效率1+效率2+...
- 工作时间=工作总量/合作效率

## 示例 (`examples`)

- 笔记第15页强调核心公式与合作效率和不变

## 易错点 (`pitfalls`)

- 工作总量未统一
- 合作时未把效率相加
- 时间单位不统一

## 避免事项 (`forbidden`)

- 不要把休息时间直接当无人工作，应判断谁在休息谁在工作

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 15

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 单独完成时间或效率比
- 合作方式
- 工作总量或可赋值总量
- 目标时间/效率

## 计算策略 (`calculation_policy`)

- mode：assign_lcm_total
- allow_exact_calculation：true
- preferred_tools：
  - 赋值法
  - 效率相加
  - 比例法

## 原程序优先级 (`solver_priority`)

10

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 时间
  - 效率
  - 工作量
  - 选项
- unit_check：时间单位统一
