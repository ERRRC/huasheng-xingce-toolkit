# 词语结构匹配法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

ar_grammar_structure_001

## 模块 (`module`)

判断推理-定义判断与类比推理

## 题型 (`question_type`)

类比推理

## 子题型 (`sub_type`)

语法关系

## 方法名称 (`method_name`)

词语结构匹配法

## 检索标签 (`tags`)

- 语法关系
- 主谓
- 动宾
- 偏正
- 词语结构

## 适用条件 (`trigger_conditions`)

- 题干是短语或词组，存在主谓、动宾、偏正等结构
- 选项词义关系接近但结构不同

## 不适用条件 (`anti_conditions`)

- 题干词语不是短语结构时，不强行分析语法结构

## 解题步骤 (`steps`)

- 判断题干短语结构：主谓、动宾、偏正等。
- 判断选项短语结构是否一致。
- 结构一致后，再看词义关系是否一致。
- 若结构不一致，优先排除。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【判断推理】类比推理.pdf
  - page：1
  - summary：资料列出虎踞-龙盘为主谓，清洗衣物为动宾，漂亮的上衣为偏正。

## 易错点 (`pitfalls`)

- 把词语结构和逻辑对应关系混用。

## 避免事项 (`forbidden`)

- 不得仅因字数相同就判结构相同。

## 来源文件 (`source_file`)

- 【判断推理】类比推理.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】类比推理.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 22

## 原卡置信度 (`confidence`)

0.93

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- stem_phrase_structure
- option_phrase_structure

## 计算策略 (`calculation_policy`)

- mode：grammar_structure_match

## 原程序优先级 (`solver_priority`)

31

## 原卡输出约束 (`output_constraints`)

- must_output：
  - stem_structure
  - option_structure_match

## definition_elements (`definition_elements`)

- （空映射）

## relation_type (`relation_type`)

语法关系-词语结构

## secondary_check (`secondary_check`)

- 主谓:n.+n.
- 动宾:v.+n.
- 主宾:两词中间可加“v.”
- 偏正:两词中间可加“的/地”
- 主动/被动关系
