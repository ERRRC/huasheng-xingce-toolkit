# 越接近圆/球极值越优

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

qr_geometry_extreme_001

## 模块 (`module`)

数量关系

## 题型 (`question_type`)

几何问题

## 子题型 (`sub_type`)

几何最值

## 方法名称 (`method_name`)

越接近圆/球极值越优

## 检索标签 (`tags`)

- 几何最值
- 周长一定
- 面积一定
- 表面积一定
- 长方体切割

## 适用条件 (`trigger_conditions`)

- 题干问面积最大/周长最小/体积最大/表面积最小/切面最大

## 不适用条件 (`anti_conditions`)

- 若只是普通面积计算，调用几何公式

## 解题步骤 (`steps`)

- 周长一定时，越接近圆面积越大；面积一定时越接近圆周长越小
- 表面积一定时越接近球体积越大；体积一定时越接近球表面积越小
- 矩形中周长一定，正方形面积最大
- 长方体切割从最长边沿侧面对角线切割，切面周长、面积最大

## 公式 (`formulas`)

- 周长一定：正方形是矩形面积最大特例

## 示例 (`examples`)

- 思维导图第2页和笔记第29页均列出几何最值性质

## 易错点 (`pitfalls`)

- 把圆/球方向反了
- 只凭视觉不检验约束条件

## 避免事项 (`forbidden`)

- 不要在约束不是周长/面积/表面积/体积固定时套此性质

## 来源文件 (`source_file`)

- 【花生十三】数量思维导图.pdf
- 花生数量关系笔记.pdf

## 来源页码 (`source_page`)

-
  - file：【花生十三】数量思维导图.pdf
  - pages：
    - 2
-
  - file：花生数量关系笔记.pdf
  - pages：
    - 29

## 原卡置信度 (`confidence`)

0.94

## 来源待复核 (`need_review`)

false

## 所需信息 (`required_inputs`)

- 固定量类型
- 候选图形
- 所求最大/最小
- 是否为矩形或长方体切割

## 计算策略 (`calculation_policy`)

- mode：property_shortcut
- allow_exact_calculation：false
- preferred_tools：
  - 最值性质
  - 候选比较

## 原程序优先级 (`solver_priority`)

18

## 原卡输出约束 (`output_constraints`)

- answer_type：
  - 图形选择
  - 最大/最小值
  - 选项
- must_report：固定量和最值方向
