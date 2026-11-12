# 元素种类与元素个数法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_quantity_element_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

数量规律

## 子题型 (`sub_type`)

素

## 方法名称 (`method_name`)

元素种类与元素个数法

## 检索标签 (`tags`)

- 素
- 元素
- 种类
- 个数
- 生活化图形
- 黑色相连图形

## 适用条件 (`trigger_conditions`)

- 出现多个小元素
- 生活化图形或黑色相连图形
- 不同元素种类或个数明显变化

## 不适用条件 (`anti_conditions`)

- 元素之间有位置移动规律时不要只数个数
- 元素换算关系不清时不要编造等价

## 解题步骤 (`steps`)

- 先数元素种类，再数每种元素个数。
- 判断是否有元素间换算或等价关系。
- 若多个图形可分为数部分，先确定相连/分离规则。
- 用选项验证元素数量、种类或等价关系。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记素页将特征列为很多小元素、生活化图形、黑色相连彩图形，并列元素种类、数量、换算。

## 易错点 (`pitfalls`)

- 把相连元素拆错
- 把外观相似但不同的元素归为一类
- 没有依据地设换算比例

## 避免事项 (`forbidden`)

- 禁止自造元素换算关系

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 14
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.89

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 元素种类
- 元素个数
- 是否相连
- 是否存在换算提示

## 计算策略 (`calculation_policy`)

- mode：element_count_classification
- conversion_requires_evidence：true

## 原程序优先级 (`solver_priority`)

45

## 原卡输出约束 (`output_constraints`)

- must_define_element_category：true

## check_order (`check_order`)

- 数种类
- 数个数
- 是否换算
- 是否数部分
- 选项验证
