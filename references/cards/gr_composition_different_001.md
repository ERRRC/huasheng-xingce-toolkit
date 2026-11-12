# 组成不同优先看属性与数量

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_composition_different_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

组成判断

## 子题型 (`sub_type`)

元素组成不同

## 方法名称 (`method_name`)

组成不同优先看属性与数量

## 检索标签 (`tags`)

- 组成不同
- 属性规律
- 数量规律
- 曲直
- 对称
- 开闭
- 点线面角素

## 适用条件 (`trigger_conditions`)

- 各图元素差异较大
- 没有明显相同元素可移动或叠加
- 每图整体特征可归类

## 不适用条件 (`anti_conditions`)

- 存在明显相同元素移动时不要先数数量
- 有黑白块/汉字/数字/字母等特殊题型时先走专项

## 解题步骤 (`steps`)

- 先看属性：曲直性、对称性、开闭性。
- 属性无规律再看数量：点、线、角、面、素、笔画。
- 出现明显提示图形时优先使用提示考点，如T点、出头、田字、五角星等。
- 用候选规律反查题干所有图形与选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 解题思维页标注“元素组成不同→属性规律、数量规律”。

## 易错点 (`pitfalls`)

- 没有触发点就盲目数复杂数量
- 只数前两个图后直接选

## 避免事项 (`forbidden`)

- 禁止未验证全题就确定数量规律

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 4
    - 7
    - 8
    - 9
    - 10
    - 11
    - 12
    - 13
    - 14
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 图形整体属性
- 点线角面素可数对象
- 特殊数量提示

## 计算策略 (`calculation_policy`)

- mode：attribute_then_quantity
- allow_multiple_candidate_rules：true

## 原程序优先级 (`solver_priority`)

6

## 原卡输出约束 (`output_constraints`)

- must_test_attribute_before_deep_count：true

## check_order (`check_order`)

- 曲直
- 对称
- 开闭
- 点
- 线/笔画
- 角
- 面
- 素
- 选项验证
