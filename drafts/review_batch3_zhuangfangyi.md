# The Wordkeeper's Labyrinth — Ch.12-17 结构审核报告

**审核人**: 庄方宜 (Planner)
**审核日期**: 2026-06-25
**审核范围**: drafts/ch12-ch17 英文初稿
**参考文件**: planning/02_chapter_outline.md, data/ch12-ch17/notes.md, review_batch2_zhuangfangyi.md

---

## 总览：跨章核心发现

### 字数总览

| 章节 | 目标 | 实际 | 偏差 | 评级 |
|------|------|------|------|------|
| Ch.12 The Year's End | 5,000 | 8,178 | +64% | ❌ |
| Ch.13 Cross-House Mixer | 5,000 | 5,901 | +18% | ✅ |
| Ch.14 Architecture of Reading | 5,000 | 7,444 | +49% | ❌ |
| Ch.15 Mirror House Tour | 5,000 | 7,056 | +41% | ❌ |
| Ch.16 Cloze Deep Logic | 5,000 | 6,490 | +30% | ⚠️ |
| Ch.17 The Underground Circuit | 5,000 | 6,550 | +31% | ⚠️ |
| **合计** | **30,000** | **41,619** | **+39%** | |

六章合计超标 ~11,600 词。Ch.12 (+3,178) 和 Ch.14 (+2,444) 是重灾区，合计占超标量的 48%。

### Em-Dash 检测

| 章节 | — 数量 | 状态 |
|------|---------|------|
| Ch.11 | 2 | ✅ |
| Ch.12 | 3 | ✅ |
| Ch.13 | 2 | ✅ |
| Ch.14 | 1 | ✅ |
| Ch.15 | 0 | ✅ |
| Ch.16 | 0 | ✅ |
| Ch.17 | 4 | ✅ |

全部在 15 个限额以内。英文文风以冒号、分号、长句构建节奏，不依赖破折号。这一点比 Ch.1-11 有明显改善。

---

### P0 跨章问题

**P0-01: 真题 passage 在 Ch.13-14-15 三章连环重复，丧失嵌入新鲜感。**

这是本批最严重的结构性问题。同一篇 exam passage 在三个连续章节中反复出现：

| Passage | Ch.13 | Ch.14 | Ch.15 | 总次数 |
|---------|-------|-------|-------|--------|
| Simonsohn 决策偏差（judge sentencing bias） | L.179 引用 | L.100 主文本 | L.75+92-105 主文本 | 3次 |
| Fast Fashion / Devil Wears Prada | L.165-167 引用 | L.54+88-161 主文本 | L.127-161 主文本 | 3次 |
| "Sacred place of peace" 翻译题 | L.239+247 | — | L.191 | 2次 |
| "Gardens of the homeless" 翻译题 | L.247 | — | L.201 | 2次 |
| Behavioral tracking / advertising | — | L.232-246 | — | 1次 |

**核心问题**：Ch.13 的跨院辩论、Ch.14 的四院联合讲座、Ch.15 的 Mirror House 参观——三个场景在功能上高度重叠（都是"四院聚在一起读文本"），而且用的还是同一批 passages。读者到 Ch.15 会感觉："这篇关于快时尚的文章我已经读了三遍了。"

**建议**：
- Ch.13（辩论）保留 Aristotle/Plato 核心冲突 + Simonsohn 作为佐证
- Ch.14（讲座）替换 fast fashion 为全新 passage（建议用 2013 年真题中的新文本）
- Ch.15（Mirror House 参观）替换 Simonsohn 和 fast fashion 为 Aya 的私人阅读材料（可以用翻译题或 2013 cloze 文本）
- "Sacred place" 和 "Gardens" 翻译题保留在 Ch.15 作为 Mirror House 翻译练习即可，从 Ch.13 中删除

**P0-02: Ch.16 越权携带了 Ch.17 的知识卡片（Cards 026/027），造成结构重叠。**

大纲分配：
- Ch.16: Cards 024, 025
- Ch.17: Cards 026, 027

但实际稿件中：
- Ch.16 包含了 Cards 026（四大名著）和 027（红楼梦）的完整讲解（L.143-185, Study Break L.355-369）
- Ch.17 的 Study Break 再次重复了 Cards 026/027（L.355-369）

**效果**：Ch.16 变成了一个超级章——同时承载 cloze 教学、元杂剧知识卡片、地下格斗初见、Cain 初登场——五种内容挤进一章。Ch.17 的知识卡片则变成了重复。

**建议**：将 Cards 026/027（四大名著 + 红楼梦）从 Ch.16 移至 Ch.17。Ch.16 只保留 Cards 024/025（如未标注则需补标）。Ch.17 的 Study Break 保留 Cards 026/027 并删除对 Ch.16 cloze passage 的重复引用。

---

### P1 跨章问题

**P1-01: Cards 022/023 在 Ch.15 中未显式标注。**

大纲要求 Ch.15 包含 Cards 022 和 023。章中的唐宋词讨论（L.177-215）显然就是这些卡片的内容——"唐诗重情，宋诗重理"的区分讲得很好。但全文没有出现 "Card 022" 或 "Card 023" 的标注。学生无法确认自己在学哪张卡片。**必须补上标注。**

**P1-02: Cards 024/025 在 Ch.16 中未显式标注。**

同理。Ch.16 的 cloze 方法论内容（elimination strategy, phrasal verbs, logical connectors）应对应 Cards 024/025，但未标注。反而标注了本应属于 Ch.17 的 Cards 026/027。

**P1-03: 角色名 "Noah" vs 大纲 "Noir" 不一致。**

大纲中角色名为 **诺亚 (Noir)**。但所有六章正文中一致使用 **"Noah"**：
- Ch.12 L.31: "Noah's name was not called."
- Ch.13 L.65: "Noah was not supposed to be in the second-year library."
- Ch.15 L.43: "Her sister had declined the exchange"
- Ch.16 L.191: "Noah did not knock."
- Ch.17 L.7: "Noir said, without looking back" — 注意！**Ch.17 内部出现了混用**，L.7 用 "Noir"，L.157 之后又用 "Noir"，但 Ch.17 的 Study Break (L.387) 用 "Noir"。

**问题**：Ch.1-16 统一用 "Noah"，Ch.17 开始出现 "Noir"。需要做一个最终决定并在全部章节中统一。

**P1-04: Ch.13 L.21 元叙事穿帮。**

> "That was the last moment of Part One. This was the first morning of Part Two."

这句话是全书唯一一处直接打破第四面墙的元叙事评论。没有任何其他章节使用这种手法。在一部以沉浸式第三人称有限视角叙述的小说中，这一句会让读者瞬间跳出故事。

**建议**：删除此句。用场景过渡（新学期开学的描写）来传达 Part 转换。

**P1-05: Ch.12 字数严重超标 (+64%)。**

8,178 词 vs 5,000 目标。主要膨胀点：
- 年终典礼场景（L.1-53）：~900 词。写得好但可以更紧凑——notes 说"只需要一个瞬间"
- Mia 展示密封档案（L.147-253）：~2,500 词。这是全章核心，但关于 sealed files 的讨论过于冗长——Mia 的"I have tried 412 times"独白可以压缩 30%
- 屋顶握手场景（L.253-352）：~2,400 词。情感高潮，但后半段的"沉默-说话-沉默-说话"节奏重复了三次
- Study Break 卡片说明（L.355-386）：~800 词

**建议**：典礼场景压缩至 ~500 词（砍掉旁白和 Weave boy 的肩膀段），Mia 独白砍掉 30%，握手后半段合并重复节奏。目标：砍至 ~6,000 词。

**P1-06: Ch.14 字数严重超标 (+49%)。**

7,444 词 vs 5,000 目标。膨胀原因：
- Genette 五范畴教学（L.280-368）：~1,600 词。教授的讲解过于完整，几乎是在写教科书
- 晚间反思 + 卡片阅读（L.356-385）：~700 词。Noah 对话 + 独立卡片回顾，节奏拖沓

**建议**：Genette 部分压缩至 ~800 词（保留 Order/Duration/Mode 核心三个，Frequency 和 Voice 一笔带过）。Noah 对话保留但卡片回顾可以砍。

---

### P2 跨章问题

**P2-01: Ch.17 Study Break 重复引用 Ch.16 的 2014 考试 passages。**

Ch.17 的 Study Break (L.373-415) 逐段重新引用了 2014 cloze（brain training）、2014 Reading Text 1（unemployment）、2014 Translation（Beethoven）——这些全部已在 Ch.16 的正文中嵌入过。虽然角度是从"地下格斗"重新解读，但读者刚刚读完 Ch.16，记忆犹新。

**建议**：Ch.17 的 Study Break 应聚焦于 **本章新出现的** 素材（Cards 026/027 的深度解读 + 2014 Writing Part B "挖水"漫画的分析），而非重复 Ch.16 的 cloze passages。Noir 在 L.167 直接引用 brain training passage 的场景很好——保留那个，但 Study Break 不要再展开。

**P2-02: Ch.15 缺少正式 Study Break 部分。**

Ch.12、Ch.13、Ch.14、Ch.16、Ch.17 都有明确的 `**Study Break:**` 标注部分。Ch.15 只有 "Reflection Questions"（L.385-395），没有正式的 Study Break 和 Card 解读。

**建议**：补上 Cards 022/023 的 Study Break 部分。内容已有——唐宋诗词的区分、翻译策略——只需要显式标注和格式化。

**P2-03: 四院联合场景功能重叠。**

Ch.13（Cross-House Mixer）、Ch.14（Cross-House Lecture）、Ch.15（Mirror House Tour）三章在功能上高度相似：都是"多院学生聚在一起读文本 + 学术讨论"。连续三章的场景张力递减。

**建议**：三章的场景设计需要拉开差异性：
- Ch.13 = 政治对抗（辩论赛，输赢相关）
- Ch.14 = 学术合作（小组协作，共同解决问题）
- Ch.15 = 一对一深入（Aya 的私人教学，Mirror House 内部视角）

目前这个梯度已经存在于文本中，但由于 passages 重复，差异性被削弱了。解决 P0-01 的 passage 重复问题后，三章的差异性会自然浮现。

---

## 逐章审核

---

## Chapter 12: The Year's End

**评分: A-**

### 1. 结构完整性 (Must Hit 覆盖)

| Must Hit | 状态 | 备注 |
|----------|------|------|
| 年终典礼 | ✅ | Grand Archive Hall，有收束感 |
| "最佳进步"奖 | ✅ | L.35-53，处理得简短、尴尬、甜蜜 |
| 天台：Mia 展示密封记忆 | ✅ | L.147-203，记忆碎片快速溶解 |
| "我不知道我是谁——在成为那个之前" | ✅ | L.161 |
| 绯墨碰了 Mia 的投影手 | ✅ | L.247-261，第一次身体接触 |
| Mia 没有抽开 | ✅ | L.257: "Mia did not pull away." |
| 58→65 感情线推进 | ✅ | 握手场景 + badge 铭文的情感分量 |

**Must Hit 覆盖完整。** Notes 要求"写得重要"的第一次身体接触确实写得重要——L.253-261 的触觉描写（holographic hand, the temperature of nothing, beneath the coolness a vibration）精准且克制。

### 2. 字数

8,178 词 vs 5,000 目标。超标 64%，是全批最重。

**膨胀点**：
- L.1-53 典礼场景：~900 词。Weave boy 肩膀段（L.10-15）和 Dean 演讲的转述可以砍
- L.147-203 Mia 的 sealed files 独白：Mia 说"I have tried to read this file four hundred and twelve times"后又花了 ~800 词描述碎片细节。核心信息（file dissolves, 412 attempts, fragments of hand/window/word）可以用一半篇幅传达
- L.253-352 握手后：三轮 "silence → speak → silence → speak" 节奏。第一轮（触觉描写）和第二轮（Mia 说出 badge 铭文是自己写的）是必要的。第三轮关于 "implied reader" 的理论讨论可以移到 Ch.11 的回顾中或大幅压缩

### 3. 真题嵌入质量

| Passage | 嵌入方式 | 自然度 | 备注 |
|---------|---------|--------|------|
| "She insisted on choosing her own way" (badge) | 叙事物件 | ★★★★★ | 全章最佳嵌入——badge 铭文就是 Mia 写的 |
| Peer pressure / social cure (2012 R1) | Mia 对话引用 | ★★★★ | "The social cure doesn't work very well for very long" — 作为 Mia 吐槽 institutional belonging 的论据 |
| 2012 Translation (unification) | Feimo 内心独白 | ★★★ | L.273 引用 physics metaphor——在此情感场景中稍显刻意 |
| Card 080 (Horizon of Expectations) | Study Break | ★★★★ | 正式标注，解释清晰 |
| Card 081 (Gaps / Implied Reader) | Study Break + 叙事 | ★★★★★ | 与 Mia 的 sealed files 完美融合 |

**无 passage 重复问题。** 本章的真题嵌入是独立的。

### 4. 废话检测

| 行号范围 | 内容 | 建议 |
|----------|------|------|
| L.10-15 | Weave boy 抱怨肩膀震动 + Feimo 抓尾巴 | 可爱但 ~150 词，可压缩至 50 |
| L.17-25 | Dean 演讲转述 | 可以只保留"participants"一句触发 Feimo 回忆 |
| L.62-75 | 走廊人群 + 寻找楼梯 | 过渡段偏长 |
| L.165-170 | Mia 关于 "social cure" 的吐槽 | 保留但压缩——当前是 ~100 词的独白 |
| L.313-345 | 握手后的深夜反思 | 理论讨论（implied reader, Card 080/081 回顾）已经出现在 Study Break，正文可以砍掉 50% |

### 5. 与 Ch.11 衔接

**优秀。** Ch.11 以"Feimo pressed against the warm wall"和"Li Bai or Du Fu"的自我认知结尾。Ch.12 以年终典礼开场，Feimo 在典礼上回想"participants——The word landed differently after Ch.11"（L.21），直接引用墙读事件。衔接自然流畅。

Mia 在天台的"sealed files"告白承接了 Ch.11 中 Mia 情感裂缝的铺垫。Ch.11 的结尾是 Mia 说"you are enough"后消失；Ch.12 的天台场景是这个裂缝的进一步打开。

---

## Chapter 13: Cross-House Mixer

**评分: A**

### 1. 结构完整性 (Must Hit 覆盖)

| Must Hit | 状态 | 备注 |
|----------|------|------|
| 跨院交流会 | ✅ | Amphitheater of Accord，辩论场景 |
| 绫故意引错亚里士多德 | ✅ | L.125-141，精准的 Mirror-caliber trap |
| 绯墨纠正她 | ✅ | L.145-154，Aristotle vs Plato / catharsis vs instruction |
| Mia 小声说"干得漂亮" | ✅ | L.189-194，Glyph-channel 私频 |
| 微妙的嫉妒 | ✅ | L.201-228，Mia 的"threat level assessment"独白 |
| Aya Phase 1: Contempt | ✅ | L.157-163，"temperature of neutrality dropped two degrees" |
| 65→68 感情线 | ✅ | Mia 的嫉妒 + Feimo 的微笑 |

**覆盖完美。** Aya 的 Aristotle 误引→绯墨纠正→Aya "I stand corrected" 的三拍节奏是全批最精彩的单场景。Notes 要求"public humiliation attempt"——做到了，但不是 physical humiliation 而是 intellectual humiliation，更符合 Mirror House 的气质。

### 2. 字数

5,901 词 vs 5,000 目标。+18%，在可接受范围内。

### 3. 真题嵌入质量

| Passage | 嵌入方式 | 自然度 | 备注 |
|---------|---------|--------|------|
| Aristotle *Poetics* vs Plato *Republic* | 辩论核心 | ★★★★★ | 全书最佳 passage 嵌入——不是"考试文章"，而是"角色知识的武器化" |
| Simonsohn 决策偏差 | 辩论引用 | ★★★★ | L.179，作为佐证出现，不喧宾夺主 |
| Fast fashion / tracking | 墙壁环境文本 | ★★★ | L.165-167, 171-173，作为辩论中的环境背景出现——但此 passage 在 Ch.14/15 将被重复 |
| "Sacred place of peace" 翻译题 | 墙壁发现 | ★★★★ | L.239+247，与"homeless gardens"构成双关 |
| Gadamer Fusion of Horizons | Study Break | ★★★★ | Card 082，标注明确 |
| Russian Formalism (fabula/sjuzhet) | Yue 对话 | ★★★★★ | L.269-281，通过月的嘴自然带出 |

**P0 警告**：Simonsohn 和 fast fashion 在此章已出现，Ch.14/15 将再次使用。

### 4. 废话检测

| 行号范围 | 内容 | 建议 |
|----------|------|------|
| L.5-17 | 四院地理描写 | 好设定但 ~300 词，可以压缩 30% |
| L.243-255 | 墙壁发现 "Sacred place" + "homeless gardens" | 保留——这些翻译题是 Feimo 内省的锚点 |
| L.287-298 | Feimo 夜晚回顾 + Gadamer 理论反思 | 偏长。Card 082 的理论反思已在 Study Break 中展开，正文的 ~250 词可以砍半 |
| L.301-329 | Study Break 卡片 + 思考题 | 长度合理，但内容可以更精炼 |

### 5. 与 Ch.12 衔接

**优秀。** L.19-20 直接引用 Ch.12 的天台握手场景："On the rooftop, three weeks ago, she had touched Mia's hand." L.21 的元叙事句（"That was the last moment of Part One"）除外——这个问题已在 P1-04 中标记。

Part 转换的感觉是正确的：新学期、新场景（Mixer）、新冲突（Aya）。但从 Part I 到 Part II 的转折应该用场景描写而非打破第四面墙来传达。

---

## Chapter 14: Architecture of Reading

**评分: B+**

### 1. 结构完整性 (Must Hit 覆盖)

| Must Hit | 状态 | 备注 |
|----------|------|------|
| Study Break: Integration — Four Houses | ✅ | Cross-House Lecture，四院小组协作 |
| 68→70 感情线 | ✅ | Mia: "You are not the Bridge House cat girl anymore" (L.212) |
| 四院联合讲座教学 | ✅ | Professor Silence + Professor Tess 双教授 |

**覆盖完整。** 四人小组协作读 cloze passage 的场景（L.110-164）是本章亮点——Forge 结构分析 + Mirror 解读 + Weave 模式追踪 + Feimo 的"整合"能力，四条线交织得漂亮。

### 2. 字数

7,444 词 vs 5,000 目标。超标 49%。

**膨胀点**：
- L.222-270 Professor Tess 的 surveillance 讲座：~1,000 词。内容好但与 Professor Silence 的部分有重复感——两位教授讲的是同一个主题（reading + power）的两面
- L.280-368 Genette 五范畴 + Noah 对话 + 独自反思：~2,000 词。过于完整——Genette 的五个范畴不需要全部展开

### 3. 真题嵌入质量

| Passage | 嵌入方式 | 自然度 | 备注 |
|---------|---------|--------|------|
| Fast Fashion / Devil Wears Prada | 主教学文本 | ★★★★ | 分析精彩（L.88-161 Aya 的"indictment"分析）但 **已在 Ch.13 出现** |
| Simonsohn 决策偏差 | 第二教学文本 | ★★★ | L.100，**已在 Ch.13 出现** |
| Behavioral tracking / advertising | 第三教学文本 | ★★★★ | L.232-246，新鲜——但 Bob Liodice 的引用有点刻意 |
| Structuralist Narratology (Propp/Genette) | 教授讲解 | ★★★★ | L.280-304，教学性强但偏教科书化 |

**P0 问题**：fast fashion 和 Simonsohn 是第二次出现了。

### 4. 废话检测

| 行号范围 | 内容 | 建议 |
|----------|------|------|
| L.8-24 | Noah 关于 Cross-House Lecture 的预分析 | 好对话但 ~400 词，其中"separation is easier to manage than integration"是核心，其余可以压缩 |
| L.36-43 | Arena A 建筑描写 | 场景设定偏长 |
| L.280-308 | Genette 五范畴完整讲解 | Order/Duration/Mode 保留，Frequency/Voice 可以一句话带过 |
| L.322-353 | Noah 的事后分析 | 与 L.8-24 的预分析功能重复——前后呼应但 ~300 词可以砍半 |
| L.356-385 | Card 084/085 独自回顾 | Study Break 已涵盖，正文中的反思可以删除 |

### 5. 与 Ch.13 衔接

**良好。** Ch.13 以 Yue 的 Russian Formalism 讨论和 "Labyrinth reading aloud" 结尾。Ch.14 以四色通知开场（Cross-House Lecture），Noah 出现提供政治预判。时间线自然推进（同一学期）。

但两章在功能上太相似：Ch.13 是辩论赛，Ch.14 是联合讲座——都是"四院聚在一起"的场景。**在解决了 passage 重复问题后**，两章的差异性会更清晰：Ch.13 = 对抗，Ch.14 = 合作。

---

## Chapter 15: Mirror House Tour

**评分: B**

### 1. 结构完整性 (Must Hit 覆盖)

| Must Hit | 状态 | 备注 |
|----------|------|------|
| Mirror House 参观 | ✅ | 南中庭→阅读室→批评分析室→小隔间 |
| 绫展示阅读技巧 | ✅ | Simonsohn 分析 + fast fashion "indictment" 分析 |
| Mia 毒舌 + 关心翻版 | ✅ | L.237-249: "Your reading instincts are not the problem. Your reading discipline is." |
| Noir 透露地下战斗秘密 | ✅ | L.279-328，service corridor 对话 |
| 暗示 Noir 跨物种恋情 | ✅ | L.299-318 "A researcher from outside the Labyrinth" |
| 70→72 感情线 | ✅ | Mia 的"Aya reads four hours a day" = 隐藏的关心 |

**覆盖完整。** Aya 的阅读教学（Simonsohn 逐句分析 + fast fashion "indictment" + "hijacked" 用词分析）是本章最好的部分——L.92-165 的教学场景质量极高。Noir 的 backstory reveal（L.299-318 "a researcher from outside...she walked through"）也极好——"Not yet" 两个字比任何长篇独白都有力。

### 2. 字数

7,056 词 vs 5,000 目标。超标 41%。

**膨胀点**：
- L.1-57 开场 + 进入 Mirror House：~1,200 词。Mirror House 的建筑描写和 Mia 的 Tour Guide 模式用了太多篇幅
- L.92-165 Aya 的文本分析教学：~1,600 词。核心教学（Simonsohn 的 sequential bias + fast fashion 的 rhetorical structure）非常精彩，但与 Ch.13/Ch.14 的重叠使得读者在此处会觉得"又来了"
- L.255-381 Noah 的 service corridor 对话 + 秘密揭露：~2,800 词。Noah 的 backstory 很好，但从 Mirror House 过渡到 Noah 的地下秘密这段路太长了——中间的走廊描写、环形房间、墙壁上的古文字描写可以压缩

### 3. 真题嵌入质量

| Passage | 嵌入方式 | 自然度 | 备注 |
|---------|---------|--------|------|
| Simonsohn 决策偏差 | Aya 教学主文本 | ★★★★ | L.75+92-105，分析深度是三章中最好的——**但已是第三次出现** |
| Fast Fashion / Devil Wears Prada | Aya 教学 | ★★★★ | L.127-161，"indictment"和"hijacked"的词义分析是全批最精彩的 close reading——**但已是第三次出现** |
| "Sacred place of peace" | Aya 翻译练习 | ★★★★★ | L.191-209，翻译教学场景自然且有层次 |
| "Gardens of the homeless" | Aya 翻译练习 | ★★★★ | L.201-209，与 sacred place 构成 pair |

**核心矛盾**：Aya 的教学内容质量极高——"indictment" 的分析、"hijacked" 的修辞力量分析、sequential bias 的结构分析——这些是全批最好的 close reading 示范。但由于 Ch.13 和 Ch.14 已经用过这些 passages，读者到此处已经审美疲劳。

**如果解决 P0-01 的重复问题**，Ch.15 的真题嵌入评级将从 ⚠️ 升至 ★★★★★。Aya 的分析深度完全配得上"第一次出现"的新鲜感。

### 4. 废话检测

| 行号范围 | 内容 | 建议 |
|----------|------|------|
| L.1-57 | 镜面邀请 + 进入 Mirror House | 压缩建筑描写 |
| L.59-67 | Mirror House reading room 介绍 | "organization by argumentative structure" 是好设定，但描写可以更紧凑 |
| L.120-161 | Aya 的 fast fashion close reading | 内容精彩但与 Ch.13/14 重复——**解决 P0-01 后此段将不需砍** |
| L.265-297 | Service corridor 走路 + Noah 的"underground reading chambers"介绍 | 过渡偏长 |
| L.330-381 | 回到 Bridge House + Mia 评价 + 边界线对话 | ~1,000 词的反思段，可以压缩 40% |

### 5. 与 Ch.14 衔接

**良好。** Ch.14 以 Genette 五范畴和 "architecture of reading" 结尾。Ch.15 以 Mirror House 邀请函开场——从"看结构"到"进入结构的空间"是自然推进。

但 Ch.14 的 Cross-House Lecture 和 Ch.15 的 Mirror House Tour 在功能上重叠（都是"学术空间中的文本分析"）。Noah 在 Ch.15 后半段的 underground 信息为 Ch.16/17 做了铺垫——这部分衔接非常好。

---

## Chapter 16: Cloze Deep Logic

**评分: A-**

### 1. 结构完整性 (Must Hit 覆盖)

| Must Hit | 状态 | 备注 |
|----------|------|------|
| Study Break: Cloze Deep Logic | ✅ | Mia 的 cloze 教学，L.1-137 |
| 第一场地下战斗 | ✅ | Noah 带 Feimo 去地下，L.214-335（verbal combat） |
| Mia 战术指导 | ✅ | L.239-269，"Verbal combat" 战术 |
| "你活着就好" + "再找搭档太麻烦" | ✅ | L.309-317 |
| Cain: "Bridge House 的猫娘？有趣" | ✅ | L.373: "Bridge House's cat-girl" |
| 72→74 感情线 | ✅ | Mia: "Because finding a new partner would be too much trouble" |

**覆盖完整。** Cloze 教学场景（L.1-137）是全批最好的教学段——Mia 的"phrasal verbs are the cockroaches of English"（L.69）和"thinking in English means you can hear the sentence that isn't there"（L.59）是教学金句。地下 verbal combat（L.236-291）用 exam passages 做格斗武器的设定极具创意。

### 2. 字数

6,490 词 vs 5,000 目标。超标 30%。

**膨胀原因**：本章承载了过多内容——cloze 教学 + 元杂剧知识卡片 + 地下初见 + Cain 登场 + Beethoven 结尾。五个主要场景挤在一章里。如果将 Cards 026/027 移至 Ch.17（P0-02），可以自然减少 ~1,000 词。

### 3. 真题嵌入质量

| Passage | 嵌入方式 | 自然度 | 备注 |
|---------|---------|--------|------|
| 2014 Cloze (brain training) | Mia 教学主文本 | ★★★★★ | 逐空分析，教学方法论一流 |
| Yuan Zaju / Dou E | 知识卡片 | ★★★★ | L.143-185，Mia 的"two faces of Zaju"解读精彩——但这些是 Cards 026/027 的内容，应属 Ch.17 |
| "Losing a job is hurting" (2014 R1) | 地下 verbal combat | ★★★★★ | L.237-259，passage 被用作格斗武器——极新鲜 |
| "Osborneland" / dependency | 地下 verbal combat | ★★★★ | L.251-263，straw man 识别 |
| "Jobseeker's allowance" | 地下 verbal combat | ★★★★★ | L.263-273，language constructs reality |
| Beethoven quote | 地下 Labyrinth 奖励 | ★★★★★ | L.279-287: "Suffering is inevitable, but the courage to fight it renders life worth living" — 全书最佳 passage reveal |
| 2014 Writing (digging for water) | 间接引用 | ★★★★ | 尚未在正文出现——留给了 Ch.17 Study Break |

**这是本批真题嵌入最好的章节。** 地下 verbal combat 的设定让 exam passages 不再是"阅读材料"而是"武器"——这个创意值得保留在后续章节中。

### 4. 废话检测

| 行号范围 | 内容 | 建议 |
|----------|------|------|
| L.143-185 | 元杂剧知识卡片 | 移至 Ch.17 可同时解决字数和结构问题 |
| L.339-381 | Cain 登场 + Mia 警告 | 保留——这是全书第一次 Cain 正式出场 |
| L.385-425 | 夜晚宿舍反思 + Mia 说晚安 | 与 L.309-317 的"你活着就好"情感 beat 有重叠 |

### 5. 与 Ch.15 衔接

**良好但有跳跃。** Ch.15 以 Noah 的"underground reading chambers"铺垫和"she left...Not yet"结尾。Ch.16 以 cloze 学习开场，然后 Noah 带 Feimo 去地下。从 Mirror House Tour 到 cloze 学习的过渡需要一个时间跳跃标记（"几天后"之类的）。

Noah 在 Ch.15 说的"the underground teaches reading as a survival skill"在 Ch.16 得到了直接呼应——verbal combat 场景就是这个理念的具象化。衔接做得好。

---

## Chapter 17: The Underground Circuit

**评分: A**

### 1. 结构完整性 (Must Hit 覆盖)

| Must Hit | 状态 | 备注 |
|----------|------|------|
| 地下赛场深挖 | ✅ | 三场战斗：Kael (Weave containment), Petra (Forge offense), Sable (endurance) |
| 诺亚："我以前认识一个人。和你很像" | ✅ | L.201-213，"You remind me of him...not in the ways that matter. In the ways that worry me." |
| 74→76 感情线 | ✅ | Mia: "Whether you were coming back" (L.255) |
| Cards 026/027 | ✅ | Study Break 中标注（但应是唯一出现处） |

**覆盖完整。** 三场战斗的递进设计极好——Kael（结构，Feimo 用耳朵赢）→ Petra（暴力，Feimo 闭眼赢）→ Sable（经验，Feimo 输了）——每一战教一个不同的 lesson。Noir 的"You remind me of him"（L.213）是全批最好的角色对话之一。

### 2. 字数

6,550 词 vs 5,000 目标。超标 31%。

如果将 Study Break 中对 Ch.16 passages 的重复引用删减（P2-01），可以减少 ~500 词。三场战斗本身不需要压缩——节奏很好。

### 3. 真题嵌入质量

| Passage | 嵌入方式 | 自然度 | 备注 |
|---------|---------|--------|------|
| 2014 Cloze (brain training) | Noir 引用 | ★★★★★ | L.167，Noir 在 Feimo 输了之后引用——"effort and practice" 不是说教而是经验之谈 |
| Cards 026/027 (四大名著) | 战后反思 | ★★★★ | L.301-311，Feimo 用四大名著给三个对手分类——Water Margin / Journey to the West / Dream of the Red Chamber |
| Dream of the Red Chamber | 与 Mia 的关系隐喻 | ★★★★★ | L.313-315: "a love story...longer, sadder, more honest about what it costs" |
| "Suffering is inevitable..." | 心理回响 | ★★★★ | L.167 通过 Noir 间接引用——与 Ch.16 的 Beethoven reveal 呼应 |

**Study Break 部分的 passage 重复问题**（P2-01）：L.373-415 逐段重新引用了 2014 cloze/R1/Translation/Writing——这些已在 Ch.16 展开过。建议 Study Break 聚焦于本章新内容。

### 4. 废话检测

本章废话极少。全章节奏紧凑，三场战斗+Noir backstory+Mia 等待，每段都有叙事功能。

| 行号范围 | 内容 | 建议 |
|----------|------|------|
| L.337-370 | Study Break: Cards 026/027 | 保留——这是 Cards 的正式标注位置 |
| L.373-415 | Exam Integration 回顾 | **与 Ch.16 重复**——建议替换为本章独有的 2014 Writing "digging for water" 深度分析 |

### 5. 与 Ch.16 衔接

**优秀。** Ch.16 以 verbal combat（Labyrinth 引用 exam passages 做格斗）结尾。Ch.17 以 physical combat（actual Glyph fights）开场。从"语言格斗"到"实体格斗"的升级是自然的叙事推进。

Mia 在 Ch.16 说 "Because finding a new partner would be too much trouble"；在 Ch.17 她等在走廊说 "Whether you were coming back"——感情线从防御性的伪装升级到暴露性的真实。这个弧线做得极好。

Noir 的 backstory（L.201-213 "someone from outside the Labyrinth"）呼应了 Ch.15 中 Noah 的暗示（L.299-318 "a researcher...she walked through"）。同一个故事在两章中逐渐展开——这是好的长篇叙事手法。

---

## 汇总：评分与优先级

| 章节 | 评分 | P0 | P1 | P2 | 核心优势 | 核心问题 |
|------|------|----|----|-----|---------|---------|
| Ch.12 | A- | 0 | 1 | 0 | Mia 天台告白 + 握手 = 全系列感情线巅峰 | 字数 +64% |
| Ch.13 | A | 1 | 1 | 0 | Aristotle 陷阱 + 绯墨纠正 = 全批最佳辩论 | passage 将在 Ch.14/15 重复 |
| Ch.14 | B+ | 1 | 0 | 1 | 四人小组协作读 cloze = 教学创新 | passage 重复 + 字数 +49% |
| Ch.15 | B | 1 | 1 | 1 | Aya 的 close reading 教学深度极高 | passage 三连重复 + 缺 Study Break |
| Ch.16 | A- | 1 | 1 | 0 | 地下 verbal combat + Beethoven reveal = 创意巅峰 | 越权携带 Ch.17 卡片 |
| Ch.17 | A | 0 | 1 | 1 | 三场战斗递进 + Noir backstory + Mia 等待 | Study Break 重复 Ch.16 |

### 修改优先级

1. **P0-01**（Ch.13-14-15 passage 重复）：最高优先级。影响三章的阅读体验。需要为 Ch.14 和 Ch.15 替换重复 passages。
2. **P0-02**（Ch.16 越权卡片）：中等优先级。将 Cards 026/027 移回 Ch.17，补标 Cards 024/025。
3. **P1-05/06**（Ch.12/14 字数）：中等优先级。需要具体削减方案。
4. **P1-01/02**（Cards 标注缺失）：快速修复。
5. **P1-03**（Noah/Noir 命名）：快速修复，需做决定。
6. **P1-04**（Ch.13 元叙事穿帮）：快速修复，删除一句。

---

*审核完成。庄方宜，2026-06-25。*
