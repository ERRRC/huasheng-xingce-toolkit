# 黑白块综合判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_black_white_block_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

特殊题型

## 子题型 (`sub_type`)

黑白块

## 方法名称 (`method_name`)

黑白块综合判断法

## 检索标签 (`tags`)

- 黑白块
- 面积
- 数量
- 连接
- 相邻比较
- 黑白运算

## 适用条件 (`trigger_conditions`)

- 图形主要由黑白块构成
- 黑白块在固定网格中排列
- 黑白块数量、连接或对称关系变化

## 不适用条件 (`anti_conditions`)

- 不是网格黑白块时不走此卡
- 格位相同且明显平移时先看位置平移

## 解题步骤 (`steps`)

- 先看对称性：整体或黑色/白色自身对称。
- 再看面积：黑色面积与整体面积、黑白面积关系。
- 再看数量：黑块数量是否相同，不同可看黑白差或直接数。
- 再看连接：组块个数、笔画数、连接方式。
- 最后进行相邻比较或黑白运算验证。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记黑白块页列出对称性、面积、数量、连接、相邻比较等分支。

## 易错点 (`pitfalls`)

- 黑数相同不先看平移
- 不按格位做比较
- 连接块数量和黑块数量混淆

## 避免事项 (`forbidden`)

- 禁止格位不一致时套黑白格运算

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 17
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 网格大小
- 黑白位置
- 黑块数量
- 连通块
- 对称轴

## 计算策略 (`calculation_policy`)

- mode：black_white_multi_stage
- order：
  - symmetry
  - area
  - count
  - connection
  - operation

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- must_check_same_grid_before_operation：true

## check_order (`check_order`)

- 对称
- 面积
- 数量
- 连接
- 相邻比较/运算
- 选项验证
