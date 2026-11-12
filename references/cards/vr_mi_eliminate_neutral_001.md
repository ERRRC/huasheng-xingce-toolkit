# 太中性/未体现问题态度排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_eliminate_neutral_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

选项排除

## 子题型 (`sub_type`)

太中性选项

## 方法名称 (`method_name`)

太中性/未体现问题态度排除法

## 检索标签 (`tags`)

- 太中性
- 问题意识
- 态度

## 适用条件 (`trigger_conditions`)

- 文段指出顽疾、风险、困境、问题或负面现象
- 选项只是中性介绍话题，没有体现问题或态度

## 不适用条件 (`anti_conditions`)

- 文段是纯说明或科普，没有明显问题态度

## 解题步骤 (`steps`)

- 识别文段是否有明显问题色彩
- 若有问题，选项需体现问题、危害或对策
- 排除只介绍对象、过于平淡或主语过宽的选项
- 若文段纯说明，则不适用该规则

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

-
  - source：【言语理解与表达】主旨意图.pdf
  - page：1
  - summary：斑马线之争例中“交通出行与每个人生活息息相关”太中性，没有体现顽疾问题。
  - lesson：问题型文段的答案要体现问题或对策。

## 易错点 (`pitfalls`)

- 选看起来稳妥但态度缺失的选项
- 问题文段选成科普说明

## 避免事项 (`forbidden`)

- 问题明显时选择无问题色彩的中性项

## 来源文件 (`source_file`)

- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：problem_attitude_check
- focus_rule：问题文段答案需体现问题/危害/对策，不能过中性

## option_elimination (`option_elimination`)

-
  - type：太中性
  - rule：未体现文段问题或态度的泛泛选项排除

## 所需信息 (`required_inputs`)

- 文段问题词
- 作者态度
- 选项情感/问题色彩

## 计算策略 (`calculation_policy`)

- mode：attitude_match_check
- allow_pure_language_feel：false

## 原程序优先级 (`solver_priority`)

28

## 原卡输出约束 (`output_constraints`)

- answer_format：option_with_reason
- reason_must_include：
  - 文段结构
  - 重点句位置
  - 选项排除依据
- do_not_output：
  - 只凭语感
  - 只凭关键词硬选
