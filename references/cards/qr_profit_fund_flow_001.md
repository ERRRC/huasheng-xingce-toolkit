# 只看应收回金额不看过程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_profit_fund_flow_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

经济利润问题

## 子题型 (`sub_type`)

资金往来

## 方法名称 (`method_name`)

只看应收回金额不看过程

## 检索标签 (`tags`)

- 资金往来
- 分账
- 收益
- 损失
- 合伙

## 适用条件 (`trigger_conditions`)

- 题干描述两人或多人垫付、收益分配、损失承担、最后应收回多少钱

## 不适用条件 (`anti_conditions`)

- 若没有资金投入和收益/损失分担关系，不走资金往来

## 解题步骤 (`steps`)

- 忽略中间转账过程
- 计算每人拿出的所有钱
- 加上应得收益，减去应承担损失
- 得到应收回金额或应补金额

## 公式 (`formulas`)

- 某人应收回的钱=拿出的所有钱+应得收益-应承担的损失

## 示例 (`examples`)

- 思维导图第5页给出该资金往来核心思路

## 易错点 (`pitfalls`)

- 被复杂转账过程干扰
- 收益和损失分摊比例混淆

## 避免事项 (`forbidden`)

- 不要逐笔模拟导致重复计算

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 各人垫付款
- 收益总额及分配规则
- 损失总额及承担规则

## 计算策略 (`calculation_policy`)

- mode：net_amount
- allow_exact_calculation：true
- preferred_tools：
  - 净额法

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 应收金额
  - 应付金额
  - 选项
- must_report：净额公式
