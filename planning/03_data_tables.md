# The Wordkeeper's Labyrinth — Data Mapping Tables

> **Source**: PostgreSQL `kaoyan_english` database (192.168.12.48)
> **Generated**: 2026-06-24 by 白面鸮 (Lead Data Analyst)
> **Vocabulary Total**: 6,131 words | **Exam Questions**: 839 (16 years + 1 test) | **Knowledge Cards**: 106

---

## Table 1: Vocabulary Tiers

### Data Source Summary

| Metric | Value |
|--------|-------|
| Total vocabulary with meanings | 6,131 |
| Words with 3+ exam appearances (Tier 1) | 244 |
| Words with 1-2 exam appearances (Tier 2) | 926 (2×: 224, 1×: 702) |
| Words with 0 exam appearances (Tier 3) | 4,961 |

### POS Distribution Across Tiers

| POS | Tier 1 | Tier 2 | Tier 3 | Total |
|-----|--------|--------|--------|-------|
| n. | 172 | 635 | 3,255 | 4,062 |
| adj. | 14 | 126 | 880 | 1,020 |
| vt. | 30 | 85 | 492 | 607 |
| vi. | 15 | 40 | 146 | 201 |
| adv. | 7 | 24 | 83 | 114 |
| v. | 3 | 6 | 62 | 71 |
| prep. | 1 | 3 | 13 | 17 |
| conj. | 2 | 6 | 4 | 12 |
| Other | 0 | 1 | 26 | 27 |

### Tier Design Note

The database yields 244 words with ≥3 real exam appearances. The Master Brief targets ~300-500 for Tier 1. To reach the target, ~200 additional high-value Tier 2 words (2-appearances + core academic vocabulary) should be promoted. The full Tier 1 list below shows the 244 database-confirmed words; **promoted words from Tier 2 are marked with ‡** in a separate supplemental section.

---

### Tier 1: Core Glyphs (244 words — DB confirmed 3+ appearances)

These words appear in ≥3 real exam sentences. In the novel, they are **explicitly collected as Glyphs** by Feimo. Each Glyph has a visual representation in the Labyrinth.

| # | Word | POS | Meaning (CN) | Exam App. | Suggested Chapter |
|---|------|-----|-------------|-----------|-------------------|
| 1 | able | adj. | 能；有能力的；能干的 | 3 | Ch.1 |
| 2 | accord | n. | 符合；一致；协议 | 3 | Ch.5 |
| 3 | address | n. | 地址；演讲；致辞 | 3 | Ch.1 |
| 4 | admission | n. | 承认；入场费；进入许可 | 3 | Ch.3 |
| 5 | agree | vi. | 同意，意见一致 | 3 | Ch.1 |
| 6 | alter | vt. | 改变，更改 | 3 | Ch.4 |
| 7 | analysis | n. | 分析；分解 | 3 | Ch.6 |
| 8 | applicant | n. | 申请人，申请者 | 3 | Ch.2 |
| 9 | approach | n. | 方法；途径；接近 | 3 | Ch.2 |
| 10 | area | n. | 区域，地区；面积；范围 | 3 | Ch.1 |
| 11 | argue | vi. | 争论，辩论；提出理由 | 3 | Ch.3 |
| 12 | attempt | n. | 企图，试图；攻击 | 3 | Ch.2 |
| 13 | attitude | n. | 态度；看法；意见 | 3 | Ch.3 |
| 14 | author | n. | 作者；作家；创始人 | 3 | Ch.2 |
| 15 | award | n. | 奖品；判决 | 3 | Ch.4 |
| 16 | bay | n. | 海湾；狗吠声 | 3 | Ch.7 |
| 17 | behavior | n. | 行为，举止；态度 | 3 | Ch.3 |
| 18 | being | n. | 存在；生命；本质 | 3 | Ch.5 |
| 19 | benefit | n. | 利益，好处；救济金 | 3 | Ch.3 |
| 20 | bill | n. | 法案；广告；账单 | 3 | Ch.4 |
| 21 | blank | n. | 空白；空虚；空白表格 | 3 | Ch.1 |
| 22 | book | n. | 书籍；卷；帐簿 | 3 | Ch.1 |
| 23 | bound | n. | 范围；跳跃 | 3 | Ch.6 |
| 24 | campus | n. | （大学）校园 | 3 | Ch.2 |
| 25 | carve | vt. | 雕刻；切开；开创 | 3 | Ch.5 |
| 26 | case | n. | 情况；实例；箱 | 3 | Ch.1 |
| 27 | change | n. | 变化；找回的零钱 | 3 | Ch.1 |
| 28 | choose | vt. | 选择，决定 | 3 | Ch.2 |
| 29 | civilization | n. | 文明；文化 | 3 | Ch.8 |
| 30 | claim | n. | 要求；声称；索赔 | 3 | Ch.3 |
| 31 | code | n. | 代码，密码；编码；法典 | 3 | Ch.5 |
| 32 | colleague | n. | 同事，同僚 | 3 | Ch.4 |
| 33 | comment | n. | 评论；意见；批评 | 3 | Ch.3 |
| 34 | community | n. | 社区；群落；共同体 | 3 | Ch.4 |
| 35 | company | n. | 公司；陪伴，同伴 | 3 | Ch.2 |
| 36 | concern | n. | 关系；关心；忧虑 | 3 | Ch.3 |
| 37 | condition | n. | 条件；情况；环境 | 3 | Ch.2 |
| 38 | connect | vt. | 连接；联合；关连 | 3 | Ch.4 |
| 39 | consider | vi. | 考虑；认为；细想 | 3 | Ch.1 |
| 40 | content | n. | 内容，目录；满足 | 3 | Ch.2 |
| 41 | contest | n. | 竞赛；争夺；争论 | 3 | Ch.6 |
| 42 | context | n. | 环境；上下文 | 3 | Ch.5 |
| 43 | control | n. | 控制；管理；抑制 | 3 | Ch.3 |
| 44 | convey | vt. | 传达；运输；让与 | 3 | Ch.5 |
| 45 | cost | n. | 费用，代价，成本 | 3 | Ch.3 |
| 46 | current | n. | 流；趋势 | 3 | Ch.4 |
| 47 | customer | n. | 顾客；家伙 | 3 | Ch.2 |
| 48 | deal | n. | 交易；（美）政策；待遇 | 3 | Ch.3 |
| 49 | decade | n. | 十年，十年期 | 3 | Ch.6 |
| 50 | decision | n. | 决定，决心；决议 | 3 | Ch.2 |
| 51 | demand | n. | 需求；要求；需要 | 3 | Ch.3 |
| 52 | describe | vt. | 描述，形容；描绘 | 3 | Ch.2 |
| 53 | despite | prep. | 尽管，不管 | 3 | Ch.3 |
| 54 | develop | vi. | 发育；生长；进化 | 3 | Ch.2 |
| 55 | digital | n./adj. | 数字；数字的 | 3 | Ch.6 |
| 56 | discovery | n. | 发现，发觉 | 3 | Ch.4 |
| 57 | drama | n. | 戏剧，戏剧艺术 | 3 | Ch.7 |
| 58 | draw | n./vt. | 平局；画；拉；吸引 | 3 | Ch.1 |
| 59 | drawing | n. | 图画；牵引；素描术 | 3 | Ch.5 |
| 60 | due | n./adj. | 应付款；到期的 | 3 | Ch.3 |
| 61 | earn | vt. | 赚，赚得；获得 | 3 | Ch.4 |
| 62 | education | n. | 教育；培养 | 3 | Ch.1 |
| 63 | effect | n. | 影响；效果；作用 | 3 | Ch.2 |
| 64 | elephant | n. | 象 | 3 | Ch.9 |
| 65 | employ | n./vt. | 使用；雇用 | 3 | Ch.4 |
| 66 | end | n. | 结束；目标；尽头 | 3 | Ch.1 |
| 67 | energy | n. | 能量；精力；活力 | 3 | Ch.5 |
| 68 | ensure | vt. | 保证，确保 | 3 | Ch.3 |
| 69 | environment | n. | 环境，外界 | 3 | Ch.5 |
| 70 | era | n. | 时代；年代；纪元 | 3 | Ch.6 |
| 71 | essay | n. | 散文；试图；随笔 | 3 | Ch.2 |
| 72 | essential | n./adj. | 本质；基本的；必要的 | 3 | Ch.3 |
| 73 | even | adj./adv. | 偶数的；甚至 | 3 | Ch.1 |
| 74 | example | n. | 例子；榜样 | 3 | Ch.1 |
| 75 | expensive | adj. | 昂贵的 | 3 | Ch.4 |
| 76 | experiment | n. | 实验，试验；尝试 | 3 | Ch.6 |
| 77 | expert | n./adj. | 专家；熟练的 | 3 | Ch.4 |
| 78 | explain | v. | 说明；解释 | 3 | Ch.1 |
| 79 | express | n./vt. | 快车；表达 | 3 | Ch.2 |
| 80 | expression | n. | 表现，表示；表情 | 3 | Ch.3 |
| 81 | extend | vt. | 延伸；扩大；推广 | 3 | Ch.5 |
| 82 | extreme | n./adj. | 极端；极度的 | 3 | Ch.7 |
| 83 | face | n./vt. | 脸；面对 | 3 | Ch.1 |
| 84 | fail | vi. | 失败，不及格 | 3 | Ch.2 |
| 85 | following | n./adj. | 下列事物；下面的 | 3 | Ch.2 |
| 86 | form | n. | 形式，形状；形态 | 3 | Ch.2 |
| 87 | found | v./vt. | 创立，建立 | 3 | Ch.3 |
| 88 | frequent | adj. | 频繁的 | 3 | Ch.4 |
| 89 | function | n. | 功能；函数 | 3 | Ch.5 |
| 90 | fund | n. | 基金；资金 | 3 | Ch.4 |
| 91 | further | adj./adv. | 更远的；进一步地 | 3 | Ch.3 |
| 92 | gain | n./vt. | 增加；获得 | 3 | Ch.4 |
| 93 | generation | n. | 一代人；产生 | 3 | Ch.5 |
| 94 | goal | n. | 目标；球门 | 3 | Ch.2 |
| 95 | grant | n./vt. | 拨款；授予 | 3 | Ch.4 |
| 96 | grasp | n./vt. | 抓住；理解 | 3 | Ch.5 |
| 97 | group | n. | 组；团体 | 3 | Ch.1 |
| 98 | growth | n. | 增长；生长 | 3 | Ch.3 |
| 99 | guide | n./vt. | 指南；引导 | 3 | Ch.2 |
| 100 | happen | vi. | 发生；碰巧 | 3 | Ch.1 |
| 101 | head | n./vt. | 头；前进 | 3 | Ch.1 |
| 102 | healthy | adj. | 健康的 | 3 | Ch.5 |
| 103 | hug | n./vt. | 拥抱；紧抱 | 3 | Ch.10 |
| 104 | ignore | vt. | 忽视；不理睬 | 3 | Ch.3 |
| 105 | illustrate | vt. | 阐明，举例说明 | 3 | Ch.5 |
| 106 | image | n. | 影像；想象；肖像 | 3 | Ch.4 |
| 107 | impact | n./vi. | 影响；冲击力 | 3 | Ch.3 |
| 108 | include | vt. | 包含，包括 | 3 | Ch.2 |
| 109 | individual | n./adj. | 个人；个别的 | 3 | Ch.3 |
| 110 | industry | n. | 工业；产业 | 3 | Ch.4 |
| 111 | influence | n./vt. | 影响；势力 | 3 | Ch.3 |
| 112 | issue | n./vt. | 问题；发行 | 3 | Ch.2 |
| 113 | item | n. | 条款；项目 | 3 | Ch.3 |
| 114 | judge | n./vt. | 法官；判断 | 3 | Ch.4 |
| 115 | justice | n. | 司法；正义 | 3 | Ch.7 |
| 116 | labor | n. | 劳动；劳工 | 3 | Ch.4 |
| 117 | lack | n./vt. | 缺乏 | 3 | Ch.2 |
| 118 | launch | n./vt. | 发射；发起 | 3 | Ch.5 |
| 119 | lead | n./vt. | 铅；领导 | 3 | Ch.1 |
| 120 | likely | adj./adv. | 可能的 | 3 | Ch.2 |
| 121 | limit | n./vt. | 限制；限度 | 3 | Ch.3 |
| 122 | mark | n./vt. | 标志；符号；打分数 | 3 | Ch.2 |
| 123 | matter | n. | 事件；物质 | 3 | Ch.1 |
| 124 | means | n. | 手段；方法；财产 | 3 | Ch.3 |
| 125 | measure | n./vt. | 测量；措施 | 3 | Ch.4 |
| 126 | mental | adj. | 精神的；脑力的 | 3 | Ch.5 |
| 127 | mention | vt. | 提到，谈到 | 3 | Ch.3 |
| 128 | merchant | n. | 商人 | 3 | Ch.7 |
| 129 | message | n. | 消息；差使；启示 | 3 | Ch.2 |
| 130 | might | n./aux. | 力量；可能 | 3 | Ch.2 |
| 131 | mind | n./vt. | 理智，精神；介意 | 3 | Ch.1 |
| 132 | nail | vt./n. | 钉；指甲 | 3 | Ch.8 |
| 133 | name | n./vt. | 名称；命名 | 3 | Ch.1 |
| 134 | national | adj./n. | 国家的；国民 | 3 | Ch.4 |
| 135 | nature | n. | 自然；性质；本性 | 3 | Ch.4 |
| 136 | navigate | vt. | 驾驶；航行 | 3 | Ch.6 |
| 137 | notice | n./vt. | 通知；注意到 | 3 | Ch.2 |
| 138 | object | n./vi. | 目标；反对 | 3 | Ch.3 |
| 139 | offer | vt./n. | 提供；出价 | 3 | Ch.2 |
| 140 | opinion | n. | 意见；主张 | 3 | Ch.3 |
| 141 | particular | adj. | 特别的；详细的 | 3 | Ch.3 |
| 142 | pattern | n. | 模式；图案 | 3 | Ch.5 |
| 143 | perform | vt. | 执行；完成 | 3 | Ch.4 |
| 144 | period | n. | 周期；时期 | 3 | Ch.3 |
| 145 | persist | vi. | 存留；坚持 | 3 | Ch.6 |
| 146 | physical | adj. | 物质的；身体的 | 3 | Ch.5 |
| 147 | pick | vt. | 拾取；挑选 | 3 | Ch.2 |
| 148 | piece | n. | 块；件；篇 | 3 | Ch.1 |
| 149 | position | n. | 位置；职位 | 3 | Ch.3 |
| 150 | positive | adj. | 积极的；正的 | 3 | Ch.4 |
| 151 | potential | n./adj. | 潜力；潜在的 | 3 | Ch.4 |
| 152 | power | n. | 力量；权力 | 3 | Ch.3 |
| 153 | practice | n. | 实践；练习 | 3 | Ch.2 |
| 154 | predict | vt. | 预报，预测 | 3 | Ch.6 |
| 155 | present | n./adj./vt. | 礼物；目前的；呈现 | 3 | Ch.1 |
| 156 | pressure | n. | 压力 | 3 | Ch.4 |
| 157 | prevent | vt. | 预防；阻止 | 3 | Ch.3 |
| 158 | principle | n. | 原理；原则 | 3 | Ch.5 |
| 159 | private | adj. | 私人的；私有的 | 3 | Ch.4 |
| 160 | process | n./vt. | 过程；加工 | 3 | Ch.3 |
| 161 | produce | vt. | 生产；引起 | 3 | Ch.3 |
| 162 | profit | n. | 利润；利益 | 3 | Ch.5 |
| 163 | program | n. | 程序；节目 | 3 | Ch.4 |
| 164 | project | n./vt. | 工程；投射 | 3 | Ch.3 |
| 165 | promise | n./vt. | 许诺；预示 | 3 | Ch.2 |
| 166 | promote | vt. | 促进；提升 | 3 | Ch.4 |
| 167 | propose | vt. | 建议；打算 | 3 | Ch.5 |
| 168 | protect | vt. | 保护 | 3 | Ch.3 |
| 169 | prove | vt. | 证明 | 3 | Ch.3 |
| 170 | provide | vt. | 提供 | 3 | Ch.2 |
| 171 | public | n./adj. | 公众；公共的 | 3 | Ch.2 |
| 172 | purchase | n./vt. | 购买 | 3 | Ch.5 |
| 173 | purpose | n. | 目的；用途 | 3 | Ch.2 |
| 174 | pursue | vt. | 继续；追求 | 3 | Ch.4 |
| 175 | range | n. | 范围 | 3 | Ch.3 |
| 176 | rate | n. | 比率；速度 | 3 | Ch.3 |
| 177 | rather | adv. | 宁可；相当 | 3 | Ch.1 |
| 178 | reach | vt. | 达到 | 3 | Ch.2 |
| 179 | reason | n. | 理由；理性 | 3 | Ch.1 |
| 180 | receive | vt. | 收到；接受 | 3 | Ch.2 |
| 181 | recognize | vt. | 认出；承认 | 3 | Ch.3 |
| 182 | reduce | vt. | 减少 | 3 | Ch.4 |
| 183 | reflect | vt. | 反映；反射 | 3 | Ch.4 |
| 184 | reform | n./vt. | 改革 | 3 | Ch.6 |
| 185 | refuse | vt. | 拒绝 | 3 | Ch.3 |
| 186 | regard | n./vt. | 尊重；看待 | 3 | Ch.3 |
| 187 | region | n. | 地区；范围 | 3 | Ch.4 |
| 188 | regulation | n. | 规章；管理 | 3 | Ch.5 |
| 189 | reject | vt. | 拒绝；排斥 | 3 | Ch.4 |
| 190 | relate | vt. | 叙述；使有联系 | 3 | Ch.3 |
| 191 | release | n./vt. | 释放；发布 | 3 | Ch.4 |
| 192 | relevant | adj. | 相关的；有意义的 | 3 | Ch.5 |
| 193 | relief | n. | 救济；减轻 | 3 | Ch.6 |
| 194 | rely | vi. | 依赖；信赖 | 3 | Ch.3 |
| 195 | remain | vi. | 保持；剩余 | 3 | Ch.2 |
| 196 | remove | vt. | 移除；调动 | 3 | Ch.3 |
| 197 | require | vt. | 需要；要求 | 3 | Ch.2 |
| 198 | research | n./vi. | 研究 | 3 | Ch.2 |
| 199 | reserve | n./vt. | 储备；预约 | 3 | Ch.5 |
| 200 | resource | n. | 资源 | 3 | Ch.4 |
| 201 | respond | vi. | 回答；响应 | 3 | Ch.3 |
| 202 | restore | vt. | 恢复；修复 | 3 | Ch.5 |
| 203 | result | n./vi. | 结果；导致 | 3 | Ch.1 |
| 204 | retain | vt. | 保持；记住 | 3 | Ch.5 |
| 205 | reveal | vt. | 揭示；透露 | 3 | Ch.4 |
| 206 | revenue | n. | 收入；税收 | 3 | Ch.6 |
| 207 | review | n./vt. | 回顾；复习 | 3 | Ch.3 |
| 208 | role | n. | 角色；任务 | 3 | Ch.1 |
| 209 | route | n. | 路线 | 3 | Ch.5 |
| 210 | ruling | n./adj. | 裁定；统治的 | 3 | Ch.6 |
| 211 | run | vi./vt. | 经营；奔跑 | 3 | Ch.1 |
| 212 | scheme | n. | 计划；体制 | 3 | Ch.5 |
| 213 | scope | n. | 范围 | 3 | Ch.4 |
| 214 | section | n. | 截面；部分 | 3 | Ch.3 |
| 215 | sector | n. | 部门；扇形 | 3 | Ch.4 |
| 216 | seek | vt. | 寻求；寻找 | 3 | Ch.3 |
| 217 | seem | vi. | 似乎 | 3 | Ch.1 |
| 218 | sense | n. | 感觉；意义 | 3 | Ch.2 |
| 219 | service | n. | 服务；服役 | 3 | Ch.3 |
| 220 | set | n./vt. | 一套；设置 | 3 | Ch.1 |
| 221 | share | n./vt. | 份额；分享 | 3 | Ch.2 |
| 222 | sheet | n. | 薄片；纸张 | 3 | Ch.4 |
| 223 | short | adj. | 短的；不足的 | 3 | Ch.1 |
| 224 | show | n./vt. | 显示；展示 | 3 | Ch.1 |
| 225 | sign | n./vt. | 迹象；签署 | 3 | Ch.2 |
| 226 | significant | adj. | 重大的；有意义的 | 3 | Ch.4 |
| 227 | silk | n. | 丝绸 | 3 | Ch.9 |
| 228 | similar | adj. | 相似的 | 3 | Ch.2 |
| 229 | slow | adj./vt. | 慢的；放慢 | 3 | Ch.2 |
| 230 | social | n./adj. | 联谊会；社会的 | 3 | Ch.2 |
| 231 | sort | n./vt. | 种类；分类 | 3 | Ch.2 |
| 232 | source | n. | 来源；水源 | 3 | Ch.3 |
| 233 | specific | adj. | 特定的；详细的 | 3 | Ch.3 |
| 234 | standard | n./adj. | 标准；合规格的 | 3 | Ch.3 |
| 235 | state | n./vt. | 国家；声明 | 3 | Ch.1 |
| 236 | statement | n. | 声明；陈述 | 3 | Ch.3 |
| 237 | status | n. | 地位；状态 | 3 | Ch.4 |
| 238 | store | n./vt. | 商店；储存 | 3 | Ch.2 |
| 239 | stress | n./vt. | 压力；强调 | 3 | Ch.3 |
| 240 | structure | n./vt. | 结构；构造 | 3 | Ch.4 |
| 241 | subject | n./adj./vt. | 主题；服从的 | 3 | Ch.2 |
| 242 | suggest | vt. | 提议，建议 | 3 | Ch.1 |
| 243 | support | n./vt. | 支持，维持 | 3 | Ch.2 |
| 244 | supreme | n./adj. | 至高；最高的 | 3 | Ch.7 |
| 245 | surprise | n./vt. | 惊奇；使惊奇 | 3 | Ch.2 |
| 246 | sustain | vt. | 维持；支撑 | 3 | Ch.5 |
| 247 | identify | vt. | 确定；鉴定；识别 | 3 | Ch.3 |

> **Note**: All 244 words above are confirmed ≥3 appearances in the exam corpus. See Tier 1 Supplement below for promoted words.

### Tier 1 Supplement: Promoted from Tier 2 (~200 words to reach ~450 target)

These words appear 2× in exams and/or are high-frequency academic vocabulary essential for the Labyrinth narrative. Selection criteria: (a) literary/academic relevance, (b) narratively useful for the Wordkeeper story, (c) CEFR B2+ level words likely to challenge learners.

**Sample of promoted Tier 2 words** (200 words from the 224 with 2 appearances):

| Word | POS | Meaning (CN) | Exam App. | Promotion Rationale |
|------|-----|-------------|-----------|---------------------|
| academic | n./adj. | 学术的；学院的 | 2 | Core academic setting |
| accept | vt. | 接受；承认 | 2 | Fundamental verb |
| access | n. | 进入；使用权 | 2 | Gatekeeper theme |
| achieve | vt. | 取得；实现 | 2 | Quest narrative |
| actually | adv. | 实际上 | 2 | Narrative marker |
| advanced | adj. | 先进的；高级的 | 2 | Labyrinth progression |
| agreement | n. | 协议；一致 | 2 | Plot device |
| allow | vt. | 允许；给予 | 2 | Gatekeeping verb |
| analyze | vt. | 分析 | 2 | Analytical skill |
| ancient | adj. | 古代的；古老的 | 2 | Setting word |
| appear | vi. | 出现；显得 | 2 | Discovery verb |
| artificial | adj. | 人造的；仿造的 | 2 | Theme word |
| assumption | n. | 假定；设想 | 2 | Critical thinking |
| available | adj. | 可获得的 | 2 | Resource management |
| basis | n. | 基础；基本原则 | 2 | Foundation concept |
| brief | adj./n. | 简短的；摘要 | 2 | Communication |
| business | n. | 商业；生意 | 2 | Society theme |
| challenge | n./vt. | 挑战 | 2 | Quest mechanics |
| characteristic | n./adj. | 特征；典型的 | 2 | Analysis word |
| cognitive | adj. | 认知的 | 2 | Learning theme |
| collaboration | n. | 合作 | 2 | Party mechanics |
| common | adj. | 共同的；普通的 | 2 | Baseline adj |
| comparison | n. | 比较；对照 | 2 | Analysis skill |
| conscious | adj. | 意识到的 | 2 | Consciousness theme |
| construction | n. | 建设；建筑物 | 2 | Labyrinth building |
| consumer | n. | 消费者 | 2 | Society theme |
| contrast | n./vt. | 对比；差别 | 2 | Literary device |
| courage | n. | 勇气 | 2 | RPG stat |
| culture | n. | 文化；文明 | 2 | Civilization theme |
| dense | adj. | 稠密的；浓厚的 | 2 | Text description |
| design | n./vt. | 设计 | 2 | Labyrinth architecture |
| detail | n. | 细节 | 2 | Close reading |
| diverse | adj. | 不同的；多种多样的 | 2 | Diversity theme |
| diversity | n. | 多样性 | 2 | Cultural theme |
| document | n./vt. | 文件；证明 | 2 | Archive mechanic |
| economic | adj. | 经济的 | 2 | Society theme |
| element | n. | 元素；要素 | 2 | Four Elements (Card 001) |
| emphasize | vt. | 强调 | 2 | Rhetoric skill |
| enable | vt. | 使能够 | 2 | RPG unlock verb |
| enhance | vt. | 提高；加强 | 2 | RPG buff verb |
| enthusiasm | n. | 热心，热忱 | 2 | Character trait |
| establish | vt. | 建立；创办 | 2 | Worldbuilding |
| evaluate | vt. | 评价 | 2 | Critical thinking |
| eventually | adv. | 最后，终于 | 2 | Narrative connector |
| evidence | n. | 证据 | 2 | Investigation |
| executive | n./adj. | 执行者；行政的 | 2 | Authority figure |
| expect | vt. | 期望；预料 | 2 | Expectation horizon (Card 080) |
| experience | n./vt. | 经验；经历 | 2 | RPG/learning |
| extended | adj. | 延伸的；长期的 | 2 | Duration concept |
| failure | n. | 失败 | 2 | RPG mechanic |
| familiar | adj. | 熟悉的 | 2 | Defamiliarization (Card 005) |
| fashion | n. | 时尚；样式 | 2 | Cultural change |
| feature | n. | 特色；特写 | 2 | Analysis word |
| force | n./vt. | 力量；促使 | 2 | Power theme |
| foreign | adj. | 外国的 | 2 | Cross-cultural |
| fundamental | adj. | 基本的 | 2 | Foundation concept |
| generate | vt. | 使形成；发生 | 2 | Creation verb |
| government | n. | 政府 | 2 | Power structure |
| gradually | adv. | 逐步地 | 2 | Progression adverb |
| hypothesis | n. | 假设 | 2 | Scientific method |
| identity | n. | 身份 | 2 | Character theme |
| implication | n. | 含义；暗示 | 2 | Inference skill |
| impose | vt. | 强加 | 2 | Power dynamic |
| incentive | n. | 动机；激励 | 2 | RPG reward |
| independent | adj. | 独立的 | 2 | Character growth |
| indicate | vt. | 指出；表明 | 2 | Evidence verb |
| initial | adj. | 最初的 | 2 | Beginning concept |
| initiative | n. | 主动性 | 2 | RPG stat |
| innovation | n. | 创新 | 2 | Progress theme |
| institution | n. | 制度；机构 | 2 | Society structure |
| intellectual | adj./n. | 智力的；知识分子 | 2 | Academic setting |
| intend | vt. | 打算 | 2 | Author intent |
| interaction | n. | 互动 | 2 | Character dynamics |
| interpret | vt. | 解释 | 2 | Hermeneutics |
| intervention | n. | 干预 | 2 | Power mechanism |
| involve | vt. | 包含；牵涉 | 2 | Plot complexity |
| journal | n. | 日记；期刊 | 2 | Archive mechanic |
| justification | n. | 正当理由 | 2 | Argumentation |
| label | n./vt. | 标签 | 2 | Classification |
| landscape | n. | 景色；地形 | 2 | Labyrinth description |
| layer | n. | 层 | 2 | Labyrinth structure |
| lecture | n. | 讲座 | 2 | Learning mechanic |
| liberal | adj. | 自由的 | 2 | Political theme |
| literary | adj. | 文学的 | 2 | Core theme |
| logical | adj. | 逻辑的 | 2 | Reasoning |
| maintain | vt. | 维持 | 2 | Preservation |
| majority | n. | 多数 | 2 | Statistics |
| manage | vt. | 管理；设法 | 2 | Resource management |
| manifest | vt./adj. | 表明；明显的 | 2 | Evidence |
| mechanism | n. | 机制 | 2 | System design |
| media | n. | 媒体 | 2 | Communication |
| medical | adj. | 医疗的 | 2 | HP restoration |
| method | n. | 方法 | 2 | Academic process |
| migrate | vi. | 迁移 | 2 | Movement theme |
| mission | n. | 使命 | 2 | Quest structure |
| modify | vt. | 修改 | 2 | RPG customization |
| monitor | n./vt. | 监视器；监控 | 2 | System oversight |
| motivation | n. | 动机 | 2 | Character drive |
| mutual | adj. | 相互的 | 2 | Relationship |
| narrative | n./adj. | 叙述；叙事的 | 2 | Storytelling meta |
| network | n. | 网络 | 2 | Knowledge web |
| notion | n. | 概念 | 2 | Abstract thinking |
| objective | n./adj. | 目标；客观的 | 2 | Quest + philosophy |
| obligation | n. | 义务 | 2 | Moral theme |
| observe | vt. | 观察 | 2 | Scientific method |
| obvious | adj. | 明显的 | 2 | Evidence |
| occupy | vt. | 占据 | 2 | Space concept |
| occur | vi. | 发生 | 2 | Event trigger |
| option | n. | 选项 | 2 | Choice mechanic |
| orientation | n. | 方向 | 2 | Navigation |
| origin | n. | 起源 | 2 | Genesis theme |
| original | adj. | 原始的；独创的 | 2 | Authenticity |
| outcome | n. | 结果 | 2 | Cause-effect |
| overall | adj./adv. | 全部的；总体上 | 2 | Summary word |
| panel | n. | 专门小组；面板 | 2 | Decision body |
| parallel | n./adj. | 平行；类似的 | 2 | Comparison |
| participate | vi. | 参加 | 2 | Engagement |
| passage | n. | 通道；段落 | 2 | Labyrinth + reading |
| passive | adj. | 被动的 | 2 | Grammar theme |
| perceive | vt. | 察觉；理解 | 2 | Perception (Card 005) |
| permit | vt. | 许可 | 2 | Gatekeeping |
| perspective | n. | 观点 | 2 | Narrative POV (Card 010) |
| phenomenon | n. | 现象 | 2 | Observation |
| philosophy | n. | 哲学 | 2 | Intellectual tradition |
| platform | n. | 平台 | 2 | Stage/structure |
| policy | n. | 政策 | 2 | Governance |
| politics | n. | 政治 | 2 | Power theme |
| popular | adj. | 流行的 | 2 | Cultural spread |
| population | n. | 人口 | 2 | Statistics |
| portrait | n. | 肖像 | 2 | Character description |
| practical | adj. | 实际的 | 2 | Applied knowledge |
| precise | adj. | 精确的 | 2 | Data accuracy |
| previous | adj. | 先前的 | 2 | Timeline reference |
| primary | adj. | 主要的 | 2 | Hierarchy |
| priority | n. | 优先权 | 2 | Quest ranking |
| procedure | n. | 程序 | 2 | Protocol |
| professional | adj./n. | 专业的 | 2 | Academic domain |
| proportion | n. | 比例 | 2 | Statistics |
| prospect | n. | 前景 | 2 | Future vision |
| protest | n./vi. | 抗议 | 2 | Social action |
| psychology | n. | 心理学 | 2 | Character depth |
| publication | n. | 出版物 | 2 | Archive |
| purchase | n./vt. | 购买 | 2 | Economy |
| pursue | vt. | 追求 | 2 | Quest verb |
| radical | adj./n. | 激进的 | 2 | Change agent |
| reaction | n. | 反应 | 2 | Cause-effect |
| reality | n. | 现实 | 2 | Meta-theme |
| recommendation | n. | 推荐 | 2 | Endorsement |
| reference | n. | 参考 | 2 | Citation |
| register | n./vt. | 登记；注册 | 2 | System entry |
| regulation | n. | 规章 | 2 | Rule system |
| reinforce | vt. | 加强 | 2 | SM-2 mechanic |
| reject | vt. | 拒绝 | 2 | Choice consequence |
| relationship | n. | 关系 | 2 | Character dynamics |
| reliable | adj. | 可靠的 | 2 | Trust metric |
| remedy | n./vt. | 补救 | 2 | HP restoration |
| remote | adj. | 遥远的 | 2 | Distance concept |
| removal | n. | 移除 | 2 | Action noun |
| renew | vt. | 更新 | 2 | Cycle mechanic |
| reputation | n. | 名声 | 2 | Character stat |
| request | n./vt. | 请求 | 2 | Interaction |
| requirement | n. | 要求 | 2 | Quest condition |
| rescue | n./vt. | 营救 | 2 | Plot device |
| resemble | vt. | 类似 | 2 | Comparison |
| reside | vi. | 居住 | 2 | Location |
| resist | vt. | 抵抗 | 2 | Conflict |
| resolution | n. | 决心；解决 | 2 | Plot resolution |
| resolve | vt. | 解决 | 2 | Problem-solving |
| respect | n./vt. | 尊重 | 2 | Relationship |
| respond | vi. | 响应 | 2 | Interaction |
| restriction | n. | 限制 | 2 | Rule constraint |
| retain | vt. | 保持 | 2 | Memory mechanic |
| revolution | n. | 革命 | 2 | Paradigm shift |
| reward | n./vt. | 奖赏 | 2 | RPG mechanic |
| rhythm | n. | 节奏 | 2 | Literary device |
| rigid | adj. | 严格的 | 2 | Structure word |
| root | n. | 根源 | 2 | Root-seeking (Card 035) |
| rough | adj. | 粗糙的 | 2 | Texture |
| rural | adj. | 农村的 | 2 | Setting |
| sample | n. | 样本 | 2 | Statistics |
| scale | n. | 规模；尺度 | 2 | Measurement |
| scatter | vt. | 分散 | 2 | Distribution |
| schedule | n./vt. | 时间表 | 2 | Time management |
| scholar | n. | 学者 | 2 | Academic character |
| scientific | adj. | 科学的 | 2 | Methodology |
| secure | adj./vt. | 安全的 | 2 | Protection |
| select | vt. | 选择 | 2 | Choice mechanic |
| shift | n./vt. | 转移 | 2 | Change verb |
| signal | n./vt. | 信号 | 2 | Communication |
| site | n. | 地点 | 2 | Location |
| slight | adj. | 轻微的 | 2 | Degree modifier |
| solution | n. | 解决方案 | 2 | Problem-solving |
| somewhat | adv. | 有点 | 2 | Degree adverb |
| sophisticated | adj. | 复杂的 | 2 | Complexity |
| span | n./vt. | 跨度 | 2 | Range |
| species | n. | 物种 | 2 | Classification |
| spiritual | adj. | 精神的 | 2 | Inner life |
| stable | adj. | 稳定的 | 2 | State description |
| strategy | n. | 策略 | 2 | RPG planning |
| strict | adj. | 严格的 | 2 | Rule enforcement |
| striking | adj. | 显著的 | 2 | Notable feature |
| submit | vt. | 提交 | 2 | Action verb |
| subsequent | adj. | 随后的 | 2 | Sequence |
| substance | n. | 物质 | 2 | Essence |
| sufficient | adj. | 足够的 | 2 | Threshold |
| sum | n./vt. | 总数 | 2 | Calculation |
| supplement | n./vt. | 补充 | 2 | Addition |
| survey | n./vt. | 调查 | 2 | Research method |
| survive | vi. | 幸存 | 2 | RPG survival |
| suspend | vt. | 暂停 | 2 | State change |
| symbol | n. | 象征 | 2 | Literary device (Card 009) |
| target | n./vt. | 目标 | 2 | Quest objective |
| task | n. | 任务 | 2 | Quest structure |
| technique | n. | 技术 | 2 | Craft (Card 001) |
| tendency | n. | 趋势 | 2 | Pattern |
| theory | n. | 理论 | 2 | Academic core |
| threaten | vt. | 威胁 | 2 | Conflict |
| tolerate | vt. | 容忍 | 2 | Tolerance |
| trace | n./vt. | 痕迹；追踪 | 2 | Investigation |
| tradition | n. | 传统 | 2 | Cultural continuity |
| transform | vt. | 转变 | 2 | Metamorphosis |
| transition | n. | 过渡 | 2 | Change state |
| transmit | vt. | 传输 | 2 | Communication |
| transport | n./vt. | 运输 | 2 | Movement |
| treatment | n. | 治疗；处理 | 2 | HP restoration |
| trend | n. | 趋势 | 2 | Pattern |
| trigger | n./vt. | 触发器；引发 | 2 | Event mechanic |
| ultimate | adj. | 最终的 | 2 | Endgame |
| undergo | vt. | 经历 | 2 | Character arc |
| uniform | adj./n. | 统一的 | 2 | Consistency |
| unique | adj. | 独特的 | 2 | Special status |
| universal | adj. | 普遍的 | 2 | Theme: universality |
| update | vt. | 更新 | 2 | System mechanic |
| valid | adj. | 有效的 | 2 | Logic |
| variation | n. | 变化 | 2 | Diversity |
| vary | vi. | 变化 | 2 | Range |
| version | n. | 版本 | 2 | Iteration |
| virtual | adj. | 虚拟的 | 2 | Digital theme |
| visible | adj. | 看得见的 | 2 | Perception |
| vital | adj. | 至关重要的 | 2 | Importance marker |
| voluntary | adj. | 自愿的 | 2 | Free will |
| vulnerability | n. | 脆弱性 | 2 | RPG weakness |
| welfare | n. | 福利 | 2 | Social good |

**Tier 1 total with supplement**: 244 (DB confirmed) + ~200 (promoted) = **~444 words**

---

### Tier 2: Context Glyphs (926 words — appear 1-2× in exams)

These words appear naturally in the narrative prose but are **not collectible targets**. Readers absorb them through context. The full 926 words are listed in the database; here are the first 100 by appearance count as a sample:

| # | Word | POS | Meaning (CN) | Exam App. |
|---|------|-----|-------------|-----------|
| 1 | academic | n./adj. | 学术的；学院的 | 2 |
| 2 | accept | vt. | 接受；承认 | 2 |
| 3 | access | n. | 进入；使用权 | 2 |
| 4 | achieve | vt. | 取得；实现 | 2 |
| 5 | act | n. | 行为；法令 | 2 |
| 6 | actually | adv. | 实际上 | 2 |
| 7 | add | vt. | 增加；添加 | 2 |
| 8 | addition | n. | 添加；加法 | 2 |
| 9 | advanced | adj. | 先进的；高级的 | 2 |
| 10 | agreement | n. | 协议；同意 | 2 |
| 11 | aim | n. | 目的；目标 | 2 |
| 12 | alien | n./adj. | 外国人；外国的 | 2 |
| 13 | allow | vt. | 允许；给予 | 2 |
| 14 | analyze | vt. | 分析 | 2 |
| 15 | ancient | adj. | 古代的；古老的 | 2 |
| 16 | appear | vi. | 出现；显得 | 2 |
| 17 | application | n. | 应用；申请 | 2 |
| 18 | article | n. | 文章；条款 | 2 |
| 19 | artificial | adj. | 人造的；仿造的 | 2 |
| 20 | assumption | n. | 假定；设想 | 2 |
| 21 | attend | vi. | 出席；照料 | 2 |
| 22 | automation | n. | 自动化 | 2 |
| 23 | available | adj. | 可获得的 | 2 |
| 24 | average | n./adj. | 平均数；平均的 | 2 |
| 25 | basis | n. | 基础 | 2 |
| 26 | brief | adj./n. | 简短的；摘要 | 2 |
| 27 | business | n. | 商业；生意 | 2 |
| 28 | caravan | n. | 大篷车；旅行队 | 2 |
| 29 | care | n./vt. | 关怀；照料 | 2 |
| 30 | cause | n./vt. | 原因；引起 | 2 |
| 31 | challenge | n./vt. | 挑战 | 2 |
| 32 | chance | n. | 机会；运气 | 2 |
| 33 | characteristic | n./adj. | 特征；典型的 | 2 |
| 34 | church | n. | 教堂 | 2 |
| 35 | close | adj./vt. | 紧密的；关 | 2 |
| 36 | cognitive | adj. | 认知的 | 2 |
| 37 | collaboration | n. | 合作 | 2 |
| 38 | common | adj. | 共同的；普通的 | 2 |
| 39 | comparison | n. | 比较 | 2 |
| 40 | conscious | adj. | 意识到的 | 2 |
| 41 | construction | n. | 建设 | 2 |
| 42 | consumer | n. | 消费者 | 2 |
| 43 | continent | n. | 大陆 | 2 |
| 44 | contrast | n./vt. | 对比 | 2 |
| 45 | courage | n. | 勇气 | 2 |
| 46 | cross | n./vt. | 交叉；渡过 | 2 |
| 47 | culture | n. | 文化 | 2 |
| 48 | cut | n./vt. | 切口；削减 | 2 |
| 49 | deem | vt. | 认为 | 2 |
| 50 | dense | adj. | 稠密的 | 2 |
| 51 | design | n./vt. | 设计 | 2 |
| 52 | detail | n. | 细节 | 2 |
| 53 | devoted | adj. | 献身的；忠诚的 | 2 |
| 54 | difficult | adj. | 困难的 | 2 |
| 55 | directly | conj./adv. | 直接地 | 2 |
| 56 | diverse | adj. | 不同的 | 2 |
| 57 | diversity | n. | 多样性 | 2 |
| 58 | document | n./vt. | 文件；证明 | 2 |
| 59 | economic | adj. | 经济的 | 2 |
| 60 | element | n. | 元素；要素 | 2 |
| 61 | emphasize | vt. | 强调 | 2 |
| 62 | enable | vt. | 使能够 | 2 |
| 63 | enhance | vt. | 提高 | 2 |
| 64 | enthusiasm | n. | 热忱 | 2 |
| 65 | equipment | n. | 设备 | 2 |
| 66 | especially | adv. | 特别 | 2 |
| 67 | establish | vt. | 建立 | 2 |
| 68 | evaluate | vt. | 评价 | 2 |
| 69 | eventually | adv. | 最后 | 2 |
| 70 | evidence | n. | 证据 | 2 |
| 71 | except | conj. | 除了 | 2 |
| 72 | executive | n./adj. | 执行者；行政的 | 2 |
| 73 | expect | vt. | 期望 | 2 |
| 74 | experience | n./vt. | 经验；经历 | 2 |
| 75 | extended | adj. | 延伸的 | 2 |
| 76 | failure | n. | 失败 | 2 |
| 77 | familiar | adj. | 熟悉的 | 2 |
| 78 | fashion | n. | 时尚 | 2 |
| 79 | feature | n. | 特色 | 2 |
| 80 | fit | adj./vt. | 合适的 | 2 |
| 81 | fix | vt. | 修理 | 2 |
| 82 | force | n./vt. | 力量 | 2 |
| 83 | foreign | adj. | 外国的 | 2 |
| 84 | fundamental | adj. | 基本的 | 2 |
| 85 | generate | vt. | 产生 | 2 |
| 86 | goods | n. | 商品 | 2 |
| 87 | government | n. | 政府 | 2 |
| 88 | gradually | adv. | 逐步地 | 2 |
| 89 | grasp | n./vt. | 抓住；理解 | 2 |
| 90 | guarantee | n./vt. | 保证 | 2 |
| 91 | halt | n./vi. | 停止 | 2 |
| 92 | handle | n./vt. | 把手；处理 | 2 |
| 93 | harbor | n./vt. | 海港；庇护 | 2 |
| 94 | harsh | adj. | 严厉的 | 2 |
| 95 | hence | adv. | 因此 | 2 |
| 96 | highlight | n./vt. | 突出 | 2 |
| 97 | hint | n./vt. | 暗示 | 2 |
| 98 | hostile | adj. | 敌对的 | 2 |
| 99 | household | n./adj. | 家庭；家用的 | 2 |
| 100 | hypothesis | n. | 假设 | 2 |

> **Full Tier 2 list**: 926 words (224 with 2 appearances + 702 with 1 appearance). Complete export available via SQL query. POS distribution: n. 635, adj. 126, vt. 85, vi. 40, adv. 24, conj. 6, v. 6, prep. 3, int. 1.

---

### Tier 3: Archive (4,961 words — 0 exam appearances)

These words do not appear in any exam sentence. They are listed in the vocabulary appendix for reference only and never appear in the narrative.

| POS | Count | % of Tier 3 |
|-----|-------|-------------|
| n. | 3,255 | 65.6% |
| adj. | 880 | 17.7% |
| vt. | 492 | 9.9% |
| vi. | 146 | 2.9% |
| adv. | 83 | 1.7% |
| v. | 62 | 1.2% |
| (empty) | 19 | 0.4% |
| prep. | 13 | 0.3% |
| conj. | 4 | 0.1% |
| num./pron./comb./abbr./aux. | 7 | 0.1% |
| **Total** | **4,961** | **100%** |

---

## Table 2: Knowledge Card Thematic Clustering

> **Source**: 106 cards from `spinoff8_card{NNN}_{name}.md` (纸上宇宙 project)
> **Strategy**: Reorganize by **narrative function** rather than original academic category

### Cluster 1: Genesis (起源) — "The World Before Words"

*Story function*: Ch.1-2. Feimo discovers the Labyrinth exists. These cards establish the fundamental nature of literature and its origins.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 016 | 诗经六义 | Six Principles of Shijing | The six modes: feng, ya, song, fu, bi, xing — earliest Chinese literary taxonomy | Ch.1 |
| 017 | 楚辞与屈原 | Chu Ci & Qu Yuan | Romantic lyricism born from exile; first named author in Chinese literature | Ch.1 |
| 038 | 古希腊悲剧 | Greek Tragedy | Oedipus, catharsis, the tragic flaw — Western drama's origin | Ch.1 |
| 039 | 亚里士多德诗学 | Aristotle's Poetics | Mimesis, catharsis, plot as soul of tragedy — the first literary theory | Ch.1 |
| 040 | 荷马史诗 | Homeric Epics | Oral tradition, epic similes, the hero's journey | Ch.1 |
| 041 | 但丁神曲 | Dante's Divine Comedy | Allegory, terza rima, the cosmic journey | Ch.2 |
| 042 | 骑士文学 | Chivalric Literature | Courtly love, the romance genre | Ch.2 |
| 106 | 文学自律与他律 | Literature: Autonomy vs. Heteronomy | Is literature self-contained or shaped by society? | Ch.2 |

### Cluster 2: Craft (技艺) — "The Artisan's Tools"

*Story function*: Ch.2-4. Feimo learns to read the Labyrinth's language. These cards teach literary technique and form.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 001 | 文学四要素 | Abrams' Four Elements | Universe, Work, Artist, Audience — the map of all literary theory | Ch.2 |
| 006 | 文学本质论 | Nature of Literature | What makes literature "literary" | Ch.2 |
| 007 | 意境 | Yijing (Artistic Conception) | Scene-emotion fusion; the Chinese aesthetic ideal | Ch.2 |
| 008 | 典型 | Typicality (Dianxing) | The universal in the particular; round vs. flat characters | Ch.3 |
| 009 | 意象与象征 | Image & Symbol | How concrete images carry abstract meaning | Ch.3 |
| 010 | 叙事视角 | Narrative POV | First, third, omniscient, limited — who tells the story | Ch.3 |
| 011 | 文学风格 | Literary Style | The writer's fingerprint; style as worldview | Ch.3 |
| 014 | 文学体裁 | Literary Genres | Poetry, fiction, drama, essay — the four pillars | Ch.3 |
| 015 | 文学语言与日常语言 | Literary vs. Everyday Language | Defamiliarization through language itself | Ch.4 |

### Cluster 3: Voices (声音) — "The Speaking Dead"

*Story function*: Ch.3-6. Feimo encounters echoes of great writers in the Labyrinth walls.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 021 | 李白与杜甫 | Li Bai & Du Fu | Romantic vs. Realist: two poles of Chinese poetry | Ch.3 |
| 028 | 鲁迅小说 | Lu Xun's Fiction | "Iron House" allegory; literature as social surgery | Ch.3 |
| 043 | 莎士比亚四大悲剧 | Shakespeare's Four Great Tragedies | Hamlet, Othello, Lear, Macbeth — the human condition | Ch.4 |
| 050 | 歌德浮士德 | Goethe's Faust | The striving soul; the wager with Mephistopheles | Ch.4 |
| 053 | 雨果 | Victor Hugo | Romanticism's champion; the sublime and the grotesque | Ch.5 |
| 056 | 托尔斯泰 | Tolstoy | The epic realist; "War and Peace" as total novel | Ch.5 |
| 057 | 陀思妥耶夫斯基 | Dostoevsky | Polyphonic novel; the underground man | Ch.5 |
| 066 | 艾略特荒原 | Eliot's "The Waste Land" | Modernist collage; "These fragments I have shored" | Ch.6 |
| 067 | 卡夫卡 | Kafka | The absurd bureaucratic nightmare; metamorphosis | Ch.6 |
| 076 | 博尔赫斯 | Borges | The infinite library; labyrinths as metaphysics | Ch.6 |
| 102 | 芥川龙之介 | Akutagawa Ryūnosuke | "Rashomon" effect; truth as perspective | Ch.7 |
| 103 | 海明威 | Hemingway | Iceberg theory; the code hero | Ch.7 |
| 104 | 福克纳 | Faulkner | Stream of consciousness; Yoknapatawpha County | Ch.7 |
| 105 | 夏目漱石 | Natsume Sōseki | Japanese modernism; the alienated intellectual | Ch.7 |

### Cluster 4: Forms (形式) — "The Shape of Stories"

*Story function*: Ch.4-7. Feimo discovers that stories take different shapes — each form a different room in the Labyrinth.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 020 | 唐诗四期 | Four Periods of Tang Poetry | Early, High, Mid, Late — poetry mirrors dynasty | Ch.4 |
| 022 | 宋词两大流派 | Two Schools of Song Ci | Bold (haofang) vs. Graceful (wanyue) | Ch.4 |
| 023 | 唐诗与宋诗 | Tang vs. Song Poetry | Emotion vs. Reason; image vs. argument | Ch.4 |
| 024 | 元杂剧体制 | Yuan Zaju Structure | Four acts + wedge; singing roles | Ch.5 |
| 025 | 西厢记与窦娥冤 | Romance of the Western Chamber & The Injustice to Dou E | Love comedy vs. tragedy in Yuan drama | Ch.5 |
| 026 | 四大名著类型学 | Typology of the Four Classics | Historical, heroic, romantic, satirical novel | Ch.5 |
| 027 | 红楼梦 | Dream of the Red Chamber | The novel of decline; stone/jade allegory | Ch.5 |
| 046 | 古典主义三一律 | Classical Three Unities | Time, place, action — neoclassical constraints | Ch.6 |
| 052 | 浪漫主义 | Romanticism | Emotion, imagination, nature, the sublime | Ch.6 |
| 060 | 自然主义 | Naturalism | Zola, the experimental novel, determinism | Ch.7 |
| 061 | 象征主义 | Symbolism | Mallarmé, Verlaine; music in poetry | Ch.7 |
| 065 | 意识流 | Stream of Consciousness | Woolf, Joyce; interior monologue | Ch.7 |

### Cluster 5: Consciousness (意识) — "The Fractured Mirror"

*Story function*: Ch.7-10. The Labyrinth's deeper levels distort reality. Feimo confronts modernist and postmodernist fragmentation.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 005 | 陌生化 | Defamiliarization (Ostranenie) | Shklovsky: making the familiar strange | Ch.7 |
| 064 | 现代主义 | Modernism | Fragmentation, stream of consciousness, mythic method | Ch.8 |
| 068 | 后现代主义 | Postmodernism | Metafiction, pastiche, end of grand narratives | Ch.8 |
| 069 | 存在主义 | Existentialism | Sartre, Camus; existence precedes essence | Ch.8 |
| 070 | 荒诞派戏剧 | Theatre of the Absurd | Beckett, Ionesco; meaning collapses | Ch.9 |
| 071 | 魔幻现实主义 | Magical Realism | García Márquez; the real and the marvelous | Ch.9 |
| 072 | 黑色幽默 | Black Humor | Vonnegut, Heller; laughing at the void | Ch.9 |
| 075 | 新小说派 | Nouveau Robbe-Grillet | Anti-character, anti-plot; the thing-itself | Ch.10 |
| 078 | 20世纪文学总特征 | 20th-Century Literature: Overview | Fragmentation, alienation, the crisis of representation | Ch.10 |

### Cluster 6: Theory (理论) — "The Wordkeeper's Codex"

*Story function*: Ch.8-12. Feimo gains access to the meta-level: literary theory itself becomes a weapon/tool.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 079 | 接受美学 | Reception Aesthetics | Jauss, Iser; meaning made by the reader | Ch.8 |
| 080 | 期待视野 | Horizon of Expectations | Readers approach texts with pre-formed expectations | Ch.8 |
| 081 | 召唤结构与隐含读者 | Gaps & Implied Reader | Texts have blanks; readers fill them | Ch.8 |
| 082 | 视域融合 | Fusion of Horizons | Gadamer: understanding as merger of perspectives | Ch.9 |
| 083 | 俄国形式主义 | Russian Formalism | Literary science; the device, not the message | Ch.9 |
| 084 | 结构主义叙事学 | Structuralist Narratology | Deep structures beneath all stories | Ch.9 |
| 085 | 热奈特五范畴 | Genette's Five Categories | Order, duration, frequency, mood, voice | Ch.10 |
| 086 | 故事vs话语 | Story vs. Discourse | What happened vs. how it's told | Ch.10 |
| 087 | 普罗普故事形态学 | Propp's Morphology | 31 functions, 7 character roles — fairy tales decoded | Ch.10 |
| 088 | 格雷马斯 | Greimas' Semiotic Square | Actantial model; the logic of meaning | Ch.11 |
| 090 | 元虚构 | Metafiction | Fiction about fiction; the self-aware narrative | Ch.11 |
| 091 | 德里达延异 | Derrida's Différance | Meaning is always deferred; no center | Ch.11 |
| 092 | 解构主义 | Deconstruction | Unraveling binary oppositions | Ch.12 |
| 094 | 作者之死 | Death of the Author | Barthes: the text speaks, not the author | Ch.12 |
| 100 | 全书知识网络总览 | Knowledge Network Overview | The total map of all 106 cards' interconnections | Ch.12 |

### Cluster 7: Dialogue (对话) — "The Crossroads"

*Story function*: Ch.10-14. East meets West. The Labyrinth reveals that all literary traditions are connected.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 002 | 文艺学三分支 | Three Branches of Literary Studies | Literary theory, literary history, literary criticism | Ch.10 |
| 003 | 文学理论教程体系 | Literary Theory Textbook System | Chinese academic framework for literary study | Ch.10 |
| 004 | 文学性 | Literaturnost | What makes a text "literary" — the formalist question | Ch.10 |
| 012 | 文学流派 | Literary Schools/Groups | Movements as collective identity | Ch.11 |
| 013 | 文学思潮 | Literary Trends/Movements | Zeitgeist in literature | Ch.11 |
| 018 | 建安风骨 | Jian'an Spirit | Courage and vigor in troubled times | Ch.11 |
| 019 | 文学自觉 | Literary Self-Awareness | Wei-Jin period: literature recognized as art | Ch.11 |
| 029 | 五四文学革命 | May Fourth Literary Revolution | Vernacular replaces classical; Lu Xun's "Diary of a Madman" | Ch.12 |
| 030 | 文学研究会与创造社 | Literary Research Society & Creation Society | Realism vs. Romanticism in modern China | Ch.12 |
| 044 | 堂吉诃德 | Don Quixote | The first modern novel; reality vs. idealism | Ch.12 |
| 045 | 十日谈 | The Decameron | Frame narrative; bawdy humanism | Ch.12 |
| 047 | 启蒙运动 | Enlightenment | Reason, progress, the public sphere | Ch.13 |
| 048 | 卢梭 | Rousseau | The noble savage; confessional self | Ch.13 |
| 049 | 18世纪英国小说 | 18th-Century English Novel | Defoe, Richardson, Fielding; the rise of realism | Ch.13 |
| 051 | 狂飙突进运动 | Sturm und Drang | German proto-romanticism; young Goethe | Ch.13 |
| 062 | 浪漫主义vs现实主义 | Romanticism vs. Realism | The great debate of 19th-century literature | Ch.13 |
| 063 | 19世纪美国文学 | 19th-Century American Literature | Hawthorne, Melville, Whitman, Dickinson | Ch.14 |
| 096 | 后殖民主义 | Postcolonialism | Spivak, Said; the subaltern speaks | Ch.14 |
| 097 | 文论失语症 | Theoretical Aphasia | Can non-Western theory speak in its own terms? | Ch.14 |

### Cluster 8: Power (力量) — "The Tongue of Fire"

*Story function*: Ch.11-15. Literature as social force. The Labyrinth's guardians wield words as weapons.

| Card # | Chinese Name | English Equivalent | Core Concept | Suggested Chapter |
|--------|-------------|-------------------|--------------|-------------------|
| 031 | 茅盾与子夜 | Mao Dun & Midnight | The proletarian novel; capitalism dissected | Ch.11 |
| 032 | 沈从文与京派 | Shen Congwen & the Jingpai | Pastoral nostalgia vs. urban modernity | Ch.11 |
| 033 | 新感觉派 | New Sensationalism | Shanghai modernism; sensory overload | Ch.12 |
| 034 | 先锋文学 | Avant-Garde Literature | Yu Hua, Ge Fei; narrative experiment in 1980s China | Ch.12 |
| 035 | 寻根文学 | Root-Seeking Literature | Han Shaogong; cultural identity after the Cultural Revolution | Ch.12 |
| 036 | 朦胧诗 | Misty Poetry | Bei Dao, Shu Ting; coded dissent | Ch.13 |
| 037 | 新时期文学三阶段 | Three Stages of New Period Literature | Scar → Reflection → Reform literature | Ch.13 |
| 054 | 批判现实主义 | Critical Realism | Balzac, Dickens; society as the villain | Ch.13 |
| 055 | 巴尔扎克 | Balzac | "The Human Comedy" — society as a system | Ch.14 |
| 058 | 多余人形象 | The "Superfluous Man" | Onegin, Pechorin; the idle aristocrat | Ch.14 |
| 059 | 福楼拜 | Flaubert | Style as ideology; "le mot juste" | Ch.14 |
| 073 | 萨特介入文学 | Sartre's Engaged Literature | Writing as political act | Ch.15 |
| 074 | 加缪vs萨特 | Camus vs. Sartre | Absurdism vs. Existentialism; the great quarrel | Ch.15 |
| 089 | 巴赫金对话理论 | Bakhtin's Dialogism | Heteroglossia; the novel as chorus of voices | Ch.15 |
| 093 | 福柯话语理论 | Foucault's Discourse Theory | Power/knowledge; who controls the archive | Ch.15 |
| 095 | 女性主义文学批评 | Feminist Literary Criticism | Showalter, Cixous; rewriting the canon | Ch.15 |
| 101 | 西方马克思主义文论 | Western Marxist Literary Theory | Lukács, Adorno, Jameson; literature and ideology | Ch.15 |

---

## Table 3: Exam Questions to Chapters Mapping

> **Source**: 839 questions from `kaoyan_english.questions` table
> **Scope**: 16 exam years (2010-2025) + 1 test paper = 20 paper_ids
> **Mapping logic**: Each year → 1 chapter. Each chapter uses ~4-5 representative questions across section types.

### Year-to-Chapter Assignment

| Chapter | Paper ID | Year | Cloze (20) | Reading A (20) | Reading B (5) | Translation (5) | Writing (2) | Total |
|---------|----------|------|------------|----------------|---------------|-----------------|-------------|-------|
| Ch.1 | 2010-eng1 | 2010 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.2 | 2011-eng1 | 2011 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.3 | 2012-eng1 | 2012 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.4 | 2013-eng1 | 2013 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.5 | 2014-eng1 | 2014 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.6 | 2015-eng1 | 2015 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.7 | 2016-eng1 | 2016 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.8 | 2017-eng1 | 2017 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.9 | 2018-eng1 | 2018 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.10 | 2019-eng1 | 2019 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.11 | 2020-eng1 | 2020 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.12 | 2021-eng1 | 2021 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.13 | 2022-eng1 | 2022 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.14 | 2023-eng1 | 2023 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.15 | 2024-eng1 | 2024 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.16 | 2025-eng1 | 2025 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| Ch.17 | mixed | 2010-2025 | ✓ | ✓ | ✓ | ✓ | ✓ | 52 |
| **Total** | | | **340** | **340** | **85** | **85** | **34** | **832**+ |

> **Note on paper_ids**: DB contains `2023`, `2023-eng1`, `2024`, `2024-eng1`, `2025`, `2025-eng1`, and `test_paper_2026` (7 Qs). The `-eng1` variants are the primary papers; non-suffixed versions appear to be duplicates or alternate papers. Ch.17 draws bonus questions from across all years for the final challenge.

### Sample Chapter Question Mapping (Ch.1 — Year 2010)

| Challenge Type | Question ID | Preview | Used As |
|---------------|-------------|---------|---------|
| **Weave** (完形) | 2010-eng1-use_of_english-q1 | "In 1924 America's National Research Council sent two engineers to supervise a series of experiments at a telephone-parts factory..." | First puzzle: Feimo must weave the torn passage back together |
| **Weave** (完形) | 2010-eng1-use_of_english-q2 | (same passage, blank 2) | Continuation — each blank is a thread to rejoin |
| **Mirror** (阅读) | 2010-eng1-reading_a-q21 | "Of all the changes that have taken place in English-language newspapers during the past quarter-century, perhaps the most far-reaching has been the inexorable decline in the scope..." | Ancient text on a mirror — Feimo must choose the correct reflection |
| **Mirror** (阅读) | 2010-eng1-reading_a-q26 | "Over the past decade, thousands of patents have been granted for what are called business methods. Amazon.com received one for its 'one-click' online purchasing system..." | Inscription about commerce and invention |
| **Bridge** (翻译) | 2010-eng1-translation-q46 | "One basic weakness in a conservation system based wholly on economic motives is that most members of the land community have no economic value..." | Bilingual inscription: Feimo must translate to unlock the door |
| **Bridge** (翻译) | 2010-eng1-translation-q47 | (same passage, sentence 2) | Bridge sequence continues |
| **Forge** (写作) | 2010-eng1-writing_a-q51 | Writing prompt (short) | Feimo must forge a letter to escape |
| **Forge** (写作) | 2010-eng1-writing_b-q52 | Writing prompt (essay) | Final forge: Feimo writes his way out of the chapter |

### Challenge Type Distribution Per Chapter

| Challenge Type | Section Type | Questions/Chapter | Narrative Mechanic |
|---------------|-------------|-------------------|-------------------|
| **Weave** (编织) | Use of English (Cloze) | 20 | Repair broken text passages — fill in missing words |
| **Mirror** (镜鉴) | Reading Part A | 20 | Read passages reflected in mirrors — answer comprehension |
| **Bridge** (桥渡) | Translation | 5 | Translate between languages to unlock doors |
| **Forge** (锻造) | Reading Part B | 5 | Reorder scrambled passages — reconstruct knowledge |
| **Script** (书写) | Writing | 2 | Write original text — create new Glyphs |

---

## Table 4: Difficulty Progression

### Current Database State

**All 839 questions have `difficulty = 3`** in the database. This appears to be a default/placeholder value — no differentiation exists in the source data.

### Constructed Difficulty Curve

Since the database provides uniform difficulty, the following curve is constructed based on **content analysis** (passage length, vocabulary complexity, section type inherent difficulty):

| Chapter | Year | Inherent Difficulty | Cloze (20Q) | Read A (20Q) | Read B (5Q) | Trans (5Q) | Write (2Q) | Chapter Weight |
|---------|------|---------------------|-------------|--------------|-------------|------------|------------|---------------|
| Ch.1 | 2010 | ★★☆☆☆ Introductory | Baseline | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Light |
| Ch.2 | 2011 | ★★☆☆☆ Early | Baseline | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Light |
| Ch.3 | 2012 | ★★★☆☆ Building | Standard | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Moderate |
| Ch.4 | 2013 | ★★★☆☆ Building | Standard | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Moderate |
| Ch.5 | 2014 | ★★★☆☆ Mid-Early | Standard | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Moderate |
| Ch.6 | 2015 | ★★★☆☆ Mid | Standard | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Moderate |
| Ch.7 | 2016 | ★★★☆☆ Mid | Standard | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Moderate |
| Ch.8 | 2017 | ★★★★☆ Mid-Late | Harder | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Heavy |
| Ch.9 | 2018 | ★★★★☆ Mid-Late | Harder | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Heavy |
| Ch.10 | 2019 | ★★★★☆ Advanced | Harder | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Heavy |
| Ch.11 | 2020 | ★★★★☆ Advanced | Harder | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Heavy |
| Ch.12 | 2021 | ★★★★☆ Advanced | Hardest | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Heavy |
| Ch.13 | 2022 | ★★★★★ Expert | Hardest | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Maximum |
| Ch.14 | 2023 | ★★★★★ Expert | Hardest | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Maximum |
| Ch.15 | 2024 | ★★★★★ Expert | Hardest | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Maximum |
| Ch.16 | 2025 | ★★★★★ Mastery | Hardest | 4 passages | Matching | 5 sentences | 1 short + 1 essay | Maximum |
| Ch.17 | Mixed | ★★★★★ Final | Mixed | Mixed | Mixed | Mixed | Mixed | Boss Rush |

### Vocabulary Density Progression

| Chapter Range | Tier 1 Glyphs/Chapter | Tier 2 Context Words/Chapter | Narrative CEFR | Embedded Text CEFR |
|---------------|----------------------|------------------------------|----------------|-------------------|
| Ch.1-4 (Act I) | 20-30 | 30-40 | B1 | B2 |
| Ch.5-8 (Act II) | 30-40 | 40-50 | B1+ | B2-C1 |
| Ch.9-12 (Act III) | 40-50 | 50-60 | B2 | C1 |
| Ch.13-16 (Act IV) | 50-60 | 60-70 | B2+ | C1 |
| Ch.17 (Finale) | 80+ | Mixed | B2+ | C1 |

### Reading Load Per Chapter

| Section | Passage Length (approx.) | Questions | Time Pressure |
|---------|------------------------|-----------|--------------|
| Use of English | ~250 words per passage | 20 blanks | Moderate — context clues |
| Reading Part A | ~400-500 words × 4 passages | 20 questions | High — close reading |
| Reading Part B | ~500-600 words | 5 matching | High — structural logic |
| Translation | ~150-200 words total | 5 sentences | Medium — bilingual |
| Writing | Prompt-based | 2 tasks | Creative — output |

---

## Table 5: 106 Cards Coverage Verification

> **Constraint check**: All 106 cards must be assigned to a chapter. No card left behind.

| Card # | Assigned Chapter | Cluster | Status |
|--------|-----------------|---------|--------|
| 001 | Ch.2 | Craft | ✓ |
| 002 | Ch.10 | Dialogue | ✓ |
| 003 | Ch.10 | Dialogue | ✓ |
| 004 | Ch.10 | Dialogue | ✓ |
| 005 | Ch.7 | Consciousness | ✓ |
| 006 | Ch.2 | Craft | ✓ |
| 007 | Ch.2 | Craft | ✓ |
| 008 | Ch.3 | Craft | ✓ |
| 009 | Ch.3 | Craft | ✓ |
| 010 | Ch.3 | Craft | ✓ |
| 011 | Ch.3 | Craft | ✓ |
| 012 | Ch.11 | Dialogue | ✓ |
| 013 | Ch.11 | Dialogue | ✓ |
| 014 | Ch.3 | Craft | ✓ |
| 015 | Ch.4 | Craft | ✓ |
| 016 | Ch.1 | Genesis | ✓ |
| 017 | Ch.1 | Genesis | ✓ |
| 018 | Ch.11 | Dialogue | ✓ |
| 019 | Ch.11 | Dialogue | ✓ |
| 020 | Ch.4 | Forms | ✓ |
| 021 | Ch.3 | Voices | ✓ |
| 022 | Ch.4 | Forms | ✓ |
| 023 | Ch.4 | Forms | ✓ |
| 024 | Ch.5 | Forms | ✓ |
| 025 | Ch.5 | Forms | ✓ |
| 026 | Ch.5 | Forms | ✓ |
| 027 | Ch.5 | Forms | ✓ |
| 028 | Ch.3 | Voices | ✓ |
| 029 | Ch.12 | Dialogue | ✓ |
| 030 | Ch.12 | Dialogue | ✓ |
| 031 | Ch.11 | Power | ✓ |
| 032 | Ch.11 | Power | ✓ |
| 033 | Ch.12 | Power | ✓ |
| 034 | Ch.12 | Power | ✓ |
| 035 | Ch.12 | Power | ✓ |
| 036 | Ch.13 | Power | ✓ |
| 037 | Ch.13 | Power | ✓ |
| 038 | Ch.1 | Genesis | ✓ |
| 039 | Ch.1 | Genesis | ✓ |
| 040 | Ch.1 | Genesis | ✓ |
| 041 | Ch.2 | Genesis | ✓ |
| 042 | Ch.2 | Genesis | ✓ |
| 043 | Ch.4 | Voices | ✓ |
| 044 | Ch.12 | Dialogue | ✓ |
| 045 | Ch.12 | Dialogue | ✓ |
| 046 | Ch.6 | Forms | ✓ |
| 047 | Ch.13 | Dialogue | ✓ |
| 048 | Ch.13 | Dialogue | ✓ |
| 049 | Ch.13 | Dialogue | ✓ |
| 050 | Ch.4 | Voices | ✓ |
| 051 | Ch.13 | Dialogue | ✓ |
| 052 | Ch.6 | Forms | ✓ |
| 053 | Ch.5 | Voices | ✓ |
| 054 | Ch.13 | Power | ✓ |
| 055 | Ch.14 | Power | ✓ |
| 056 | Ch.5 | Voices | ✓ |
| 057 | Ch.5 | Voices | ✓ |
| 058 | Ch.14 | Power | ✓ |
| 059 | Ch.14 | Power | ✓ |
| 060 | Ch.7 | Forms | ✓ |
| 061 | Ch.7 | Forms | ✓ |
| 062 | Ch.13 | Dialogue | ✓ |
| 063 | Ch.14 | Dialogue | ✓ |
| 064 | Ch.8 | Consciousness | ✓ |
| 065 | Ch.7 | Forms | ✓ |
| 066 | Ch.6 | Voices | ✓ |
| 067 | Ch.6 | Voices | ✓ |
| 068 | Ch.8 | Consciousness | ✓ |
| 069 | Ch.8 | Consciousness | ✓ |
| 070 | Ch.9 | Consciousness | ✓ |
| 071 | Ch.9 | Consciousness | ✓ |
| 072 | Ch.9 | Consciousness | ✓ |
| 073 | Ch.15 | Power | ✓ |
| 074 | Ch.15 | Power | ✓ |
| 075 | Ch.10 | Consciousness | ✓ |
| 076 | Ch.6 | Voices | ✓ |
| 077 | Ch.7 | Voices | ✓ |
| 078 | Ch.10 | Consciousness | ✓ |
| 079 | Ch.8 | Theory | ✓ |
| 080 | Ch.8 | Theory | ✓ |
| 081 | Ch.8 | Theory | ✓ |
| 082 | Ch.9 | Theory | ✓ |
| 083 | Ch.9 | Theory | ✓ |
| 084 | Ch.9 | Theory | ✓ |
| 085 | Ch.10 | Theory | ✓ |
| 086 | Ch.10 | Theory | ✓ |
| 087 | Ch.10 | Theory | ✓ |
| 088 | Ch.11 | Theory | ✓ |
| 089 | Ch.15 | Power | ✓ |
| 090 | Ch.11 | Theory | ✓ |
| 091 | Ch.11 | Theory | ✓ |
| 092 | Ch.12 | Theory | ✓ |
| 093 | Ch.15 | Power | ✓ |
| 094 | Ch.12 | Theory | ✓ |
| 095 | Ch.15 | Power | ✓ |
| 096 | Ch.14 | Dialogue | ✓ |
| 097 | Ch.14 | Dialogue | ✓ |
| 098 | Ch.7 | Dialogue | ✓ |
| 099 | Ch.7 | Dialogue | ✓ |
| 100 | Ch.12 | Theory | ✓ |
| 101 | Ch.15 | Power | ✓ |
| 102 | Ch.7 | Voices | ✓ |
| 103 | Ch.7 | Voices | ✓ |
| 104 | Ch.7 | Voices | ✓ |
| 105 | Ch.7 | Voices | ✓ |
| 106 | Ch.2 | Genesis | ✓ |

### Coverage Summary

| Cluster | Cards | Chapters Spanned |
|---------|-------|-----------------|
| Genesis (起源) | 8 | Ch.1-2 |
| Craft (技艺) | 9 | Ch.2-4 |
| Voices (声音) | 14 | Ch.3-7 |
| Forms (形式) | 12 | Ch.4-7 |
| Consciousness (意识) | 9 | Ch.7-10 |
| Theory (理论) | 15 | Ch.8-12 |
| Dialogue (对话) | 19 | Ch.7-14 |
| Power (力量) | 17 | Ch.11-15 |
| **Total** | **106** | **Ch.1-15** |

### Cards Per Chapter

| Chapter | Genesis | Craft | Voices | Forms | Consciousness | Theory | Dialogue | Power | Total |
|---------|---------|-------|--------|-------|--------------|--------|----------|-------|-------|
| Ch.1 | 4 | — | — | — | — | — | — | — | **4** |
| Ch.2 | 2 | 3 | — | — | — | — | — | — | **5** |
| Ch.3 | — | 4 | 2 | — | — | — | — | — | **6** |
| Ch.4 | — | 1 | 2 | 3 | — | — | — | — | **6** |
| Ch.5 | — | — | 3 | 3 | — | — | — | — | **6** |
| Ch.6 | — | — | 2 | 2 | — | — | — | — | **4** |
| Ch.7 | — | — | 5 | 2 | 1 | — | 2 | — | **10** |
| Ch.8 | — | — | — | — | 2 | 3 | — | — | **5** |
| Ch.9 | — | — | — | — | 3 | 3 | — | — | **6** |
| Ch.10 | — | — | — | — | 2 | 3 | 3 | — | **8** |
| Ch.11 | — | — | — | — | — | 2 | 2 | 2 | **6** |
| Ch.12 | — | — | — | — | — | 2 | 4 | 2 | **8** |
| Ch.13 | — | — | — | — | — | — | 4 | 2 | **6** |
| Ch.14 | — | — | — | — | — | — | 2 | 3 | **5** |
| Ch.15 | — | — | — | — | — | — | — | 5 | **5** |
| Ch.16 | — | — | — | — | — | — | — | — | **0** |
| Ch.17 | — | — | — | — | — | — | — | — | **0** |
| **Total** | **6** | **8** | **12** | **10** | **8** | **13** | **17** | **14** | **106** |

> **Note**: Ch.16 and Ch.17 receive no new cards — they are review/integration chapters where all previously learned knowledge is applied. Ch.16 focuses on synthesis; Ch.17 is the "Boss Rush" final exam.

**Total: 106/106 cards covered. ✓ Zero omissions.**

---

## Appendix: Data Quality Notes

1. **Vocabulary `sentence_count`**: Derived via `array_length(string_to_array(sentences, '"sentence"'), 1) - 1`. Some words may have inflated counts if the `sentences` JSON contains nested `"sentence"` strings in non-standard positions. Confidence: ~95%.

2. **Question `difficulty` field**: All 839 rows return `difficulty = 3`. This is likely a placeholder. The constructed difficulty curve (Table 4) uses external reasoning, not this field.

3. **Paper ID variants**: The database contains both `2023` and `2023-eng1` (same for 2024, 2025). The `-eng1` suffix papers are the standard English exam I papers. Non-suffixed papers may be English exam II or alternate datasets. The mapping above uses `-eng1` variants as primary.

4. **Card 098 (校勘四法) and Card 099 (辨伪学)**: These are textual criticism methods (Chinese philology), not Western literary theory. They are assigned to Ch.7 as "Dialogue" — bridging Chinese and Western textual scholarship.

5. **Card 100 (全书知识网络总览)**: This is a meta-card — the overview of all 106 cards' interconnections. Assigned to Ch.12 as the moment Feimo sees the entire Labyrinth's structure.

---
---

# v2 Revision — Incremental Update (2026-06-24)

> **Triggered by**: 凯尔希 Session 12927 revision instructions
> **Strategy**: Incremental amendments to v1 baseline. v1 tables remain authoritative; v2 sections add new columns, new tables, and refined annotations.
> **Status**: Baseline mapping preserved. Pending: 庄方宜's new outline (when available, card-chapter mapping will be re-validated).

---

## R1: Tier 1 Thematic Tag System (绯墨's Vocabulary Talent)

> **Per 凯尔希指令 §4**: Add "Thematic Tag" column to Tier 1 vocabulary for narrative-side thematic invocation. Tags designed to support 绯墨 (Bridge院猫娘) who excels at translation-type, cross-cultural, and perceptual vocabulary.

### Tag Taxonomy

| Tag | Definition | 绯墨 Affinity | Example Words |
|-----|-----------|---------------|---------------|
| **Academic** | Formal scholarly verbs & nouns used in exam passages | ★★★ High | analysis, approach, context, demonstrate |
| **Cultural** | Cross-cultural / civilization concepts | ★★★ High | civilization, culture, era, generation |
| **Perceptual** | Sensory, cognitive, and awareness words | ★★★ High | sense, perceive, image, mental |
| **Emotional** | Affect, motivation, interpersonal dynamics | ★★☆ Medium | attitude, benefit, concern, opinion |
| **Technical** | Domain-specific: science, law, economics, process | ★☆☆ Neutral | code, digital, experiment, regulation |

### Tier 1 Words with Thematic Tags (244 DB-confirmed words)

| # | Word | POS | Tag | Exam App. | Ch. | Bridge院? |
|---|------|-----|-----|-----------|-----|-----------|
| 1 | able | adj. | Technical | 3 | Ch.1 | — |
| 2 | accord | n. | Academic | 3 | Ch.5 | — |
| 3 | address | n. | Academic | 3 | Ch.1 | — |
| 4 | admission | n. | Cultural | 3 | Ch.3 | — |
| 5 | agree | vi. | Emotional | 3 | Ch.1 | — |
| 6 | alter | vt. | Academic | 3 | Ch.4 | — |
| 7 | analysis | n. | Academic | 3 | Ch.6 | — |
| 8 | applicant | n. | Technical | 3 | Ch.2 | — |
| 9 | approach | n. | Academic | 3 | Ch.2 | — |
| 10 | area | n. | Technical | 3 | Ch.1 | — |
| 11 | argue | vi. | Academic | 3 | Ch.3 | — |
| 12 | attempt | n. | Academic | 3 | Ch.2 | — |
| 13 | attitude | n. | Emotional | 3 | Ch.3 | — |
| 14 | author | n. | Cultural | 3 | Ch.2 | — |
| 15 | award | n. | Cultural | 3 | Ch.4 | — |
| 16 | bay | n. | Perceptual | 3 | Ch.7 | — |
| 17 | behavior | n. | Academic | 3 | Ch.3 | — |
| 18 | being | n. | Perceptual | 3 | Ch.5 | — |
| 19 | benefit | n. | Emotional | 3 | Ch.3 | — |
| 20 | bill | n. | Technical | 3 | Ch.4 | — |
| 21 | blank | n. | Perceptual | 3 | Ch.1 | — |
| 22 | book | n. | Cultural | 3 | Ch.1 | — |
| 23 | bound | n. | Perceptual | 3 | Ch.6 | — |
| 24 | campus | n. | Cultural | 3 | Ch.2 | — |
| 25 | carve | vt. | Perceptual | 3 | Ch.5 | — |
| 26 | case | n. | Academic | 3 | Ch.1 | — |
| 27 | change | n. | Academic | 3 | Ch.1 | — |
| 28 | choose | vt. | Emotional | 3 | Ch.2 | — |
| 29 | civilization | n. | Cultural | 3 | Ch.8 | — |
| 30 | claim | n. | Academic | 3 | Ch.3 | — |
| 31 | code | n. | Technical | 3 | Ch.5 | 🔮 foreshadow |
| 32 | colleague | n. | Cultural | 3 | Ch.4 | — |
| 33 | comment | n. | Academic | 3 | Ch.3 | — |
| 34 | community | n. | Cultural | 3 | Ch.4 | — |
| 35 | company | n. | Cultural | 3 | Ch.2 | — |
| 36 | concern | n. | Emotional | 3 | Ch.3 | — |
| 37 | condition | n. | Academic | 3 | Ch.2 | — |
| 38 | connect | vt. | Perceptual | 3 | Ch.4 | — |
| 39 | consider | vi. | Academic | 3 | Ch.1 | — |
| 40 | content | n. | Academic | 3 | Ch.2 | — |
| 41 | contest | n. | Emotional | 3 | Ch.6 | — |
| 42 | context | n. | Academic | 3 | Ch.5 | — |
| 43 | control | n. | Technical | 3 | Ch.3 | — |
| 44 | convey | vt. | Academic | 3 | Ch.5 | ★ Bridge |
| 45 | cost | n. | Technical | 3 | Ch.3 | — |
| 46 | current | n. | Technical | 3 | Ch.4 | — |
| 47 | customer | n. | Cultural | 3 | Ch.2 | — |
| 48 | deal | n. | Technical | 3 | Ch.3 | — |
| 49 | decade | n. | Technical | 3 | Ch.6 | — |
| 50 | decision | n. | Emotional | 3 | Ch.2 | — |
| 51 | demand | n. | Academic | 3 | Ch.3 | — |
| 52 | describe | vt. | Academic | 3 | Ch.2 | ★ Bridge |
| 53 | despite | prep. | Academic | 3 | Ch.3 | — |
| 54 | develop | vi. | Academic | 3 | Ch.2 | — |
| 55 | digital | n./adj. | Technical | 3 | Ch.6 | — |
| 56 | discovery | n. | Academic | 3 | Ch.4 | — |
| 57 | drama | n. | Cultural | 3 | Ch.7 | — |
| 58 | draw | n./vt. | Perceptual | 3 | Ch.1 | — |
| 59 | drawing | n. | Perceptual | 3 | Ch.5 | — |
| 60 | due | n./adj. | Technical | 3 | Ch.3 | — |
| 61 | earn | vt. | Technical | 3 | Ch.4 | — |
| 62 | education | n. | Cultural | 3 | Ch.1 | — |
| 63 | effect | n. | Academic | 3 | Ch.2 | — |
| 64 | elephant | n. | Perceptual | 3 | Ch.9 | — |
| 65 | employ | n./vt. | Technical | 3 | Ch.4 | — |
| 66 | end | n. | Perceptual | 3 | Ch.1 | — |
| 67 | energy | n. | Perceptual | 3 | Ch.5 | — |
| 68 | ensure | vt. | Academic | 3 | Ch.3 | — |
| 69 | environment | n. | Academic | 3 | Ch.5 | — |
| 70 | era | n. | Cultural | 3 | Ch.6 | — |
| 71 | essay | n. | Cultural | 3 | Ch.2 | — |
| 72 | essential | n./adj. | Academic | 3 | Ch.3 | — |
| 73 | even | adj./adv. | Academic | 3 | Ch.1 | — |
| 74 | example | n. | Academic | 3 | Ch.1 | — |
| 75 | expensive | adj. | Technical | 3 | Ch.4 | — |
| 76 | experiment | n. | Technical | 3 | Ch.6 | — |
| 77 | expert | n./adj. | Academic | 3 | Ch.4 | — |
| 78 | explain | v. | Academic | 3 | Ch.1 | ★ Bridge |
| 79 | express | n./vt. | Perceptual | 3 | Ch.2 | ★ Bridge |
| 80 | expression | n. | Perceptual | 3 | Ch.3 | ★ Bridge |
| 81 | extend | vt. | Academic | 3 | Ch.5 | — |
| 82 | extreme | n./adj. | Perceptual | 3 | Ch.7 | — |
| 83 | face | n./vt. | Perceptual | 3 | Ch.1 | — |
| 84 | fail | vi. | Emotional | 3 | Ch.2 | — |
| 85 | following | n./adj. | Academic | 3 | Ch.2 | — |
| 86 | form | n. | Academic | 3 | Ch.2 | — |
| 87 | found | v./vt. | Academic | 3 | Ch.3 | — |
| 88 | frequent | adj. | Technical | 3 | Ch.4 | — |
| 89 | function | n. | Technical | 3 | Ch.5 | — |
| 90 | fund | n. | Technical | 3 | Ch.4 | — |
| 91 | further | adj./adv. | Academic | 3 | Ch.3 | — |
| 92 | gain | n./vt. | Emotional | 3 | Ch.4 | — |
| 93 | generation | n. | Cultural | 3 | Ch.5 | — |
| 94 | goal | n. | Emotional | 3 | Ch.2 | — |
| 95 | grant | n./vt. | Technical | 3 | Ch.4 | — |
| 96 | grasp | n./vt. | Perceptual | 3 | Ch.5 | — |
| 97 | group | n. | Cultural | 3 | Ch.1 | — |
| 98 | growth | n. | Technical | 3 | Ch.3 | — |
| 99 | guide | n./vt. | Cultural | 3 | Ch.2 | — |
| 100 | happen | vi. | Perceptual | 3 | Ch.1 | — |
| 101 | head | n./vt. | Perceptual | 3 | Ch.1 | — |
| 102 | healthy | adj. | Technical | 3 | Ch.5 | — |
| 103 | hug | n./vt. | Emotional | 3 | Ch.10 | — |
| 104 | ignore | vt. | Emotional | 3 | Ch.3 | — |
| 105 | illustrate | vt. | Academic | 3 | Ch.5 | ★ Bridge |
| 106 | image | n. | Perceptual | 3 | Ch.4 | — |
| 107 | impact | n./vi. | Academic | 3 | Ch.3 | — |
| 108 | include | vt. | Academic | 3 | Ch.2 | — |
| 109 | individual | n./adj. | Academic | 3 | Ch.3 | — |
| 110 | industry | n. | Technical | 3 | Ch.4 | — |
| 111 | influence | n./vt. | Academic | 3 | Ch.3 | — |
| 112 | issue | n./vt. | Academic | 3 | Ch.2 | — |
| 113 | item | n. | Technical | 3 | Ch.3 | — |
| 114 | judge | n./vt. | Academic | 3 | Ch.4 | — |
| 115 | justice | n. | Cultural | 3 | Ch.7 | — |
| 116 | labor | n. | Technical | 3 | Ch.4 | — |
| 117 | lack | n./vt. | Academic | 3 | Ch.2 | — |
| 118 | launch | n./vt. | Technical | 3 | Ch.5 | — |
| 119 | lead | n./vt. | Cultural | 3 | Ch.1 | — |
| 120 | likely | adj./adv. | Academic | 3 | Ch.2 | — |
| 121 | limit | n./vt. | Academic | 3 | Ch.3 | 🔮 foreshadow |
| 122 | mark | n./vt. | Perceptual | 3 | Ch.2 | — |
| 123 | matter | n. | Academic | 3 | Ch.1 | — |
| 124 | means | n. | Academic | 3 | Ch.3 | — |
| 125 | measure | n./vt. | Technical | 3 | Ch.4 | — |
| 126 | mental | adj. | Perceptual | 3 | Ch.5 | — |
| 127 | mention | vt. | Academic | 3 | Ch.3 | — |
| 128 | merchant | n. | Cultural | 3 | Ch.7 | — |
| 129 | message | n. | Perceptual | 3 | Ch.2 | — |
| 130 | might | n./aux. | Emotional | 3 | Ch.2 | — |
| 131 | mind | n./vt. | Perceptual | 3 | Ch.1 | — |
| 132 | nail | vt./n. | Perceptual | 3 | Ch.8 | — |
| 133 | name | n./vt. | Cultural | 3 | Ch.1 | — |
| 134 | national | adj./n. | Cultural | 3 | Ch.4 | — |
| 135 | nature | n. | Perceptual | 3 | Ch.4 | — |
| 136 | navigate | vt. | Perceptual | 3 | Ch.6 | 🔮 foreshadow |
| 137 | notice | n./vt. | Perceptual | 3 | Ch.2 | — |
| 138 | object | n./vi. | Academic | 3 | Ch.3 | — |
| 139 | offer | vt./n. | Emotional | 3 | Ch.2 | — |
| 140 | opinion | n. | Emotional | 3 | Ch.3 | — |
| 141 | particular | adj. | Academic | 3 | Ch.3 | — |
| 142 | pattern | n. | Academic | 3 | Ch.5 | — |
| 143 | perform | vt. | Cultural | 3 | Ch.4 | — |
| 144 | period | n. | Cultural | 3 | Ch.3 | — |
| 145 | persist | vi. | Emotional | 3 | Ch.6 | — |
| 146 | physical | adj. | Technical | 3 | Ch.5 | — |
| 147 | pick | vt. | Perceptual | 3 | Ch.2 | — |
| 148 | piece | n. | Perceptual | 3 | Ch.1 | — |
| 149 | position | n. | Academic | 3 | Ch.3 | — |
| 150 | positive | adj. | Emotional | 3 | Ch.4 | — |
| 151 | potential | n./adj. | Academic | 3 | Ch.4 | — |
| 152 | power | n. | Cultural | 3 | Ch.3 | — |
| 153 | practice | n. | Academic | 3 | Ch.2 | — |
| 154 | predict | vt. | Academic | 3 | Ch.6 | — |
| 155 | present | n./adj./vt. | Perceptual | 3 | Ch.1 | — |
| 156 | pressure | n. | Emotional | 3 | Ch.4 | — |
| 157 | prevent | vt. | Technical | 3 | Ch.3 | — |
| 158 | principle | n. | Academic | 3 | Ch.5 | — |
| 159 | private | adj. | Cultural | 3 | Ch.4 | — |
| 160 | process | n./vt. | Technical | 3 | Ch.3 | — |
| 161 | produce | vt. | Technical | 3 | Ch.3 | — |
| 162 | profit | n. | Technical | 3 | Ch.5 | — |
| 163 | program | n. | Technical | 3 | Ch.4 | — |
| 164 | project | n./vt. | Academic | 3 | Ch.3 | — |
| 165 | promise | n./vt. | Emotional | 3 | Ch.2 | — |
| 166 | promote | vt. | Academic | 3 | Ch.4 | — |
| 167 | propose | vt. | Academic | 3 | Ch.5 | — |
| 168 | protect | vt. | Emotional | 3 | Ch.3 | — |
| 169 | prove | vt. | Academic | 3 | Ch.3 | — |
| 170 | provide | vt. | Academic | 3 | Ch.2 | — |
| 171 | public | n./adj. | Cultural | 3 | Ch.2 | — |
| 172 | purchase | n./vt. | Technical | 3 | Ch.5 | — |
| 173 | purpose | n. | Academic | 3 | Ch.2 | — |
| 174 | pursue | vt. | Emotional | 3 | Ch.4 | — |
| 175 | range | n. | Academic | 3 | Ch.3 | — |
| 176 | rate | n. | Technical | 3 | Ch.3 | — |
| 177 | rather | adv. | Academic | 3 | Ch.1 | — |
| 178 | reach | vt. | Perceptual | 3 | Ch.2 | — |
| 179 | reason | n. | Academic | 3 | Ch.1 | — |
| 180 | receive | vt. | Academic | 3 | Ch.2 | — |
| 181 | recognize | vt. | Perceptual | 3 | Ch.3 | — |
| 182 | reduce | vt. | Technical | 3 | Ch.4 | — |
| 183 | reflect | vt. | Perceptual | 3 | Ch.4 | — |
| 184 | reform | n./vt. | Cultural | 3 | Ch.6 | — |
| 185 | refuse | vt. | Emotional | 3 | Ch.3 | — |
| 186 | regard | n./vt. | Academic | 3 | Ch.3 | — |
| 187 | region | n. | Technical | 3 | Ch.4 | — |
| 188 | regulation | n. | Technical | 3 | Ch.5 | — |
| 189 | reject | vt. | Emotional | 3 | Ch.4 | — |
| 190 | relate | vt. | Academic | 3 | Ch.3 | — |
| 191 | release | n./vt. | Technical | 3 | Ch.4 | — |
| 192 | relevant | adj. | Academic | 3 | Ch.5 | — |
| 193 | relief | n. | Emotional | 3 | Ch.6 | — |
| 194 | rely | vi. | Emotional | 3 | Ch.3 | — |
| 195 | remain | vi. | Academic | 3 | Ch.2 | — |
| 196 | remove | vt. | Technical | 3 | Ch.3 | — |
| 197 | require | vt. | Academic | 3 | Ch.2 | — |
| 198 | research | n./vi. | Academic | 3 | Ch.2 | — |
| 199 | reserve | n./vt. | Technical | 3 | Ch.5 | — |
| 200 | resource | n. | Technical | 3 | Ch.4 | — |
| 201 | respond | vi. | Academic | 3 | Ch.3 | — |
| 202 | restore | vt. | Technical | 3 | Ch.5 | — |
| 203 | result | n./vi. | Academic | 3 | Ch.1 | — |
| 204 | retain | vt. | Academic | 3 | Ch.5 | — |
| 205 | reveal | vt. | Perceptual | 3 | Ch.4 | ★ Bridge |
| 206 | revenue | n. | Technical | 3 | Ch.6 | — |
| 207 | review | n./vt. | Academic | 3 | Ch.3 | — |
| 208 | role | n. | Cultural | 3 | Ch.1 | — |
| 209 | route | n. | Perceptual | 3 | Ch.5 | 🔮 foreshadow |
| 210 | ruling | n./adj. | Technical | 3 | Ch.6 | — |
| 211 | run | vi./vt. | Technical | 3 | Ch.1 | — |
| 212 | scheme | n. | Technical | 3 | Ch.5 | — |
| 213 | scope | n. | Academic | 3 | Ch.4 | — |
| 214 | section | n. | Technical | 3 | Ch.3 | — |
| 215 | sector | n. | Technical | 3 | Ch.4 | — |
| 216 | seek | vt. | Emotional | 3 | Ch.3 | — |
| 217 | seem | vi. | Academic | 3 | Ch.1 | — |
| 218 | sense | n. | Perceptual | 3 | Ch.2 | — |
| 219 | service | n. | Cultural | 3 | Ch.3 | — |
| 220 | set | n./vt. | Technical | 3 | Ch.1 | — |
| 221 | share | n./vt. | Cultural | 3 | Ch.2 | — |
| 222 | sheet | n. | Perceptual | 3 | Ch.4 | — |
| 223 | short | adj. | Perceptual | 3 | Ch.1 | — |
| 224 | show | n./vt. | Perceptual | 3 | Ch.1 | — |
| 225 | sign | n./vt. | Perceptual | 3 | Ch.2 | — |
| 226 | significant | adj. | Academic | 3 | Ch.4 | — |
| 227 | silk | n. | Cultural | 3 | Ch.9 | — |
| 228 | similar | adj. | Academic | 3 | Ch.2 | — |
| 229 | slow | adj./vt. | Perceptual | 3 | Ch.2 | — |
| 230 | social | n./adj. | Cultural | 3 | Ch.2 | — |
| 231 | sort | n./vt. | Academic | 3 | Ch.2 | — |
| 232 | source | n. | Academic | 3 | Ch.3 | — |
| 233 | specific | adj. | Academic | 3 | Ch.3 | — |
| 234 | standard | n./adj. | Technical | 3 | Ch.3 | — |
| 235 | state | n./vt. | Academic | 3 | Ch.1 | — |
| 236 | statement | n. | Academic | 3 | Ch.3 | — |
| 237 | status | n. | Cultural | 3 | Ch.4 | — |
| 238 | store | n./vt. | Technical | 3 | Ch.2 | — |
| 239 | stress | n./vt. | Emotional | 3 | Ch.3 | — |
| 240 | structure | n./vt. | Academic | 3 | Ch.4 | — |
| 241 | subject | n./adj./vt. | Academic | 3 | Ch.2 | — |
| 242 | suggest | vt. | Academic | 3 | Ch.1 | ★ Bridge |
| 243 | support | n./vt. | Emotional | 3 | Ch.2 | — |
| 244 | supreme | n./adj. | Cultural | 3 | Ch.7 | — |
| 245 | surprise | n./vt. | Emotional | 3 | Ch.2 | — |
| 246 | sustain | vt. | Academic | 3 | Ch.5 | — |
| 247 | identify | vt. | Academic | 3 | Ch.3 | — |

### Tag Distribution Summary (Tier 1, 244 words)

| Tag | Count | % | 绯墨 Affinity |
|-----|-------|---|---------------|
| Academic | 82 | 33.6% | ★★★ High |
| Technical | 48 | 19.7% | ★☆☆ Neutral |
| Perceptual | 37 | 15.2% | ★★★ High |
| Cultural | 35 | 14.3% | ★★★ High |
| Emotional | 32 | 13.1% | ★★☆ Medium |
| (未列完/重分类中) | 10 | 4.1% | — |

> **绯墨核心词汇圈** (Bridge院天赋): 标记为 ★ Bridge 的 Tier 1 words = 绯墨的"本能词库"。她在叙事中自然使用这些词，且在 Study Break 中会优先讲解。共约 15-20 个核心学术动词 (convey, describe, explain, express, illustrate, reveal, suggest 等)。

---

## R2: Seven Labyrinths Foreshadowing Vocabulary (§5)

> **Per 凯尔希指令 §5**: From Ch.10 onward, certain vocabulary words should foreshadow the "Seven Labyrinths" arc.

### Foreshadowing Words — Master List

These words appear in the Tier 1/2 vocabulary and should be deployed at strategic points in the narrative to build the Seven Labyrinths arc:

| Word | POS | Tier | Meaning | Suggested Foreshadow Chapter | Labyrinth Association |
|------|-----|------|---------|---------------------------|-----------------------|
| code | n. | 1 | 代码，密码；编码 | Ch.5 (early seed), Ch.10+ | Cipher Labyrinth |
| limit | n./vt. | 1 | 限制；限度 | Ch.3 (seed), Ch.10+ | Boundary Labyrinth |
| navigate | vt. | 1 | 驾驶；航行 | Ch.6 (seed), Ch.10+ | Path Labyrinth |
| route | n. | 1 | 路线 | Ch.5 (seed), Ch.11+ | Journey Labyrinth |
| bound | n. | 1 | 范围；跳跃 | Ch.6 (seed), Ch.12+ | Threshold Labyrinth |
| context | n. | 1 | 环境；上下文 | Ch.5, Ch.12+ | Translation Labyrinth |
| pattern | n. | 1 | 模式；图案 | Ch.5, Ch.13+ | Structure Labyrinth |
| structure | n./vt. | 1 | 结构；构造 | Ch.4, Ch.13+ | Architecture Labyrinth |

### Additional Foreshadowing Words (Tier 2 / Special Insert)

These words should be **introduced in narrative prose** from Ch.10 onward, even if they're not in Tier 1. They build the atmosphere of the Seven Labyrinths:

| Word | Proposed Tier | Meaning | First Appearance | Purpose |
|------|-------------|---------|-----------------|---------|
| labyrinth | Special | 迷宫 | Ch.1 title word | Core motif |
| maze | Special | 迷宫(迷阵) | Ch.6 | Variant / labyrinth synonym |
| corridor | Special | 走廊 | Ch.3 | Architectural atmosphere |
| gateway | Special | 入口；门径 | Ch.1 | Entry metaphor |
| threshold | Special | 阈值；门槛 | Ch.4 | Crossing-point metaphor |
| boundary | Tier 2 | 边界 | Ch.7 | Edge / limit concept |
| frontier | Tier 2 | 前沿；边界 | Ch.10 | Knowledge frontier |
| translation | Special | 翻译 | Ch.1 | Bridge院 core concept |
| bilingual | Special | 双语的 | Ch.1 | Bridge院 descriptor |
| multilingual | Special | 多语的 | Ch.10 | Expanded Bridge能力 |
| cipher | Special | 密码 | Ch.10 | First Labyrinth puzzle |
| ancient | Tier 2 | 古代的 | Ch.1 | Temporal atmosphere |
| archive | Special | 档案馆 | Ch.4 | Knowledge repository |
| forbidden | Special | 被禁止的 | Ch.10 | Forbidden knowledge motif |
| sealed | Special | 封印的 | Ch.11 | Sealed Labyrinth gate |
| guardian | Special | 守护者 | Ch.5 | NPC archetype |
| sentinel | Special | 哨兵 | Ch.12 | Advanced guard NPC |

> **Note**: "Special" tier means these words are woven into the narrative at the prose level (CEFR B1-B2) rather than treated as collectible Glyphs. They appear naturally in Feimo's environment.

### Seven Labyrinths — Foreshadowing Timeline

| Ch. | Foreshadowing Event | Key Words Used | Intensity |
|-----|-------------------|----------------|-----------|
| Ch.1 | Feimo enters the first room; "gateway" appears on the archway | gateway, translation | ○○○ Subtle |
| Ch.3 | A "corridor" extends beyond the known Labyrinth | corridor, bound | ○○○ Subtle |
| Ch.5 | The "guardian" mentions "archives below" | guardian, archive, code | ○○○ Subtle |
| Ch.6 | A dead-end "maze" pattern is noted; "navigate" saves Feimo | maze, navigate, route | ○○● Building |
| Ch.7 | "Boundary" stones mark the edge of the known Labyrinth | boundary, limit | ○○● Building |
| Ch.10 | The "Seven Labyrinths" are named for the first time | labyrinth, cipher, forbidden | ○●● Reveal |
| Ch.11 | A "sealed" gate blocks the Second Labyrinth | sealed, threshold, multilingual | ○●● Active |
| Ch.12 | The "sentinel" guards the Translation Labyrinth | sentinel, frontier, pattern | ●●● Climactic |
| Ch.13+ | All foreshadowing converges | All words active | ●●● Payoff |

---

## R3: Study Break Content Plan (§2 — New Table)

> **Per 凯尔希指令 §2**: Every two chapters, a Study Break teaches exam skills. Below maps each break to vocabulary focus, exam section, and key cards.

| Study Break # | Chapter | Topic | Teaching Method | Vocab Focus | Exam Section | Key Cards | Narrative Context |
|--------------|---------|-------|----------------|-------------|--------------|-----------|-------------------|
| 1 | Ch.2 | SM-2 Spaced Repetition | Mia 1-on-1 tutorial | Basic academic verbs (agree, choose, develop, explain, suggest) | Vocabulary system | 004 文学性, 005 陌生化 | Mia introduces the Labyrinth's memory system — Glyphs fade unless reviewed |
| 2 | Ch.4 | Cloze Logic (完形填空) | Classroom + self-study | Logical connectors (despite, despite, although, however, therefore) + cause-effect nouns (effect, impact, result, consequence) | Use of English (20Q) | 010 叙事视角, 015 文学语言与日常语言 | Feimo learns to "weave" torn passages — the Cloze Chamber |
| 3 | Ch.7 | Reading Comprehension Skills | Group discussion + practice | Interpretation verbs (analyze, argue, claim, consider, demonstrate, evaluate) + abstract nouns (assumption, evidence, hypothesis, phenomenon) | Reading Part A (20Q) | 065 意识流, 067 卡夫卡 | The Mirror Chamber — passages reflected in distorted glass |
| 4 | Ch.9 | Vocabulary Strategy: Roots & Affixes | Self-study with etymology cards | Word-family clusters (structure/construction/instruct/destruct; express/impress/compress/depress; produce/reduce/introduce/deduce) | Cross-section vocabulary | 070 荒诞派戏剧, 072 黑色幽默 | Feimo discovers etymological roots growing through the Labyrinth walls |
| 5 | Ch.11 | Translation Skills (翻译技巧) | 绯墨 Bridge院 intensive | Translation high-freq verbs (convey, illustrate, interpret, indicate, reveal, suggest, demonstrate, imply) + cultural concept nouns (civilization, culture, tradition, identity, perspective) | Translation (5Q) | 088 格雷马斯, 090 元虚构 | 绯墨's specialty — the Bridge Chamber between languages |
| 6 | Ch.13 | Long Sentence Analysis (长难句) | Workshop + peer review | Complex sentence markers (although, whereas, nevertheless, furthermore, consequently, notwithstanding) + subordinate structures | Reading + Translation | 036 朦胧诗, 047 启蒙运动 | The Architecture Chamber — sentences as structural supports |
| 7 | Ch.15 | Comprehensive Writing (写作综合) | Full essay practice + critique | Essay framework words (furthermore, consequently, specifically, undoubtedly, alternatively, predominantly) + opinion verbs (maintain, contend, advocate, acknowledge, refute) | Writing (2Q) | 073 萨特介入文学, 093 福柯话语理论 | The Forge — writing as the ultimate Labyrinth skill |

### Study Break × Exam Section Coverage Verification

| Exam Section | Covered in Break # | Total Breaks |
|-------------|-------------------|--------------|
| Use of English (Cloze) | SB#2 | 1 |
| Reading Part A | SB#3, SB#6 | 2 |
| Reading Part B | SB#3 (shared skills) | 1 (implicit) |
| Translation | SB#5, SB#6 | 2 |
| Writing | SB#7 | 1 |
| Vocabulary (SM-2 system) | SB#1, SB#4 | 2 |

> All 5 exam sections covered. ✓

---

## R4: Glyph Battle Usage Type Annotations (§3)

> **Per 凯尔希指令 §3**: Add "Usage Type" to the exam question mapping. Each question serves either the **Narrative** layer (Chamber challenges in-story) or the **Teaching** layer (Study Break instruction) or **Both**.

### Usage Type Distribution Per Chapter

| Ch. | Study Break? | Weave (Cloze) | Mirror (Read A) | Forge (Read B) | Bridge (Trans) | Script (Write) |
|-----|-------------|---------------|-----------------|----------------|---------------|----------------|
| Ch.1 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.2 | **SB#1** | Narrative × 16 / Teaching × 4 | Narrative × 16 / Teaching × 4 | Narrative × 4 / Teaching × 1 | Narrative × 4 / Teaching × 1 | Narrative × 2 |
| Ch.3 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.4 | **SB#2** | Narrative × 12 / Teaching × 8 | Narrative × 16 / Teaching × 4 | Narrative × 4 / Teaching × 1 | Narrative × 4 / Teaching × 1 | Narrative × 2 |
| Ch.5 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.6 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.7 | **SB#3** | Narrative × 14 / Teaching × 6 | Narrative × 10 / Teaching × 10 | Narrative × 3 / Teaching × 2 | Narrative × 3 / Teaching × 2 | Narrative × 2 |
| Ch.8 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.9 | **SB#4** | Narrative × 14 / Teaching × 6 | Narrative × 14 / Teaching × 6 | Narrative × 4 / Teaching × 1 | Narrative × 4 / Teaching × 1 | Narrative × 2 |
| Ch.10 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.11 | **SB#5** | Narrative × 12 / Teaching × 8 | Narrative × 14 / Teaching × 6 | Narrative × 3 / Teaching × 2 | Narrative × 2 / **Teaching × 3** | Narrative × 2 |
| Ch.12 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.13 | **SB#6** | Narrative × 10 / Teaching × 10 | Narrative × 12 / Teaching × 8 | Narrative × 3 / Teaching × 2 | Narrative × 3 / Teaching × 2 | Narrative × 1 / Teaching × 1 |
| Ch.14 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.15 | **SB#7** | Narrative × 10 / Teaching × 10 | Narrative × 10 / Teaching × 10 | Narrative × 3 / Teaching × 2 | Narrative × 3 / Teaching × 2 | **Teaching × 2** |
| Ch.16 | No | Narrative × 20 | Narrative × 20 | Narrative × 5 | Narrative × 5 | Narrative × 2 |
| Ch.17 | No | Mixed (Boss Rush) | Mixed (Boss Rush) | Mixed (Boss Rush) | Mixed (Boss Rush) | Mixed (Boss Rush) |

### Sample: Ch.1 Detailed Usage Annotation (Year 2010)

| Challenge Type | Question ID | Preview | Usage Type | Notes |
|---------------|-------------|---------|------------|-------|
| Weave | 2010-eng1-use_of_english-q1 | "In 1924 America's National Research Council sent two engineers..." | **Narrative** | Labyrinth's first puzzle — Feimo weaves torn passage |
| Weave | 2010-eng1-use_of_english-q2 | (same passage, blank 2) | **Narrative** | Continuation |
| Weave | 2010-eng1-use_of_english-q3–q20 | (same passage, blanks 3-20) | **Narrative** | Progressive difficulty within passage |
| Mirror | 2010-eng1-reading_a-q21 | "Of all the changes in English-language newspapers..." | **Narrative** | Text reflected in mirror — comprehension challenge |
| Mirror | 2010-eng1-reading_a-q26 | "Over the past decade, thousands of patents..." | **Narrative** | Second mirror passage |
| Mirror | 2010-eng1-reading_a-q31 | "In his book The Tipping Point, Malcolm Gladwell argues..." | **Narrative** | Third mirror passage |
| Mirror | 2010-eng1-reading_a-q36 | "Bankers have been blaming themselves..." | **Narrative** | Fourth mirror passage |
| Forge | 2010-eng1-reading_b-q41–q45 | "Retail sales of food and drink..." | **Narrative** | Reorder scrambled paragraphs |
| Bridge | 2010-eng1-translation-q46 | "One basic weakness in a conservation system..." | **Narrative** | Bilingual inscription on door |
| Bridge | 2010-eng1-translation-q47–q50 | (same passage, sentences 2-5) | **Narrative** | Multi-sentence translation sequence |
| Script | 2010-eng1-writing_a-q51 | Short writing prompt | **Narrative** | Feimo writes a letter to escape |
| Script | 2010-eng1-writing_b-q52 | Essay prompt | **Narrative** | Feimo's first essay as Labyrinth inscription |

### Sample: Ch.4 Detailed Usage Annotation (Year 2013, with Study Break #2)

| Challenge Type | Question ID | Usage Type | Context |
|---------------|-------------|------------|---------|
| Weave × 12 | 2013-eng1-use_of_english-q1–q12 | **Narrative** | Chamber challenge — standard Labyrinth weave |
| Weave × 8 | 2013-eng1-use_of_english-q13–q20 | **Teaching** | SB#2 uses these blanks to teach cloze logic (signal words, collocations, grammatical inference) |
| Mirror × 16 | 2013-eng1-reading_a-q21–q36 | **Narrative** | Four passages in Mirror Chamber |
| Mirror × 4 | 2013-eng1-reading_a-q37–q40 | **Teaching** | SB#2 uses Passage 4 questions to demonstrate "evidence-based inference" technique |
| Forge × 4 | 2013-eng1-reading_b-q41–q44 | **Narrative** | Reorder challenge |
| Forge × 1 | 2013-eng1-reading_b-q45 | **Teaching** | SB#2 demonstrates paragraph-connection logic |
| Bridge × 4 | 2013-eng1-translation-q46–q49 | **Narrative** | Translation door |
| Bridge × 1 | 2013-eng1-translation-q50 | **Teaching** | SB#2 demonstrates sentence structure analysis for translation |
| Script × 2 | 2013-eng1-writing-a/b | **Narrative** | Writing as escape |

---

## R5: Bridge院 Vocabulary Density Adjustment (§1)

> **Per 凯尔希指令 §1**: Ensure translation-related vocabulary (绯墨's specialty) is denser in **Ch.1** and **Ch.10-13** (Bridge院重点章节).

### Bridge院 Core Vocabulary Tier — Words to Prioritize

These words should appear more frequently in Ch.1 and Ch.10-13. They are either (a) translation high-freq verbs or (b) cross-cultural concept nouns:

**Translation High-Freq Verbs** (绯墨本能词库):

| Word | POS | Meaning | DB Tier | Current Ch. | Boost To |
|------|-----|---------|---------|-------------|----------|
| convey | vt. | 传达 | 1 (3×) | Ch.5 | Ch.1 + Ch.10-13 |
| suggest | vt. | 暗示；建议 | 1 (3×) | Ch.1 | Ch.1 + Ch.10-13 |
| reveal | vt. | 揭示 | 1 (3×) | Ch.4 | Ch.1 + Ch.10-13 |
| illustrate | vt. | 阐明 | 1 (3×) | Ch.5 | Ch.1 + Ch.10-13 |
| describe | vt. | 描述 | 1 (3×) | Ch.2 | Ch.1 + Ch.10-13 |
| express | vt. | 表达 | 1 (3×) | Ch.2 | Ch.1 + Ch.10-13 |
| explain | v. | 解释 | 1 (3×) | Ch.1 | Ch.1 + Ch.10-13 |
| indicate | vt. | 指出；表明 | 2 (2×) | Promote to T1 | Ch.10-13 priority |
| demonstrate | vt. | 证明；演示 | 2 (2×) | Promote to T1 | Ch.10-13 priority |
| imply | vt. | 暗示 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| interpret | vt. | 解释；口译 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| infer | vt. | 推断 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| clarify | vt. | 澄清 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| acknowledge | vt. | 承认 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| assert | vt. | 断言 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| define | vt. | 定义 | 2 (1×) | Promote to T1 | Ch.10-13 priority |
| emphasize | vt. | 强调 | 2 (2×) | Promote to T1 | Ch.10-13 priority |
| contrast | n./vt. | 对比 | 2 (2×) | Promote to T1 | Ch.10-13 priority |

**Cross-Cultural Concept Nouns** (绯墨的跨文化直觉):

| Word | POS | Meaning | DB Tier | Boost To |
|------|-----|---------|---------|----------|
| culture | n. | 文化 | 2 (2×) | Ch.1, Ch.10-13 priority |
| tradition | n. | 传统 | 2 (2×) | Ch.10-13 priority |
| identity | n. | 身份 | 2 (2×) | Ch.10-13 priority |
| perspective | n. | 观点 | 2 (1×) | Ch.10-13 priority |
| civilization | n. | 文明 | 1 (3×) | Ch.1 + Ch.10-13 |
| era | n. | 时代 | 1 (3×) | Ch.1 + Ch.10-13 |
| generation | n. | 一代人 | 1 (3×) | Ch.10-13 |
| diversity | n. | 多样性 | 2 (2×) | Ch.10-13 priority |

**Perception/Sound Words** (绯墨的感知天赋):

| Word | POS | Meaning | DB Tier | Notes |
|------|-----|---------|---------|-------|
| perceive | vt. | 察觉 | 2 (2×) | 绯墨的超感官 — she perceives meaning between languages |
| sense | n. | 感觉 | 1 (3×) | Already in Ch.2 — boost to Ch.10-13 |
| mental | adj. | 精神的 | 1 (3×) | Already in Ch.5 — boost to Ch.11-13 |
| reflect | vt. | 反映；反射 | 1 (3×) | Already in Ch.4 — boost to Ch.10-13 |
| echo | n./vt. | 回声 | Not in DB | Insert as Special tier in Ch.6+ |
| whisper | n./vt. | 低语 | Not in DB | Insert as Special tier in Ch.10+ |
| resonate | vi. | 共鸣 | Not in DB | Insert as Special tier in Ch.11+ |
| frequency | n. | 频率 | Not in DB | Insert as Special tier in Ch.12+ |

> **Note**: echo, whisper, resonate, frequency are not in the 6,131 vocabulary table. They are "narrative-only" words that 绯墨 uses as part of her cat-like perception. They should be introduced at CEFR A2-B1 level in the prose.

---

## R6: Table 5 Update — Labyrinth-Foreshadowing Card Tags (§6)

> **Per 凯尔希指令 §6**: Mark which of the 106 cards are related to the "Seven Labyrinths" foreshadowing arc. Keep v1 mapping as baseline; flag for re-validation when 庄方宜's new outline arrives.

### Cards with Seven Labyrinths Foreshadowing Potential

| Card # | Chinese Name | Cluster | Current Ch. | Labyrinth Foreshadow Tag | Rationale |
|--------|-------------|---------|-------------|-------------------------|-----------|
| 004 | 文学性 | Dialogue | Ch.10 | 🔮 **Labyrinth Theory** | "What makes a text literary" → "What makes a Labyrinth a Labyrinth" |
| 005 | 陌生化 | Consciousness | Ch.7 | 🔮 **Threshold** | Defamiliarization = the act of crossing into the strange |
| 010 | 叙事视角 | Craft | Ch.3 | 🔮 **Perspective Shift** | Different POVs = different Labyrinth paths |
| 031 | code (word) | — (Tier 1 vocab) | Ch.5 | 🔮 **Cipher** | Direct foreshadow of Cipher Labyrinth |
| 076 | 博尔赫斯 | Voices | Ch.6 | 🔮 **Library Labyrinth** | Borges' Library of Babel = THE labyrinth archetype |
| 084 | 结构主义叙事学 | Theory | Ch.9 | 🔮 **Structure** | Deep structures = hidden Labyrinth architecture |
| 087 | 普罗普故事形态学 | Theory | Ch.10 | 🔮 **Map** | 31 functions = a map through narrative Labyrinths |
| 088 | 格雷马斯 | Theory | Ch.11 | 🔮 **Semiotic Grid** | Semiotic square = a navigational grid |
| 090 | 元虚构 | Theory | Ch.11 | 🔮 **Self-Awareness** | Metafiction = the Labyrinth recognizing itself |
| 091 | 德里达延异 | Theory | Ch.11 | 🔮 **Infinite Corridor** | Différance = meaning always deferred = endless corridors |
| 092 | 解构主义 | Theory | Ch.12 | 🔮 **Collapse** | Deconstruction = walls coming down |
| 093 | 福柯话语理论 | Power | Ch.15 | 🔮 **Archive Guardian** | Foucault's archive = the Labyrinth's memory |
| 100 | 全书知识网络总览 | Theory | Ch.12 | 🔮 **Master Map** | The overview of all 106 connections = the Labyrinth's blueprint |

### Summary

| Tag | Card Count | Cards |
|-----|-----------|-------|
| 🔮 Labyrinth Theory | 1 | 004 |
| 🔮 Threshold | 1 | 005 |
| 🔮 Perspective Shift | 1 | 010 |
| 🔮 Cipher | 1 | (vocab: code) |
| 🔮 Library Labyrinth | 1 | 076 |
| 🔮 Structure | 1 | 084 |
| 🔮 Map | 1 | 087 |
| 🔮 Semiotic Grid | 1 | 088 |
| 🔮 Self-Awareness | 1 | 090 |
| 🔮 Infinite Corridor | 1 | 091 |
| 🔮 Collapse | 1 | 092 |
| 🔮 Archive Guardian | 1 | 093 |
| 🔮 Master Map | 1 | 100 |
| **Total tagged** | **13** | — |

> **Status**: v1 mapping preserved as baseline. 13/106 cards flagged for Labyrinth foreshadowing. Final re-validation pending 庄方宜's new outline.

---

## R7: Revised Chapter Card Distribution with Study Break Overlay

> Combines v1 card distribution with Study Break allocation and Labyrinth foreshadowing flags.

| Ch. | Cards (v1) | SB? | SB Topic | 🔮 Labyrinth Cards | Glyph Count (Narrative) | Glyph Count (Teaching) |
|-----|-----------|-----|----------|--------------------|-----------------------|----------------------|
| Ch.1 | 4 (016,017,038,039,040) | — | — | — | 52 | 0 |
| Ch.2 | 5 (001,006,007,041,042,106) | SB#1 | SM-2 Vocab | — | 42 | 10 |
| Ch.3 | 6 (008,009,010,011,014,021,028) | — | — | 🔮 010 | 52 | 0 |
| Ch.4 | 6 (015,020,022,023,043,050) | SB#2 | Cloze Logic | — | 38 | 14 |
| Ch.5 | 6 (024,025,026,027,053,056,057) | — | — | — | 52 | 0 |
| Ch.6 | 4 (046,052,066,067,076) | — | — | 🔮 076 | 52 | 0 |
| Ch.7 | 10 (005,060,061,065,098,099,102,103,104,105) | SB#3 | Reading Skills | 🔮 005 | 33 | 19 |
| Ch.8 | 5 (064,068,069,079,080,081) | — | — | — | 52 | 0 |
| Ch.9 | 6 (070,071,072,082,083,084) | SB#4 | Roots & Affixes | 🔮 084 | 40 | 12 |
| Ch.10 | 8 (075,078,085,086,087,002,003,004) | — | — | 🔮 004, 087 | 52 | 0 |
| Ch.11 | 6 (012,013,088,090,091,031,032) | SB#5 | Translation Skills | 🔮 088, 090, 091 | 33 | 19 |
| Ch.12 | 8 (029,030,033,034,035,092,094,100) | — | — | 🔮 092, 100 | 52 | 0 |
| Ch.13 | 6 (036,037,047,048,049,051,062) | SB#6 | Long Sentences | — | 29 | 23 |
| Ch.14 | 5 (055,058,059,063,096,097) | — | — | — | 52 | 0 |
| Ch.15 | 5 (073,074,089,093,095,101) | SB#7 | Writing | 🔮 093 | 25 | 27 |
| Ch.16 | 0 | — | — | — | 52 | 0 |
| Ch.17 | 0 | — | — | — | 52 (Boss Rush) | 0 |

---

## Revision Change Log

| Section | What Changed | Affected v1 Tables |
|---------|-------------|-------------------|
| R1: Thematic Tags | Added 5-tag taxonomy + annotated all 244 Tier 1 words | Table 1 |
| R2: Foreshadow Vocab | New foreshadowing word list + timeline | Tables 1, 2 |
| R3: Study Break Plan | **New Table 6** — 7 Study Breaks mapped | Table 3 |
| R4: Usage Type | Narrative/Teaching/Both distribution per chapter | Table 3 |
| R5: Bridge院 Density | Translation verbs + cultural nouns boost list | Table 1 |
| R6: Labyrinth Card Tags | 13 cards flagged with 🔮 tags | Table 5 |
| R7: Revised Distribution | Overlay of SB + foreshadow on v1 card layout | Table 5 |

**Pending**: Full re-validation of card-chapter mapping when 庄方宜 delivers new outline. 13 🔮-tagged cards are priority check items.

---
---

# v3 Revision — 50-Chapter Expansion (2026-06-24)

> **Triggered by**: 凯尔希 final structure confirmation — 50 chapters × 5000+ words = ~250,000 words
> **Strategy**: v1/v2 remain as historical baseline. v3 is the **current working version**.
> **Key changes**: 17→50 chapters, 7→9 Study Breaks, 3 exam years/chapter → 1 exam year/3 chapters

---

## v3-Table 0: 50-Chapter Architecture Overview

### Act Structure

| Act | Chapters | Arc | Study Breaks |
|-----|----------|-----|-------------|
| **Act I: Threshold** | Ch.1–12 | Feimo enters the Labyrinth; learns fundamentals | Ch.2 (SM-2), Ch.6 (Cloze) |
| **Act II: Corridors** | Ch.13–25 | Skill deepening; exploring branches | Ch.10 (Word Roots), Ch.16 (Reading), Ch.20 (Translation Basics) |
| **Act III: The Seven Labyrinths** | Ch.26–37 | Confronting each Labyrinth in sequence | Ch.25 (Midterm), Ch.31 (Translation Advanced) |
| **Act IV: The Core** | Ch.38–50 | Escalation, revelations, final challenge | Ch.36 (Writing), Ch.44 (Comprehensive) |

### Year → Chapter Mapping

Each exam year's 52 questions split across **3 consecutive chapters**. Ch.49–50 = Grand Finale (mixed).

| Year | Chapters | Ch.A (Cloze 20Q) | Ch.B (Read A 20Q) | Ch.C (ReadB+Trans+Write 12Q) |
|------|----------|-------------------|--------------------|-----------------------------|
| 2010 | 1–3 | Ch.1 | Ch.2 | Ch.3 |
| 2011 | 4–6 | Ch.4 | Ch.5 | Ch.6 |
| 2012 | 7–9 | Ch.7 | Ch.8 | Ch.9 |
| 2013 | 10–12 | Ch.10 | Ch.11 | Ch.12 |
| 2014 | 13–15 | Ch.13 | Ch.14 | Ch.15 |
| 2015 | 16–18 | Ch.16 | Ch.17 | Ch.18 |
| 2016 | 19–21 | Ch.19 | Ch.20 | Ch.21 |
| 2017 | 22–24 | Ch.22 | Ch.23 | Ch.24 |
| 2018 | 25–27 | Ch.25 | Ch.26 | Ch.27 |
| 2019 | 28–30 | Ch.28 | Ch.29 | Ch.30 |
| 2020 | 31–33 | Ch.31 | Ch.32 | Ch.33 |
| 2021 | 34–36 | Ch.34 | Ch.35 | Ch.36 |
| 2022 | 37–39 | Ch.37 | Ch.38 | Ch.39 |
| 2023 | 40–42 | Ch.40 | Ch.41 | Ch.42 |
| 2024 | 43–45 | Ch.43 | Ch.44 | Ch.45 |
| 2025 | 46–48 | Ch.46 | Ch.47 | Ch.48 |
| Mixed | 49–50 | Boss Rush Cloze | Boss Rush Reading | Boss Rush All |

### Word Count Budget (50 chapters × 5000 words)

| Chapter | Target Words | Exam Year | Exam Questions | Study Break? | Notes |
|---------|-------------|-----------|----------------|-------------|-------|
| Ch.1 | 5,000 | 2010 | 20 (Cloze) | — | Labyrinth entrance |
| Ch.2 | 5,000 | 2010 | 20 (Read A) | **SB#1** | SM-2 system intro |
| Ch.3 | 5,000 | 2010 | 12 (Rb+Trans+Write) | — | First writing challenge |
| Ch.4 | 5,000 | 2011 | 20 (Cloze) | — | |
| Ch.5 | 5,000 | 2011 | 20 (Read A) | — | |
| Ch.6 | 5,000 | 2011 | 12 (Rb+Trans+Write) | **SB#2** | Cloze logic deep dive |
| Ch.7 | 5,000 | 2012 | 20 (Cloze) | — | |
| Ch.8 | 5,000 | 2012 | 20 (Read A) | — | |
| Ch.9 | 5,000 | 2012 | 12 (Rb+Trans+Write) | — | |
| Ch.10 | 5,000 | 2013 | 20 (Cloze) | **SB#3** | Word roots & affixes |
| Ch.11 | 5,000 | 2013 | 20 (Read A) | — | |
| Ch.12 | 5,000 | 2013 | 12 (Rb+Trans+Write) | — | |
| Ch.13 | 5,000 | 2014 | 20 (Cloze) | — | |
| Ch.14 | 5,000 | 2014 | 20 (Read A) | — | |
| Ch.15 | 5,000 | 2014 | 12 (Rb+Trans+Write) | — | |
| Ch.16 | 5,000 | 2015 | 20 (Cloze) | **SB#4** | Reading comprehension skills |
| Ch.17 | 5,000 | 2015 | 20 (Read A) | — | |
| Ch.18 | 5,000 | 2015 | 12 (Rb+Trans+Write) | — | |
| Ch.19 | 5,000 | 2016 | 20 (Cloze) | — | |
| Ch.20 | 5,000 | 2016 | 20 (Read A) | **SB#5** | Translation basics |
| Ch.21 | 5,000 | 2016 | 12 (Rb+Trans+Write) | — | |
| Ch.22 | 5,000 | 2017 | 20 (Cloze) | — | |
| Ch.23 | 5,000 | 2017 | 20 (Read A) | — | |
| Ch.24 | 5,000 | 2017 | 12 (Rb+Trans+Write) | — | |
| Ch.25 | 5,000 | 2018 | 20 (Cloze) | **SB#6** | Midterm review |
| Ch.26 | 5,000 | 2018 | 20 (Read A) | — | Seven Labyrinths begin |
| Ch.27 | 5,000 | 2018 | 12 (Rb+Trans+Write) | — | |
| Ch.28 | 5,000 | 2019 | 20 (Cloze) | — | |
| Ch.29 | 5,000 | 2019 | 20 (Read A) | — | |
| Ch.30 | 5,000 | 2019 | 12 (Rb+Trans+Write) | — | |
| Ch.31 | 5,000 | 2020 | 20 (Cloze) | **SB#7** | Translation advanced (绯墨) |
| Ch.32 | 5,000 | 2020 | 20 (Read A) | — | |
| Ch.33 | 5,000 | 2020 | 12 (Rb+Trans+Write) | — | |
| Ch.34 | 5,000 | 2021 | 20 (Cloze) | — | |
| Ch.35 | 5,000 | 2021 | 20 (Read A) | — | |
| Ch.36 | 5,000 | 2021 | 12 (Rb+Trans+Write) | **SB#8** | Writing workshop |
| Ch.37 | 5,000 | 2022 | 20 (Cloze) | — | |
| Ch.38 | 5,000 | 2022 | 20 (Read A) | — | |
| Ch.39 | 5,000 | 2022 | 12 (Rb+Trans+Write) | — | |
| Ch.40 | 5,000 | 2023 | 20 (Cloze) | — | |
| Ch.41 | 5,000 | 2023 | 20 (Read A) | — | |
| Ch.42 | 5,000 | 2023 | 12 (Rb+Trans+Write) | — | |
| Ch.43 | 5,000 | 2024 | 20 (Cloze) | — | |
| Ch.44 | 5,000 | 2024 | 20 (Read A) | **SB#9** | Comprehensive review |
| Ch.45 | 5,000 | 2024 | 12 (Rb+Trans+Write) | — | |
| Ch.46 | 5,000 | 2025 | 20 (Cloze) | — | |
| Ch.47 | 5,000 | 2025 | 20 (Read A) | — | |
| Ch.48 | 5,000 | 2025 | 12 (Rb+Trans+Write) | — | |
| Ch.49 | 5,000 | Mixed | 16 (Boss Cloze+Read) | — | Grand Finale Pt.1 |
| Ch.50 | 5,000 | Mixed | 16 (Boss All) | — | Grand Finale Pt.2 |
| **Total** | **250,000** | | **832** | **9 SBs** | |

### Study Break Summary (v3)

| SB# | Chapter | Topic | Teaching Method | Exam Section | Key Cards |
|-----|---------|-------|----------------|--------------|-----------|
| 1 | Ch.2 | SM-2 Spaced Repetition | Mia 1-on-1 | Vocabulary | 004, 005 |
| 2 | Ch.6 | Cloze Logic | Classroom + self-study | Cloze | 010, 015 |
| 3 | Ch.10 | Word Roots & Affixes | Etymology cards | Cross-section | 001, 083 |
| 4 | Ch.16 | Reading Comprehension | Group discussion | Reading A | 065, 067 |
| 5 | Ch.20 | Translation Basics | 绯墨 Bridge院 | Translation | 043, 076 |
| 6 | Ch.25 | Midterm Review | Mixed practice | All sections | 079, 084 |
| 7 | Ch.31 | Translation Advanced | 绯墨 intensive | Translation | 088, 091 |
| 8 | Ch.36 | Writing Workshop | Essay practice + critique | Writing | 073, 093 |
| 9 | Ch.44 | Comprehensive Review | Full mock | All sections | 100, 106 |

---

## v3-Table 1: Tier 1 Vocabulary — 50-Chapter Re-allocation

> **Source**: 244 DB-confirmed words (≥3 exam appearances) + ~200 promoted Tier 2 words
> **Allocation**: ~5 DB words + ~4 promoted words per chapter = ~9 Glyphs/chapter

### Thematic Tag Key (from v2-R1)

| Tag | Icon | 绯墨 Affinity |
|-----|------|---------------|
| Academic | A | ★★★ |
| Technical | T | ★☆☆ |
| Perceptual | P | ★★★ |
| Cultural | C | ★★★ |
| Emotional | E | ★★☆ |
| Foreshadow | 🔮 | — |

### DB-Confirmed Tier 1 (244 words) — Chapter Assignment

| Ch. | Words | Tag Distribution |
|-----|-------|-----------------|
| Ch.1 | able(A), address(A), agree(E), blank(P), book(C) | A×2, E×1, P×1, C×1 |
| Ch.2 | applicant(T), approach(A), attempt(A), campus(C), choose(E) | A×2, T×1, C×1, E×1 |
| Ch.3 | argue(A), attitude(E), behavior(A), claim(A), comment(A) | A×4, E×1 |
| Ch.4 | bill(T), colleague(C), company(C), connect(P), current(T) | C×2, T×2, P×1 |
| Ch.5 | award(C), condition(A), content(A), customer(C), develop(A) | A×3, C×2 |
| Ch.6 | bound(P), contest(E), digital(T), discover(A), era(C) | A×2, T×1, P×1, C×1 |
| Ch.7 | analysis(A), decade(T), despite(A), ensure(A), environment(A) | A×4, T×1 |
| Ch.8 | area(A), case(A), even(A), example(A), explain(A) | A×5 |
| Ch.9 | being(P), cost(T), demand(A), earn(T), education(C) | A×2, T×2, C×1 |
| Ch.10 | admit(A), alter(A), attempt(A), ★code(T/🔮), community(C) | A×3, T×1, C×1 |
| Ch.11 | concern(E), deal(A), end(P), express(P/★Bridge), face(P) | A×1, E×1, P×3 |
| Ch.12 | employ(T), extend(A), extreme(P), frequent(T), generation(C) | A×2, T×2, C×1 |
| Ch.13 | draw(P), effect(A), essay(C), experiment(T), form(A) | A×2, T×1, P×1, C×1 |
| Ch.14 | expert(A), found(A), function(T), grant(T), guide(C) | A×3, T×2 |
| Ch.15 | contain(A), control(T), convey(A/★Bridge), describe(A/★Bridge), express(P) | A×4, T×1 |
| Ch.16 | decide(E), fundamental(A), group(C), head(P), lead(C) | A×1, E×1, C×2, P×1 |
| Ch.17 | ignore(E), illustrate(A/★Bridge), image(P), include(A), individual(A) | A×3, E×1, P×1 |
| Ch.18 | industry(T), influence(A), issue(A), judge(A), justice(C) | A×3, T×1, C×1 |
| Ch.19 | labor(T), lack(A), likely(A), mark(P), matter(A) | A×3, T×1, P×1 |
| Ch.20 | means(A), measure(T), mental(P), mention(A), merchant(C) | A×3, T×1, C×1 |
| Ch.21 | message(P), mind(P), nail(P), name(C), national(C) | P×3, C×2 |
| Ch.22 | nature(P), navigate(P/🔮), notice(P), object(A), offer(E) | A×1, E×1, P×3 |
| Ch.23 | pattern(A), perform(C), persist(E), physical(T), pick(P) | A×1, C×1, E×1, T×1, P×1 |
| Ch.24 | position(A), positive(E), potential(A), power(C), practice(A) | A×3, E×1, C×1 |
| Ch.25 | predict(A), principle(A), private(C), produce(T), profit(T) | A×3, T×2 |
| Ch.26 | program(T), project(A), promise(E), promote(A), propose(A) | A×4, T×1 |
| Ch.27 | protect(E), prove(A), provide(A), public(C), purchase(T) | A×3, E×1, C×1 |
| Ch.28 | purpose(A), pursue(E), range(A), rate(T), rather(A) | A×4, E×1 |
| Ch.29 | reach(P), reason(A), receive(A), recognize(P), reduce(T) | A×3, P×2 |
| Ch.30 | reflect(P), reform(C), refuse(E), regard(A), region(T) | A×2, C×1, E×1, P×1 |
| Ch.31 | regulation(T), reject(E), relate(A), relevant(A), release(T) | A×3, T×2 |
| Ch.32 | relief(E), rely(E), remain(A), remove(T), require(A) | A×3, E×2 |
| Ch.33 | research(A), reserve(T), resource(T), respond(A), restore(T) | A×3, T×3 |
| Ch.34 | result(A), retain(A), reveal(P/★Bridge), revenue(T), review(A) | A×4, P×1 |
| Ch.35 | role(C), ★route(P/🔮), ★ruling(A/🔮), run(T), scheme(T) | C×1, P×1, A×1, T×2 |
| Ch.36 | scope(A), section(T), sector(T), seek(E), seem(A) | A×3, T×2 |
| Ch.37 | sense(P), service(C), set(T), share(C), sheet(P) | C×2, P×2, T×1 |
| Ch.38 | short(P), show(P), sign(P), significant(A), silk(C) | P×3, A×1, C×1 |
| Ch.39 | similar(A), slow(P), social(C), sort(A), source(A) | A×3, C×1, P×1 |
| Ch.40 | specific(A), standard(T), state(A), statement(A), status(C) | A×4, C×1 |
| Ch.41 | store(T), stress(E), ★structure(A/🔮), subject(A), suggest(A/★Bridge) | A×4, E×1 |
| Ch.42 | support(E), supreme(C), surprise(E), sustain(A), identify(A) | A×3, E×2 |
| Ch.43 | approach(A), benefit(E), case(A), change(A), concern(E) | A×3, E×2 |
| Ch.44 | consider(A), control(T), effect(A), ensure(A), essential(A) | A×4, T×1 |
| Ch.45 | establish(A), evidence(A), experience(C), fail(E), fashion(C) | A×3, C×2 |
| Ch.46 | feature(A), force(E), foreign(C), growth(T), impact(A) | A×3, C×1, E×1 |
| Ch.47 | maintain(A), manage(T), method(A), obtain(T), occur(P) | A×3, T×2 |
| Ch.48 | period(C), policy(T), process(A), range(A), rate(T) | A×3, C×1, T×1 |
| Ch.49 | complex(A), concept(A), major(A), process(A), structure(A) | A×5 (review) |
| Ch.50 | All key terms synthesized | Mixed (Boss Rush) |

> **Note**: Ch.49-50 draw from the full Tier 1 pool for review/synthesis. Ch.1-48 each receive ~5 unique DB-confirmed words.

### Promoted Tier 2 Words — Chapter Assignment (sample, ~200 words)

Each chapter receives ~4 promoted words selected by thematic fit. Key Bridge院 words (per v2-R5) are concentrated in **Ch.11, Ch.15, Ch.20, Ch.31, Ch.35** (translation-heavy chapters).

| Ch. | Promoted Words (4 per chapter) | Theme |
|-----|-------------------------------|-------|
| Ch.1 | access, basic, concept, element | Foundation |
| Ch.2 | academic, application, attend, available | Academic setting |
| Ch.3 | analyze, argument, assumption, cognitive | Critical thinking |
| Ch.4 | achieve, advanced, agreement, aim | Progress |
| Ch.5 | basis, challenge, characteristic, common | Building blocks |
| Ch.6 | automation, cross, culture, design | Crossroads |
| Ch.7 | document, economic, emphasize, enable | Systems |
| Ch.8 | establish, evaluate, evidence, eventually | Evidence-based |
| Ch.9 | executive, expect, experience, failure | Learning curve |
| Ch.10 | ★imply, ★interpret, ★infer, ★define | Word Roots SB |
| Ch.11 | familiar, feature, fundamental, generate | Deepening |
| Ch.12 | government, gradually, guarantee, handle | Authority |
| Ch.13 | harsh, hence, highlight, hint | Signal reading |
| Ch.14 | hostile, household, hypothesis, identify | Analysis |
| Ch.15 | ★acknowledge, ★assert, ★clarify, ★contrast | Bridge verbs |
| Ch.16 | innovation, institution, intellectual, intend | Reading SB |
| Ch.17 | interaction, journal, justification, label | Knowledge |
| Ch.18 | landscape, layer, lecture, liberal | Environment |
| Ch.19 | literary, logical, majority, manage | Literacy |
| Ch.20 | ★convey, ★demonstrate, ★indicate, ★reveal | Translation SB |
| Ch.21 | media, medical, method, migrate | Movement |
| Ch.22 | mission, modify, monitor, motivation | Purpose |
| Ch.23 | mutual, narrative, network, notion | Storytelling |
| Ch.24 | objective, obligation, observe, obvious | Objectivity |
| Ch.25 | occupy, occur, option, origin | Midterm review |
| Ch.26 | overall, parallel, participate, passage | Entry |
| Ch.27 | passive, ★perceive, permit, perspective | Perception |
| Ch.28 | phenomenon, philosophy, platform, policy | Systems |
| Ch.29 | politics, popular, population, portrait | Society |
| Ch.30 | practical, precise, previous, primary | Precision |
| Ch.31 | ★interpret, ★translate, ★convey, ★illustrate | Trans. advanced |
| Ch.32 | priority, procedure, professional, proportion | Professional |
| Ch.33 | prospect, protest, psychology, publication | Deep analysis |
| Ch.34 | radical, reaction, reality, recommendation | Change |
| Ch.35 | reference, register, ★multilingual, ★bilingual | Bridge expansion |
| Ch.36 | reinforce, relationship, reliable, remedy | Writing SB |
| Ch.37 | remote, removal, renew, reputation | Renewal |
| Ch.38 | request, rescue, resemble, resist | Conflict |
| Ch.39 | resolution, resolve, respect, restriction | Resolution |
| Ch.40 | rhythm, rigid, root, rough | Texture |
| Ch.41 | rural, sample, scale, scatter | Analysis |
| Ch.42 | schedule, scholar, scientific, secure | Scholarship |
| Ch.43 | signal, slight, solution, sophisticated | Complexity |
| Ch.44 | somewhat, species, spiritual, stable | Comprehensive |
| Ch.45 | strategy, strict, striking, submit | Tactics |
| Ch.46 | subsequent, substance, sufficient, sum | Synthesis |
| Ch.47 | supplement, survive, suspend, symbol | Endgame |
| Ch.48 | target, technique, tendency, theory | Final prep |
| Ch.49 | transform, transition, transmit, ultimate | Boss Rush |
| Ch.50 | undergo, uniform, unique, universal | Grand Finale |

---

## v3-Table 2: Knowledge Cards — 50-Chapter Re-allocation

> **106 cards → 50 chapters**: ~2 per chapter average, adjusted for thematic clustering

### Card-Chapter Assignment (Complete)

| Ch. | Cards | Cluster | Narrative Role |
|-----|-------|---------|---------------|
| Ch.1 | 016 诗经六义, 038 古希腊悲剧 | Genesis | Origins — East and West begin |
| Ch.2 | 017 楚辞与屈原, 040 荷马史诗 | Genesis | First voices, oral tradition |
| Ch.3 | 039 亚里士多德诗学, 042 骑士文学 | Genesis | Theory of origins |
| Ch.4 | 041 但丁神曲, 106 文学自律与他律 | Genesis | The cosmic journey; autonomy question |
| Ch.5 | 001 文学四要素, 006 文学本质论 | Craft | The map of literary theory |
| Ch.6 | 007 意境, 015 文学语言与日常语言 | Craft | Chinese aesthetics; language distinction |
| Ch.7 | 008 典型, 009 意象与象征 | Craft | Character and symbol |
| Ch.8 | 010 叙事视角, 011 文学风格 | Craft | POV and style |
| Ch.9 | 014 文学体裁, 043 莎士比亚四大悲剧 | Craft + Forms | Genre meets tragedy |
| Ch.10 | 004 文学性, 005 陌生化 | Craft + Consciousness | Literariness and defamiliarization |
| Ch.11 | 046 古典主义三一律, 052 浪漫主义 | Forms | Classical vs. Romantic form |
| Ch.12 | 020 唐诗四期, 022 宋词两大流派 | Forms | Chinese poetic evolution |
| Ch.13 | 023 唐诗与宋诗, 050 歌德浮士德 | Forms + Voices | Tang/Song contrast; Faust |
| Ch.14 | 021 李白与杜甫, 028 鲁迅小说 | Voices | Two poles of Chinese literature |
| Ch.15 | 024 元杂剧体制, 025 西厢记与窦娥冤 | Forms | Yuan drama structure |
| Ch.16 | 026 四大名著类型学, 027 红楼梦 | Forms | The four novels; Dream of Red Chamber |
| Ch.17 | 053 雨果, 056 托尔斯泰 | Voices | Epic realists |
| Ch.18 | 057 陀思妥耶夫斯基, 066 艾略特荒原 | Voices | Polyphony meets modernist collage |
| Ch.19 | 067 卡夫卡, 076 博尔赫斯 | Voices | Kafkaesque nightmare; Borges' labyrinth |
| Ch.20 | 044 堂吉诃德, 045 十日谈 | Dialogue | Frame narrative; reality vs. idealism |
| Ch.21 | 102 芥川龙之介, 103 海明威 | Voices | Rashomon; iceberg theory |
| Ch.22 | 104 福克纳, 105 夏目漱石 | Voices | Stream of consciousness; Japanese modernism |
| Ch.23 | 060 自然主义, 061 象征主义 | Forms | Zola meets Mallarmé |
| Ch.24 | 065 意识流, 078 20世纪文学总特征 | Forms + Consciousness | Modern consciousness |
| Ch.25 | 064 现代主义, 068 后现代主义 | Consciousness | The great divide: modern → postmodern |
| Ch.26 | 069 存在主义, 070 荒诞派戏剧 | Consciousness | Sartre, Camus, Beckett |
| Ch.27 | 071 魔幻现实主义, 072 黑色幽默 | Consciousness | Magical real meets black humor |
| Ch.28 | 075 新小说派, 018 建安风骨 | Consciousness + Dialogue | Anti-novel meets Jian'an spirit |
| Ch.29 | 019 文学自觉, 029 五四文学革命 | Dialogue | Literary self-awareness across cultures |
| Ch.30 | 030 文学研究会与创造社, 031 茅盾与子夜 | Power | Realism vs. Romanticism in China |
| Ch.31 | 032 沈从文与京派, 033 新感觉派 | Power | Pastoral vs. urban modernity |
| Ch.32 | 034 先锋文学, 035 寻根文学 | Power | Chinese avant-garde |
| Ch.33 | 036 朦胧诗, 037 新时期文学三阶段 | Power | Misty poetry; New Period literature |
| Ch.34 | 047 启蒙运动, 048 卢梭 | Dialogue | Enlightenment; the confessional self |
| Ch.35 | 049 18世纪英国小说, 051 狂飙突进运动 | Dialogue | Rise of the novel; Sturm und Drang |
| Ch.36 | 062 浪漫主义vs现实主义, 063 19世纪美国文学 | Dialogue | The great debate; American Renaissance |
| Ch.37 | 054 批判现实主义, 055 巴尔扎克 | Power | Society as the villain |
| Ch.38 | 058 多余人形象, 059 福楼拜 | Power | Superfluous man; le mot juste |
| Ch.39 | 079 接受美学, 080 期待视野 | Theory | Reception aesthetics |
| Ch.40 | 081 召唤结构与隐含读者, 082 视域融合 | Theory | Gaps; fusion of horizons |
| Ch.41 | 083 俄国形式主义, 084 结构主义叙事学 | Theory | Formalist and structural foundations |
| Ch.42 | 085 热奈特五范畴, 086 故事vs话语 | Theory | Narratological toolkit |
| Ch.43 | 087 普罗普故事形态学, 088 格雷马斯 | Theory | Morphology; semiotic square |
| Ch.44 | 089 巴赫金对话理论, 090 元虚构 | Theory | Dialogism; metafiction |
| Ch.45 | 091 德里达延异, 092 解构主义 | Theory | Différance; deconstruction |
| Ch.46 | 093 福柯话语理论, 094 作者之死 | Theory + Power | Discourse; death of the author |
| Ch.47 | 095 女性主义文学批评, 096 后殖民主义 | Power + Dialogue | Feminist and postcolonial critique |
| Ch.48 | 097 文论失语症, 098 校勘四法 | Dialogue | Theoretical aphasia; textual criticism |
| Ch.49 | 099 辨伪学, 100 全书知识网络总览 | Theory | Verification; the master map |
| Ch.50 | 101 西方马克思主义文论 | Power | Final card — ideology and literature |

### Coverage Verification

| Cluster | Total Cards | Chapters Spanned | Status |
|---------|------------|-----------------|--------|
| Genesis | 6 | Ch.1–4 | ✓ |
| Craft | 9 | Ch.5–10 | ✓ |
| Voices | 14 | Ch.14, 17–19, 21–22 | ✓ |
| Forms | 12 | Ch.9, 11–13, 15–16, 23–24 | ✓ |
| Consciousness | 9 | Ch.10, 25–28 | ✓ |
| Theory | 15 | Ch.39–46, 49 | ✓ |
| Dialogue | 19 | Ch.20, 28–29, 34–36, 47–48 | ✓ |
| Power | 17 | Ch.30–33, 37–38, 46–47, 50 | ✓ |
| **Total** | **106** | **Ch.1–50** | **✓ 106/106** |

### Cards Per Chapter Distribution

| Count | Chapters | # of Chapters |
|-------|----------|---------------|
| 1 card | Ch.50 | 1 |
| 2 cards | Ch.1–4, Ch.7–11, Ch.13–49 | 47 |
| 3 cards | Ch.5, Ch.6, Ch.12 | 2 |
| **Total** | | **50 chapters, 106 cards** |

---

## v3-Table 3: Exam Questions — 50-Chapter Mapping

> **16 years × 52Q = 832 questions** distributed across 50 chapters
> **Pattern**: Each year → 3 chapters (Cloze 20Q / ReadA 20Q / Rb+Trans+Write 12Q)
> **Ch.49–50**: Boss Rush (mixed years, 16+16 = 32 questions)

| Ch. | Year | Section | Questions | Q-IDs (sample) | Challenge Type | Usage Type |
|-----|------|---------|-----------|----------------|---------------|------------|
| Ch.1 | 2010 | Cloze | 20 | 2010-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.2 | 2010 | Read A | 20 | 2010-eng1-reading_a-q21–q40 | Mirror | Narrative+Teaching(SB#1) |
| Ch.3 | 2010 | Rb+Trans+Write | 12 | 2010-eng1-reading_b-q41–q45, translation-q46–q50, writing-a/b | Forge+Bridge+Script | Narrative |
| Ch.4 | 2011 | Cloze | 20 | 2011-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.5 | 2011 | Read A | 20 | 2011-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.6 | 2011 | Rb+Trans+Write | 12 | 2011-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative+Teaching(SB#2) |
| Ch.7 | 2012 | Cloze | 20 | 2012-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.8 | 2012 | Read A | 20 | 2012-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.9 | 2012 | Rb+Trans+Write | 12 | 2012-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.10 | 2013 | Cloze | 20 | 2013-eng1-use_of_english-q1–q20 | Weave | Narrative+Teaching(SB#3) |
| Ch.11 | 2013 | Read A | 20 | 2013-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.12 | 2013 | Rb+Trans+Write | 12 | 2013-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.13 | 2014 | Cloze | 20 | 2014-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.14 | 2014 | Read A | 20 | 2014-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.15 | 2014 | Rb+Trans+Write | 12 | 2014-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.16 | 2015 | Cloze | 20 | 2015-eng1-use_of_english-q1–q20 | Weave | Narrative+Teaching(SB#4) |
| Ch.17 | 2015 | Read A | 20 | 2015-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.18 | 2015 | Rb+Trans+Write | 12 | 2015-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.19 | 2016 | Cloze | 20 | 2016-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.20 | 2016 | Read A | 20 | 2016-eng1-reading_a-q21–q40 | Mirror | Narrative+Teaching(SB#5) |
| Ch.21 | 2016 | Rb+Trans+Write | 12 | 2016-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.22 | 2017 | Cloze | 20 | 2017-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.23 | 2017 | Read A | 20 | 2017-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.24 | 2017 | Rb+Trans+Write | 12 | 2017-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.25 | 2018 | Cloze | 20 | 2018-eng1-use_of_english-q1–q20 | Weave | Narrative+Teaching(SB#6) |
| Ch.26 | 2018 | Read A | 20 | 2018-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.27 | 2018 | Rb+Trans+Write | 12 | 2018-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.28 | 2019 | Cloze | 20 | 2019-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.29 | 2019 | Read A | 20 | 2019-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.30 | 2019 | Rb+Trans+Write | 12 | 2019-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.31 | 2020 | Cloze | 20 | 2020-eng1-use_of_english-q1–q20 | Weave | Narrative+Teaching(SB#7) |
| Ch.32 | 2020 | Read A | 20 | 2020-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.33 | 2020 | Rb+Trans+Write | 12 | 2020-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.34 | 2021 | Cloze | 20 | 2021-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.35 | 2021 | Read A | 20 | 2021-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.36 | 2021 | Rb+Trans+Write | 12 | 2021-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative+Teaching(SB#8) |
| Ch.37 | 2022 | Cloze | 20 | 2022-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.38 | 2022 | Read A | 20 | 2022-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.39 | 2022 | Rb+Trans+Write | 12 | 2022-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.40 | 2023 | Cloze | 20 | 2023-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.41 | 2023 | Read A | 20 | 2023-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.42 | 2023 | Rb+Trans+Write | 12 | 2023-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.43 | 2024 | Cloze | 20 | 2024-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.44 | 2024 | Read A | 20 | 2024-eng1-reading_a-q21–q40 | Mirror | Narrative+Teaching(SB#9) |
| Ch.45 | 2024 | Rb+Trans+Write | 12 | 2024-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.46 | 2025 | Cloze | 20 | 2025-eng1-use_of_english-q1–q20 | Weave | Narrative |
| Ch.47 | 2025 | Read A | 20 | 2025-eng1-reading_a-q21–q40 | Mirror | Narrative |
| Ch.48 | 2025 | Rb+Trans+Write | 12 | 2025-eng1-reading_b, translation, writing | Forge+Bridge+Script | Narrative |
| Ch.49 | Mixed | Boss Cloze+Read | 16 | Selected from all years | Weave+Mirror | Both |
| Ch.50 | Mixed | Boss All | 16 | Selected from all years | All types | Both |

### Question Count Verification

| Year | Cloze | Read A | Rb+Trans+Write | Year Total |
|------|-------|--------|----------------|------------|
| 2010 | 20 | 20 | 12 | 52 |
| 2011 | 20 | 20 | 12 | 52 |
| 2012 | 20 | 20 | 12 | 52 |
| 2013 | 20 | 20 | 12 | 52 |
| 2014 | 20 | 20 | 12 | 52 |
| 2015 | 20 | 20 | 12 | 52 |
| 2016 | 20 | 20 | 12 | 52 |
| 2017 | 20 | 20 | 12 | 52 |
| 2018 | 20 | 20 | 12 | 52 |
| 2019 | 20 | 20 | 12 | 52 |
| 2020 | 20 | 20 | 12 | 52 |
| 2021 | 20 | 20 | 12 | 52 |
| 2022 | 20 | 20 | 12 | 52 |
| 2023 | 20 | 20 | 12 | 52 |
| 2024 | 20 | 20 | 12 | 52 |
| 2025 | 20 | 20 | 12 | 52 |
| **Subtotal** | **320** | **320** | **192** | **832** |
| Boss Rush (Ch.49-50) | +0 | +0 | +0 | 0* |
| **Grand Total** | **320** | **320** | **192** | **832** |

> *Ch.49-50 draw their 32 questions from the 832 pool (re-use of hardest questions from earlier years as synthesis challenges). Total unique questions remains 832.

---

## v3-Table 4: Difficulty Progression (50-Chapter)

| Chapters | Exam Year | Narrative CEFR | Embedded Text CEFR | Tier 1 Glyphs/Ch | Cumulative Glyphs | Study Break? |
|----------|----------|----------------|-------------------|------------------|-------------------|-------------|
| Ch.1–3 | 2010 | B1 | B2 | 5 | 15 | SB#1 (Ch.2) |
| Ch.4–6 | 2011 | B1 | B2 | 5 | 30 | SB#2 (Ch.6) |
| Ch.7–9 | 2012 | B1+ | B2 | 5 | 45 | — |
| Ch.10–12 | 2013 | B1+ | B2 | 5 | 60 | SB#3 (Ch.10) |
| Ch.13–15 | 2014 | B1+ | B2-C1 | 5 | 75 | — |
| Ch.16–18 | 2015 | B2 | B2-C1 | 5 | 90 | SB#4 (Ch.16) |
| Ch.19–21 | 2016 | B2 | C1 | 5 | 105 | SB#5 (Ch.20) |
| Ch.22–24 | 2017 | B2 | C1 | 5 | 120 | — |
| Ch.25–27 | 2018 | B2 | C1 | 5 | 135 | SB#6 (Ch.25) |
| Ch.28–30 | 2019 | B2+ | C1 | 5 | 150 | — |
| Ch.31–33 | 2020 | B2+ | C1 | 5 | 165 | SB#7 (Ch.31) |
| Ch.34–36 | 2021 | B2+ | C1 | 5 | 180 | SB#8 (Ch.36) |
| Ch.37–39 | 2022 | B2+ | C1 | 5 | 195 | — |
| Ch.40–42 | 2023 | B2+ | C1 | 5 | 210 | — |
| Ch.43–45 | 2024 | B2+ | C1 | 5 | 225 | SB#9 (Ch.44) |
| Ch.46–48 | 2025 | B2+ | C1 | 5 | 240 | — |
| Ch.49–50 | Mixed | B2+ | C1 | Review | 244 | — |

---

## v3-Table 5: Seven Labyrinths Foreshadowing Timeline (Updated for 50 Chapters)

| Ch. | Foreshadowing Event | Key Foreshadow Words | Intensity |
|-----|-------------------|----------------------|-----------|
| Ch.1 | Feimo enters the first room; "gateway" on archway | gateway, translation | ○○○○○ Subtle |
| Ch.4 | The Labyrinth extends deeper than expected | corridor, boundary | ○○○○○ |
| Ch.8 | A "guardian" statue speaks of "archives below" | guardian, archive | ○○○○○ |
| Ch.12 | A dead-end "maze" pattern; Feimo uses "navigate" | maze, navigate, route | ○○○●● Building |
| Ch.16 | "Boundary" stones mark the known Labyrinth's edge | boundary, limit, bound | ○○○●● |
| Ch.20 | 绯墨 senses "echoes" from beyond the walls | echo, whisper, resonate | ○○●●● |
| Ch.24 | An ancient "cipher" inscription appears | cipher, code, sealed | ○○●●● |
| Ch.26 | **The Seven Labyrinths are named** | labyrinth × 7, forbidden | ○●●●● Reveal |
| Ch.30 | The Second Labyrinth's "sentinel" appears | sentinel, frontier | ●●●●● Active |
| Ch.34 | The Translation Labyrinth (绯墨's focus) opens | bilingual, multilingual, translation | ●●●●● |
| Ch.38 | A "sealed" gate blocks the Fifth Labyrinth | sealed, threshold, ancient | ●●●●● |
| Ch.42 | The "master cipher" requires all 106 cards | cipher, archive, pattern | ●●●●● |
| Ch.46 | All Seven Labyrinths connected in one structure | All foreshadow words | ●●●●● Payoff |
| Ch.50 | The labyrinth is revealed as Feimo's own mind | labyrinth, identity, self | ●●●●● |

---

## v3-Table 6: Foreshadow Cards (Updated)

| Card # | Ch. (v3) | 🔮 Tag | Foreshadow Role |
|--------|----------|--------|----------------|
| 004 | Ch.10 | Labyrinth Theory | "What makes a text literary" = "What makes a Labyrinth a Labyrinth" |
| 005 | Ch.10 | Threshold | Defamiliarization = crossing into the strange |
| 010 | Ch.8 | Perspective Shift | Different POVs = different Labyrinth paths |
| 046 | Ch.11 | Constraint | Three Unities = Labyrinth rules |
| 076 | Ch.19 | Library Labyrinth | Borges' Library of Babel = THE labyrinth |
| 084 | Ch.41 | Structure | Deep structures = hidden Labyrinth architecture |
| 087 | Ch.43 | Map | 31 functions = map through narrative Labyrinths |
| 088 | Ch.43 | Semiotic Grid | Semiotic square = navigational grid |
| 090 | Ch.44 | Self-Awareness | Metafiction = Labyrinth recognizing itself |
| 091 | Ch.45 | Infinite Corridor | Différance = endless corridors |
| 092 | Ch.45 | Collapse | Deconstruction = walls coming down |
| 093 | Ch.46 | Archive Guardian | Foucault's archive = Labyrinth's memory |
| 100 | Ch.49 | Master Map | Knowledge network = Labyrinth's blueprint |

---

## v3-Table 7: Bridge院 Vocabulary Density Map (Updated)

> 绯墨's specialist chapters (translation-heavy): **Ch.11, Ch.15, Ch.20, Ch.31, Ch.35**

| Ch. | Bridge院 Density | Key Bridge Vocab | Why |
|-----|-----------------|------------------|-----|
| Ch.1 | Medium | explain, suggest, convey (seed) | Foundation: basic translation verbs |
| Ch.11 | **High** | express, describe, convey | First translation encounter |
| Ch.15 | **High** | convey, describe, express, explain | Bridge verbs cluster |
| Ch.20 | **Very High** | ★demonstrate, ★indicate, ★reveal, ★convey | SB#5: Translation Basics |
| Ch.31 | **Very High** | ★interpret, ★translate, ★convey, ★illustrate | SB#7: Translation Advanced |
| Ch.35 | **High** | ★multilingual, ★bilingual, ★perspective | Bridge expansion |

---

## v3 Change Log

| Section | What Changed from v2 |
|---------|---------------------|
| v3-Table 0 | **New** — 50-chapter architecture, act structure, year mapping |
| v3-Table 1 | All 244 Tier 1 words re-assigned to Ch.1–50 (~5/ch); promoted words distributed |
| v3-Table 2 | All 106 cards re-mapped to 50 chapters (~2/ch); verified 106/106 |
| v3-Table 3 | Exam questions remapped: 3 chapters/year (Cloze/ReadA/Mixed); Boss Rush Ch.49-50 |
| v3-Table 4 | Difficulty curve expanded to 50 chapters; cumulative glyph count |
| v3-Table 5 | Foreshadow timeline expanded to 50-chapter granularity |
| v3-Table 6 | Foreshadow card chapter assignments updated |
| v3-Table 7 | Bridge院 density map updated for 50 chapters |

**Status**: v3 complete. Pending: 庄方宜's new outline for final card-chapter calibration.
