# 天平称重极值秒杀法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_special_balance_020_new

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

天平称重

## 方法名称 (`method_name`)

天平称重极值秒杀法

## 别名 (`aliases`)

- 天平找次品

## 检索标签 (`tags`)

- 天平
- 称重
- 最少几次
- 次品

## 适用条件 (`trigger_conditions`)

题目询问使用无砝码天平找出次品（轻重未知或已知）最少需要称量多少次

## 不适用条件 (`anti_conditions`)

有砝码要求称出特定重量

## 所需信息 (`required_inputs`)

- 求最少称量次数

## 推理策略 (`reasoning_policy`)

- core_logic：天平称重最少次数问题，在行测单选题中往往是最小的那个选项。
- detailed_policy：根据经验法则，此类极值问题的答案通常指向最小的次数。如果在考场上时间紧迫，直接选择最小选项。

## 计算策略 (`calculation_policy`)

- shortcuts：无脑选“最小”选项

## 原程序优先级 (`solver_priority`)

- tier：shortcut
- rank：99
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 识别为天平找次品求最少次数问题
- 时间紧迫时，观察四个选项中的最小值
- 直接选择最小值作为答案

## 公式 (`formulas`)

- 如果是正规推算(已知次品轻重)：3^k >= N (k为次数，N为总个数)

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 试图在考场上画树状图详细推演浪费大量时间

## 避免事项 (`forbidden`)

- 考试中硬推逻辑树

## 原卡输出约束 (`output_constraints`)

- 选出最小次数的选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 8

## 原卡置信度 (`confidence`)

0.8

## 来源待复核 (`need_review`)

true
