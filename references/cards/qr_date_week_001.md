# 粗算修正日期差法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_date_week_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

日期星期问题

## 子题型 (`sub_type`)

天数与星期推断

## 方法名称 (`method_name`)

粗算修正日期差法

## 检索标签 (`tags`)

- 日期
- 星期
- 平年
- 闰年
- 天数计算

## 适用条件 (`trigger_conditions`)

- 题干出现几月几日到几月几日、星期几、平年闰年、工作日休息日

## 不适用条件 (`anti_conditions`)

- 若只是简单周期循环且无日期换算，优先周期余数

## 解题步骤 (`steps`)

- 先按每月30天粗算
- 对2月减天数，对大月加天数
- 最后加日期差
- 将总天数拆为整周和额外天数，推断星期或工作日

## 公式 (`formulas`)

- 平年365天=52周+1天
- 闰年366天=52周+2天
- 平年星期向后推1天，闰年向后推2天

## 示例 (`examples`)

- 平年2月1日到12月11日：300+5-2+10=313天

## 易错点 (`pitfalls`)

- 闰年判断区间错位：跨年时要看是否包含2月29日
- 额外几天放在月初/月末未按题意调整

## 避免事项 (`forbidden`)

- 不要把能被4整除但世纪年不能被400整除的年份当闰年

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
    - 13

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 起止日期
- 年份
- 是否跨年
- 已知星期
- 工作/休息规则

## 计算策略 (`calculation_policy`)

- mode：calendar_arithmetic
- allow_exact_calculation：true
- preferred_tools：
  - 粗算修正
  - 整周+余天
  - 闰年判断

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 天数
  - 星期
  - 工作日数量
  - 选项
- must_report：是否按平年/闰年处理
