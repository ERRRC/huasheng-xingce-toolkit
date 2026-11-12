# 船速水速顺逆公式

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_stream_boat_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

行程问题

## 子题型 (`sub_type`)

流水行船

## 方法名称 (`method_name`)

船速水速顺逆公式

## 检索标签 (`tags`)

- 流水行船
- 顺水
- 逆水
- 船速
- 水速

## 适用条件 (`trigger_conditions`)

- 题干出现顺流、逆流、水速、船速、漂流

## 不适用条件 (`anti_conditions`)

- 若是普通行程无水流，不走流水公式

## 解题步骤 (`steps`)

- 将顺水速度、逆水速度分解为船速和水速
- 已知顺逆速度时求平均得到船速，半差得到水速
- 漂流速度等于水速
- 结合时间路程方程求解

## 公式 (`formulas`)

- v顺=v船+v水
- v逆=v船-v水
- v船=(v顺+v逆)/2
- v水=(v顺-v逆)/2

## 示例 (`examples`)

- 笔记第32页例题按顺逆阶段分段，只考虑有效前5分钟顺水和逆水差距

## 易错点 (`pitfalls`)

- 把漂流当船速
- 顺逆阶段时间截取错误

## 避免事项 (`forbidden`)

- 不要在水速变化时套固定水速公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 3
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 32

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 顺水速度
- 逆水速度
- 船速或水速
- 时间
- 路程

## 计算策略 (`calculation_policy`)

- mode：speed_decomposition
- allow_exact_calculation：true
- preferred_tools：
  - 顺逆公式
  - 分段计算

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 速度
  - 距离
  - 时间
  - 选项
- must_report：顺/逆/漂流速度定义
