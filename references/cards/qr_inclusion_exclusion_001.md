# 圈内圈外与人次重复关系

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_inclusion_exclusion_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

容斥问题

## 子题型 (`sub_type`)

一般容斥

## 方法名称 (`method_name`)

圈内圈外与人次重复关系

## 检索标签 (`tags`)

- 容斥
- 集合
- 至少一种
- 只参加
- 重复部分

## 适用条件 (`trigger_conditions`)

- 题干出现参加A、参加B、同时参加、至少参加一项、都不参加
- 问总人数或只参加人数

## 不适用条件 (`anti_conditions`)

- 若题干问相交部分最大/最小，优先容斥最值；若是排列概率，不走容斥

## 解题步骤 (`steps`)

- 区分圈内人数和圈外人数
- 列“全部人数-圈外人数=人次之和-重复部分”
- 必要时使用只参加一种/两种/全部参加的隐含计数公式
- 代入求解

## 公式 (`formulas`)

- 全部人数-圈外人数=人次之和-重复部分
- 圈内总人数=只参加一种+只参加两种+...+都参加

## 示例 (`examples`)

- 笔记第11页强调“只参加一次”和“都参加”等语言边界

## 易错点 (`pitfalls`)

- 把“符合A和B”误认为“只符合A和B”
- 重复部分计算次数混乱

## 避免事项 (`forbidden`)

- 不要把包含关系当互斥关系

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 6
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 11

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总人数
- 圈外人数
- 各集合人数
- 交集人数
- 是否只参加

## 计算策略 (`calculation_policy`)

- mode：diagram_or_formula
- allow_exact_calculation：true
- preferred_tools：
  - 容斥公式
  - 隐含计数

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 人数
  - 选项
- must_disambiguate：
  - 符合A和B
  - 只符合A和B
