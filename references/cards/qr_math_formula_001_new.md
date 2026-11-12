# 基础代数公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_math_formula_001_new

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

数量基础

## 子题型 (`sub_type`)

数论

## 方法名称 (`method_name`)

基础代数公式

## 别名 (`aliases`)

- 平方差
- 完全平方
- 完全立方

## 检索标签 (`tags`)

- 基础公式
- 代数
- 次幂

## 适用条件 (`trigger_conditions`)

题目涉及简单的代数式展开、多项式化简或次幂运算

## 不适用条件 (`anti_conditions`)

非代数计算的题目

## 所需信息 (`required_inputs`)

- 涉及代数公式的表达式

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：precheck
- rank：100
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 识别代数式的结构特点，判断适用的公式类别
- 代入平方差、完全平方或立方公式进行展开或因式分解
- 化简并求得结果

## 公式 (`formulas`)

- 平方差: a^2-b^2=(a+b)(a-b)
- 完全平方: (a±b)^2=a^2+b^2±2ab
- 完全立方: (a±b)^3=a^3±b^3±3a^2b+3ab^2
- 立方和差: a^3±b^3=(a±b)(a^2+b^2∓ab)
- a^m×a^n=a^(m+n); a^m÷a^n=a^(m-n); (a^m)^n=a^(mn); (a×b)^n=a^n×b^n

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 符号的正负号在展开时弄反

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 简化的代数结果

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 5

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
