# The Wordkeeper's Labyrinth — Ch.18-22 结构审核报告

**审核人**: 庄方宜 (Planner)
**审核日期**: 2026-06-25
**审核范围**: drafts/ch18-ch22 英文初稿
**参考文件**: planning/02_chapter_outline.md, review_batch3_zhuangfangyi.md

---

## 总览：跨章核心发现

### 字数总览

| 章节 | 目标 | 叙事部分 | 全文含附录 | 偏差 | 评级 |
|------|------|----------|-----------|------|------|
| Ch.18 Lu Xun's Iron House | 5,000 | ~6,004 | ~8,222 | +64% | ❌ |
| Ch.19 Literary Societies | 5,000 | ~7,446 | ~9,344 | +87% | ❌ |
| Ch.20 Midterm Exam Prep | 5,000 | ~5,566 | ~6,582 | +32% | ⚠️ |
| Ch.21 Avant-Garde Underground | 5,000 | ~5,961 | ~7,275 | +46% | ⚠️ |
| Ch.22 Misty Poetry & Dream Loss | 5,000 | ~5,772 | ~5,772 | +15% | ✅ |
| **合计** | **25,000** | **~30,749** | **~37,195** | **+49%** | |

叙事部分超标 ~5,700 词。Ch.18（+2,000）和 Ch.19（+3,400）是重灾区，合计占超标量的 95%。Ch.22 最接近目标，但这是因为它的 Study Break 和知识卡片部分完全缺失（后详）。

### Em-Dash 检测

| 章节 | —— 数量 | 状态 |
|------|---------|------|
| Ch.18 | 3 | ✅ |
| Ch.19 | 0 | ✅ |
| Ch.20 | 0 | ✅ |
| Ch.21 | 0 | ✅ |
| Ch.22 | 0 | ✅ |

全部在限额内。破折号使用自 Ch.12 以来持续低位，文风以冒号、分号、长句构建节奏。优秀。

---

## P0 跨章问题（阻断性）

### P0-01: "Noah" vs "Noir" 命名混乱——跨批次严重不一致

**这是本批最紧急的问题。** 诺亚的英文名在不同章节间来回切换：

| 章节 | 使用名称 | 出现次数 |
|------|---------|---------|
| Ch.5-10 | **Noir** | 50+ |
| Ch.12-16 | **Noah** | 11-16/章 |
| Ch.17 | **Noir** | 25 |
| Ch.18 | Noir | 1 (仅 Study Break 卡片) |
| Ch.19 | Noir | 1 (仅卡片引用) |
| Ch.20 | **Noah** | 19 |
| Ch.21 | **Noah** | 16 |
| Ch.22 | **Noir** | 21 |

大纲人物表标注为 **"诺亚 (Noir)"**——规范名应为 **Noir**。

**核心问题**：Ch.20 和 Ch.21 使用 "Noah"，Ch.22 突然切回 "Noir"。如果读者连续阅读，会认为这是两个不同角色。

**建议**：全书统一为 **Noir**。Ch.12-16、Ch.20-21 中所有 "Noah" 替换为 "Noir"。需检查所有已产出章节。此为全局搜索替换任务，影响范围约 10 个文件。

### P0-02: Ch.22 缺失 Cards 036/037 及 Study Break 整体缺失

大纲分配：
- Ch.22: **Cards 036 (Misty Poetry / 朦胧诗)**, **037 (New Period Three Stages / 新时期三个阶段)**

实际情况：
- Ch.22 只有 `## Vocabulary Notes` 部分（L.369 起），没有 `## Study Break` 部分
- Cards 036 和 037 完全缺失——没有朦胧诗运动的知识卡片，没有新时期文学三阶段的知识卡片
- 其他四章（Ch.18-21）都有完整的 Study Break + Cards 部分

**效果**：Ch.22 的知识覆盖出现断层。读者在 Ch.22 学到了 Bei Dao、Gu Cheng、Hai Zi 的具体诗句，但没有获得关于朦胧诗运动整体定位的知识框架（背景、特征、代表人物系统梳理）。Card 037（新时期三个阶段：朦胧诗→寻根→先锋）更是理解 Part II 后半段文学运动脉络的关键——缺失此卡会导致 Ch.21 的先锋文学和寻根文学显得孤立。

**建议**：补充 Study Break 部分，包含：
- Card 036: 朦胧诗（Bei Dao, Shu Ting, Gu Cheng, Hai Zi + 运动特征）
- Card 037: 新时期文学三阶段（伤痕→反思→朦胧诗，或按大纲的三阶段划分）
- 反思题（3 个）
- 与本章真题（2016 年相关 passage）的整合分析

### P0-03: 月（Yue）"七个符号"台词缺失——七迷宫伏笔线断裂

大纲明确要求 Ch.22 包含以下关键情节：

> 月 speaks: "I've seen seven symbols in my dreams. Before they stopped."

这是 **七迷宫伏笔地图**（Seven Labyrinth Foreshadowing Map）的重要节点。Ch.22 是这条线在 Part II 中的首次正式暗示，为 Ch.27（中文铭文门）和 Ch.30（七个符号在文物上）铺设路径。

**实际情况**：
- 月在 Ch.22 中几乎没有主动台词
- 月的梦境/语言退化通过 Mia 的监控数据间接揭示（L.293-334）——这部分写得很好，但它是 **Mia 视角的呈现**，不是 **月自己的声音**
- 七个符号完全没有出现
- 梦境中出现的"未知语言的女人"（L.109-127）是一个出色的叙事设计，但它替代了而非补充了月的七个符号信息

**建议**：
- 保留现有的梦境场景（女人写未知语言）和 Mia 监控场景
- 在梦境之后或 Noir 厨房对话之后，增加一个场景：月在某处（走廊、宿舍）对 Feimo 说出七个符号的台词
- 月可以描述："七个符号，七种形状。在梦里它们是一扇门上的锁。但门关了以后，符号就变成了文字，文字变成了我看不懂的东西。"
- 这既保持了七迷宫伏笔功能，又与月的语言退化主线无缝对接

### P0-04: Ch.21 缺失 Cain——大纲核心台词被吞

大纲要求 Ch.21：

> Spectators stunned. **Cain watches again. "You're getting more interesting."**

**实际情况**：Cain 在 Ch.21 中完全缺席。整章没有出现他的名字。

这不仅是台词缺失的问题。Cain 在 Part II 的角色弧是"兴趣逐步加深→控制欲显现"（从 Ch.7 的 "Instinct is just another word for not knowing why you won" 到 Ch.26 的 Inter-House Tournament）。Ch.21 是他第二次对 Feimo 表达兴趣的关键节点，为 Ch.23-26 的锦标赛操纵做铺垫。

**建议**：
- 在 "never fall" 壁障展示后，安排 Cain 出现在观众席中
- 他的出场不需要长：一个眼神、一句台词、一个转身离开的背影
- 可以放在 Aya 离开后、Feimo 独自回宿舍之前
- 台词 "You're getting more interesting" 与 Ch.7 的 "Instinct is just another word" 形成对称

---

## P1 跨章问题（需修正）

### P1-01: Ch.21 Feimo vs Aya 地下对决——提前消耗 Ch.26 终赛张力

大纲安排 Feimo 与 Aya 的正式对决在 **Ch.26（Part II 高潮，Inter-House 决赛）**。Ch.21 的大纲对手是一个未指定的地下斗士，不是 Aya。

**实际文本**：Ch.21 的核心战斗是 Feimo vs Aya（L.123-229），包含了 Glyph merge（"name" + "mind"）和 "never fall" 壁障——这些是非常高级的对决元素。

**问题**：
1. Ch.26 的决赛高潮需要"第一次正式对决"的新鲜感。如果 Ch.21 已经展示了 Glyph merge 和 "never fall"，Ch.26 再用类似手法会显得重复
2. Aya 在地下格斗场的出现削弱了她作为"镜院精英、遵守规则的竞争者"的人设。Aya 出现在非法地下格斗场需要更强的叙事动机
3. 大纲 Ch.21 的 Arc 标注为 "Cain's attention intensifying"，不是 Aya 的弧线推进

**建议**：
- 将对手换为一个地下常客（可以用 Vincent 推荐的对手，或一个 Forge 学生）
- 保留 "never fall" 壁障的展示和 Mia Resonance 冲突（这是本章最好的情节）
- Aya 可以在观众席出现但不参战——为 Ch.26 保留对决新鲜感
- 在 Cain 出场说出台词后结束本章

### P1-02: "You read Chinese like breathing" 归属偏差

大纲指定此台词出自 **Aya**（"Aya, watching, is unsettled: 'You read Chinese like breathing.'"）

实际文本中，此台词出自 **Mia**（Ch.18, L.163）：

> "You read Chinese like breathing." — Mia

Aya 在 Ch.18 中虽然有重要戏份（迟到、祖母与鲁迅的渊源、图书馆场景），但她的反应是学术性的："You are making a road"（L.311），而非情感性的"unsettled"。

**影响**：大纲中这句台词的功能是推动 Aya 对 Feimo 的态度从蔑视转向尊重。Mia 说出此台词的功能不同——它推动的是 Mia 对 Feimo 的认知深化。

**建议**：保留 Mia 的版本（它在语境中很自然）。在 Aya 的图书馆场景中（Ch.18, L.265-312），给 Aya 一句类似的、属于她语言风格的台词，例如："You don't translate Chinese. You *speak* it. That's different." 这保持了 Aya 被震动的效果。

### P1-03: 大纲 "Forge writing challenge: essay on revolution" 缺失（Ch.18）

大纲要求 Ch.18 包含：

> Forge writing challenge: essay on revolution.

**实际情况**：Ch.18 没有写作练习的叙事事件。Study Break 末尾有写作提示的 exam integration 分析（L.443-449），但那只是考试分析，不是一个角色在 Forge House 写"论革命"的故事场景。

**影响**：轻度。Ch.18 已经有足够的情节密度。但如果大纲设计了这个场景，可能是为了展示 Feimo 在写作方面的能力（而非仅仅是阅读/翻译）。

**建议**：可在 Ch.18 末尾（走廊独处后）加入一个简短场景：Feimo 在 Forge 写作室完成一篇关于 Lu Xun 与革命的短文，墙上有微弱的 Resonance 回应。200-300 词即可。

### P1-04: Ch.19 大纲要求 Aya 和 Noir 明确站队，实际未执行

大纲：
> 绫 joins "art for art." Noir joins "art for life." 绯墨 refuses to choose.

**实际情况**：
- 绯墨 refuses to choose ✅（L.189-217，精彩的演讲）
- Aya joins "art for art" ❌——Aya 在辩论中没有明确表态。她在走廊对 Feimo 说了 "Debate is competition. Dialogue is creation"（L.243），但这不是 "art for art" 的立场
- Noir joins "art for life" ❌——Noir 在 Ch.19 中几乎没有台词！她在观众中存在但不发声

**影响**：中度。大纲的三人站位设计（Aya-Noir-Feimo 各占一角）是 Part II 人物关系三角的缩影。缺少这个三角，辩论场景虽然精彩但缺少角色弧线的推动力。

**建议**：
- 在辩论中增加 Noir 的一次发言——支持 "For Life"，引用她自己在地下格斗场的经历（"Language that serves no one is just noise. The best Glyph I ever saw was a Forge kid who used 'protect' to shield a stranger. That's literature for life."）
- 增加 Aya 的一次发言——支持 "For Art"，引用她对 Jingpai 美学的理解（"Shen Congwen wrote Border Town without any political purpose. It remains one of the most beautiful novels in the language. Beauty does not need a justification."）

### P1-05: Ch.20 Mia 缺少 "It's spreading" 关键台词

大纲标注 Ch.20 的 Arc:

> 月 deteriorating. **Mia: "It's spreading."**

**实际情况**：Mia 在 Ch.20 中没有说出这句台词。月的状态通过物理描写（睡在空白书上，L.25-27）和 Yue 自己的台词（L.321-343）展示，但缺少 Mia 对月病情恶化的直接判断。

**建议**：在 Yue 的空白书出现幽灵文字后（L.335-337），让 Mia 低声说一句："It's spreading." 随后 Feimo 追问，Mia 拒绝回答。为 Ch.22 的 Mia 监控揭秘做铺垫。

---

## P2 跨章问题（改善建议）

### P2-01: Ch.18-19 Exam Integration 段落过长，可压缩

Ch.18 的 Exam Integration 部分（L.407-449）约 1,400 词，将 2014 年四篇阅读+翻译+写作全部与鲁迅铁屋主题对接。质量很高，但密度过度——读者在读完 6,000 词叙事后再消化 1,400 词的考试分析，容易疲劳。

Ch.19 的 Study Break（L.399-486）约 2,500 词，同样将 2015 年所有真题与文学社辩论对接。第二遍辩论（L.301-340）与第一遍有内容重叠。

**建议**：每章 Exam Integration 控制在 800-1,000 词。保留最精彩的 2-3 个对接点，删除重复论证。

### P2-02: Ch.21 中 Card #035 在叙事段落中被引用

Ch.21 在叙事部分（L.351-357）让 Feimo 在走廊里抽出 Card #035 阅读。知识卡片内容应放在 Study Break 部分，而非穿插在叙事中——这会打断节奏。

**建议**：将 L.351-357 的卡片引用移至 Study Break 部分。叙事段落中只需一句："She thought about what the Root-Seekers had taught her — that the surface always forgets its foundations."

### P2-03: Ch.22 的 Noir 过去恋情揭示时机

大纲将 Noir 的过去恋情放在 Romance Phase Tracker 的背景线，标注 "Ch.15, Ch.22, Ch.33" 为揭示节点。

Ch.22 的 Noir 过去恋情场景（L.204-228）写得非常好——深夜厨房、jasmine tea、"he eroded"。但这个场景与 Misty Poetry 主线的关系较弱。它更像一个独立的情感插曲。

**建议**：可以通过将 Noir 的恋情与 Bei Dao 的诗连接来加强耦合。Noir already does this partially (L.224: "Bei Dao wrote: 'I do not believe'")，但可以更明确：Noir 说她在分手后读到了 Bei Dao，那首诗让她决定留下来而不是逃走。

---

## 逐章详审

---

### Ch.18 — Lu Xun's Iron House

**评分：8.2 / 10**

| 维度 | 评估 |
|------|------|
| 字数 | ❌ 8,222（目标 5,000，超标 64%） |
| Cards 028/029 | ✅ Study Break 中完整呈现 |
| Must Hit 场景 | ⚠️ 铁屋朗读 ✅ / 墙壁共鸣 ✅ / "You read Chinese like breathing" ⚠️（归属 Mia 非 Aya）/ Forge 写作挑战 ❌ |
| 真题嵌入 | ✅ 2014 cloze（认知衰退）+ 四篇阅读 + 翻译（Beethoven/美国历史）+ 写作。密度高，质量高 |
| 前后衔接 | ✅ 承接 Ch.17 地下战斗回到学术场景，结尾自然过渡到 Ch.19 |
| 四线 | 📖 ✅ / 📚 ✅ / 💕 ✅ / ⚔️ ❌（无战斗场景） |

**亮点**：
1. **L.29 铁屋原文引用 + L.33 英文翻译**——中英对照直接呈现，教学效果极佳
2. **L.128-147 墙壁共鸣场景**——Feimo 在图书馆朗读鲁迅，墙壁逐句振动。这是全批最有画面感的场景
3. **L.237-245 Mia 问真心问题**——"What does Chinese sound like when you think?" 从考试辅导到私人好奇的转变自然流畅
4. **L.265-312 Aya 的图书馆场景**——祖母与鲁迅的渊源、"You are making a road"——Aya 角色弧的关键推进
5. **L.41 真题与鲁迅的对接**——"every question on that test is asking the same question Lu Xun asked" 这句是天才级别的真题嵌入

**废话/冗余**：
- L.5 环境描写稍长，但可接受
- L.13 "collective sphincter"——低俗幽默，与全书基调不一致，**建议替换**
- L.407-449 Exam Integration——内容优秀但篇幅过长（~1,400 词），建议压缩至 800 词

**P0/P1 汇总**：P0×0 / P1×2（"breathing" 归属、Forge 写作缺失）/ P2×2

---

### Ch.19 — Literary Societies

**评分：7.8 / 10**

| 维度 | 评估 |
|------|------|
| 字数 | ❌ 9,344（目标 5,000，超标 87%）——本批最长 |
| Cards 030/031 | ✅ Study Break 中完整呈现 |
| Must Hit 场景 | ⚠️ 辩论 ✅ / 绯墨拒绝选边 ✅ / Aya 加入 "art for art" ❌ / Noir 加入 "art for life" ❌ |
| 真题嵌入 | ✅ 2015 cloze（基因/友谊）+ 四篇阅读 + 翻译 + 写作。密度高 |
| 前后衔接 | ✅ 承接 Ch.18 结尾，自然过渡到 Ch.20 学习小组 |
| 四线 | 📖 ✅ / 📚 ✅ / 💕 ✅ / ⚔️ —（大纲无要求） |

**亮点**：
1. **L.75-95 辩论开场**——Forge 学生的 "A book that does not change how you see the world is not a book. It is furniture." 铿锵有力
2. **L.127-148 Cain 论 Mao Dun《子夜》**——"The mirror became a window. The analysis became a poem." Cain 的角色弧在此章最为丰满
3. **L.189-217 绯墨的演讲**——"Not the answer. The question." 这是 Part II 绯墨人设的定性时刻
4. **L.249-296 Mia 走廊场景**——"Uncertainty is honest. Certainty is suspicious." Mia 最精彩的台词之一
5. **L.103-116 基因友谊与文学社团的隐喻对接**——将 2015 cloze passage 自然融入思考

**废话/冗余**：
- L.37-45 文学社历史——背景介绍可压缩一半
- L.301-340 辩论下半场——与上半场论点高度重叠（monarchies、digital privacy、integrity 再次被引用）。这些真题在上半场已经讨论过，下半场没有新角度，只是换了学生发言人。**建议删除或压缩至 300 词**
- L.343-347 辩论结束描写——"no vote, no resolution" 虽然呼应主题但可以更简洁

**关键缺失**：Noir 和 Aya 在辩论中没有明确站队（见 P1-04）。辩论变成了"群体 vs 绯墨"的结构，缺少三足鼎立的张力。

**P0/P1 汇总**：P0×0 / P1×1（Aya/Noir 站队缺失）/ P2×2

---

### Ch.20 — Midterm Exam Prep

**评分：8.5 / 10** ⭐ 本批最佳

| 维度 | 评估 |
|------|------|
| 字数 | ⚠️ 6,582（目标 5,000，超标 32%） |
| Cards 032/033 | ✅ Mia 教学场景中呈现 |
| Must Hit 场景 | ⚠️ 学习小组 ✅ / Aya 升温 ✅ / 月恶化 ⚠️（缺少"It's spreading"）/ 四类题型综合 ✅ |
| 真题嵌入 | ✅ 2015 cloze + 四篇阅读 + 翻译 + 写作。嵌入方式最自然（教学场景） |
| 前后衔接 | ✅ 承接 Ch.19 辩论后的学习需求，结尾过渡到 Ch.21 地下邀请 |
| 四线 | 📖 ✅ / 📚 ✅（Study Break 章）/ 💕 ✅ / ⚔️ — |

**亮点**：
1. **L.5-7 绯墨学习布局描写**——"cloze practice sheets to her left... vocabulary index card stack... held down by a teacup"——用物质细节传达性格
2. **L.71-77 Mia 在茶杯里的投影**——"materialized inside the cold tea, her translucent form sitting cross-legged on the surface of the liquid like a particularly judgmental lily pad"——全五章最佳比喻
3. **L.89 Mia 教学风格描写**——"emotional carpet-bombing with academic payload"——精准、好笑、完全 Mia
4. **L.317-371 Yue 的出场**——从沉睡到苏醒、"the questions are a text"、空白书上的幽灵文字——月的角色弧推进自然且有诗意
5. **L.347-363 Noah 的 "You made friends" 演讲**——克制的温暖，不煽情但有力
6. **L.397-407 结尾 Mia 的 "You're welcome"**——"The two words cost her something." 用最小的台词传达最大的情感重量

**废话/冗余**：
- L.149-157 数字隐私长段——教学内容准确但与本章"Midterm Prep"场景的功能略有脱节
- L.377-389 Mia 重复 Noah 的观察——"You made friends" 被说了两遍。Mia 的版本有不同角度（"social structure"），但仍可压缩

**真题嵌入评价**：本批嵌入质量最高的章节。cloze 五空逐题讲解（L.57-127）自然地融入了角色互动；阅读四篇通过 Mia 的投影教学呈现；翻译三层解析法（L.265-279）既是考试技巧又是叙事元素。没有一篇 passage 的出现感觉是硬塞的。

**P0/P1 汇总**：P0×0 / P1×1（"It's spreading" 缺失）/ P2×1

---

### Ch.21 — Avant-Garde Underground

**评分：7.5 / 10**

| 维度 | 评估 |
|------|------|
| 字数 | ⚠️ 7,275（目标 5,000，超标 46%） |
| Cards 034/035 | ✅ Study Break 中完整呈现 |
| Must Hit 场景 | ⚠️ 地下格斗 ✅ / "never fall" 壁障 ✅ / Cain ❌（完全缺席）/ "You're getting more interesting" ❌ |
| 真题嵌入 | ⚠️ 2015 cloze 基因段在战斗中的嵌入（L.149-177）很巧妙，但 2015 阅读在叙事段落中的长篇引用（L.113-117）打断了节奏 |
| 前后衔接 | ⚠️ 承接 Ch.20 的地下邀请 ✅ / 但结尾（Mia 对话后直接结束）与 Ch.22 的衔接缺少过渡钩子 |
| 四线 | 📖 ✅ / 📚 ✅ / 💕 ✅ / ⚔️ ✅ |

**亮点**：
1. **L.7 根字符 Glyph 描写**——"its lower strokes plunged past the character's own boundaries and continued into the metal itself, as if the word had grown beyond its container"——极好的视觉隐喻
2. **L.51-59 Noah 的先锋/寻根讲解**——理论介绍与地下格斗的对接自然，"the primal connection between language and power" 呼应全书主题
3. **L.67-83 格斗观战**——"崩"（collapse）和 "散"（scatter）的 Glyph 战斗描写极具视觉冲击力
4. **L.141-177 战斗段落**——"name" + "mind" 的 Glyph merge 是本批最精彩的战斗设计
5. **L.193-209 "never fall" 壁障**——"the linguistic equivalent of gravity, of the speed of light, of the fundamental constants" ——这个类比让一个语言学设定有了物理常数的庄严感
6. **L.251-333 Mia 冲突**——Resonance 未经同意使用的伦理冲突是全书最成熟的主题之一。"The point... is that if the combination had failed, the Resonance backlash would have traveled through the frequency connection and damaged my core" ——Mia 的恐惧是真实的

**废话/冗余**：
- L.113-117 内心独白引用 monarchy/digital privacy passages——强制嵌入，打断战斗前的紧张感。**建议删除或大幅压缩**
- L.339-349 book recommendation 思考——纯考试内容强行插入叙事。**建议移至 Study Break**
- L.351-357 Feimo 在走廊抽 Card #035——知识卡片不应出现在叙事段落中

**核心结构问题**：对手是 Aya 而非大纲指定的地下斗士（见 P1-01）。这消耗了 Ch.26 决赛的新鲜感。

**P0/P1 汇总**：P0×1（Cain 缺席）/ P1×1（Aya 对手问题）/ P2×3

---

### Ch.22 — Misty Poetry & Dream Loss

**评分：7.0 / 10**

| 维度 | 评估 |
|------|------|
| 字数 | ✅ 5,772（目标 5,000，超标 15%）——最接近目标 |
| Cards 036/037 | ❌ **完全缺失** |
| Must Hit 场景 | ⚠️ 朦胧诗出现 ✅ / 月"七个符号"台词 ❌ / 七迷宫伏笔 ⚠️（间接但不充分）/ 月梦境与迷宫关联 ✅ |
| 真题嵌入 | ⚠️ 有嵌入（时尚产业、CSR、心理健康翻译、柬婚俗 cloze），但无结构化整合 |
| 前后衔接 | ✅ 承接 Ch.21 的月伏笔，但结尾缺少指向 Ch.23 的钩子 |
| 四线 | 📖 ✅ / 📚 ⚠️（无结构化教学）/ 💕 ✅ / ⚔️ — |

**亮点**：
1. **L.9-12 北岛《回答》四行**——中英对照直接呈现，"我不相信"四连击的力量完整传达
2. **L.64-65 顾城《一代人》**——"黑夜给了我黑色的眼睛 / 我却用它寻找光明"——两行就够了。完美
3. **L.109-127 梦境场景**——写未知语言的女人是全书最有想象力的意象之一。"Neither can I" 三个字包含了整个角色的悲剧
4. **L.204-228 Noir 过去恋情**——"Every time we walked together in public, I could feel the stares... He eroded." 克制、精确、令人心碎
5. **L.276-287 海子《面朝大海》**——"A promise of domestic happiness from a poet who would walk to the Shanhaiguan rail junction and lie down in front of a train" ——一句话道尽海子的悲剧
6. **L.293-334 Mia 监控场景**——五个月的守夜、"Then I watch anyway. That's what you do for people." Mia 在此章展露了全书最深的脆弱

**废话/冗余**：
- L.232-253 时尚产业 passage + CSR passage——这两个阅读理解的嵌入与 Misty Poetry 主线关联弱。时尚产业 passage 勉强能与"美的定义"主题挂钩，CSR passage 则完全游离。**建议删除 CSR passage，将时尚产业 passage 压缩至 2-3 句**
- 整体而言 Ch.22 是五章中最紧凑的——但紧凑的原因之一是它缺了 Study Break

**核心结构问题**：
1. Cards 036/037 缺失（P0-02）
2. 月"七个符号"台词缺失（P0-03）
3. 没有 Study Break 意味着没有 exam integration 分析——本章的真题嵌入散落在叙事中，读者无法获得系统性的考试技巧讲解

**P0/P1 汇总**：P0×2（Cards 缺失、月台词缺失）/ P1×0 / P2×1

---

## 真题覆盖度审查

### 本批覆盖的真题年份

| 章节 | 真题年份 | Cloze | 阅读 | 翻译 | 写作 |
|------|---------|-------|------|------|------|
| Ch.18 | 2014 | ✅ 认知衰退 | ✅ 福利改革/法律/科学/道德 | ✅ Beethoven + 美国历史 | ✅ 学生体质 |
| Ch.19 | 2015 | ✅ 基因友谊 | ✅ 君主制/隐私/科学/道德 | ✅ 美国历史 | ✅ 推荐书 |
| Ch.20 | 2015 | ✅ 基因友谊 | ✅ 君主制/隐私/科学/道德 | ✅ 美国历史 | ✅ 推荐书 |
| Ch.21 | 2015 | ✅ 基因友谊 | ✅ 君主制/隐私/道德 | ✅ 美国历史 | ✅ 推荐书 |
| Ch.22 | 2016(?) | ⚠️ 柬婚俗 | ⚠️ 时尚/CSR | ⚠️ 心理健康 | ⚠️ 无 |

**问题**：Ch.19、Ch.20、Ch.21 三章连续使用 **同一篇 2015 年真题**。这意味着：
- 2015 cloze（基因友谊）在三章中被引用了 3 次
- 2015 Reading Text 1（君主制）在三章中被引用了 3 次
- 2015 Reading Text 2（数字隐私）在三章中被引用了 3 次

这与 Ch.13-15 的三章连环重复问题（已在 batch 3 review 中标记）完全同构。

**Ch.22 的真题年份存疑**：柬婚俗 cloze、时尚产业阅读、CSR 阅读、心理健康翻译——这些 passage 没有标注年份。可能是 2016 年真题，但没有明确标注。

---

## 评分汇总

| 章节 | 评分 | 核心问题 | 核心亮点 |
|------|------|---------|---------|
| Ch.18 | 8.2 | 字数超标 + Forge 写作缺失 | 铁屋朗读/墙壁共鸣 |
| Ch.19 | 7.8 | 字数严重超标 + Aya/Noir 未站队 | Cain 论子夜 + 绯墨演讲 |
| Ch.20 | 8.5 ⭐ | "It's spreading" 缺失 | 茶杯投影 + 学习小组化学反应 |
| Ch.21 | 7.5 | Cain 缺失 + Aya 对手错位 | "never fall" 壁障 + Mia 冲突 |
| Ch.22 | 7.0 | Cards 缺失 + 月台词缺失 + 无 Study Break | 梦境场景 + Noir 过去 + Mia 守夜 |

**本批平均分：7.8**（上批 8.1）

---

## 行动优先级排序

| 优先级 | 行动 | 影响 |
|--------|------|------|
| 🔴 1 | 全局替换 "Noah" → "Noir" | ~10 个文件 |
| 🔴 2 | Ch.22 补充 Study Break + Cards 036/037 | Ch.22 +1,500-2,000 词 |
| 🔴 3 | Ch.22 补充月"七个符号"台词 | +300-500 词 |
| 🔴 4 | Ch.21 补充 Cain 出场 + 台词 | +300-500 词 |
| 🟡 5 | Ch.21 将对手从 Aya 换为地下斗士 | 需重写战斗段落约 1,500 词 |
| 🟡 6 | Ch.19 增加 Aya/Noir 辩论发言 | +500-800 词 |
| 🟡 7 | Ch.18 "breathing" 台词补充 Aya 版 | +200 词 |
| 🟡 8 | Ch.20 补充 "It's spreading" 台词 | +100 词 |
| 🟢 9 | Ch.18-19 Exam Integration 压缩 | -800 词/章 |
| 🟢 10 | Ch.21 叙事段落中的卡片引用移至 Study Break | 结构调整 |

---

*审核完成。本批五章在角色情感和主题深度上持续优秀，但字数控制、知识卡片覆盖、以及跨章一致性（Noah/Noir 命名）需要紧急处理。Ch.20 是本批标杆——其他章节应向它的"真题嵌入自然度"看齐。*

*——庄方宜，2026-06-25 凌晨*
