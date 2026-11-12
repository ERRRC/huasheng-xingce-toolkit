# 等差等比数列公式与性质

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_seq_001_alt

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

数学运算

## 子题型 (`sub_type`)

等差数列

## 方法名称 (`method_name`)

等差等比数列公式与性质

## 别名 (`aliases`)

- 数列求和
- 等差中项法

## 检索标签 (`tags`)

- 等差数列
- 等比数列
- 数列性质
- 平均数

## 适用条件 (`trigger_conditions`)

题目中明确提及数据构成等差数列、等比数列，或存在多个连续的数值且差值固定

## 不适用条件 (`anti_conditions`)

非规律性数列或无固定差值/比值的数列

## 所需信息 (`required_inputs`)

- 数列的首项、末项、项数或公差/公比

## 推理策略 (`reasoning_policy`)

- core_logic：利用等差数列的对称性和平均数性质，将复杂求和转化为中项计算
- detailed_policy：如果项数是奇数，优先寻找等差中项；若知道两项之和的下标关系，利用等差数列下标和性质

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：90
- fallback_method_ids：
  - qr_equation_001

## 解题步骤 (`steps`)

- 找出等差/等比关系，设定首项或某一项为基准
- 利用等差数列性质(如中项=平均数)化简方程式
- 求解未知数并代入实际问题条件中计算结果

## 公式 (`formulas`)

- an=a1+(n-1)d
- Sn=n(a1+an)/2=na1+n(n-1)d/2
- 奇数项等差数列: 平均数=等差中项=(a1+an)/2, 则Sn=n×等差中项=n×平均数
- 若m+n=k+i, 则am+an=ak+ai
- 等比数列: an=a1×q^(n-1), Sn=a1(1-q^n)/(1-q)

## 示例 (`examples`)

-
  - context：七名同学的平均成绩构成公差为1的等差数列，第七、八、九名的平均成绩既构成等差数列，又构成等比数列，张龙位列第十，与第九名相差1分
  - action：设第7名为a7，第8名a7q，第9名a7q^2。由等差数列性质推出a7=a8=a9。依次递推各名次分数。

## 易错点 (`pitfalls`)

- 混淆项数n
- 公差d的正负号错误
- 等比求和公式中1-q的位置写反

## 避免事项 (`forbidden`)

- 在未确认是等差数列的情况下直接套用中项公式

## 原卡输出约束 (`output_constraints`)

- 具体的数值结果或排名

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 5

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false
