# 等价推出与逆推法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_deduction_003_alt

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

推出类

## 方法名称 (`method_name`)

等价推出与逆推法

## 别名 (`aliases`)

- 正推法
- 逆推法

## 检索标签 (`tags`)

- 等价推出
- 正推
- 逆推
- 两难推理

## 适用条件 (`trigger_conditions`)

题干给出一系列逻辑条件，要求推出结论（正推），或给出结论要求补充前提（逆推）。

## 不适用条件 (`anti_conditions`)

削弱加强类题目。

## 所需信息 (`required_inputs`)

- 逻辑条件链
- 已知事实或目标结论

## 推理策略 (`reasoning_policy`)

- core_logic：利用A->B->C的传递性进行正推。若是逆推补充前提，则从结论反推所需条件。注意比较类、原因类选项通常不是逻辑推理过程，应排除。
- detailed_policy：将题干翻译成逻辑链。寻找确定事实作为推理起点。若选项以C或-A开头（A->B->C），则推不出任何东西，直接排除。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：20
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 翻译题干条件，形成逻辑链（如 A->B->C）。
- 2. 定位确定性条件或事实。
- 3. 顺着箭头方向正推，或逆着箭头方向并取非（逆否）进行推理。
- 4. 排除'比较类'、'原因类'等非逻辑推理的无关选项。

## 公式 (`formulas`)

- A->B->C = 非C->非B->非A

## 示例 (`examples`)

-
  - context：不交流互鉴取长补短 -> 不会保持旺盛生命力，由此可推出？
  - action：直接选等价的逆否命题，或寻找相同起点的同伙选项，排除强加因果或比较的选项。

## 易错点 (`pitfalls`)

- 选择包含主观比较或原因分析的选项。
- 从逻辑链的中间节点错误推导。

## 避免事项 (`forbidden`)

- 选择'忠于箭头'之外的推理方向（即肯后或否前）。

## 原卡输出约束 (`output_constraints`)

- 输出符合逻辑链推导的必然选项。

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 51

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
