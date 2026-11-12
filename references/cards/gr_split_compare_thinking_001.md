# 拆分思维与对比思维卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_split_compare_thinking_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

图推总流程

## 子题型 (`sub_type`)

拆分与对比思维

## 方法名称 (`method_name`)

拆分思维与对比思维卡

## 检索标签 (`tags`)

- 拆分思维
- 对比思维
- 局部观察
- 分组分类

## 适用条件 (`trigger_conditions`)

- 整体规律不明显
- 图形由上下、内外、左右、横线、黑白、曲直等部分构成
- 分组分类题需要找相同与不同

## 不适用条件 (`anti_conditions`)

- 整体规律非常明确时不必过度拆分
- 拆分后各部分无稳定对应关系时回到总流程

## 解题步骤 (`steps`)

- 位置拆分可看上下、内外、左右或横线分开规律。
- 样式拆分可看黑白、曲直分开规律。
- 对比图形看不变部分，对比题干看相邻变化。
- 分组分类先找共性再找差异。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记解题思维页列出位置拆分、样式拆分和对比思维。

## 易错点 (`pitfalls`)

- 拆分维度过多导致自造规律
- 只看某个局部不验证全图

## 避免事项 (`forbidden`)

- 禁止拆分后只验证一幅图

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 4

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 可拆分区域
- 部分对应关系
- 相邻图变化
- 分组目标

## 计算策略 (`calculation_policy`)

- mode：decompose_then_compare
- require_stable_subpart_mapping：true

## 原程序优先级 (`solver_priority`)

25

## 原卡输出约束 (`output_constraints`)

- must_verify_all_subparts：true

## check_order (`check_order`)

- 上下/内外/左右/横线
- 黑白/曲直
- 不变部分
- 相邻变化
- 选项验证
