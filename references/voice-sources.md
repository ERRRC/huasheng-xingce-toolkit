# 讲题风格调研与来源

检索日期：2026-11-12。目标是为本方法库补充课堂表达，不增加考试科目，也不将其他仓库的完整技能并入本库。

后续已扩大到公开视频页面与自动文稿，新增结果见[公开网络口头表达线索](public-voice-evidence.md)。下文 GitHub 检索与本地资料的判断保留其原有证据范围。

## GitHub 检索结果

检索词包括“花生十三 SKILL.md”“huasheng skill 花生”“花生十三 口头禅”，并检查了下列公开文件。搜索结果覆盖有限，不代表 GitHub 上不存在其他相关项目。

| 项目与阅读入口 | 观察 | 本次处理 |
|---|---|---|
| [WangJunqing-coder/huasheng13-skill](https://github.com/WangJunqing-coder/huasheng13-skill/blob/master/SKILL.md) | 综合公考工作流，主入口侧重分类、解法和解析结构，口癖描述较少 | 对照其任务组织方式；未复制其全文或扩充本库科目 |
| [cchuanbai/huasheng13-skill](https://github.com/cchuanbai/huasheng13-skill/blob/main/SKILL.md) | 主入口与上一项目高度相似，不能当作互相独立的课堂语料证据 | 作为另一公开实现记录，不用重复内容提高证据强度 |
| [hilltahuang/gongkao-distill](https://github.com/hilltahuang/gongkao-distill) 中花生十三部分 | 侧重教学步骤，明确区分资料整理、行业通用和推断；该部分自述缺少字幕和一手讲义 | 参考其对证据边界的处理，不把教学口令标成已核验的本人原话 |

第三个项目实际查阅的文件位于 `source/公务员/行测/言语理解/花生十三/`：

- [SKILL.canonical.md](https://github.com/hilltahuang/gongkao-distill/blob/master/source/公务员/行测/言语理解/花生十三/SKILL.canonical.md)
- [03-expression-dna.md](https://github.com/hilltahuang/gongkao-distill/blob/master/source/公务员/行测/言语理解/花生十三/references/research/03-expression-dna.md)

仓库 README 提到了 publish 入口，但本次递归文件树中定位到的花生十三内容在 source 目录；本记录以实际读取文件为准。

结论：本次检查的公开主入口更适合参考方法组织，尚不足以单独证明某个口癖的频率或逐字原貌。

## 本机已有的风格整理资料

另外参考了用户本机已有的三份二手技能资料。以下标识仅用于记录来源，本 skill 不依赖这些技能安装，不随包转载其完整文本。

| 资料标识 | 实际查阅部分 | 用于本次设计的线索 |
|---|---|---|
| huasheng-ziliao-perspective | “讲解风格”“表达 DNA”，尤其口头禅、确认句式、比喻库 | 称呼、份数与生活比喻、估算时减轻精度焦虑、用省时省脑作方法选择标准 |
| huasheng-verbal-perspective | “角色扮演规则”“表达DNA” | 短句、先结论再展开、对难点设问、以文段结构引导选项分析 |
| huasheng-panduan | “讲解风格规则” | 确认语择一、互动不过量、口语化条件拆解、不确定时保留边界 |

这些资料自述依据课程文稿整理，但本次未重新查阅原始视频或逐字稿，因此只作为二手风格线索，不能据此将本项目示例标成“花生十三原话”。本地整理之间也可能同源，不能当成独立证据互相验证。

## 本项目新增内容的性质

- `teaching-voice.md` 的流程、频率建议、使用条件、示例题与示范解析均为本项目重新编写。
- 少量通用短语作为表达示例；不复刻整段课文，不将未核验的长句当作课堂引语。
- 默认减少直播刷屏、试音及重复确认；保留自然称呼和设问解释。互动强弱可随用户要求调整。
- 不照搬“有对策必选”“无条件估算”等过强说法。条件、误差与选项验证仍由原方法卡及题目事实约束。
- 本次只增强讲法，不声称提升了答题准确率或达到了与真人一致的效果。

本文件记录参考与设计判断，不改变原知识库的授权说明；完整原课及第三方技能文本未作为新增资源分发。
