# 全变原则与常见矛盾关系

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

logic_contradiction_001_alt

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

翻译推理

## 方法名称 (`method_name`)

全变原则与常见矛盾关系

## 别名 (`aliases`)

- 矛盾法
- 找矛盾

## 检索标签 (`tags`)

- 全变原则
- 矛盾关系
- 或且非

## 适用条件 (`trigger_conditions`)

题干或选项中出现逻辑关联词（或、且、所有、有些、必然、可能）的否定或求矛盾命题时。

## 不适用条件 (`anti_conditions`)

不涉及逻辑词否定的日常推理。

## 所需信息 (`required_inputs`)

- 包含逻辑关联词的命题

## 推理策略 (`reasoning_policy`)

- core_logic：找矛盾时，将命题中的'A'变'-A'，'且'变'或'，'所有'变'有的'，'必然'变'可能'。常见矛盾关系如'所有'与'有些不'，'A->B'与'A且非B'。
- detailed_policy：分析命题结构，按照全变原则逐一替换关键词，得到矛盾命题。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：10
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 1. 识别命题中的逻辑关联词（且、或、所有、有些、可能、必然、->）。
- 2. 根据全变原则，将所有关键词替换为其对立面。
- 3. 得到矛盾命题。

## 公式 (`formulas`)

- A或B的否定 = 非A且非B
- A且B的否定 = 非A或非B
- A->B的矛盾 = A且非B

## 示例 (`examples`)

-
  - context：所有同学都是和小张同学不是
  - action：注意：'所有'与'特指不'为反对关系，可同假，不是矛盾。

## 易错点 (`pitfalls`)

- 将'所有'的矛盾误认为'所有不'，实际应为'有些不'。
- 将'反对关系'（如所有与特指不）当成'矛盾关系'。

## 避免事项 (`forbidden`)

- 随意添加或删除逻辑否定词。

## 原卡输出约束 (`output_constraints`)

- 输出正确的矛盾命题表达式或文字。

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 50

## 原卡置信度 (`confidence`)

1.0

## 来源待复核 (`need_review`)

false
