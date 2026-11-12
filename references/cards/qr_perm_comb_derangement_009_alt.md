# 错位排序模型

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_perm_comb_derangement_009_alt

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

排列组合与概率

## 子题型 (`sub_type`)

错位排序

## 方法名称 (`method_name`)

错位排序模型

## 别名 (`aliases`)

- 信封信纸问题
- 装错信封

## 检索标签 (`tags`)

- 都不在自己位置
- 全错
- 错排

## 适用条件 (`trigger_conditions`)

题目要求所有元素或者部分元素“全都不在原来/属于自己的位置上”

## 不适用条件 (`anti_conditions`)

位置不互相对应

## 所需信息 (`required_inputs`)

- 参与错位排序的元素个数

## 推理策略 (`reasoning_policy`)

- core_logic：记住1到6个元素的完全错位排序数分别是 0、1、2、9、44、265，直接代入即可。
- detailed_policy：如果题目要求有部分元素错位（例如5人中仅有1人回到自己公司，其他人错排），则先选出对的元素（C_n^m），然后对剩下的元素应用错位排序常数相乘。

## 计算策略 (`calculation_policy`)

- shortcuts：D1=0, D2=1, D3=2, D4=9, D5=44, D6=265

## 原程序优先级 (`solver_priority`)

- tier：shortcut
- rank：95
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 识别出需要完全错位排序的元素个数K
- 如果是部分错排，先用组合数 C_n^{n-K} 选出位置正确的元素
- 剩余的K个元素调用错排数列中对应的数字
- 两者相乘即为所求情况数

## 公式 (`formulas`)

- D_n = (n-1) * (D_{n-1} + D_{n-2})
- 常考错排数: D1=0, D2=1, D3=2, D4=9, D5=44, D6=265

## 示例 (`examples`)

-
  - context：5个参加培训的人，有且仅有1人在培训后返回原分公司
  - action：5人中选1人回自己公司C(5,1)=5，剩下4人错排是9。5×9=45种情况

## 易错点 (`pitfalls`)

- 忘记选出位置正确的元素
- 记错了错排数列的具体数值

## 避免事项 (`forbidden`)

- 在考场上试图用全排列慢慢推导错排情况

## 原卡输出约束 (`output_constraints`)

- 输出合法整数

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 4

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
