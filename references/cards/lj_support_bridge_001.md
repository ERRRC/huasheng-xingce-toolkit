# 支持类断点搭桥法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_support_bridge_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强

## 子题型 (`sub_type`)

断点搭桥

## 方法名称 (`method_name`)

支持类断点搭桥法

## 检索标签 (`tags`)

- 支持类
- 断点搭桥
- 论证缺口

## 适用条件 (`trigger_conditions`)

- 论据与论点之间存在概念跳跃
- 题干由A现象推出B结论
- 选项连接论据概念和论点概念

## 不适用条件 (`anti_conditions`)

- 选项只是重复论点或补充无关事实时不适用

## 解题步骤 (`steps`)

- 提取论据中的关键词 A。
- 提取论点中的关键词 B。
- 判断 A 到 B 之间缺少哪一环。
- 寻找选项是否把 A 与 B 建立直接联系。
- 若能补上断点，优先于一般事实支持。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 学习机例题：拥有学习机人数最多的班成绩最好→学习机提高成绩；正确支持需补充这些学生更多利用学习机学习数学。

## 易错点 (`pitfalls`)

- 把相关性当作桥梁
- 选项只说明A更明显但没连接B

## 避免事项 (`forbidden`)

- 不得用题干外常识替代选项桥梁

## 来源文件 (`source_file`)

- 【判断推理】支持、前提假设、比例、解释说明.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】支持、前提假设、比例、解释说明.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 11

## 原卡置信度 (`confidence`)

0.97

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim_keyword
- evidence_keyword
- gap
- options

## 计算策略 (`calculation_policy`)

- mode：bridge_gap
- verification：
  - A_keyword
  - B_keyword
  - option_links_A_to_B

## 原程序优先级 (`solver_priority`)

21

## 原卡输出约束 (`output_constraints`)

- must_output：
  - gap
  - bridge_content
- must_not_output：
  - 选只加强A但不连接B的选项

## argument_structure (`argument_structure`)

- claim：A导致/支持B的结论。
- evidence：题干只给出了A与B的并列或相关事实。
- link：选项需连接A与B。

## strength_order (`strength_order`)

- 断点搭桥/必要条件：直接补足论据到论点的缺口，力度强
- 自断一臂/排除关键漏洞：排除最主要替代路径，力度强
- 加入论据和事实：直接增加支持事实，力度中强
- 解释说明机制：解释为什么论点可能成立，力度中等
- 举例或类比支持：支持但范围较窄，力度较弱
- 主体或话题不一致：无关
