# 相对面排除法

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

gr_cube_opposite_faces_001

## 模块 (`module`)

判断推理-图形推理

## 题型 (`question_type`)

空间重构

## 子题型 (`sub_type`)

相对面

## 方法名称 (`method_name`)

相对面排除法

## 检索标签 (`tags`)

- 相对面
- 展开图
- 六面体
- 排除法

## 适用条件 (`trigger_conditions`)

- 正方体展开图中需要判断两个面能否相邻出现
- 选项立体同时展示若干面

## 不适用条件 (`anti_conditions`)

- 非六面体或非展开图题不用
- 两个面是否相对不确定时继续公共边验证

## 解题步骤 (`steps`)

- 在展开图中找相对面：同行/同列隔一面常为相对面；一列/一行两端也可能为相对面。
- 检查选项立体可见面中是否同时出现相对面。
- 若相对面同时出现，直接排除该选项。
- 剩余选项再做公共边或时针法验证。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- 笔记页标注“立体中相对面不能同时出现”。

## 易错点 (`pitfalls`)

- 把相邻面误判为相对面
- 只用相对面无法唯一确定却直接选

## 避免事项 (`forbidden`)

- 禁止不验证展开结构就判相对面

## 来源文件 (`source_file`)

- 花生图形推理笔记.pdf
- 【判断推理】图形推理.pdf

## 来源页码 (`source_page`)

-
  - file：花生图形推理笔记.pdf
  - pages：
    - 21
-
  - file：【判断推理】图形推理.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.9

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 展开图面编号
- 行列相对位置
- 选项可见面

## 计算策略 (`calculation_policy`)

- mode：opposite_face_elimination
- confirm_with_edge_if_not_unique：true

## 原程序优先级 (`solver_priority`)

11

## 原卡输出约束 (`output_constraints`)

- must_not_confirm_answer_by_opposite_only_unless_unique：true

## check_order (`check_order`)

- 标面
- 找相对面
- 排除同时出现
- 再验公共边
