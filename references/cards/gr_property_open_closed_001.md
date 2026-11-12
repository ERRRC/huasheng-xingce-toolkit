# 开闭性判断法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_property_open_closed_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

属性规律

## 子题型 (`sub_type`)

开闭性

## 方法名称 (`method_name`)

开闭性判断法

## 检索标签 (`tags`)

- 开闭性
- 开放图形
- 封闭图形
- 半开半闭

## 适用条件 (`trigger_conditions`)

- 图形有缺口或封闭空间
- 出现0/4/6/8/9等数字、字母或类似闭合图形
- 组成元素不同且曲直无规律

## 不适用条件 (`anti_conditions`)

- 图形仅开闭变化不稳定且有更明显对称/曲直规律时后置
- 封闭面数量变化明显时转面数量

## 解题步骤 (`steps`)

- 判断每图是开放、封闭还是半开半闭。
- 看开闭状态是否分组、交替或递推。
- 若出现数字/字母，按其封闭面数量或开闭属性核对。
- 选项开闭状态必须与题干序列一致。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记开闭性页列出开放图形、封闭图形、半开半闭图形，并提示数字/字母可能触发。

## 易错点 (`pitfalls`)

- 把有阴影区域误当封闭空间
- 忽略图形缺口
- 开闭性和封闭面数量混淆

## 避免事项 (`forbidden`)

- 禁止在曲直性已有明确规律时强行只看开闭

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 8
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

- 图形是否闭合
- 缺口位置
- 封闭空间数量

## 计算策略 (`calculation_policy`)

- mode：open_closed_classification
- fallback：face_count

## 原程序优先级 (`solver_priority`)

31

## 原卡输出约束 (`output_constraints`)

- must_distinguish_state_vs_count：true

## check_order (`check_order`)

- 开放
- 封闭
- 半开半闭
- 交替/分组
- 选项验证
