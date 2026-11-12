# 排除替代路径加强法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_support_self_block_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

加强

## 子题型 (`sub_type`)

自断一臂

## 方法名称 (`method_name`)

排除替代路径加强法

## 检索标签 (`tags`)

- 支持类
- 自断一臂
- 排除漏洞
- 加强因果

## 适用条件 (`trigger_conditions`)

- 选项排除一个可能削弱论证的替代路径
- 题干论证有可替代解释或可绕开结论的漏洞

## 不适用条件 (`anti_conditions`)

- 选项只是新增背景但不排除漏洞时不适用

## 解题步骤 (`steps`)

- 找出论证依赖的路径。
- 想出会使该路径失效的替代可能。
- 检查选项是否明确排除该替代可能。
- 若排除后题干路径只能成立，支持力度较强。
- 与断点搭桥比较：本方法侧重堵漏洞，不一定连接新概念。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 烟草税例题中，排除烟草公司通过降低其他成本抵消多缴税金，迫使提高价格路径更成立。

## 易错点 (`pitfalls`)

- 排除的不是关键漏洞
- 排除后仍有多个替代路径

## 避免事项 (`forbidden`)

- 不得把与漏洞无关的限制条件当作自断一臂

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

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- claim
- proposed_path
- possible_loophole
- options

## 计算策略 (`calculation_policy`)

- mode：loophole_blocking
- verification：
  - identify_loophole
  - option_blocks_loophole

## 原程序优先级 (`solver_priority`)

23

## 原卡输出约束 (`output_constraints`)

- must_output：
  - blocked_loophole
  - strength_reason
- must_not_output：
  - 把一般限制当关键排除

## argument_structure (`argument_structure`)

- claim：题干提出某对策或因果路径会导致结果。
- evidence：已有路径存在可替代绕行。
- link：选项排除绕行路径，使论证更稳。

## strength_order (`strength_order`)

- 断点搭桥/必要条件：直接补足论据到论点的缺口，力度强
- 自断一臂/排除关键漏洞：排除最主要替代路径，力度强
- 加入论据和事实：直接增加支持事实，力度中强
- 解释说明机制：解释为什么论点可能成立，力度中等
- 举例或类比支持：支持但范围较窄，力度较弱
- 主体或话题不一致：无关
