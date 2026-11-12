# 常用代数公式与乘方尾数法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_calculation_formula_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

数论与计算

## 子题型 (`sub_type`)

基础公式

## 方法名称 (`method_name`)

常用代数公式与乘方尾数法

## 检索标签 (`tags`)

- 平方差
- 完全平方
- 立方和差
- 尾数
- 幂运算

## 适用条件 (`trigger_conditions`)

- 题干出现平方、立方、乘方、尾数、快速计算
- 选项只看末位数字或要求化简

## 不适用条件 (`anti_conditions`)

- 若题干主线是排列、行程、工程等应用题，代数公式只作辅助，不单独路由

## 解题步骤 (`steps`)

- 识别能否套平方差、完全平方、立方和差或提公因式
- 乘方尾数先保留底数个位
- 指数除以4取余，余0按4处理
- 用尾数排除选项或完成速算

## 公式 (`formulas`)

- a^2-b^2=(a+b)(a-b)
- (a+b)^2=a^2+2ab+b^2
- a^3+b^3=(a+b)(a^2-ab+b^2)
- 乘方尾数：底数留个位，指数除4留余数，整除按4

## 示例 (`examples`)

- 2016^2013尾数与6相同；2017^2014尾数与7^2相同

## 易错点 (`pitfalls`)

- 指数整除4时不能记作余0参与尾数循环，应按第4项处理
- 立方差在笔记中部分符号可能排版不清，使用时应按标准公式复核

## 避免事项 (`forbidden`)

- 不要在需要完整精算的题中只凭尾数给最终值

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

## 原卡置信度 (`confidence`)

0.86

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- 底数
- 指数
- 表达式结构
- 选项尾数或数值

## 计算策略 (`calculation_policy`)

- mode：shortcut_first
- allow_exact_calculation：true
- preferred_tools：
  - 公式展开
  - 尾数排除
  - 提取公因式

## 原程序优先级 (`solver_priority`)

35

## 原卡输出约束 (`output_constraints`)

- must_report：若使用尾数法，说明只用于排除或判断末位
- answer_type：
  - 数值
  - 选项
