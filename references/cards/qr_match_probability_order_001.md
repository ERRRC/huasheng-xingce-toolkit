# 负场位置限制

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_match_probability_order_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

比赛类概率

## 方法名称 (`method_name`)

负场位置限制

## 检索标签 (`tags`)

- 比赛概率
- 几局几胜
- 负场位置
- 提前结束

## 适用条件 (`trigger_conditions`)

- 题干出现三局两胜、五局三胜、七局四胜、比分为x:y的概率或场次

## 不适用条件 (`anti_conditions`)

- 若只是循环赛场次，不是概率，调用比赛场次规则

## 解题步骤 (`steps`)

- 先确定获胜所需胜场数
- 最后一场必须是最终胜者赢
- 负场只能出现在前面的比赛中
- 计算前若干场负场位置组合并乘各场概率

## 公式 (`formulas`)

- 若胜者以a:b获胜，总场次a+b，最后一场胜者胜，负场b场从前a+b-1场中选

## 示例 (`examples`)

- 甲乙比赛结果2:1，甲输的1场只能在第一、二场，不能在第三场

## 易错点 (`pitfalls`)

- 把最后一场也纳入负场位置选择
- 忽略比赛提前结束

## 避免事项 (`forbidden`)

- 不要按固定打满全部场次处理几局几胜

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 赛制
- 最终比分
- 单场胜负概率
- 最终胜者

## 计算策略 (`calculation_policy`)

- mode：last_game_constraint
- allow_exact_calculation：true
- preferred_tools：
  - 位置组合
  - 独立概率相乘

## 原程序优先级 (`solver_priority`)

26

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 概率
  - 方案数
  - 选项
- must_report：最后一场胜负限制
