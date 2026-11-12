# 十五字口诀调用卡

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_mnemonic_15_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

图推总流程

## 子题型 (`sub_type`)

口诀

## 方法名称 (`method_name`)

十五字口诀调用卡

## 检索标签 (`tags`)

- 十五字口诀
- 屈臣氏整风
- 点线面角素
- 直接想位移

## 适用条件 (`trigger_conditions`)

- 需要快速遍历图推考点
- 没有明显切入点
- AI解题器需要统一搜索顺序

## 不适用条件 (`anti_conditions`)

- 已有明确专项触发时可先用专项，但答题前仍回到口诀检验是否遗漏

## 解题步骤 (`steps`)

- 屈：曲线直线；臣：对称；氏：相同相似图形；整：整体部分；风：封闭开放。
- 点线面角素用于数量观察。
- 直接想位移用于位置观察：垂直/平行、连接方式、方向、位置、平移、旋转。
- 按口诀生成候选规律，不得跳步猜答案。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 思维导图页直接给出十五字口诀及其展开。

## 易错点 (`pitfalls`)

- 背口诀但不判断组成
- 只看数量不看属性
- 位移类忘记先确认组成相同

## 避免事项 (`forbidden`)

- 禁止把口诀作为答案本身，必须落到具体规律

## 来源文件 (`source_file`)

- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 图形组成初判
- 属性特征
- 数量对象
- 位置变化

## 计算策略 (`calculation_policy`)

- mode：mnemonic_guided_screening
- order：屈臣氏整风-点线面角素-直接想位移

## 原程序优先级 (`solver_priority`)

3

## 原卡输出约束 (`output_constraints`)

- must_translate_mnemonic_to_specific_rule：true

## check_order (`check_order`)

- 屈
- 臣
- 氏
- 整
- 风
- 点线面角素
- 直接想位移
- 选项验证
