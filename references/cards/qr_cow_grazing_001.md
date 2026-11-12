# 白吃牛与干活牛三步法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_cow_grazing_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

牛吃草问题

## 子题型 (`sub_type`)

原有草与生长草

## 方法名称 (`method_name`)

白吃牛与干活牛三步法

## 检索标签 (`tags`)

- 牛吃草
- 草场
- 原有草
- 生长量
- 时间

## 适用条件 (`trigger_conditions`)

- 题干出现草每天生长、若干牛若干天吃完、问时间或牛数

## 不适用条件 (`anti_conditions`)

- 没有持续增长或消耗背景时，不应路由为牛吃草

## 解题步骤 (`steps`)

- 将牛分为“白吃牛”和“干活牛”
- 第一步求每日草生长量/白吃牛
- 第二步求草场原有草量
- 第三步按所问求时间或牛数

## 公式 (`formulas`)

- 白吃牛=每日草生长量=(t大×牛数大-t小×牛数小)/(t大-t小)
- 原有草=(牛数-白吃牛)×时间
- 时间=原有草/干活牛
- 牛数=原有草/时间+白吃牛

## 示例 (`examples`)

- 笔记第11页口诀：“白吃牛原有草，问中数字少不了”

## 易错点 (`pitfalls`)

- 时间大的在前顺序弄反
- 把所有牛都当成吃原有草
- 忘记每日生长量

## 避免事项 (`forbidden`)

- 不要在草量不增长的普通工程题中套牛吃草

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 8
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 11

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 方案1牛数与时间
- 方案2牛数与时间
- 目标时间或目标牛数

## 计算策略 (`calculation_policy`)

- mode：three_step_formula
- allow_exact_calculation：true
- preferred_tools：
  - 白吃牛
  - 原有草
  - 方程法

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 时间
  - 牛数
  - 选项
- must_check：时间大的在前计算生长量
