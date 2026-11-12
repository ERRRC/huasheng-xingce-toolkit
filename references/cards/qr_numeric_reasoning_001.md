# 差商幂修正与分组观察法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_numeric_reasoning_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

数字推理

## 子题型 (`sub_type`)

无特征数列

## 方法名称 (`method_name`)

差商幂修正与分组观察法

## 检索标签 (`tags`)

- 数字推理
- 无特征数列
- 多重数列
- 机械拆分
- 幂次数列
- 图形数列

## 适用条件 (`trigger_conditions`)

- 题干只给数字序列或图形数字
- 选项要求填缺项

## 不适用条件 (`anti_conditions`)

- 若题干有明确应用场景，如工程、行程、概率，不走数字推理

## 解题步骤 (`steps`)

- 变化较小时优先做差、做和、加法递推
- 变化较大时优先看倍数、乘法递推、幂次并修正
- 数项较多时奇偶交叉或分组观察
- 机械拆分数列按整数/小数或位数拆开
- 图形数列先看中心、对角线和行列关系

## 公式 (`formulas`)

- 常见基础：1非质非合；2是唯一偶质数；0的任何次方为0；任何数的0次方为1

## 示例 (`examples`)

- 笔记第34页给出等差/等比、质数/合数、循环、递推、机械拆分、幂次、根式和图形数列路径

## 易错点 (`pitfalls`)

- 急于套单一规律；多重数列未分组；根式未统一到根号内

## 避免事项 (`forbidden`)

- 不要为凑选项编造复杂规律，优先选择可稳定解释全序列的规律

## 来源文件 (`source_file`)

- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生数量关系笔记.pdf
  - pages：
    - 34

## 原卡置信度 (`confidence`)

0.88

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 数字序列或图形数字
- 选项
- 已知项数量

## 计算策略 (`calculation_policy`)

- mode：pattern_search
- allow_exact_calculation：false
- preferred_tools：
  - 差分
  - 倍数
  - 分组
  - 幂次修正
  - 图形关系

## 原程序优先级 (`solver_priority`)

30

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 选项
  - 缺失数字
- must_report：至少说明采用的规律类型
