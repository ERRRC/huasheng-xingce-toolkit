# 汉字图形规律法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_chinese_character_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

特殊题型

## 子题型 (`sub_type`)

汉字类

## 方法名称 (`method_name`)

汉字图形规律法

## 检索标签 (`tags`)

- 汉字
- 结构
- 偏旁
- 笔画
- 封闭面
- 曲直
- 对称

## 适用条件 (`trigger_conditions`)

- 题干为汉字或类汉字符号
- 汉字结构、偏旁、笔画、封闭面或读音特征明显

## 不适用条件 (`anti_conditions`)

- 汉字仅作为普通线条且有更明显图形规律时可回到通用卡
- 不得引入资料外的生僻汉字知识

## 解题步骤 (`steps`)

- 先看结构：内外、上下、左右。
- 再看样式：遍历、偏旁遍历、加减同异。
- 再看属性：对称性、曲直性、开闭性。
- 再看数量：点、线、面、部件数。
- 必要时看特殊：拼音音调、拼音字母个数、笔画顺序起笔。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记汉字页将结构、样式、属性、数量、特殊五类并列。

## 易错点 (`pitfalls`)

- 只数笔画忽略结构
- 把汉字语义当规律
- 拼音类证据不足时乱用

## 避免事项 (`forbidden`)

- 禁止用汉字含义猜规律

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 18
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.91

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 汉字本体
- 结构类型
- 偏旁/部件
- 笔画/封闭面
- 拼音信息

## 计算策略 (`calculation_policy`)

- mode：symbol_as_shape_then_language_feature
- language_features_last：true

## 原程序优先级 (`solver_priority`)

19

## 原卡输出约束 (`output_constraints`)

- must_prioritize_shape_over_semantics：true

## check_order (`check_order`)

- 结构
- 样式
- 属性
- 数量
- 特殊
- 选项验证
