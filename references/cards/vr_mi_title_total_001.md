# 标题拟定总流程卡片

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_title_total_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

标题填入

## 子题型 (`sub_type`)

标题总流程

## 方法名称 (`method_name`)

标题拟定总流程卡片

## 检索标签 (`tags`)

- 标题选择
- 标题填入
- 主旨压缩
- 简洁准确

## 适用条件 (`trigger_conditions`)

- 题干问“最适合做标题/题目的是”
- 选项多为短语或概括性表达

## 不适用条件 (`anti_conditions`)

- 文段中心尚未确定

## 解题步骤 (`steps`)

- 先按主旨意图流程确定文段中心
- 标题必须包含核心话题或主体词
- 标题要能概括观点/问题/对策，不只抓局部细节
- 排除无主题词、不准确、不醒目、范围过宽或过窄的选项
- 若出现对策型文段，标题可体现对策方向但需简洁

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：花生言语理解笔记.pdf
  - page：13
  - summary：标题拟定笔记强调标题选项要准确、醒目且匹配文段核心。
  - lesson：标题题仍先做主旨，后做标题表达筛选。

## 易错点 (`pitfalls`)

- 只选吸引眼球但不准确的标题
- 选过细例子作标题
- 标题缺核心主体词

## 避免事项 (`forbidden`)

- 跳过主旨分析直接比较标题好不好听

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 12
    - 13

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：title_selection
- focus_rule：标题=中心内容的简洁表达；先定中心，再验标题

## option_elimination (`option_elimination`)

-
  - type：标题不合格
  - rule：无关键词、太泛、太细、与文段态度不符或不够准确的标题排除

## 所需信息 (`required_inputs`)

- 题干问法
- 文段中心
- 核心主题词
- 标题选项长度与覆盖度

## 计算策略 (`calculation_policy`)

- mode：main_idea_then_title
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

4

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段中心
  - 标题覆盖度
  - 排除理由
