# 对称展开与垂线最短

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_shortest_distance_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

几何问题

## 子题型 (`sub_type`)

最短距离

## 方法名称 (`method_name`)

对称展开与垂线最短

## 检索标签 (`tags`)

- 最短距离
- 对称点
- 展开
- 垂线

## 适用条件 (`trigger_conditions`)

- 题干问最短路径、最短距离、点到线、立体表面路径

## 不适用条件 (`anti_conditions`)

- 若问遍历所有边或一笔画，调用最短遍历路径

## 解题步骤 (`steps`)

- 两点间线段最短：必要时做对称点再连接
- 点到直线垂线最短：直接作垂线
- 立体图形跨面时先展开到同一平面
- 再用勾股或几何公式计算

## 公式 (`formulas`)

- 两点之间线段最短；点到直线垂线最短

## 示例 (`examples`)

- 思维导图第2页与笔记第29页均强调利用对称构造最短距离

## 易错点 (`pitfalls`)

- 未展开立体表面
- 对称点作错面
- 把折线路径当直线距离

## 避免事项 (`forbidden`)

- 不要在有障碍或路径限制时直接连直线

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

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 起点终点
- 所在面或直线
- 是否可展开
- 路径限制

## 计算策略 (`calculation_policy`)

- mode：geometric_construction
- allow_exact_calculation：true
- preferred_tools：
  - 对称点
  - 展开图
  - 垂线

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 距离
  - 路径
  - 选项
- must_report：构造方式
