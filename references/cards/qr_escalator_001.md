# 变形行船模型

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_escalator_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

上下扶梯

## 方法名称 (`method_name`)

变形行船模型

## 检索标签 (`tags`)

- 扶梯
- 电梯
- 上行
- 下行
- 级数
- 变形行船

## 适用条件 (`trigger_conditions`)

- 题干出现扶梯、自动扶梯、人走过的级数、顺行逆行

## 不适用条件 (`anti_conditions`)

- 若扶梯不运动，退化为普通行程

## 解题步骤 (`steps`)

- 将扶梯运动类比水流
- 顺行扶梯长度=(人速+扶梯速度)×顺行时间
- 逆行扶梯长度=(人速-扶梯速度)×逆行时间
- 级数也按人走过级数±扶梯运行级数处理

## 公式 (`formulas`)

- 顺行扶梯级数=人走过的级数+扶梯运行级数
- 逆行扶梯级数=人走过的级数-扶梯运行级数

## 示例 (`examples`)

- 笔记第32页标注上下扶梯本质是变形的行船问题

## 易错点 (`pitfalls`)

- 把人走过的级数当扶梯总级数
- 顺逆符号相反

## 避免事项 (`forbidden`)

- 不要在扶梯长度/级数变化时套固定级数公式

## 来源文件 (`source_file`)

- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生数量关系笔记.pdf
  - pages：
    - 32

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 人速或每分钟走级数
- 扶梯速度或运行级数
- 顺/逆时间
- 总级数

## 计算策略 (`calculation_policy`)

- mode：boat_model_transfer
- allow_exact_calculation：true
- preferred_tools：
  - 顺逆分解
  - 级数方程

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 级数
  - 速度
  - 时间
  - 选项
- must_report：类比流水行船
