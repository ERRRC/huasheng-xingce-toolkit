# 拆分与对比思维

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_graphic_split_contrast_001_alt

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

图形推理

## 子题型 (`sub_type`)

拆分与对比思维

## 方法名称 (`method_name`)

拆分与对比思维

## 别名 (`aliases`)

- 拆分法
- 对比法

## 检索标签 (`tags`)

- 位置拆分
- 样式拆分
- 对比选项

## 适用条件 (`trigger_conditions`)

图形由多个独立或可区分的部分组成，整体找不出规律时

## 不适用条件 (`anti_conditions`)

单一不可分割的简单图形

## 所需信息 (`required_inputs`)

- 图形各组成部分

## 推理策略 (`reasoning_policy`)

- core_logic：通过将复杂图形拆分为简单的上下、内外、左右或样式属性，降低寻找规律的难度；或通过对比选项和相邻图形锁定关键差异。
- detailed_policy：位置拆分找上下/内外/左右各自规律；样式拆分找横竖/黑白/曲直各自规律；对比选项找不变的部分，对比题干找相邻部分变化。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：fallback
- rank：80
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 位置拆分：将图形分为上下、内外、左右进行分别寻找规律。
- 样式拆分：将图形分为横竖、黑白、曲直部分分开看。
- 对比思维：对比选项（看哪些部分不变），对比题干（看相邻图形的差异）。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 整体观察无果时依然不愿拆分图形

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 输出拆分后的各个部分规律

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 72

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false
