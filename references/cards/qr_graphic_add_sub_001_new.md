# 加减同异规律

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_graphic_add_sub_001_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

图形推理

## 子题型 (`sub_type`)

样式规律

## 方法名称 (`method_name`)

加减同异规律

## 别名 (`aliases`)

- 去同存异
- 去异存同

## 检索标签 (`tags`)

- 叠加
- 去同存异
- 去异存同

## 适用条件 (`trigger_conditions`)

元素组成相似，存在相同线条重复出现，且图形存在两两叠加生成第三个图的特征

## 不适用条件 (`anti_conditions`)

元素组成完全不同

## 所需信息 (`required_inputs`)

- 叠加的两个基础图形
- 生成的目标图形

## 推理策略 (`reasoning_policy`)

- core_logic：通过对比两图相同及不同位置的线条保留情况，得出叠加规则，再应用到下一个推理环节。
- detailed_policy：明确是直接加减，还是去同存异（不同留下，相同去掉）或去异存同（不同去掉，相同留下）。经常需要先对图1或图2进行旋转翻转。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：87
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 加减：图形、线条之间直接相加或相减。
- 去异存同：去掉不同部分，相同部分组成第三个图。
- 去同存异：去掉相同部分，不同部分组成第三个图。
- 注意验证变体：此类规律常与旋转和翻转结合考查，即先将图1或图2进行旋转/翻转后，再执行加减同异操作。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 未考虑基础图发生过旋转翻转再叠加的情况
- 在去同存异时将部分相同线段遗漏

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 输出叠加结果

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 74

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false
