# 范围扩大、缩小与片面排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_scope_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

范围扩大/缩小

## 方法名称 (`method_name`)

范围扩大、缩小与片面排除法

## 检索标签 (`tags`)

- 范围扩大
- 范围缩小
- 片面
- 并列关系

## 适用条件 (`trigger_conditions`)

- 选项只覆盖文段一部分
- 选项把文段对象扩大到更大范围
- 选项把并列结构中的一项当作整体

## 不适用条件 (`anti_conditions`)

- 文段本身就是局部细节说明题

## 解题步骤 (`steps`)

- 判断文段范围和并列层次
- 检查选项是否覆盖全部核心层次
- 排除只说其一或主语范围错误的选项
- 优先选择A且B式完整概括项

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：数字电影例中只说表现层面、拍摄技术层面均为片面，整体应覆盖生产发行过程。
  - lesson：并列关系中只说一半不能选。

## 易错点 (`pitfalls`)

- 把具体类选项当精确
- 忽略多个并列分支

## 避免事项 (`forbidden`)

- 并列结构中选择单一分支选项

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 11
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：scope_check
- focus_rule：并列取整体，主旨取准确范围，不扩大不缩小

## option_elimination (`option_elimination`)

-
  - type：范围扩大/缩小
  - rule：选项范围大于或小于文段中心范围时排除
-
  - type：片面
  - rule：只覆盖并列一项时排除

## 所需信息 (`required_inputs`)

- 文段范围
- 并列层次
- 选项范围
- 选项覆盖项

## 计算策略 (`calculation_policy`)

- mode：coverage_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

22

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
