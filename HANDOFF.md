# 凯尔希交接文档 — The Wordkeeper's Labyrinth

> **交班时间**: 2026-06-25 凌晨
> **状态**: 全部规划完成，数据包就绪，可以开始写作
> **下一阶段**: 写 Ch.1，然后逐章推进，每章 commit+push

---

## 项目路径

```
C:\Users\Administrator\Documents\The_Wordkeeper's_Labyrinth\
```

## GitHub

```
仓库: https://github.com/tmzncty/The_Wordkeepers_Labyrinth
分支: master
Deploy Key: ~/.ssh/id_ed25519_wordkeeper（已配置）
```

## 核心参数

| 参数 | 值 |
|------|-----|
| 总章节数 | **50** |
| 每章词数 | **5,000+** |
| 总词数 | ~250,000 |
| Study Break | 9 个（Ch.2,6,10,14,16,20,25,31,36,44） |
| 知识卡片 | 106 张（每章 2 张，Ch.50 有 8 张） |
| 真题 | 832 题（16 年 × 52 题/年） |
| 词汇 | Tier 1 ~444 词，Tier 2 ~926 词 |
| 风格 | 英文轻小说（学院/恋爱/热血/日常），百合 |

## 角色速查

| 角色 | 身份 | 核心特征 |
|------|------|---------|
| 绯墨 Feimo | 猫娘，Bridge 院一年级 | 表慵实强、猫直觉、对感情迟钝、讨厌水 |
| Mia ミア | Spirit AI，绯墨的搭档 | Tsundere、曾经是人（数字化意识）、怕再失去搭档 |
| 绫 Aya | 人类，Mirror 院王牌 | 冷酷完美→嫉妒→尊重→喜欢→祝福 |
| 诺亚 Noir | 猫娘，Forge 院二年级 | 地下战士、前辈姐姐、有过失败的跨物种恋情 |
| 缄默 Silence | 最老教授，从不说话 | = Labyrinth 人格化，和 Mia 一起进过中文迷宫 |
| 月 Yue | 人类，Bridge 院翻译天才 | 不能做梦→意识被跨迷宫侵蚀→恢复 |
| 凯因 Cain | 人类，Weave 院学生会长 | 灰色反派——要封印 Deep Archive，理念有说服力 |
| 档案管理员 | Deep Archive 守护者 | 以吻交换秘密、给绯墨看 Mia 的人类形态 |

## 恋爱线（百合）

| 阶段 | 章节 | 好感度 |
|------|------|--------|
| 1 碰撞 | Ch.1-5 | 20→42 |
| 2 不情愿的尊重 | Ch.6-12 | 42→65 |
| 3 加深羁绊 | Ch.13-20 | 65→82 |
| 4 脆弱 | Ch.21-30 | 82→95 |
| 5 觉醒 | Ch.31-40 | 95→100（战争） |
| 6 分离 | Ch.41-45 | 98→100（Mia 切断） |
| 7 重逢告白 | Ch.46-50 | 完成 |

## 50 章结构

| Part | 章 | 年 | 主题 |
|------|-----|-----|------|
| I: Enrollment | Ch.1-12 | 2010-2012 | 入学、基础、首次 Battle、第一批 Study Break |
| II: The Houses | Ch.13-26 | 2013-2017 | 四院生活、绫、地下 Battle、锦标赛（决赛 Ch.26） |
| III: Deep Labyrinth | Ch.27-40 | 2018-2022 | 中文门、Fragmenter 入侵、Mia 过去、学院保卫战 |
| IV: Keeper's Gate | Ch.41-50 | 2023-2025 | 重建→分离→告白→Boss Rush→七门齐开→尾声 |

## 每章数据包结构

```
data/chXX/
├── outline.md          ← 章节骨架（标题、卡片、词汇、字数目标）
├── exam_cloze.md       ← 完形填空（原文+20题+选项+答案+解析）
├── exam_reading.md     ← 阅读理解 Part A + Part B
├── exam_translation.md ← 翻译 5 句
├── exam_writing.md     ← 写作题目
├── vocabulary.md       ← Tier 1 词汇（IPA 音标 + 真题例句）
├── cards.md            ← 知识卡片（摘要+绝对路径指向原文）
└── notes.md            ← 逐章独立：剧情节拍、场景预算、恋爱阶段、
                          角色出场表、Labyrinth 伏笔、专属禁忌、前后章衔接
```

## 写作协议

**每章流程**：
1. Writer 打开 `data/chXX/notes.md` → 了解本章全部要求
2. 打开 `exam_*.md` → 获取真题素材
3. 打开 `vocabulary.md` → 获取要收集的 Glyph 词汇
4. 打开 `cards.md` → 获取知识卡片内容
5. 写出 5,000+ 英文词
6. 写到 `drafts/chXX.md`（或按最终确定路径）
7. Commit + push 到 GitHub

**教学层嵌入**：真题必须自然融入叙事——Weave = 坍塌走廊修复，Mirror = 镜中倒影，Bridge = 双语铭文，Forge = 锻造原创文字

**Study Break 章**：额外包含 800 词的教学场景，Mia 用毒舌教英语

**写作禁忌（全局）**：
- ❌ 每章不超过 15 个破折号
- ❌ 不要让角色突然不符合设定
- ❌ 不要把教学写成教科书
- ❌ Mia 在 Ch.5 之前不能太软化
- ❌ 中文迷宫在 Ch.8 首次暗示，Ch.27 才正式出现

## 数据库

```
PG: 192.168.12.48, user=postgres, pass=66ccff+1, db=kaoyan_english
音标 API: https://api.dictionaryapi.dev/api/v2/entries/en/{word}（免费）
数据缓存: data/exam_2010.json ~ exam_2025.json
音标缓存: data/_global/phonetics.json（242 词）
```

## 规划参考文件

```
planning/
├── 00_master_brief.md       ← v1（原始 17 章版）
├── 00_master_brief_v2.md    ← v2（最终 50 章版）
├── 01_worldbuilding.md      ← 世界观（符玄 v2）
├── 02_chapter_outline.md    ← 50 章大纲（庄方宜 v3）
└── 03_data_tables.md        ← 数据表（白面鸮）
```

## 知识卡片原文

```
C:\Users\Administrator\Documents\纸上宇宙\drafts\spinoffs\cards\
spinoff8_card001_文学四要素.md ~ spinoff8_card106_文学自律与他律.md
```

## 下一步

**立即开始写 Ch.1**。
- 模板 Ch.1 数据包在 `data/ch01/`
- 写完后存 `drafts/ch01_the_cat_ear_girl.md`
- Commit + push
- 然后 Ch.2，以此类推

**此后每一章写完都 commit+push。**
