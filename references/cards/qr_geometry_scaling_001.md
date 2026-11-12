# 边长、面积、体积倍数关系

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_geometry_scaling_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

几何问题

## 子题型 (`sub_type`)

等比放缩

## 方法名称 (`method_name`)

边长、面积、体积倍数关系

## 检索标签 (`tags`)

- 几何放缩
- 相似
- 比例
- 面积倍数
- 体积倍数

## 适用条件 (`trigger_conditions`)

- 题干出现边长扩大n倍、半径为n倍、相似图形、面积比、体积比

## 不适用条件 (`anti_conditions`)

- 若图形不相似，不能直接套放缩倍数

## 解题步骤 (`steps`)

- 确认图形相似或等比放缩
- 边长或半径为n倍，则周长n倍
- 面积n^2倍
- 体积n^3倍
- 按所求量换算

## 公式 (`formulas`)

- 边长/半径×n -> 周长×n，面积×n^2，体积×n^3

## 示例 (`examples`)

- 思维导图第2页和笔记第29页均强调几何等比放缩性质

## 易错点 (`pitfalls`)

- 面积比误用边长比
- 体积比误用面积比

## 避免事项 (`forbidden`)

- 不要对非相似图形套n^2或n^3

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 2
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 29

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 边长或半径比例
- 是否相似
- 所求周长/面积/体积

## 计算策略 (`calculation_policy`)

- mode：scale_ratio
- allow_exact_calculation：true
- preferred_tools：
  - 倍数换算

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 比例
  - 倍数
  - 面积/体积
  - 选项
- must_check：相似或等比放缩
