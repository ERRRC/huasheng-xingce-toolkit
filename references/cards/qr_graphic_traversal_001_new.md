# 遍历规律

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_graphic_traversal_001_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

图形推理

## 子题型 (`sub_type`)

样式规律

## 方法名称 (`method_name`)

遍历规律

## 别名 (`aliases`)

- 缺啥补啥

## 检索标签 (`tags`)

- 形状遍历
- 数量遍历
- 位置遍历
- 偏旁遍历

## 适用条件 (`trigger_conditions`)

元素组成相似，相同元素重复出现，常见于九宫格和两组图

## 不适用条件 (`anti_conditions`)

各图元素完全独立，无重复出现

## 所需信息 (`required_inputs`)

- 每行/每组出现的元素类型

## 推理策略 (`reasoning_policy`)

- core_logic：确认特定集合的样式或元素在每一行、列或组中必须且仅完整出现一次（或特定次数），据此补齐缺失部分。
- detailed_policy：寻找外框、内部填充、位置或数量的固定组合，发现缺失项直接补全。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：88
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 形状遍历：观察外框形状是否在行列中遍历，或内部线条/阴影/空白图案是否遍历。
- 数量遍历：每种样式的图形在行列中出现的次数是否相同，或每一组图是否都有一个固定相同的元素。
- 位置遍历：相同样式的图形是否在各个预定位置都出现过一遍。
- 偏旁遍历：汉字类图形重点考虑偏旁部首的遍历。
- 综合上述特征，使用“缺啥补啥”的核心解题思维选出答案。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 未能识别出内外分开遍历
- 将数量遍历误认为简单相加

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 输出缺失的图形样式

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 74

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false
