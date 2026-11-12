# 一笔画奇点规则

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_one_stroke_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

几何问题

## 子题型 (`sub_type`)

最短遍历路径

## 方法名称 (`method_name`)

一笔画奇点规则

## 检索标签 (`tags`)

- 一笔画
- 奇点
- 最短遍历
- 重复边

## 适用条件 (`trigger_conditions`)

- 题干问一笔画、遍历路线、最短走完所有边、邮递员路径

## 不适用条件 (`anti_conditions`)

- 若只问两点间最短距离，调用最短距离

## 解题步骤 (`steps`)

- 数每个点发出边数，奇数条为奇点
- 0或2个奇点可一笔画完
- 0奇点可任意点开始并回到起点；2奇点须从一个奇点到另一个奇点
- 按起点终点要求保留奇点，消去奇点需重复走过两个奇点的最短连线

## 公式 (`formulas`)

- 可一笔画条件：奇点数为0或2

## 示例 (`examples`)

- 思维导图第2页给出奇点规则和重复最短连线思路

## 易错点 (`pitfalls`)

- 奇点数错算
- 忽略题干指定起点终点
- 重复路径选择非最短

## 避免事项 (`forbidden`)

- 不要在非连通图形中直接用一笔画规则

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 2

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 图形节点和边
- 起点终点要求
- 各点度数
- 边长

## 计算策略 (`calculation_policy`)

- mode：graph_parity
- allow_exact_calculation：true
- preferred_tools：
  - 奇点计数
  - 最短重复边

## 原程序优先级 (`solver_priority`)

32

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 是否可一笔画
  - 最短路径长度
  - 选项
- must_report：奇点数量
