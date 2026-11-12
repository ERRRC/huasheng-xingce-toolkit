# 理论最大值与实际值差值公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_chicken_rabbit_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

鸡兔同笼

## 方法名称 (`method_name`)

理论最大值与实际值差值公式

## 检索标签 (`tags`)

- 鸡兔同笼
- 对错题
- 工资报酬
- 阶梯收费

## 适用条件 (`trigger_conditions`)

- 题干中两类对象数量未知但总数或总腿数/总分明确
- 出现每个对象贡献不同

## 不适用条件 (`anti_conditions`)

- 若类别超过两类，需先转化或方程法，不直接套单一鸡兔公式

## 解题步骤 (`steps`)

- 假设都按较大贡献计算
- 计算理论最大数值与实际数值差
- 除以单个差值，得到较小贡献对象数量
- 再求另一类数量

## 公式 (`formulas`)

- 小数=(理论最大数值-实际数值)/单个差值

## 示例 (`examples`)

- 笔记第26页对错题得分例：错题次数=(85-55)/(5-(-1))=5

## 易错点 (`pitfalls`)

- 理论最大和理论最小方向反
- 单个差值漏掉负分

## 避免事项 (`forbidden`)

- 不要把“盈亏问题”误称为“一盈一余”的鸡兔题

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
    - 26

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总对象数
- 理论最大/最小贡献
- 实际总值
- 两类单个贡献差

## 计算策略 (`calculation_policy`)

- mode：assume_extreme_difference
- allow_exact_calculation：true
- preferred_tools：
  - 假设法
  - 差值法

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 数量
  - 比例
  - 选项
- must_report：假设对象和单个差值
