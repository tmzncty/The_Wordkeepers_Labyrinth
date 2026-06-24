# The Wordkeeper's Labyrinth — Master Planning Brief

## Project Overview
An English novel that organically integrates:
- 16 years of Chinese postgraduate entrance exam English papers (2010-2025)
- 106 literary theory knowledge cards (from 纸上宇宙 spinoff8)
- 6,131 vocabulary words with definitions, phonetics, and real exam sentences
- SM-2 spaced repetition memory system as a narrative mechanic
- RPG progression system (HP, EXP, Level) as in-world game mechanics

## Source Data Summary

### Exam Papers (2010-2025)
Each year has IDENTICAL structure — 52 questions:
| Section | Type | Questions/Year | 16-Year Total |
|---------|------|----------------|---------------|
| Use of English | Cloze (4 options × 20 blanks) | 20 | 320 |
| Reading Part A | 4 passages × 5 questions | 20 | 320 |
| Reading Part B | Matching/ordering | 5 | 80 |
| Translation | EN→CN sentences | 5 | 80 |
| Writing Part A | Short writing (~100 words) | 1 | 16 |
| Writing Part B | Essay (~160 words) | 1 | 16 |
| **Total** | | **52** | **832** |

### Vocabulary (6,131 words)
| POS | Count | % |
|-----|-------|---|
| Noun | 4,062 | 66.3% |
| Adjective | 1,020 | 16.6% |
| Verb (transitive) | 607 | 9.9% |
| Verb (intransitive) | 201 | 3.3% |
| Adverb | 114 | 1.9% |
| Other (prep/conj/pron/num/int/aux/abbr) | 127 | 2.1% |

Each word has: phonetic, POS, meanings (CN), sentences from real exams with year/source.

### Knowledge Cards (106 cards)
Organized by category:

**A. Basic Literary Theory (Cards 001-015)**
001 文学四要素(Abrams), 002 文艺学三分支, 003 文学理论教程体系, 004 文学性, 005 陌生化, 006 文学本质论, 007 意境, 008 典型, 009 意象与象征, 010 叙事视角, 011 文学风格, 012 文学流派, 013 文学思潮, 014 文学体裁, 015 文学语言与日常语言

**B. Chinese Literature (Cards 016-037)**
016 诗经六义, 017 楚辞与屈原, 018 建安风骨, 019 文学自觉, 020 唐诗四期, 021 李白与杜甫, 022 宋词两大流派, 023 唐诗与宋诗, 024 元杂剧体制, 025 西厢记与窦娥冤, 026 四大名著类型学, 027 红楼梦, 028 鲁迅小说, 029 五四文学革命, 030 文学研究会与创造社, 031 茅盾与子夜, 032 沈从文与京派, 033 新感觉派, 034 先锋文学, 035 寻根文学, 036 朦胧诗, 037 新时期文学三阶段

**C. Western Literature (Cards 038-078)**
038 古希腊悲剧, 039 亚里士多德诗学, 040 荷马史诗, 041 但丁神曲, 042 骑士文学, 043 莎士比亚四大悲剧, 044 堂吉诃德, 045 十日谈, 046 古典主义三一律, 047 启蒙运动, 048 卢梭, 049 18世纪英国小说, 050 歌德浮士德, 051 狂飙突进运动, 052 浪漫主义, 053 雨果, 054 批判现实主义, 055 巴尔扎克, 056 托尔斯泰, 057 陀思妥耶夫斯基, 058 多余人形象, 059 福楼拜, 060 自然主义, 061 象征主义, 062 浪漫主义vs现实主义, 063 19世纪美国文学, 064 现代主义, 065 意识流, 066 艾略特荒原, 067 卡夫卡, 068 后现代主义, 069 存在主义, 070 荒诞派戏剧, 071 魔幻现实主义, 072 黑色幽默, 073 萨特介入文学, 074 加缪vs萨特, 075 新小说派, 076 博尔赫斯, 077 川端康成, 078 20世纪文学总特征

**D. Literary Theory & Criticism (Cards 079-106)**
079 接受美学, 080 期待视野, 081 召唤结构与隐含读者, 082 视域融合, 083 俄国形式主义, 084 结构主义叙事学, 085 热奈特五范畴, 086 故事vs话语, 087 普罗普故事形态学, 088 格雷马斯, 089 巴赫金对话理论, 090 元虚构, 091 德里达延异, 092 解构主义, 093 福柯话语理论, 094 作者之死, 095 女性主义文学批评, 096 后殖民主义, 097 文论失语症, 098 校勘四法, 099 辨伪学, 100 全书知识网络总览, 101 西方马克思主义文论, 102 芥川龙之介, 103 海明威, 104 福克纳, 105 夏目漱石, 106 文学自律与他律

### Original RPG System (from EnglishExamRPG)
- **HP**: Health points, depleted by wrong answers, restored by rest
- **EXP**: Earned per correct answer, accumulates to level up
- **Level**: 1-??, unlocks harder content
- **Mia Affection**: 0-100, affects Mia's helpfulness and dialogue
- **Daily Streak**: Consecutive days of study
- **SM-2 Algorithm**: Spaced repetition for vocabulary (ease factor, interval, next review date)

## Design Constraints
1. Language difficulty: CEFR B1-B2 for narrative prose
2. Embedded exam passages: keep original difficulty (B2-C1)
3. All 106 cards must appear in the story (can be reordered freely)
4. Vocabulary collection: tiered system (not all 6131 words appear in narrative)
5. Thought questions at chapter end: literal → inferential → evaluative
6. The novel must work as a STORY first, learning tool second
