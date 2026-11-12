# 二次函数顶点与均值定理

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_extreme_function_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

最值问题

## 子题型 (`sub_type`)

函数最值

## 方法名称 (`method_name`)

二次函数顶点与均值定理

## 检索标签 (`tags`)

- 函数最值
- 二次函数
- 顶点
- 均值定理

## 适用条件 (`trigger_conditions`)

- 题干可转化为y=ax^2+bx+c或(x+a)(b-x)
- 问最大值/最小值

## 不适用条件 (`anti_conditions`)

- 若变量只能取离散整数，应在顶点附近取合法整数检验

## 解题步骤 (`steps`)

- 将题干表达式化为二次函数或乘积形式
- 二次函数用顶点x=-b/2a
- 乘积和为定值时令两因子相等取最大
- 结合整数和范围修正

## 公式 (`formulas`)

- y=ax^2+bx+c，x=-b/(2a)时取最值
- 若y=(x+a)(b-x)，当x+a=b-x时乘积最大

## 示例 (`examples`)

- y=(x+2)(8-2x)=2(x+2)(4-x)，x=1时最大为18

## 易错点 (`pitfalls`)

- 忽略定义域或整数限制
- a的正负与最大/最小判断反了

## 避免事项 (`forbidden`)

- 不要在两因子和不定时套均值定理

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 4
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 19

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 目标表达式
- 变量范围
- 变量是否整数
- 所求最大/最小

## 计算策略 (`calculation_policy`)

- mode：formula_then_domain_check
- allow_exact_calculation：true
- preferred_tools：
  - 顶点公式
  - 均值定理

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最大值
  - 最小值
  - 选项
- must_check：定义域和整数性
