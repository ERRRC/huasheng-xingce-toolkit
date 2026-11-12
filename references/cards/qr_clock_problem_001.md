# 时针分针追及模型

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_clock_problem_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

特殊情景应用

## 子题型 (`sub_type`)

钟表问题

## 方法名称 (`method_name`)

时针分针追及模型

## 检索标签 (`tags`)

- 钟表
- 时针
- 分针
- 夹角
- 坏表

## 适用条件 (`trigger_conditions`)

- 题干出现钟表、时针分针重合/垂直/夹角、快慢表

## 不适用条件 (`anti_conditions`)

- 若是普通时间换算无指针运动，不走钟表追及

## 解题步骤 (`steps`)

- 分针速度6°/分钟，时针速度0.5°/分钟
- 相对速度5.5°/分钟
- 按追及距离=角度差列方程
- 坏表题用坏表时间/正常时间比例换算

## 公式 (`formulas`)

- v分=6°/min，v时=0.5°/min，相对速度=5.5°/min
- 一整天分针走24圈，时针走2圈，重合22次，垂直44次

## 示例 (`examples`)

- 笔记第27页给出坏表快3分钟/小时的比例解法

## 易错点 (`pitfalls`)

- 把小时刻度30°和分钟速度6°混淆
- 整天重合次数误记为24

## 避免事项 (`forbidden`)

- 不要在已给具体指针夹角时忽略初始角度

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
    - 27

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 初始时间
- 目标夹角
- 经过时间
- 是否坏表及快慢比例

## 计算策略 (`calculation_policy`)

- mode：relative_angular_speed
- allow_exact_calculation：true
- preferred_tools：
  - 追及模型
  - 比例换算

## 原程序优先级 (`solver_priority`)

16

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 时间
  - 角度
  - 选项
- must_report：相对角速度5.5°/min
