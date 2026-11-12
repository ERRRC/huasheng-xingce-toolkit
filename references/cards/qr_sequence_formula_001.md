# 等差、等比与递推数列公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_sequence_formula_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

数列问题

## 子题型 (`sub_type`)

基础数列

## 方法名称 (`method_name`)

等差、等比与递推数列公式

## 检索标签 (`tags`)

- 等差数列
- 等比数列
- 斐波那契
- 求和
- 归纳

## 适用条件 (`trigger_conditions`)

- 题干出现第n项、前n项和、公差、公比、递推规律
- 数字推理中呈现有规律序列

## 不适用条件 (`anti_conditions`)

- 若题干是应用题总量关系，不要仅按数列公式处理

## 解题步骤 (`steps`)

- 判断是等差、等比、递推或其他规律
- 等差先找公差和中位数
- 等比先找公比
- 递推数列先写已知项再向后递推

## 公式 (`formulas`)

- a_n=a_1+(n-1)d
- S_n=n(a_1+a_n)/2=项数×平均数
- a_n=a_1*q^(n-1)
- 1+3+...+(2n-1)=n^2

## 示例 (`examples`)

- 斐波那契：1、1、2、3、5、8、13、21、34

## 易错点 (`pitfalls`)

- 等差求和忘记项数
- 把递推数列误判为等差/等比

## 避免事项 (`forbidden`)

- 不要在规律未确认时直接套公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 7
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 4
    - 34

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 序列项
- 项数n
- 公差或公比
- 目标项或求和目标

## 计算策略 (`calculation_policy`)

- mode：pattern_first
- allow_exact_calculation：true
- preferred_tools：
  - 等差公式
  - 等比公式
  - 递推归纳

## 原程序优先级 (`solver_priority`)

24

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 数值
  - 规律说明
  - 选项
