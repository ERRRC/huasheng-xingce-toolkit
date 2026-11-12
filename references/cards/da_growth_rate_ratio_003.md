# 比值增长率公式法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

da_growth_rate_ratio_003

## 模块 (`module`)

资料分析

## 题型 (`question_type`)

增长率

## 子题型 (`sub_type`)

比值增长率

## 方法名称 (`method_name`)

比值增长率公式法

## 检索标签 (`tags`)

- 比值增长率
- 平均数增长率
- 人均增长率
- 倍数增长率
- 均前每后

## 适用条件 (`trigger_conditions`)

- 题干问平均数、人均、单位量、每...的增长率
- 题干中的指标本质是A=B/C，并分别给出分子和分母增长率
- 选项单位通常为%

## 不适用条件 (`anti_conditions`)

- 题干出现‘占...比重’且问百分点变化，应调用比重差卡片
- 分子是分母一部分且问比重变化，不属于比值增长率

## 解题步骤 (`steps`)

- 判断比值指标A=B/C，分子增长率为Rb，分母增长率为Rc
- 代入(Rb-Rc)/(1+Rc)
- 若只判断正负，比较Rb与Rc即可
- 若问平均数增长率，记住‘均前每后’：平均、每后面的量通常作分母

## 公式 (`formulas`)

- Ra = (Rb - Rc) / (1 + Rc)
- 当只判断升降：Rb > Rc则比值上升，Rb < Rc则比值下降

## 示例 (`examples`)

- 笔记比重页下方表格把比值增长率与比重差区分：选项单位为%，问法常见平均、增长率。
- ABRX例题中人均薪酬增长率用薪酬增长率减人数增长率近似判断。

## 易错点 (`pitfalls`)

- 把比值增长率误当比重差，选百分点选项
- 忘记分母1+Rc
- 平均数题中分子分母倒置

## 避免事项 (`forbidden`)

- 看到‘平均’就直接做普通增长率
- 把比重差的秒杀规则用于比值增长率

## 来源文件 (`source_file`)

- 【花生十三】资料分析思维导图.pdf
- 花生资料分析笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】资料分析思维导图.pdf
  - pages：
    - 1
    - 6
-
  - file：花生资料分析笔记.pdf
  - pages：
    - 7
    - 8
    - 9

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 分子增长率Rb
- 分母增长率Rc
- 比值指标A=B/C
- 选项单位

## 计算策略 (`calculation_policy`)

- default：先识别ABRX/分式结构，再套用对应公式；能估则估，必要时直除。
- precision：按选项差距决定估算、截位或精算
- allowed：
  - 公式法
  - 截位直除
  - 分数化估算
- avoid：
  - 未审题直接代数值
  - 把百分点当百分数
- verify：
  - 时间口径
  - 主体口径
  - 单位口径

## 原程序优先级 (`solver_priority`)

- tier：core_formula
- rank：10
- fallback_method_ids：
  - da_ratio_share_diff_005
  - da_truncate_division_001

## 原卡输出约束 (`output_constraints`)

- 输出前必须核对时间、主体、单位
- 若为选择题，优先给出最接近选项
- 结果通常输出为百分数%
- 不得把百分点变化直接当作增长率
