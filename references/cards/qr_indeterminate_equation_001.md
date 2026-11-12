# 奇偶、整除、代入、消元与赋零法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_indeterminate_equation_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

不定方程

## 子题型 (`sub_type`)

不定方程求解

## 方法名称 (`method_name`)

奇偶、整除、代入、消元与赋零法

## 检索标签 (`tags`)

- 不定方程
- 整数解
- 赋零法
- 奇偶性
- 整除

## 适用条件 (`trigger_conditions`)

- 未知数个数多于方程数量
- 题干问整数解、方案数或A+B+C总和

## 不适用条件 (`anti_conditions`)

- 若方程数量足够且能唯一解出，走普通方程；若变量非整数，整除奇偶失效

## 解题步骤 (`steps`)

- 先用奇偶、尾数、整除性质筛选
- 再用代入法或消元法缩小范围
- 若求A+B+C且和不变，可设某个未知数为0求其余未知数
- 用选项或非负性验证

## 公式 (`formulas`)

- a、b能被x整除，则a±b能被x整除
- 赋零法：求和不变时可设一个未知数为0

## 示例 (`examples`)

- 思维导图第8页列出奇偶性质、整除性质、代入法、消元法、质合性质、尾数法、赋零法

## 易错点 (`pitfalls`)

- 忘记非负整数约束
- 赋零后未验证是否符合题意范围

## 避免事项 (`forbidden`)

- 不能在求单个未知数且和不保持不变时滥用赋零法

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
    - 7

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 未知数数量
- 方程数量
- 整数/非负限制
- 是否求和
- 选项

## 计算策略 (`calculation_policy`)

- mode：properties_first
- allow_exact_calculation：true
- preferred_tools：
  - 奇偶筛选
  - 整除筛选
  - 代入消元
  - 赋零法

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 整数解
  - 方案数
  - 选项
- must_check：整数和非负限制
