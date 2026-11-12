# 图推总流程卡片

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_total_flow_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

图推总流程

## 子题型 (`sub_type`)

总观察顺序

## 方法名称 (`method_name`)

图推总流程卡片

## 检索标签 (`tags`)

- 总流程
- 观察顺序
- 图形组成
- 十五字口诀
- 优先调用

## 适用条件 (`trigger_conditions`)

- 遇到图形推理题
- 需要判断先看什么规律
- 题干没有明显单一特征时

## 不适用条件 (`anti_conditions`)

- 已经由明显特殊题型直接锁定时可进入对应专项卡片，但仍需回到总流程验证

## 解题步骤 (`steps`)

- 先识别命题形式：一组图、两组图、九宫格、分组分类、空间类。
- 再判断图形组成：元素组成相同优先位置规律；相似优先样式规律；不同优先属性规律、数量规律；特殊图形优先黑白块、汉字、数字、字母等专项。
- 按十五字口诀排查：屈臣氏整风，点线面角素，直接想位移。
- 有明显特征先做“特征图优先”，没有明显特征再从属性到数量再到位置/样式逐级验证。
- 最终必须回到选项验证：候选选项是否同时满足已发现规律，若只满足局部规律不得直接选。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 思维导图将平面类、特殊题型、空间类分列，并给出“屈臣氏整风、点线面角素、直接想位移”的总口诀。

## 易错点 (`pitfalls`)

- 只看某一个图形特征就选项
- 元素组成未判断清楚就直接数点线面
- 空间题不做选项验证

## 避免事项 (`forbidden`)

- 禁止无触发条件时跳到冷门数量规律
- 禁止只凭图形相似度猜答案

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 3
    - 4
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.96

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 题干所有图形
- 选项图形
- 题型形式
- 图形组成相同/相似/不同的初判

## 计算策略 (`calculation_policy`)

- mode：ordered_visual_screening
- first_pass：composition_and_form
- second_pass：feature_trigger
- third_pass：option_verification
- allow_guessing：false

## 原程序优先级 (`solver_priority`)

1

## 原卡输出约束 (`output_constraints`)

- must_call_first：true
- must_return_candidate_rule_before_answer：true
- must_verify_at_least_two_examples：true

## check_order (`check_order`)

- 命题形式
- 元素组成相同/相似/不同/特殊
- 属性：曲直/对称/开闭
- 数量：点/线/面/角/素/笔画
- 位置：方向/移动/旋转/翻转
- 样式：遍历/加减同异/黑白运算
- 空间：相对面/公共边/截面/三视图/拼合
- 选项验证
