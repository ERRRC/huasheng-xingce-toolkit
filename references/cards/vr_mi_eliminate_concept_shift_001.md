# 偷换概念/主体不一致排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_concept_shift_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

偷换概念

## 方法名称 (`method_name`)

偷换概念/主体不一致排除法

## 检索标签 (`tags`)

- 偷换概念
- 主语不一致
- 主题词错位

## 适用条件 (`trigger_conditions`)

- 选项与文段使用相似词但主语、对象、关系或方向改变
- 选项主体词不是文段核心主体

## 不适用条件 (`anti_conditions`)

- 选项是中心句的同义替换且主体一致

## 解题步骤 (`steps`)

- 比对选项主语与文段主体
- 比对动作关系和修饰范围
- 发现主体、对象、关系任一改变即排除
- 保留与中心句同义且方向一致的选项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：多例分析强调主语和主题词一致，如温湿度控制、治理效能等。
  - lesson：主体词错位是主旨意图高频陷阱。

## 易错点 (`pitfalls`)

- 被近义词迷惑
- 忽略主动/被动关系方向变化

## 避免事项 (`forbidden`)

- 只看关键词相似不核对关系

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 9
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：option_subject_check
- focus_rule：选项主体、对象、逻辑关系必须与中心层一致

## option_elimination (`option_elimination`)

-
  - type：偷换概念
  - rule：主语、对象、关系或方向被替换时排除

## 所需信息 (`required_inputs`)

- 文段主体词
- 选项主体词
- 中心句关系
- 选项关系

## 计算策略 (`calculation_policy`)

- mode：semantic_relation_compare
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

21

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
