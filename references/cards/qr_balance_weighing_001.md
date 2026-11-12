# 接近3^n判断称重次数

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_balance_weighing_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

统筹规划问题

## 子题型 (`sub_type`)

天平称重

## 方法名称 (`method_name`)

接近3^n判断称重次数

## 检索标签 (`tags`)

- 天平称重
- 重球
- 轻球
- 称重次数
- 三分

## 适用条件 (`trigger_conditions`)

- 题干出现天平、找重球/轻球、最少称几次

## 不适用条件 (`anti_conditions`)

- 若不是天平称重，不调用本卡

## 解题步骤 (`steps`)

- 将候选球尽量三等分
- 每称一次最多区分三种结果：左重、右重、平衡
- 若球数最接近3^n，则需要n次称重
- 选最少称重次数

## 公式 (`formulas`)

- 可区分规模约为3^n

## 示例 (`examples`)

- 笔记第27页提示“天平称重无脑选最小选项”；思维导图第5页给出接近3^n规则

## 易错点 (`pitfalls`)

- 忽略重球/轻球已知与未知的差异
- 只看选项不验证容量

## 避免事项 (`forbidden`)

- 不要在真假币轻重未知的复杂模型中直接按3^n粗判

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 27

## 原卡置信度 (`confidence`)

0.78

## 来源待复核 (`need_review`)

true

## 所需信息 (`required_inputs`)

- 球数
- 已知重球还是轻球
- 称重次数选项
- 是否只有一个异常球

## 计算策略 (`calculation_policy`)

- mode：ternary_capacity
- allow_exact_calculation：false
- preferred_tools：
  - 三分法
  - 3^n容量判断

## 原程序优先级 (`solver_priority`)

48

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 最少次数
  - 选项
- must_report：是否只适用于已知重/轻异常球
