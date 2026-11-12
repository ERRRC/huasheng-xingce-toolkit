# 盈数亏数除以分配标准差

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_surplus_deficit_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

盈亏问题

## 方法名称 (`method_name`)

盈数亏数除以分配标准差

## 检索标签 (`tags`)

- 盈亏问题
- 分配
- 坐车
- 住宿
- 盈数
- 亏数

## 适用条件 (`trigger_conditions`)

- 题干出现多/余、少/不足、每车/每房/每人分配标准不同

## 不适用条件 (`anti_conditions`)

- 若题干是鸡兔同笼假设型贡献差，调用鸡兔公式

## 解题步骤 (`steps`)

- 识别分配对象（车、房间、人等）
- 识别盈数和亏数
- 计算分配标准差
- 对象数=(盈数+亏数)/标准差
- 再求总元素数

## 公式 (`formulas`)

- 分配对象数=(盈数+亏数)/分配标准差

## 示例 (`examples`)

- 笔记第26页坐车例：车数=(6+15)/(28-25)=7，总人数=25×7+6=181

## 易错点 (`pitfalls`)

- 把盈亏题误称为盈余题导致理解错误
- 分配标准差取错方向
- 盈数亏数符号相加/相减混乱

## 避免事项 (`forbidden`)

- 不要在没有两个分配标准时套公式

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 8
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 26

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 盈数
- 亏数
- 两个分配标准
- 所求对象或元素数

## 计算策略 (`calculation_policy`)

- mode：surplus_deficit_formula
- allow_exact_calculation：true
- preferred_tools：
  - 标准差公式

## 原程序优先级 (`solver_priority`)

14

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 对象数
  - 总人数/总物品数
  - 选项
- must_report：盈数、亏数、标准差
