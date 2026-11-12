# 年龄差与现实范围切入法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_age_problem_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

年龄问题

## 子题型 (`sub_type`)

年龄差不变

## 方法名称 (`method_name`)

年龄差与现实范围切入法

## 检索标签 (`tags`)

- 年龄
- 年龄差
- 同属相
- 平方数
- 代入

## 适用条件 (`trigger_conditions`)

- 题干出现年龄、几年前、几年后、岁数和、倍数、平方数、属相

## 不适用条件 (`anti_conditions`)

- 若只是普通比例方程且不涉及时间变化，可用普通方程法

## 解题步骤 (`steps`)

- 抓住年龄差不变
- 时间改变时每个人年龄增量相同
- 结合现实年龄范围筛选：爷爷奶奶多60+，父母30-40，儿女0-10
- 必要时代入选项验证

## 公式 (`formulas`)

- 年龄差恒定
- 同属相年龄差多为24岁
- 常见年龄平方数：64、36、9；45^2=2025

## 示例 (`examples`)

- 笔记第26页例题通过平方数年龄和现实范围推断外公64、母亲36

## 易错点 (`pitfalls`)

- 把年龄差当年龄和不变
- 忽略年龄必须为正整数和现实常识

## 避免事项 (`forbidden`)

- 不要在题干无年龄背景时使用现实年龄范围

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 6
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 26

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 各人物年龄关系
- 时间点
- 倍数或和差条件
- 现实身份

## 计算策略 (`calculation_policy`)

- mode：invariant_then_substitute
- allow_exact_calculation：true
- preferred_tools：
  - 年龄差不变
  - 方程法
  - 代入法

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 年龄
  - 年份差
  - 选项
- must_check：年龄为正整数
