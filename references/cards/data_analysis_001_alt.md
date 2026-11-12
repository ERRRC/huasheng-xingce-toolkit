# 统计术语与常识基础

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

data_analysis_001_alt

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

基础知识

## 子题型 (`sub_type`)

统计术语与常识

## 方法名称 (`method_name`)

统计术语与常识基础

## 别名 (`aliases`)

- 倍数计算
- 翻番计算
- 同比环比
- 顺差逆差

## 检索标签 (`tags`)

- 统计术语
- 倍数
- 翻番
- 同比
- 环比
- 顺差
- 逆差
- 恩格尔系数
- 基尼系数

## 适用条件 (`trigger_conditions`)

题目中出现倍数、翻番、成数、同比、环比、顺差、逆差、恩格尔系数、基尼系数等统计学专业术语时

## 不适用条件 (`anti_conditions`)

常规加减乘除运算，不涉及专有术语

## 所需信息 (`required_inputs`)

- 术语名称
- 对应数值
- 比较对象

## 推理策略 (`reasoning_policy`)

- （空映射）

## 计算策略 (`calculation_policy`)

- core_method：利用公式直接转化术语为数值进行计算

## 原程序优先级 (`solver_priority`)

- tier：precheck
- rank：90
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 圈定题目中的统计术语及具体数值
- 2. 根据术语的定义或转化公式，将术语转化为常规的数学关系表述
- 3. 代入数据进行后续计算

## 公式 (`formulas`)

- 倍数 = 增长率 + 1
- 翻n番为原来的 2^n 倍
- 进出口 = 进口 + 出口
- 人口自然增长率 = 人口出生率 - 人口死亡率

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 将增加值等同于增长量
- 计算进出口时混淆顺差和逆差的定义
- 忽略人口自然增长率的单位是千分数‰

## 避免事项 (`forbidden`)

- 未理清基期和现期直接带入数据

## 原卡输出约束 (`output_constraints`)

- 得到明确的数值

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 142

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
