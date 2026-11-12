# “两个有的”秒杀法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_reasoning_001_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

翻译推理

## 方法名称 (`method_name`)

“两个有的”秒杀法

## 别名 (`aliases`)

- 两个有的

## 检索标签 (`tags`)

- 逻辑判断
- 秒杀
- 有的

## 适用条件 (`trigger_conditions`)

题干给出三句话，且其中出现“两个有的”的情况，要求找出能保证推理成立或相关的结论

## 不适用条件 (`anti_conditions`)

题干中没有出现“两个有的”

## 所需信息 (`required_inputs`)

- 包含“两个有的”的三句题干

## 推理策略 (`reasoning_policy`)

- core_logic：找点名那句，反着它说，人称变所有。
- detailed_policy：在三句话中，找到具体点名某个人的那句话。对这句话的结论进行否定（反着说），并将主语替换为“所有人”（人称变所有），即可直接得到答案匹配项。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 定位题干中具体点名的那一句话（如‘涛涛是党员’）。
- 将该句的判断反向表述（如‘涛涛不是党员’）。
- 将主语的人称变为‘所有’（如‘所有人都不不是党员’）。
- 在选项中寻找匹配该表述的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - context：题干：(1)有的同学是党员 (2)有的同学不是党员 (3)涛涛是党员
  - action：出现“两个有的”，找点名句“涛涛是党员”。反着说：“涛涛不是党员”。人称变所有：“所有人都不不是党员”，匹配选项。

## 易错点 (`pitfalls`)

- 找错点名句
- 忘记反转判断

## 避免事项 (`forbidden`)

- 使用复杂的三段论画图法浪费时间

## 原卡输出约束 (`output_constraints`)

- 输出唯一符合秒杀结论的选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 61

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
