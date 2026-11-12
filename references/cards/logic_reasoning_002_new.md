# “两个所有”秒杀法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_reasoning_002_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

翻译推理

## 方法名称 (`method_name`)

“两个所有”秒杀法

## 别名 (`aliases`)

- 两个所有

## 检索标签 (`tags`)

- 逻辑判断
- 秒杀
- 所有

## 适用条件 (`trigger_conditions`)

题干给出三句话，且其中出现“两个所有”的情况

## 不适用条件 (`anti_conditions`)

题干中未出现“两个所有”

## 所需信息 (`required_inputs`)

- 包含“两个所有”的三句题干

## 推理策略 (`reasoning_policy`)

- core_logic：找点名那句，顺着它说，人称变所有。
- detailed_policy：在三句话中，找到具体点名的那句话。保持该句的结论不变（顺着说），然后将主语替换为“所有人”，即可得到正确选项。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 定位题干中具体点名的那一句话（如‘涛涛和龙龙是党员’）。
- 顺着它的判断说（如‘涛涛和龙龙是党员’）。
- 将主语的人称变为‘所有’（如‘所有人都是党员’）。
- 匹配符合该结论的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - context：题干：(1)所有同学是党员 (2)所有同学都不是党员 (3)涛涛和龙龙是党员
  - action：出现“两个所有”，找点名句“涛涛和龙龙是党员”。顺着说，人称变所有，得出“所有人都是党员”。

## 易错点 (`pitfalls`)

- 将判断反转（与“两个有的”混淆）

## 避免事项 (`forbidden`)

- 画文氏图浪费时间

## 原卡输出约束 (`output_constraints`)

- 输出符合秒杀结论的选项

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 61

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
