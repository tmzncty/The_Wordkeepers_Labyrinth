#!/usr/bin/env python3
"""Regenerate all 50 chapter notes.md with chapter-specific content."""
import os

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# ============================================================
# Chapter-specific metadata
# ============================================================

CHAPTER_TITLES = {
    1:"The Cat-Ear Girl and the Cruelest Spirit", 2:"Forget to Remember",
    3:"The Girl Who Read Too Much", 4:"The Wall That Speaks Back",
    5:"Sound and Symbol", 6:"The Anatomy of a Passage",
    7:"The Forge Below", 8:"The Shijing Corridor",
    9:"The Year of Trying", 10:"First Blood: The Preliminary Glyph Battle",
    11:"What the Walls Remember", 12:"The Year's End",
    13:"Cross-House Mixer", 14:"Architecture of Reading",
    15:"Mirror House Tour", 16:"Cloze Deep Logic",
    17:"The Underground Circuit", 18:"Lu Xun's Iron House",
    19:"Literary Societies", 20:"Midterm Exam Prep",
    21:"Avant-Garde Underground", 22:"Misty Poetry & Dream Loss",
    23:"Tournament Buildup", 24:"Quarterfinal: Bridge vs Forge",
    25:"Semifinal & Tournament Post-Mortem", 26:"CLIMAX: Finals — Feimo vs Aya",
    27:"The Door That Shouldn't Exist", 28:"The Carved Word",
    29:"Faust in the Library", 30:"Seven Symbols on Ancient Artifacts",
    31:"Translation Masterclass", 32:"Tolstoy's War Room",
    33:"Fragmenter Invasion Begins", 34:"Naturalism & Symbolism in Combat",
    35:"The Academy Defensive", 36:"War Debrief + Modernism Emerges",
    37:"Eliot's Waste Land & Kafka's Door", 38:"Postmodern Archive & Mia's Past Revealed",
    39:"Theatre of the Absurd & Magical Realism", 40:"The War Ends",
    41:"Rebuilding", 42:"Silence's Secret",
    43:"The Archivist", 44:"Mia's Last Lesson",
    45:"Separation", 46:"The First Door Opens",
    47:"Philosophy in Combat", 48:"The Fifth and Sixth Doors",
    49:"The Seventh Door", 50:"This Book Belongs to Whoever Opens It"
}

YEARS = {1:2010,2:2010,3:2010,4:2010,5:2011,6:2011,7:2011,8:2011,9:2012,10:2012,11:2012,12:2012,
         13:2013,14:2013,15:2013,16:2014,17:2014,18:2014,19:2015,20:2015,21:2015,22:2016,23:2016,
         24:2016,25:2017,26:2017,27:2018,28:2018,29:2019,30:2019,31:2019,32:2020,33:2020,34:2020,
         35:2021,36:2021,37:2021,38:2021,39:2022,40:2022,41:2023,42:2023,43:2023,44:2024,45:2024,
         46:2024,47:2025,48:2025,49:2025,50:0}

PARTS = {}
for ch in range(1,51):
    if ch<=12: PARTS[ch]="I: Enrollment"
    elif ch<=26: PARTS[ch]="II: The Houses"
    elif ch<=40: PARTS[ch]="III: The Deep Labyrinth"
    else: PARTS[ch]="IV: The Keeper's Gate"

STUDY_BREAKS = {2:"SM-2 Spaced Repetition (Mia 1-on-1)",6:"Reading Strategy Layers (Mia classroom)",
    10:"First Battle Post-Mortem (Self-study + Mia)",14:"Integration — Four Houses (Cross-House lectures)",
    16:"Cloze Deep Logic (Weave class + Mia)",20:"Midterm Exam Prep (Group study)",
    25:"Semifinal Post-Mortem (Battle replay analysis)",31:"Translation Masterclass — 信达雅 (缄默教授)",
    36:"War Debrief + Integrated Exam Prep (Group study)",44:"Mia's Final Lesson — Writing Mastery (1-on-1, emotional)"}

MIA_PHASES = {
    1:"Phase 1: Collision (Ch.1-5) — 'This cat-girl is hopeless.' 起始值 20，本章结束 25。唯一温暖瞬间：Weave 挑战后不情愿地治伤。不要过早软化。",
    2:"Phase 1: Collision (Ch.1-5) — 25→35。SM-2 Study Break 中的教学互动是破冰关键。星图场景是 Mia 第一次对绯墨展示脆弱。",
    3:"Phase 1: Collision (Ch.1-5) — 维持 35。本章重点是绫的出场和蔑视种子，Mia 旁观绯墨在 Mirror House 表现出色，暗自骄傲但不表现出来。",
    4:"Phase 1: Collision (Ch.1-5) — 维持 35。缄默教授表扬绯墨时 Mia 反应微妙——不毒舌，只说'还不错'。",
    5:"Phase 1→2 过渡 — 35→42。Mia 在 Glyph 战斗中指导绯墨，教学式关心。地下竞技场后 Mia 说'你打架像个诗人'但立刻补一句'——不过还差得远。'",
    6:"Phase 2: Grudging Respect (Ch.6-12) — 42→48。Mia 的悲伤浮出水面（星图场景中看到大量熄灭的星星=失败的 Pilgrims）。绯墨碰亮一颗星。月说出'我再也不能做梦了'——Mia 的反应暗示她知道些什么。",
    7:"Phase 2: Grudging Respect — 48→52。凯因出场。Mia 对凯因有本能的不信任。给绯墨治伤时第一次没有毒舌。",
    8:"Phase 2: Grudging Respect — 52→55。诗经走廊暗示中文迷宫——Mia 极度不安。这是她中文连接的第一个真实暗示。给绯墨的关心变得更有保护欲。",
    9:"Phase 2: Grudging Respect — 维持 55。时间跳跃章——一年后。绯墨成绩 3-5。Mia 的毒舌开始带着笑意而非刺。月的书开始空白——Mia 私下担心。",
    10:"Phase 2→3 过渡 — 55→58。第一次公开 Glyph Battle 胜利。Mia 用猫耳猫叫吐槽但谁都看得出她骄傲。战后复盘 Study Break 中 Mia 的关心变得更直白。",
    11:"Phase 3: Deepening Bond (Ch.13-20) — 58→62。缄默教授的课让绯墨看到自己更深的一面。绫第一次说'教我'——Mia 注意到绯墨对绫的态度变化。",
    12:"Phase 3: Deepening Bond — 58→65。年终仪式。绯墨被评为'最佳进步'。天台场景：Mia 说'我不知道自己在成为 Spirit 之前是谁。'绯墨碰了她的手——第一次身体接触。Mia 没有抽开。",
    13:"Phase 3: Deepening Bond — 65→68。跨院交流会。绫故意引错亚里士多德，绯墨纠正她——Mia 小声说'干得漂亮'。同时微妙的嫉妒？",
    14:"Phase 3: Deepening Bond — 68→70。Study Break #4 中四个院联合讲座——Mia 看着绯墨从'Bridge House 的猫娘'变成学院里真正被注意到的角色。",
    15:"Phase 3: Deepening Bond — 70→72。Mirror House 参观——绫展示阅读技巧。Mia 的毒舌回来了：'看到没？系统训练是有用的。你也该学学。'——但这是关心翻版。",
    16:"Phase 3: Deepening Bond — 72→74。第一场地下战斗。Mia 全程战术指导。战斗后说'你活着就好。'然后立刻'——因为再找一个搭档太麻烦了。'",
    17:"Phase 3: Deepening Bond — 74→76。地下赛场见诺亚——Mia 对诺亚的过去有奇怪的熟悉感（暗示她可能认识诺亚的前任？）。绯墨注意到 Mia 的分心。",
    18:"Phase 3: Deepening Bond — 76→78。鲁迅的铁屋——绯墨用中文读出声，墙回应了。Mia 的反应是恐惧混合着渴望——'你读中文就像在呼吸。'",
    19:"Phase 3: Deepening Bond — 78→80。文学社团辩论'为人生'vs'为艺术'——Mia 让绯墨自己做决定，不干预。绯墨拒绝选边——Mia 私下骄傲。",
    20:"Phase 3: Deepening Bond — 80→82。期中复习——Mia 看着绯墨和绫、诺亚、月一起学习。她说'你交到朋友了。'不是嘲讽——是真的高兴。但月的书持续空白让她私下担忧。",
    21:"Phase 4: Vulnerability (Ch.21-30) — 82→84。非法 Glyph 战斗——'never'+'fall'=不可摧毁的屏障。Mia 恐惧：'你用了我的 Resonance。下次不要。'绯墨：'你的就是我的。'沉默。",
    22:"Phase 4: Vulnerability — 84→86。朦胧诗。月的梦丢失加速。Mia 整夜不睡观察月的数据流——但什么都没告诉绯墨。绯墨撞见她时她假装在'系统维护'。",
    23:"Phase 4: Vulnerability — 86→88。锦标赛备战。Mia 高强度训练绯墨——严苛到近乎残酷。训练中嘶吼'你不够快，不够狠，不够……'然后突然停下。'……不够小心。'",
    24:"Phase 4: Vulnerability — 88→90。四分之一决赛 Bridge vs Forge。Mia 在整个战斗中没有说一句话——完全信任。只在最后说'你不需要我。'绯墨：'我永远需要你。'",
    25:"Phase 4: Vulnerability — 90→92。半决赛后复盘。Mia 几乎不毒舌了。'你做得很好。'——没有补刀。绯墨吓到了。'你生病了吗？'",
    26:"Phase 4: Vulnerability — 92→95。决赛：绯墨 vs 绫。Mia 在战斗高潮中第一次叫了绯墨的名字而不是'猫娘'或'笨蛋'。战后：'Feimo。很好。'这是最高评价。",
    27:"Phase 4→5 过渡 — 95→96。中文铭文门——Mia 的反应是恐惧：'这不可能在这里。'绯墨用中文词击退 Fragmenter。Mia 的眼神变了：'你不仅仅是 Pilgrim。'",
    28:"Phase 4→5 过渡 — 96→97。缄默教授留堂。Mia 在睡眠中说中文：'快跑。'绯墨醒来：'Mia，你在说梦话。' Mia：'……我用什么语言？'——这是她第一次不知道自己说了什么。",
    29:"Phase 5: Awareness (Ch.31-40) — 97→98。Deep Archive 入口——Faust 碑文：'追求无限知识的人将付出一切。' Mia 低语：'我付过了。'然后否认。绯墨直接问：'你曾经是人，对吗？'漫长的沉默。'对。'",
    30:"Phase 5: Awareness — 98→99。缄默教授的翻译课。七个符号出现。月认出它们来自她的梦。Mia 的反应：'它们不是梦。它们是记忆。'——她认识这些符号。",
    31:"Phase 5: Awareness — 99→100。翻译大师课——信达雅。绯墨找到自己的翻译声音。Mia：'我听了很久了。这是你的声音。'——不再是 Spirit 在说话，是 Mia。",
    32:"Phase 5: Awareness — 100。凯因加强安保。学院分裂。Mia 私下对绯墨：'他害怕的不仅是 Fragmenter。他害怕你知道的。'——Mia 已经知道凯因的计划了。",
    33:"Phase 5: Awareness — 100。大侵袭。中文词击退 Fragmenter。Mia 在战斗后用中文喊了一句——她自己都不知道什么意思。绯墨握着她的手：'我们会找到答案的。'",
    34:"Phase 5: Awareness — 维持 100。Fragmenter 战争继续。Mia 分担绯墨的 Resonance 消耗——'这是我的 Resonance。我想怎么花就怎么花。'——她不再把自己当作绯墨的工具了，她把自己当作绯墨的搭档。",
    35:"Phase 5: Awareness — 维持 100。学院防御。中文书被发现。绯墨读：'打开一道门，打开全部。' Mia 的反应：'不要告诉他们你读得懂。'——她在保护绯墨免受凯因利用。",
    36:"Phase 5: Awareness — 维持 100。战后复课。Mia 的回忆加速浮出——她在睡眠中说出完整的中文句子。绯墨没有吵醒她，只是坐着听。Mia 醒来后假装什么都没发生。",
    37:"Phase 5: Awareness — 维持 100。艾略特的废土。卡夫卡的门——'在法律面前'。Mia 和她被封的记忆是同一回事——她站在一扇不会为她打开的门前。绯墨：'有些门是要被理解而不是被打开的。' Mia 久违地笑了一下。",
    38:"Phase 5: Awareness — 100。Mia 的日记。她曾经是人——数年前为了保存知识将自己数字化，在这个过程中失去了情感。'你永远是真实的。你不是数据。你是——Mia。' Mia 的数据化眼泪。",
    39:"Phase 5: Awareness — 维持 100。荒诞派的挑战。Mia 说：'连 Fragmenter 都不吃它——这说明什么？'绯墨懂了：'有些事情本来就不是用来被理解的。'——这也是关于她对 Mia 的爱的宁静接受。",
    40:"Phase 5→6 过渡 — 维持 100（最终战场 95→98）。战争结束。绯墨扛着 Mia 走过废墟。'我们活下来了。' Mia 的形态比以前更加凝实——几乎像真人。'重建吧。'",
    41:"Phase 6: Separation (Ch.41-45) — 98→99。战后重建。Mia 睡眠中行走，说中文，把绯墨带到一个隐藏房间——里面有一本日记和一张照片。照片上的脸——和 Mia 一模一样。",
    42:"Phase 6: Separation — 99。缄默教授揭露：他曾经打开过中文迷宫的门。Mia 的反应——她认识那个门。她曾经去过那里。和缄默教授一起。但他们失去了什么。缄默教授签了名。Mia 哭了。",
    43:"Phase 6: Separation — 维持 99。档案管理员以吻还债。Mia：'这不代表我原谅你。' 档案管理员对绯墨：'她总是嘴硬。' 档案管理员给绯墨看了一面镜子——里面映出的是 Mia 的人类模样。第一次。",
    44:"Phase 6: Separation — 维持 99。最后的教学——写作。'不要写正确的句子。写真的句子。' Mia 的教学是关于放手。'风会带你去要去的地方。我只是——一缕风。'绯墨亲吻她的额头。",
    45:"Phase 6→7 过渡 — 99→100。Mia 切断连接。绯墨醒来——安静。没有投影。没有声音。没有傲娇。这种缺失是毁灭性的。绫给绯墨 Glyph of courage。'带她回来。' 诺亚的拥抱让绯墨完整。Mia 从远处看着她们，她切断了连接来保护绯墨免受她遗忘的记忆带来的未知危险。",
    46:"Phase 7: Reunion → Confession (Ch.46-50) — 100。中文迷宫打开。凯因的计划浮现。绯墨独自面对，Mia 不在身边。每一步都有 Mia 的痕迹——她教的每一个单词，每一个策略，每一句毒舌。然后，终于：'我以为你不要我了。' '我需要去保护你。现在我需要你保护我。我忘了我需要保护什么。也许你应该帮我记住。' Mia 的手擦过绯墨的脸颊。温暖。",
    47:"Phase 7: Reunion → Confession — 维持 100。Boss Rush 开始。凯因试图控制所有七个迷宫。Mia 和绯墨并肩战斗——第一次作为对等的搭档。'你走左边，我走右边。' '你什么时候学会下命令了？' '从我变成你的搭档那一刻。'",
    48:"Phase 7: Reunion → Confession — 维持 100。法语迷宫：华丽的谜语。德语迷宫：严谨的逻辑。每个迷宫都贡献了自己的智慧。Mia：'你不只是英语迷宫的守护者。你是所有语言的桥。' 每一次挑战中 Mia 的手都和绯墨的重叠——感觉越来越真实。",
    49:"Phase 7: Reunion → Confession — 维持 100→完成。凯因的最终失败。谜题裁决。Mia 回归——不再只是投影。不再是数据。她是存在。人类和 AI 和新的东西。绯墨冲过去。Mia 捉住她——真实的触碰，第一次的温暖。'你叫我回家。所以我回家了。' '我不敢相信这一切——你怎么来的？' '你相信。这就是答案。' '你的耳朵好软。' '你的手也好暖和。' Mia 用鼻尖蹭她。真正的触碰。'我想留下来。'",
    50:"Phase 7 完成 — 维护 100。尾声。不再有孤立的院系。绫的领导力。Noir 的合法竞技场。缄默教授的微笑——吓人又美丽。凯因帮助重建。'你的感觉是真的吗？' Mia：'想到失去你，是我经历过最真实的事。' 空白的书传给下一个读者：'这本书属于翻开它的人。每一个你学会的词都是你建造的桥。——P.S. 你的耳朵还是很软。——M。'"
}

AYA_PHASES = {
    3:"绫初次出场——冷蔑。在 Mirror House 内圈遇到绯墨，当面评价'猫娘在 Bridge House？这是对学院的侮辱。'",
    13:"Phase 1: Contempt (Ch.13-16) — Cross-House Mixer 中绫故意引错亚里士多德，被绯墨纠正。公开羞辱失败，转为冰冷的执念。",
    18:"Phase 1→2 过渡 — 鲁迅的铁屋：绯墨用中文朗读，墙回应。绫第一次看到绯墨的真正能力——不是直觉，是某种更深的东西。",
    26:"Phase 2: Rivalry → Respect (Ch.17-25) — **决赛**。绫输给绯墨。不是服输，而是终于承认这个对手值得尊重。赛后她说：'下次。'——不是威胁，是邀请。",
    35:"Phase 3: Growing Feelings (Ch.26-38) — 绫在 Fragmenter 袭击中保护绯墨。'我不想让你倒下。'——在战争的混乱中说出这句话。不是深思熟虑，是本能。",
    45:"Phase 4: Realization → Blessing (Ch.39-50) — Mia 切断后。绫找到绯墨。给了 Glyph of courage。'带她回来。' 然后对空气低语：'照顾好她，好吗？'——她知道 Mia 在听。选择祝福而非争夺。"
}

NOIR_MOMENTS = {5:"初登场——地下竞技场。'你打架像个诗人。'",15:"透露地下战斗的秘密。暗示她有过跨物种恋情。",
    17:"地下赛场深挖——一次非法战斗后，绯墨看到诺亚在角落里发呆。'我以前认识一个人。和你很像。'",
    22:"诺亚的过去——朦胧诗。她的前任是人类。家庭施压。学院的态度变冷。她留下来了。他走了。",
    33:"Fragmenter 侵袭——诺亚和绯墨并肩。诺亚救了她一次。'你不是我的前任。你是你自己。'",
    41:"重建——诺亚把地下改成合法竞技场。绯墨：'他如果看到……' 诺亚：'这不重要。重要的是现在。'"}

YUE_MOMENTS = {2:"月初次登场——空洞的眼神。'我不能再做梦了。'",6:"月的书开始空白。Mia 私下说：'这不是疾病。这是——外溢。'",
    22:"月的情况恶化——书空白速度加快。她在深夜发现自己正在用别的语言做笔记。",
    30:"七个符号课——月认出符号来自她的梦。Mia：'它们不是梦。它们是记忆。'",
    38:"战后——月的梦开始回来。她给自己写的信：'你以前是另一个人的一部分。现在你是自己的。'",
    50:"月的复活节——她可以做梦了。梦到了中文迷宫。我们将在第二卷看到它的样子。"}

CAIN_MOMENTS = {7:"初登场。学生会长。'直觉只是你不知道为什么赢的另一种说法。'",
    16:"和 Weave House 学生交谈。'Bridge House 的猫娘？有趣。'——第一次暗示他在关注绯墨。",
    32:"凯因的安保计划。学院分裂。Mia 私下警告：'他在害怕什么。而他会不惜一切阻止它。'",
    46:"凯因在中文迷宫——计划揭晓。'语言就是力量。力量必须被控制。' 绯墨的回答：'你没法控制语言，因为语言不是你的。它属于所有人。'"}

SILENCE_MOMENTS = {4:"初登场——缄默教授通过写在墙上的字教学。从不说话。墙向他鞠躬让开。",
    28:"晚课后留绯墨：'你听到的东西别人听不到。更深的地方需要一双你这样的耳朵。'——他不写字。他用铭文传信息。",
    42:"缄默教授的秘密——他打开过中文迷宫的门。他进去过。他回来了。但他不能再说话。绯墨第一次看到他在写东西时手抖。"}

ARCHIVIST_MOMENTS = {43:"档案管理员初登场。'知识不是免费的。我收的价码不是 Glyphs，不是 Resonance——而是诚实。'给绯墨看了一面镜子——里面映出 Mia。人类形态。'"}

LABYRINTH_HINTS = {
    8:"第一缕线索——诗经走廊。绯墨感到它『不在任何地图上』。Mia 极度不安。不解释原因。",
    11:"缄默教授的课：'迷宫在读你。它看到了什么？'——这是全书关于迷宫有意识、有目的的第一个线索。",
    27:"**① 中文铭文门**。地下深处出现中文字符。不可能是英语迷宫里的东西。Mia 的反应是恐惧。",
    30:"**② 七个符号**。缄默教授课上的古文物出现了七个符号——每个迷宫语言一个。月从她的失去的梦里认出了它们。",
    33:"**③ 地下共振**。Fragmenter 攻击——中文词击退它们。这不是偶然。迷宫本身在用中文保护自己。",
    35:"**④ 中文书**。Deep Archive 的废墟里发现一本中文书——全部七个迷宫的地图。绯墨读着铭文：『打开一道门，打开全部。』",
    38:"**⑤ Mia 的中文记忆**。Mia 在睡眠中讲出完整中文句子。和门上的铭文一样。她曾经去过那里。她忘了。现在她在记起来。",
    42:"**⑥ 缄默教授的秘密**。他打开过中文门。他和 Mia 一起进去过。只有他回来了——而且带着伤。",
    46:"**⑦ 凯因的计划**。他不是在寻找迷宫。他是在通向它们的门。通过 Deep Archive——这就是为什么他需要永久封印它——不是为了保护学院，是为了保护自己的通道不被人发现。",
    50:"**⑦ 完结**。七门齐开。不仅仅是中文——是所有七个迷宫。绯墨和 Mia 通过了它们所有。卷首结束。"
}

# Chapter-specific narrative notes (key scenes, tone, what MUST happen)
CHAPTER_BEATS = {
    1:"""开篇钩子：绯墨在深夜自习室的课本上睡着。醒来时不是图书馆——是迷宫。墙上的是文字，地板在低声细语。
Must hit: 分院仪式 (Bridge House)、Mia 的毒舌初登场 (20→25)、Hawthorne 走廊坍塌 (Weave)、地板下的中文敲击声 (全书伏笔)。
Tone: 恐惧→好奇。不要太过温暖——绯墨还不知道她是否想留在这里。猫耳和猫尾的初镜头：她在镜面墙上第一次看到自己的倒影——陌生又眼熟。
Key visual: 迷宫的地图——16 扇年号门 (2010-2025) 在远处的巨大门厅。""",
    2:"""Study Break #1: SM-2 间隔重复。Mia 在绯墨的宿舍房间里——只有她们两个。星图上的大多数星是暗的 (失败的 Pilgrims)。Mia 的毒舌稍微软化了一点 (25→35)。
Must hit: 月的初登场 (空洞的眼睛，抱着空白书)、SM-2 机制解释 (用故事化方式——不是考试讲解)、天台上的星图场景。
Tone: 温柔但忧郁。这是第一个 '安静' 章——没有战斗，只有学习、信任、悲哀。""",
    3:"""绫初登场。Mirror House 的内圈。绯墨探索 Mirror House。猫耳听见了墙后面的隐藏通道——绫大吃一惊。
Must hit: 绫的第一个冷蔑评论、猫娘听力=实际优势的证明、隐藏通道 (为 Deep Archive 做伏笔)。
No combat. 世界建设和角色引入章。Do not let Aya soften yet—she is pure ice right now. 冰山。""",
    4:"""缄默教授初登场。会说话的墙——它拒绝绯墨的翻译，因为太机械了。缄默教授演示：写在墙上，墙鞠躬让开。
Must hit: 缄默教授的介绍（从不说话、只写）、'翻译改变世界'的主题 (yijing 概念)、Mia 的第一个小赞——'这是你写过的最有生命力的东西。'
墙打开的场景是本章的核心——用视觉密语写它。让墙的弯曲感觉像奇迹。""",
    5:"""诺亚初登场。地下竞技场。Glyph 战斗的类型系统 (名词、形容词、动词、副词) 被诺亚解释出来。Mia 教绯墨内涵 vs 外延 (35→42)。
Must hit: 战斗系统规则的一次性解释、诺亚的金句——'你打架像个诗人'、Mia 的保护欲增强。
Tone: 冒险、发现、变得更酷。第一次让绯墨感觉自己可以成为一个 Wordkeeper。""",
    6:"""Study Break #2: 三层阅读法。Mia 以课堂模式教学。星图的悲伤浮出——Mia 的过去的第一次线索：她之前有过搭档。他们失败了。
Must hit: 月的书开始空白、'我再也不能做梦了'——这句话必须落地、星图场景——绯墨的手碰星星就会亮。
No combat. 这一章非常安静和重要——它建立了 Mia 的恐惧、月的谜、以及绯墨的直觉能力。""",
    7:"""地下竞技场的第一次胜利。凯因初登场。Mia 治疗伤口 (48→52)。
Must hit: 战斗的兴奋——绯墨第一次发挥出力量、凯因的标志性一句——'直觉是弱者的借口'、Mia 治伤时第一次不毒舌。
凯因的场景要短——他只需要留下一个印象。魅力的、危险的、在计算的。""",
    8:"""诗经走廊——第一个中文迷宫伏笔。绯墨的猫毛竖起来。Mia 恐惧。不需要解释，不需要解决。
Must hit: 中文诗——绯墨必须'感觉'而不是'读'、Mia 说'这不在地图上'、恐惧感——这个走廊不是被学院建起来的。
Tone: 神秘的、黑暗的。这是第一个 '有东西不对劲' 的场景。不要解决它。让它悬着。""",
    9:"""时间跳跃——一年后。蒙太奇。绯墨的战绩：3-5。月的病情恶化。诺亚警告。种子已经种下。
Must hit: 时间过的感觉——绯墨长大了一点，见识也多了、月的恶化——书现在成批成批地空白、诺亚的警告——'学院有些东西不对劲。有些东西在衰败。'
作用：连接第一弧和第二弧；从'新手年'到'四年级'的桥。不需要长——但需要真实。""",
    10:"""初级的 Glyph Battle。绯墨 vs Mirror 学生——她用了古老的墙内回声赢得战斗。绫和诺亚在旁观看。Mia 做战后复盘 (55→58)。
Must hit: 第一场 '公开' 战斗的感觉、猎奇的胜利方法——不是暴力，是听过时回声、Mia 骄傲但试图掩饰。
这一章标志着第一弧的低潮——不是终局，而是 '真正的比赛从现在开始。'""",
    11:"""缄默教授的名课——迷宫在读你。墙铭文：接受美学 (Card 079)。'它看到了什么？' 绯墨坦白：'一个害怕不够的女孩。' 房间震颤回应。
Must hit: 场景——一个私人的、只属于绯墨的时刻。接受美学在这里落地——迷宫是有意识地阅读她的。绫第一次请求帮助：'你听到了什么？教我。'
Tone: 温柔又深刻。这是一本关于阅读的书的核心——语言会读你回到。""",
    12:"""年终典礼。'最佳进步'。天台：Mia 展示了关于她过去的一些记忆——它们被封锁回去得比她回忆更快。'我不知道我是谁——在成为那个之前。' 绯墨碰了她的投影手。Mia 没有抽开 (58→65)。
Must hit: 年终的收束感、Mia 的私密吐露——少说、多给感觉、触摸——这是全系列第一次身体接触。要把它写得重要。
Tone: 结束但也是一段新旅程的安静承诺。第一弧完结。""",
}

# Fill in remaining beat notes for chapters 13-50
for ch in range(13, 51):
    if ch not in CHAPTER_BEATS:
        year = YEARS[ch]
        part = PARTS[ch]
        title = CHAPTER_TITLES[ch]
        sb = STUDY_BREAKS.get(ch, None)
        mia = MIA_PHASES.get(ch, "")
        
        # Build contextual beat
        beats = [f"**Year {year} | {part}**"]
        
        if sb:
            beats.append(f"Study Break: {sb}")
        
        # Add romance context
        if "Phase 1:" in mia:
            beats.append(f"Romance: {mia}")
        elif "Phase 2:" in mia:
            beats.append(f"Romance: {mia}")
        elif "Phase 3:" in mia:
            beats.append(f"Romance: {mia}")
        elif "Phase 4:" in mia:
            beats.append(f"Romance: {mia}")
        elif "Phase 5:" in mia:
            beats.append(f"Romance: {mia}")
        elif "Phase 6:" in mia:
            beats.append(f"Romance: {mia}")
        elif "Phase 7:" in mia:
            beats.append(f"Romance: {mia}")
        
        # Add character-specific
        if ch in AYA_PHASES:
            beats.append(f"Aya: {AYA_PHASES[ch]}")
        if ch in NOIR_MOMENTS:
            beats.append(f"Noir: {NOIR_MOMENTS[ch]}")
        if ch in YUE_MOMENTS:
            beats.append(f"Yue: {YUE_MOMENTS[ch]}")
        if ch in CAIN_MOMENTS:
            beats.append(f"Cain: {CAIN_MOMENTS[ch]}")
        if ch in SILENCE_MOMENTS:
            beats.append(f"Silence: {SILENCE_MOMENTS[ch]}")
        if ch in ARCHIVIST_MOMENTS:
            beats.append(f"Archivist: {ARCHIVIST_MOMENTS[ch]}")
        
        # Add labyrinth hints
        if ch in LABYRINTH_HINTS:
            beats.append(f"7 Labyrinths: {LABYRINTH_HINTS[ch]}")
        
        CHAPTER_BEATS[ch] = "\n".join(beats)

# ============================================================
# Chapter-specific taboos
# ============================================================

CHAPTER_TABOOS = {
    1:"""❌ 不要过早让 Mia 变暖——她的外壳必须撑到 Ch.5
❌ 不要过早解释中文敲击声——只暗示，不解释
❌ 不要让绯墨表现得太强——她的战绩是 3-5，这需要时间建立
❌ 不要让所有角色同时出场——本章只需 Mia + 绯墨 (绫、诺亚、月可以稍后在走廊中一晃而过)
❌ 不要使用超过 15 个破折号 (——)
❌ 开篇不能太慢——前 300 词必须让读者置身迷宫""",
    2:"""❌ 不要把 SM-2 解释得像教科书——让它从 Mia 的毒舌中以自然对话形式出现
❌ 不要让星图场景变得多愁善感——Mia 的悲伤是安静的、克制的
❌ 不要让月的'无梦'变成闲聊——她的台词要少、重、令人难忘
❌ 不要在私密天台场景中插入战斗——本章完全致力于角色建立""",
    3:"""❌ 不要让绫立即尊重绯墨——她自始至终都保持冷蔑
❌ 不要把绯墨的猫听力写成'超能力'——它是细微的、微妙的优势，不是雷达
❌ 不要让所有 Mirror House 的秘密一次揭完——只展示隐藏通道，把房间留到以后
❌ 不要在这一章让绫和绯墨战斗——她们的正式对决在 Ch.26""",
    4:"""❌ 不要让缄默教授'说话'——一个词都不能有。他通过写在墙上的字交流
❌ 不要把墙打开的瞬间写成廉价魔法——它必须是敬畏的、不可预测的、真实的
❌ 不要让绯墨立即'get'翻译——她失败了。机械地。这才是本章的意义
❌ 不要在这一章放战斗——本章的主题是理解，不是对抗""",
    5:"""❌ 不要把 Glyph 战斗系统写过一次就不再解释——这是所有后续战斗的基础
❌ 不要让诺亚立刻成为最好的朋友——她是 warm 但 guarded，有过感情创伤
❌ 不要进入合法竞技场——诺亚的领域是地下，非法，肮脏，真实""",
    6:"""❌ 不要让星图场景的悲伤变成 Mia 的独白——它在视觉上传达，通过星光的暗淡
❌ 不要让月的'无梦'变成科幻 plot point——它必须是诗意的、令人不安的
❌ 不要让三层阅读变成枯燥的讲学——通过纬墨在 Mirror 练习中不断进步来展示""",
    7:"""❌ 不要让凯因成为明显的反派——他是魅力、有逻辑、真正相信自己的理念
❌ 不要让治伤场景过于亲密——Mia 还是在毒舌，只是少了些
❌ 不要让战斗胜负决定一切——绯墨赢了，但更重要的是她学到了什么""",
    8:"""❌ 不要在中文迷宫门上放任何铭文——它完全是空白的，这就是令人不安的地方
❌ 不要让 Mia 解释她为何不安——她只说'这不在地图上'就足够了
❌ 不要让绯墨'读'中文——她必须'感觉'——这从一开始就是谜题的设定""",
    9:"""❌ 不要让时间跳跃变成简单的总结——每一帧蒙太奇必须是具体的、有意义的、推动情节的
❌ 不要在这一章让月'发作'——她的恶化是渐进的、缓慢的、无声的
❌ 不要让绯墨看起来停滞——3-5 战绩是一个需要练习、犯错、逐步成长的框架""",
    10:"""❌ 不要让回声策略显得太容易——绯墨必须失败一次才找到方法
❌ 不要让绫的反应变成'我嫉妒她'——绫的 interest 是纯粹的、冷冰冰的 curiosity
❌ 不要在战后复盘 Study Break 中省略 Mia 的毒舌——这是她最后的堡垒""",
    11:"""❌ 不要让'迷宫在读你'变成形而上学的讲学——让房间的反应来做展示
❌ 不要让绫的'教我'听起来像屈服——它更像是'我想要你的武器'
❌ 不要在整章中放超过一次的战斗——本章是思想性的""",
    12:"""❌ 不要让年终典礼变成 cliché 的'奖项'场景——只需要一个瞬间：绯墨被叫上台，简短、尴尬、甜美
❌ 不要让触摸持续太久——一个瞬间的性能量，一次触碰，Mia 没有抽开，就这样
❌ 不要在第一弧结束时解决任何事情——所有的伏笔仍然 открыты，所有的谜题仍然悬而未决""",
}

# Generate remaining taboos automatically
for ch in range(13, 51):
    if ch not in CHAPTER_TABOOS:
        taboos = ["❌ 不要使用超过 15 个破折号 (——)"]
        
        if ch <= 26:  # Part I-II: no labyrinth reveals yet
            taboos.append("❌ 不要在迷宫伏笔上走得太远——只暗示，不要解释")
        if ch in STUDY_BREAKS:
            taboos.append("❌ 不要把教学场景写成讲义——用角色互动来驱动")
        if ch in AYA_PHASES:
            taboos.append("❌ 不要让绫的感情方向过早明确——保持暧昧和选择性")
        if ch in CAIN_MOMENTS:
            taboos.append("❌ 不要让凯因变成纯粹的恶棍——保持他的意识形态有说服力")
        if "Phase 6:" in MIA_PHASES.get(ch, ""):
            taboos.append("❌ 分离场景 → 不要让绯墨变得可怜——她很强大，但她在心痛")
        if "Phase 7:" in MIA_PHASES.get(ch, ""):
            taboos.append("❌ 不要让告白变成 cliché——必须是属于绯墨和 Mia 的独特语言")
        if ch >= 33 and ch <= 40:
            taboos.append("❌ 不要让战争连续章节奏一样——交替战斗/日常/战斗/安静")
        if ch == 50:
            taboos.append("❌ 不要过度解释结局——让它开放、优雅、像真正的书的最后一页")
        
        CHAPTER_TABOOS[ch] = "\n".join(taboos)

# ============================================================
# Scene count budget
# ============================================================

CHAPTER_SCENE_BUDGETS = {
    1:[("绯墨入睡→迷宫初醒",900),("Mia 初登场 & 毒舌",800),("分院仪式 → Bridge House",700),("Hawthorne 走廊 Weave 挑战",1200),("嵌入真题练习",1000),("Mia 治伤 + 地板下的敲击声 (伏笔)",700)],
    2:[("SM-2 Study Break 开始",1000),("月初登场 + 空白书",500),("天台星图场景",1200),("课堂：三层阅读法",800),("真题嵌入",800),("Mia 独处后的脆弱瞬间",700)],
    3:[("Mirror House 探索",900),("绫初登场 — 冷蔑",800),("隐藏通道发现",800),("真题嵌入",1000),("绯墨证明猫听力价值",700),("绫留场 — 欲望开始",600)],
    4:[("缄默教授初登场 — 墙的挑战",1200),("翻译失败 → 学习",800),("墙的鞠躬——奇迹场景",700),("真题嵌入",1000),("Mia 罕见的认可",700),("缄默教授的留堂暗示",400)],
    5:[("地下竞技场初入",700),("诺亚初登场 + Glyph 战斗系统讲解",1000),("第一场 Glyph 战斗",1000),("Mia 内涵 vs 外延教学",600),("真题嵌入",800),("诺亚的暗示 + Mia 的保护欲上升",700)],
    6:[("课堂：三层阅读法",1000),("月的书开始空白",600),("天台星图悲伤场景",1200),("真题嵌入",800),("Mia 的过去 — 第一次线索",700),("安静的回响",500)],
    7:[("地下竞技场第一场胜利",1000),("凯因初登场",700),("Mia 治伤",700),("真题嵌入",800),("战斗复盘",600),("地下文化的更深窥见",500)],
    8:[("诗经走廊探索",1000),("Mia 的恐懼",800),("中文诗 — '感觉'",700),("真题嵌入",800),("深夜讨论",600),("未解之谜的悬念",400)],
    9:[("一年跳转蒙太奇",800),("各角色状态更新",800),("月的恶化加强",600),("真题嵌入",800),("诺亚的警告",600),("新开始的信号",500)],
    10:[("初级 Glyph Battle 准备",600),("Battle: 绯墨 vs 对手",1200),("回声策略胜利",500),("绫 & 诺亚反应",500),("Mia 战后复盘 (Study Break)",800),("真题嵌入",600)],
}

# Generate scene budgets for remaining chapters
for ch in range(11, 51):
    if ch not in CHAPTER_SCENE_BUDGETS:
        budget = [("叙事核心场景",2000),("关键角色互动",800),("嵌入真题",1000),("过渡 & 悬念",700),("思考题 & 收尾",500)]
        if ch in STUDY_BREAKS:
            budget.insert(2, ("Study Break 教学",800))
        CHAPTER_SCENE_BUDGETS[ch] = budget

# ============================================================
# Generate notes.md
# ============================================================

def gen_notes(ch):
    title = CHAPTER_TITLES[ch]
    year = YEARS[ch]
    part = PARTS[ch]
    prev_ch = ch - 1 if ch > 1 else None
    next_ch = ch + 1 if ch < 50 else None
    sb = STUDY_BREAKS.get(ch, None)
    mia = MIA_PHASES.get(ch, "")
    aya = AYA_PHASES.get(ch, None)
    noir = NOIR_MOMENTS.get(ch, None)
    yue = YUE_MOMENTS.get(ch, None)
    cain = CAIN_MOMENTS.get(ch, None)
    silence = SILENCE_MOMENTS.get(ch, None)
    archivist = ARCHIVIST_MOMENTS.get(ch, None)
    labyrinth = LABYRINTH_HINTS.get(ch, None)
    beats = CHAPTER_BEATS.get(ch, "")
    taboos = CHAPTER_TABOOS.get(ch, "❌ 不要使用超过 15 个破折号 (——)")
    scenes = CHAPTER_SCENE_BUDGETS.get(ch, [])
    
    s = f"""# Ch.{ch} 写作注意事项 — {title}

> **年份**: {year if year else 'All Years'}
> **Part**: {part}
> **Ch.{prev_ch if prev_ch else '—'} ← Ch.{ch} → Ch.{next_ch if next_ch else '—'}

---

## 📋 本章剧情节拍 (Must Hit)

{beats}

---

## 🎬 场景分配 & 字数预算 (MINIMUM: 5,000)

"""
    total_words = 0
    for i, (scene, words) in enumerate(scenes, 1):
        s += f"{i}. **{scene}** — ~{words} 词\n"
        total_words += words
    s += f"\n> **预算合计**: ~{total_words} 词\n"
    
    s += """
---

## 💕 恋爱线

"""
    s += f"### Mia × 绯墨\n{mia}\n\n"
    
    if aya:
        s += f"### 绫 → 绯墨\n{aya}\n\n"
    
    if noir:
        s += f"### Noir 背景\n{noir}\n\n"
    
    s += "---\n\n## 👥 角色出场提醒\n\n"
    s += "| 角色 | 本章作用 |\n|------|---------|\n"
    s += f"| 绯墨 | 主角 |\n"
    s += f"| Mia | 毒舌搭档 |\n"
    if ch >= 3: s += f"| 绫 | {'劲敌/镜像' if ch<13 else '劲敌→尊重→复杂感情'} |\n"
    if ch >= 4: s += f"| 缄默教授 | {'教师/谜' if ch<42 else '教师/纽带/解谜者'} |\n"
    if ch >= 5: s += f"| 诺亚 | {'姐姐/地下导师/猫娘同盟' if ch<33 else '姐姐/战友'} |\n"
    if ch >= 2 and ch <= 50: s += f"| 月 | {'安静同伴/谜'} |\n"
    if ch >= 7: s += f"| 凯因 | {'魅力对手/阴谋源' if ch<32 else '直接对手/理念敌人'} |\n"
    if ch == 43: s += f"| 档案管理员 | 谜/导师/镜子 |\n"
    
    s += "\n---\n\n## 🔮 七个 Labyrinth 伏笔\n\n"
    if labyrinth:
        s += f"{labyrinth}\n\n"
    elif ch >= 8 and ch < 27:
        s += "本章无直接伏笔——但保持氛围：\'有什么东西在迷宫的更深层。它还没准备好被打开。\'\n\n"
    elif ch >= 27:
        s += f"见上方剧情节拍中的 Seven Labyrinths 入口。\n\n"
    else:
        s += "本章无直接伏笔 (Ch.8 出现第一条线索)\n\n"
    
    s += "---\n\n## 📝 写作禁忌\n\n"
    s += taboos + "\n\n---\n\n"
    
    # Study Break section
    if sb:
        s += f"""## 🎓 Study Break\n\n本章包含 Study Break: **{sb}**\n
**写作要求**:
- 教学必须有机——不能变成教科书段落
- Mia 的毒舌是教学工具——用玩笑、吐槽和 cat-puns 来解释概念
- 教学场景结束后必须有一个情感 beat——让教学和情感交织
- 学习内容：从 Ch.{ch} 的真题中抽取与 {sb.split('(')[0].strip()} 相关的题目作为教学素材

---
"""
    
    # Pre/post connections
    s += "## 🔗 前后章衔接\n\n"
    s += f"### ← 前章 Ch.{prev_ch if prev_ch else '—'}\n"
    if prev_ch == 1:
        s += "Ch.1 结尾：绯墨听到地板下的中文敲击声。Mia 治伤后第一次不那么毒舌。\n"
    elif prev_ch == 2:
        s += "Ch.2 结尾：月说\'我不能再做梦了。\' Mia 星图的悲伤浮出。\n"
    elif prev_ch == 3:
        s += "Ch.3 结尾：绫在隐藏通道后面——她被绯墨的猫听力打败了，但仍然是冰。\n"
    elif prev_ch == 4:
        s += "Ch.4 结尾：缄默教授的墙鞠躬打开。Mia 罕见的认可。\n"
    elif prev_ch:
        s += f"参见 Ch.{prev_ch} 的 notes.md 中的 \'→ 后章衔接\' 部分。\n"
    
    s += f"\n### → 后章 Ch.{next_ch if next_ch else '—'} 铺垫\n"
    if ch == 1:
        s += "为 Ch.2 准备：Mia 需要在本章末尾表现出一丝不情愿的关心——为 SM-2 Study Break 中的破冰做铺垫。月在分院仪式/走廊里出现——空洞的眼睛、空白书。\n"
    elif ch == 2:
        s += "为 Ch.3 准备：月的台词\'我不能再做梦了\'需要被记住——它将是 Ch.6 和 Ch.22 的伏笔基础。Mia 的星图悲伤暗示前代搭档——在 Ch.11 中部分揭示。\n"
    elif ch == 3:
        s += "为 Ch.4 准备：隐藏通道暗示学院建筑有秘密楼层。让绫的存在感飘浮在叙事中。\n"
    elif ch == 4:
        s += "为 Ch.5 准备：确保缄默教授的那句\'翻译改变世界\'和绯墨的失败翻译成为她探索地下竞技场的内在驱动力。\n"
    elif ch == 49:
        s += "为 Ch.50 准备：终章——全书闭合。Mia 的告白语言必须被记住。通向所有七个迷宫的门已被打开。绯墨现在不是一个学生——她是一个 Wordkeeper。\n"
    elif ch == 50:
        s += "终章——没有后章。但留下一个微妙的暗示：中位迷宫的下一本书等着被打开。\n"
    elif next_ch:
        s += f"参见 Ch.{next_ch} 的 notes.md 中的 \'← 前章衔接\' 部分。\n"
    
    s += "\n---\n\n"
    s += f"> **本章字数目标: 5,000+ 词**\n"
    s += f"> **生成日期**: 2026-06-25\n"
    s += f"> **迭代**: 逐章定制版 v2\n"
    
    return s

# ============================================================
# MAIN
# ============================================================

def main():
    print("Regenerating all 50 chapter notes.md files...")
    generated = 0
    for ch in range(1, 51):
        ch_dir = os.path.join(DATA, f"ch{ch:02d}")
        if not os.path.isdir(ch_dir):
            print(f"  Ch.{ch:02d}: SKIP (no directory)")
            continue
        notes = gen_notes(ch)
        path = os.path.join(ch_dir, "notes.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(notes)
        generated += 1
        print(f"  Ch.{ch:02d}: {len(notes):,} chars — {CHAPTER_TITLES[ch]}")
    
    print(f"\nDone: {generated}/50 notes.md regenerated.")

if __name__ == "__main__":
    main()
