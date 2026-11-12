# 记忆1-6元素错排数

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_derangement_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

错位排序

## 方法名称 (`method_name`)

记忆1-6元素错排数

## 检索标签 (`tags`)

- 错位排序
- 都不在原位置
- 信封信箱
- 错排

## 适用条件 (`trigger_conditions`)

- 题干要求每个元素都不回到原位置、信放错信箱、人员回不到本单位

## 不适用条件 (`anti_conditions`)

- 若只有部分元素不回原位，应结合组合选择和错排数

## 解题步骤 (`steps`)

- 识别错位元素个数n
- 调用记忆错排数
- 若先选择一部分错位，先组合选人再乘错排数
- 概率题除以总排列数

## 公式 (`formulas`)

- 1-6个元素错位排序数：0、1、2、9、44、265

## 示例 (`examples`)

- 4封信全放错信箱，对应4元素错排=9

## 易错点 (`pitfalls`)

- 把“至少一人回原位”与“无人回原位”混淆
- n=1错排为0

## 避免事项 (`forbidden`)

- 不要用普通全排列代替错排

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

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 错位元素数量
- 是否全部错位
- 是否有先选元素
- 总情况数

## 计算策略 (`calculation_policy`)

- mode：lookup_derangement
- allow_exact_calculation：true
- preferred_tools：
  - 错排记忆表
  - 组合选择

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 方案数
  - 概率
  - 选项
- must_report：错位元素个数
