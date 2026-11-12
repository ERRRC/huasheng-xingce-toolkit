# 主旨/意图/标题/中心题问法路由

本卡从原知识库转换，保留全部原字段。约束和优先级是原卡记录，使用时需结合当前题意判断。

## 方法 ID (`id`)

vr_mi_question_router_001

## 模块 (`module`)

言语理解-主旨意图

## 题型 (`question_type`)

题型识别

## 子题型 (`sub_type`)

问法识别

## 方法名称 (`method_name`)

主旨/意图/标题/中心题问法路由

## 检索标签 (`tags`)

- router
- 题干触发词
- 问法

## 适用条件 (`trigger_conditions`)

- 出现“主要说明/主要介绍/主要讲述/概括最准确”
- 出现“意在说明/旨在强调/想表达”
- 出现“最适合做标题/题目”
- 出现“中心意思/核心观点”

## 不适用条件 (`anti_conditions`)

- （空列表）

## 解题步骤 (`steps`)

- 根据题干关键词归类
- 主旨概括更重整体概括
- 意图判断优先找观点或对策
- 标题填入在主旨基础上要求简洁醒目
- 中心理解按照结构重点确定中心

## 公式 (`formulas`)

- （空列表）

## 示例 (`examples`)

- （空列表）

## 易错点 (`pitfalls`)

- （空列表）

## 避免事项 (`forbidden`)

- （空列表）

## 来源文件 (`source_file`)

- 花生言语理解笔记.pdf
- 【言语理解与表达】主旨意图.pdf

## 来源页码 (`source_page`)

-
  - file：花生言语理解笔记.pdf
  - pages：
    - 4
    - 6
    - 11
    - 13
-
  - file：【言语理解与表达】主旨意图.pdf
  - pages：
    - 1

## 原卡置信度 (`confidence`)

0.92

## 来源待复核 (`need_review`)

false

## passage_structure (`passage_structure`)

- type：question_form_first
- focus_rule：问法决定输出约束，但核心仍是结构分析

## option_elimination (`option_elimination`)

-
  - type：题型错配
  - rule：标题题不能选过长、过细或不醒目的表达；意图题不能只停留在背景或例子

## 所需信息 (`required_inputs`)

- 题干问法
- 选项表述类型

## 计算策略 (`calculation_policy`)

- mode：route_then_solve
- allow_multiple_routes：true

## 原程序优先级 (`solver_priority`)

2

## 原卡输出约束 (`output_constraints`)

- route_output_must_include：question_type
