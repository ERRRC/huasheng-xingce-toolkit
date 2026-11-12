# n瓶换1瓶转化为n-1个空瓶换无瓶酒

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_bottle_exchange_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

统筹规划问题

## 子题型 (`sub_type`)

空瓶换酒

## 方法名称 (`method_name`)

n瓶换1瓶转化为n-1个空瓶换无瓶酒

## 检索标签 (`tags`)

- 空瓶换酒
- 换购
- 空瓶
- 递推

## 适用条件 (`trigger_conditions`)

- 题干出现n个空瓶换1瓶酒、最多能喝多少瓶

## 不适用条件 (`anti_conditions`)

- 若换得的酒不产生新空瓶，不能用n-1转换

## 解题步骤 (`steps`)

- 把n瓶换1瓶酒转化为n-1个空瓶换1瓶无瓶酒
- 用m/(n-1)估算可多喝瓶数
- 注意是否允许借瓶或最后归还
- 加上初始瓶数得总数

## 公式 (`formulas`)

- m个空瓶最多换到m/(n-1)瓶无瓶酒

## 示例 (`examples`)

- 思维导图第5页给出该转化规则

## 易错点 (`pitfalls`)

- 忘记喝完新酒又产生空瓶
- 是否允许借瓶未判断

## 避免事项 (`forbidden`)

- 不要在不允许循环换瓶时套此公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5

## 原卡置信度 (`confidence`)

0.84

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 初始瓶数或空瓶数
- 兑换规则n换1
- 是否允许借瓶

## 计算策略 (`calculation_policy`)

- mode：conversion_formula
- allow_exact_calculation：true
- preferred_tools：
  - n-1转换
  - 整除与余数

## 原程序优先级 (`solver_priority`)

45

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 瓶数
  - 选项
- must_check：是否允许借瓶
