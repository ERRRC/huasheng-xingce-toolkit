# 休息意味着另一人继续工作

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_work_rest_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

工程问题

## 子题型 (`sub_type`)

休息时间

## 方法名称 (`method_name`)

休息意味着另一人继续工作

## 检索标签 (`tags`)

- 工程问题
- 休息时间
- 合作
- 单独工作量

## 适用条件 (`trigger_conditions`)

- 题干给出某人休息若干时间、轮休、先工作后合作

## 不适用条件 (`anti_conditions`)

- 若所有人同时停止，不能按“另一人继续工作”处理

## 解题步骤 (`steps`)

- 先算休息时另一人的单独工作量
- 从总工作量中扣除已完成工作
- 剩余工作按合作效率完成
- 合并时间得到答案

## 公式 (`formulas`)

- 剩余工作量=总工作量-单独工作效率×休息时间

## 示例 (`examples`)

- 思维导图第5页指出“一人休息意味着另一人工作，先算单独工作量，剩余工作再两人合作”

## 易错点 (`pitfalls`)

- 把休息时间误减总时间
- 未区分谁休息谁工作

## 避免事项 (`forbidden`)

- 不要在没有继续工作者时套用该方法

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 5
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 15

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 休息者
- 继续工作者效率
- 休息时长
- 合作效率
- 总工作量

## 计算策略 (`calculation_policy`)

- mode：subtract_individual_work
- allow_exact_calculation：true
- preferred_tools：
  - 工作量拆分
  - 合作效率

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 时间
  - 工作量
  - 选项
- must_report：休息期间谁在工作
