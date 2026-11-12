# 特殊图形优先专项路由

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_special_shape_routing_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

组成判断

## 子题型 (`sub_type`)

特殊图形入口

## 方法名称 (`method_name`)

特殊图形优先专项路由

## 检索标签 (`tags`)

- 黑白块
- 汉字
- 数字
- 字母
- 专项题型

## 适用条件 (`trigger_conditions`)

- 题干主体为黑白块、汉字、数字、字母
- 图形具有强符号属性
- 常规属性数量难以解释但符号本身有规律

## 不适用条件 (`anti_conditions`)

- 图形不是符号类且元素组成清晰时不强行走专项

## 解题步骤 (`steps`)

- 识别是否为黑白块、汉字、数字或字母。
- 黑白块先看对称/面积/数量/连接/运算。
- 汉字先看结构、样式、属性、数量、特殊读音或笔顺。
- 数字和字母先看对称、曲直、开闭、面数，再看本身大小、顺序或运算。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记目录和思维导图均将黑白块、汉字、数字、字母列为特殊题型。

## 易错点 (`pitfalls`)

- 把数字/字母只当普通图形，忽略本身顺序
- 黑白块不按位置比较

## 避免事项 (`forbidden`)

- 禁止在符号题中无依据引入外部冷知识

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 2
    - 17
    - 18
    - 19
    - 20
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 符号类别
- 黑白状态
- 汉字/数字/字母本体
- 题干排列顺序

## 计算策略 (`calculation_policy`)

- mode：special_type_routing
- fallback：general_attribute_quantity

## 原程序优先级 (`solver_priority`)

7

## 原卡输出约束 (`output_constraints`)

- must_preserve_symbol_identity：true

## check_order (`check_order`)

- 黑白块
- 汉字
- 数字
- 字母
- 专项规律
- 返回总流程验证
