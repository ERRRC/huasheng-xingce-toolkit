# 逻辑判断论证题总流程

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

lj_total_flow_001

## 模块 (`module`)

判断推理-逻辑判断

## 题型 (`question_type`)

逻辑判断

## 子题型 (`sub_type`)

总流程

## 方法名称 (`method_name`)

逻辑判断论证题总流程

## 检索标签 (`tags`)

- 总流程
- 论点
- 论据
- 论证关系
- 选项验证

## 适用条件 (`trigger_conditions`)

- 题干出现观点/结论/因此/所以/由此可见/认为/推测/说明
- 问法要求加强、削弱、前提、解释、评价或推出

## 不适用条件 (`anti_conditions`)

- 纯定义判断
- 类比推理
- 图形推理
- 不含论证关系的资料计算

## 解题步骤 (`steps`)

- 第一步：判断问法，区分加强、削弱、前提假设、解释说明、评价论证、结论推出。
- 第二步：划出论点，优先看因此、所以、由此、认为、说明、推测之后的内容；无明显标志时看作者最终态度。
- 第三步：划出论据，识别题干给出的事实、数据、实验、调查、类比或条件命题。
- 第四步：判断论证方式：因果归因、比例比较、实验对比、条件翻译、一般论证、解释矛盾或推出类。
- 第五步：按题型调用对应方法卡；选项必须与主体一致、话题一致、贴合题干。
- 第六步：做力度比较，优先选择直接作用于论点或论证缺口的选项，排除无关、偷换概念、只重复题干的选项。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 支持题先找论点和断点；削弱题先找结论和论据之间的漏洞；解释题先找表面矛盾双方。

## 易错点 (`pitfalls`)

- 只看选项感觉合理但没有贴合题干主体
- 把解释说明题误做成加强题
- 把前提假设题误做成普通支持题

## 避免事项 (`forbidden`)

- 不得跳过题干论证结构直接按生活常识判断
- 不得把题干没有的因果链补充为事实

## 来源文件 (`source_file`)

- 【判断推理】支持、前提假设、比例、解释说明.pdf
- 【判断推理】质疑类.pdf
- 花生判断笔记总结.pdf

## 来源页码 (`source_page`)

-
  - file：【判断推理】支持、前提假设、比例、解释说明.pdf
  - pages：
    - 1
-
  - file：【判断推理】质疑类.pdf
  - pages：
    - 1
-
  - file：花生判断笔记总结.pdf
  - pages：
    - 3
    - 8
    - 11
    - 13

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- question_stem
- argument_text
- options
- question_type_signal

## 计算策略 (`calculation_policy`)

- mode：routing_first
- sequence：
  - 识别问法
  - 抽取论点论据
  - 匹配论证类型
  - 调用专门方法
  - 验证选项力度

## 原程序优先级 (`solver_priority`)

1

## 原卡输出约束 (`output_constraints`)

- must_output：
  - question_type
  - claim
  - evidence
  - argument_link
  - method_id
  - answer_rationale
- must_not_output：
  - 仅输出选项不解释论证结构

## argument_structure (`argument_structure`)

- claim：按问法和结论标志词定位，可能是显性结论或隐含结论。
- evidence：题干事实、实验、数据、调查、条件命题均可作论据。
- link：根据论证方式调用支持/削弱/前提/解释/推出/评价流程。

## strength_order (`strength_order`)

- 直接击中论证断点/因果链/必要条件
- 补充或否定关键事实
- 解释合理但不直接改变论证
- 主体或话题相关但力度弱
- 无关项
