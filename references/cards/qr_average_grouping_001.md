# 无序除堆排序，有序直接选

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_average_grouping_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

平均分堆

## 方法名称 (`method_name`)

无序除堆排序，有序直接选

## 检索标签 (`tags`)

- 平均分堆
- 分组
- 有序组
- 无序组

## 适用条件 (`trigger_conditions`)

- 题干出现平均分成若干组、分堆、派往不同城市、组之间是否不同

## 不适用条件 (`anti_conditions`)

- 若每组人数不等，不属于平均分堆；需按一般组合分配

## 解题步骤 (`steps`)

- 判断后续组是否有顺序或标签
- 无顺序平均分堆：先选各组再除以组的全排列
- 有顺序或分配到不同城市：直接按有标签组选择，不除组排列
- 概率题还需除以总情况

## 公式 (`formulas`)

- 无序平均分n堆需除以A_n^n；有序分堆不除

## 示例 (`examples`)

- 8人平均分2组：无序为C_8^4*C_4^4/A_2^2；去不同城市则C_8^4*C_4^4

## 易错点 (`pitfalls`)

- 忘记除以组之间人为顺序
- 有标签组又错误除以组排列

## 避免事项 (`forbidden`)

- 不要在组规模不相等时机械除以n!

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 1
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 23

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 总人数
- 组数
- 每组人数
- 组是否有标签/顺序
- 附加条件

## 计算策略 (`calculation_policy`)

- mode：choose_groups_then_adjust_order
- allow_exact_calculation：true
- preferred_tools：
  - 组合
  - 除以组排列

## 原程序优先级 (`solver_priority`)

12

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 分组数
  - 概率
  - 选项
- must_report：组是否有序
