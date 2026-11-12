# 几何图形等比放缩规律

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_geometry_scaling_022_alt

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

几何问题

## 子题型 (`sub_type`)

几何等比放缩

## 方法名称 (`method_name`)

几何图形等比放缩规律

## 别名 (`aliases`)

- 相似图形
- 按比例放大

## 检索标签 (`tags`)

- 边长n倍
- 面积n平方
- 体积n立方
- 等比缩放

## 适用条件 (`trigger_conditions`)

题目描述某几何图形的边长、半径等一维尺度扩大或缩小了n倍，询问周长、面积或体积的变化倍数

## 不适用条件 (`anti_conditions`)

非相似放缩（如长方体仅长放大，宽不变）

## 所需信息 (`required_inputs`)

- 一维尺度的放缩倍数n
- 所求的特征（周长、面积、体积）

## 推理策略 (`reasoning_policy`)

- core_logic：若边长（或半径）为n倍，则周长也为n倍，面积为n²倍，体积为n³倍。
- detailed_policy：无论多么复杂的相似形状，只要是一维长度等比例放缩，直接应用次方规律求取面积或体积的放缩倍率。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 确认图形发生的是全方位的等比放缩，求出边长放缩比例 n
- 如求周长（一维），结果乘 n
- 如求面积（二维），结果乘 n²
- 如求体积/重量（三维），结果乘 n³

## 公式 (`formulas`)

- 新面积 = 旧面积 × n²
- 新体积 = 旧体积 × n³

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 将面积误乘n倍而非n平方
- 将三维的重量放缩误以为是面积放缩

## 避免事项 (`forbidden`)

- 针对非相似放大（如只放大高不变底）滥用此定律

## 原卡输出约束 (`output_constraints`)

- 输出变化倍率或新数值

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 10

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
