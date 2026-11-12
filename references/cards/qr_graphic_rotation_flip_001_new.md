# 旋转与翻转规律

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_graphic_rotation_flip_001_new

## 模块 (`module`)

判断推理

## 题型 (`question_type`)

图形推理

## 子题型 (`sub_type`)

位置规律

## 方法名称 (`method_name`)

旋转与翻转规律

## 别名 (`aliases`)

- 图形旋转
- 图形翻转

## 检索标签 (`tags`)

- 顺逆时针
- 角度
- 轴对称翻转
- 中心对称翻转

## 适用条件 (`trigger_conditions`)

元素组成相同，图形存在角度偏转或镜像变化

## 不适用条件 (`anti_conditions`)

图形无明显方向性或完全对称无法识别旋转

## 所需信息 (`required_inputs`)

- 图形的方向特征

## 推理策略 (`reasoning_policy`)

- core_logic：识别图形在二维平面内的角度旋转或跨越对称轴的翻转。
- detailed_policy：旋转需确认顺逆时针和角度数列；翻转需确认横轴、竖轴或中心对称（相当于旋转180度）。注意区分整体与局部旋转，以及与其他规律叠加。

## 计算策略 (`calculation_policy`)

- （空映射）

## 原程序优先级 (`solver_priority`)

- tier：core_method
- rank：85
- fallback_method_ids：
  - （空列表）

## 解题步骤 (`steps`)

- 考察旋转：观察方向（顺/逆时针）和角度（恒定、递增/减）。注意是否为整体旋转与局部旋转结合，或旋转+元素加减。
- 考察翻转：若两图横轴对称，通常是上下翻转；若两图竖轴对称，通常是左右翻转；若两图中心对称，则是旋转180°。

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- 将翻转误判为旋转
- 未注意到局部图形独自发生旋转或翻转

## 避免事项 (`forbidden`)

- （空列表）

## 原卡输出约束 (`output_constraints`)

- 输出旋转角度/方向或翻转轴

## 来源文件 (`source_file`)

- 花生十三丨行测考点笔记.pdf

## 来源页码 (`source_page`)

- 73

## 原卡置信度 (`confidence`)

0.95

## 来源待复核 (`need_review`)

false
