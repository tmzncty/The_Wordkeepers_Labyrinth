#!/usr/bin/env python3
"""
Batch generate all 50 chapter data packages for The Wordkeeper's Labyrinth.
- Fetches phonetics from Free Dictionary API
- Exports exam data from PostgreSQL
- Generates per-chapter markdown files
"""
import json, os, sys, time, re
import urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
GLOBAL = os.path.join(DATA, "_global")
os.makedirs(GLOBAL, exist_ok=True)

# ============================================================
# STEP 1: Chapter-Year-Card-Vocab mapping
# ============================================================

CHAPTERS = {
    1:  {"year": 2010, "title": "The Cat-Ear Girl and the Cruelest Spirit", "cards": [1,2], "study_break": False},
    2:  {"year": 2010, "title": "Forget to Remember", "cards": [3,4], "study_break": True, "sb_topic": "SM-2 Spaced Repetition"},
    3:  {"year": 2010, "title": "The Girl Who Read Too Much", "cards": [5,14], "study_break": False},
    4:  {"year": 2010, "title": "The Wall That Speaks Back", "cards": [6,15], "study_break": False},
    5:  {"year": 2011, "title": "Sound and Symbol", "cards": [7,10], "study_break": False},
    6:  {"year": 2011, "title": "The Anatomy of a Passage", "cards": [8,9], "study_break": True, "sb_topic": "Reading Strategy Layers"},
    7:  {"year": 2011, "title": "The Forge Below", "cards": [11,12], "study_break": False},
    8:  {"year": 2011, "title": "The Shijing Corridor", "cards": [13,16], "study_break": False},
    9:  {"year": 2012, "title": "The Year of Trying", "cards": [17,18], "study_break": False},
    10: {"year": 2012, "title": "First Blood: The Preliminary Glyph Battle", "cards": [19,20], "study_break": True, "sb_topic": "First Battle Post-Mortem"},
    11: {"year": 2012, "title": "What the Walls Remember", "cards": [21,79], "study_break": False},
    12: {"year": 2012, "title": "The Year's End", "cards": [80,81], "study_break": False},
    13: {"year": 2013, "title": "Cross-House Mixer", "cards": [82,83], "study_break": False},
    14: {"year": 2013, "title": "Architecture of Reading", "cards": [84,85], "study_break": True, "sb_topic": "Integration (Four Houses)"},
    15: {"year": 2013, "title": "Mirror House Tour", "cards": [22,23], "study_break": False},
    16: {"year": 2014, "title": "Cloze Deep Logic", "cards": [24,25], "study_break": True, "sb_topic": "Cloze Deep Logic"},
    17: {"year": 2014, "title": "The Underground Circuit", "cards": [26,27], "study_break": False},
    18: {"year": 2014, "title": "Lu Xun's Iron House", "cards": [28,29], "study_break": False},
    19: {"year": 2015, "title": "Literary Societies", "cards": [30,31], "study_break": False},
    20: {"year": 2015, "title": "Midterm Exam Prep", "cards": [32,33], "study_break": True, "sb_topic": "Midterm Exam Prep"},
    21: {"year": 2015, "title": "Avant-Garde Underground", "cards": [34,35], "study_break": False},
    22: {"year": 2016, "title": "Misty Poetry & Dream Loss", "cards": [36,37], "study_break": False},
    23: {"year": 2016, "title": "Tournament Buildup", "cards": [38,39], "study_break": False},
    24: {"year": 2016, "title": "Quarterfinal: Bridge vs Forge", "cards": [40,41], "study_break": False},
    25: {"year": 2017, "title": "Semifinal & Tournament Post-Mortem", "cards": [42,43], "study_break": True, "sb_topic": "Tournament Post-Mortem"},
    26: {"year": 2017, "title": "CLIMAX: Finals — Feimo vs Aya", "cards": [44,45], "study_break": False},
    27: {"year": 2018, "title": "The Door That Shouldn't Exist", "cards": [46,47], "study_break": False},
    28: {"year": 2018, "title": "The Carved Word", "cards": [48,49], "study_break": False},
    29: {"year": 2019, "title": "Faust in the Library", "cards": [50,51], "study_break": False},
    30: {"year": 2019, "title": "Seven Symbols on Ancient Artifacts", "cards": [52,53], "study_break": False},
    31: {"year": 2019, "title": "Translation Masterclass", "cards": [54,55], "study_break": True, "sb_topic": "Translation Masterclass"},
    32: {"year": 2020, "title": "Tolstoy's War Room", "cards": [56,57], "study_break": False},
    33: {"year": 2020, "title": "Fragmenter Invasion Begins", "cards": [58,59], "study_break": False},
    34: {"year": 2020, "title": "Naturalism & Symbolism in Combat", "cards": [60,61], "study_break": False},
    35: {"year": 2021, "title": "The Academy Defensive", "cards": [62,63], "study_break": False},
    36: {"year": 2021, "title": "War Debrief + Modernism Emerges", "cards": [64,65], "study_break": True, "sb_topic": "War Debrief + Exam Prep"},
    37: {"year": 2021, "title": "Eliot's Waste Land & Kafka's Door", "cards": [66,67], "study_break": False},
    38: {"year": 2021, "title": "Postmodern Archive & Mia's Past Revealed", "cards": [68,69], "study_break": False},
    39: {"year": 2022, "title": "Theatre of the Absurd & Magical Realism", "cards": [70,71], "study_break": False},
    40: {"year": 2022, "title": "The War Ends", "cards": [72,73], "study_break": False},
    41: {"year": 2023, "title": "Rebuilding", "cards": [74,75], "study_break": False},
    42: {"year": 2023, "title": "Silence's Secret", "cards": [76,77], "study_break": False},
    43: {"year": 2023, "title": "The Archivist", "cards": [78,86], "study_break": False},
    44: {"year": 2024, "title": "Mia's Last Lesson", "cards": [87,88], "study_break": True, "sb_topic": "Mia's Final Lesson (Writing Mastery)"},
    45: {"year": 2024, "title": "Separation", "cards": [89,90], "study_break": False},
    46: {"year": 2024, "title": "The First Door Opens", "cards": [91,92], "study_break": False},
    47: {"year": 2025, "title": "Philosophy in Combat", "cards": [93,94], "study_break": False},
    48: {"year": 2025, "title": "The Fifth and Sixth Doors", "cards": [95,96], "study_break": False},
    49: {"year": 2025, "title": "The Seventh Door", "cards": [97,98], "study_break": False},
    50: {"year": 0,    "title": "This Book Belongs to Whoever Opens It", "cards": [99,100,101,102,103,104,105,106], "study_break": False},
}

# Card number → Chinese name mapping
CARD_NAMES = {
    1:"文学四要素",2:"文艺学三分支",3:"文学理论教程体系",4:"文学性",5:"陌生化",
    6:"文学本质论",7:"意境",8:"典型",9:"意象与象征",10:"叙事视角",
    11:"文学风格",12:"文学流派",13:"文学思潮",14:"文学体裁",15:"文学语言与日常语言",
    16:"诗经六义",17:"楚辞与屈原",18:"建安风骨",19:"文学自觉",20:"唐诗四期",
    21:"李白与杜甫",22:"宋词两大流派",23:"唐诗与宋诗",24:"元杂剧体制",25:"西厢记与窦娥冤",
    26:"四大名著类型学",27:"红楼梦",28:"鲁迅小说",29:"五四文学革命",30:"文学研究会与创造社",
    31:"茅盾与子夜",32:"沈从文与京派",33:"新感觉派",34:"先锋文学",35:"寻根文学",
    36:"朦胧诗",37:"新时期文学三阶段",38:"古希腊悲剧",39:"亚里士多德诗学",40:"荷马史诗",
    41:"但丁神曲",42:"骑士文学",43:"莎士比亚四大悲剧",44:"堂吉诃德",45:"十日谈",
    46:"古典主义三一律",47:"启蒙运动",48:"卢梭",49:"18世纪英国小说",50:"歌德浮士德",
    51:"狂飙突进运动",52:"浪漫主义",53:"雨果",54:"批判现实主义",55:"巴尔扎克",
    56:"托尔斯泰",57:"陀思妥耶夫斯基",58:"多余人形象",59:"福楼拜",60:"自然主义",
    61:"象征主义",62:"浪漫主义vs现实主义",63:"19世纪美国文学",64:"现代主义",65:"意识流",
    66:"艾略特荒原",67:"卡夫卡",68:"后现代主义",69:"存在主义",70:"荒诞派戏剧",
    71:"魔幻现实主义",72:"黑色幽默",73:"萨特介入文学",74:"加缪vs萨特",75:"新小说派",
    76:"博尔赫斯",77:"川端康成",78:"20世纪文学总特征",79:"接受美学",80:"期待视野",
    81:"召唤结构与隐含读者",82:"视域融合",83:"俄国形式主义",84:"结构主义叙事学",85:"热奈特五范畴",
    86:"故事vs话语",87:"普罗普故事形态学",88:"格雷马斯",89:"巴赫金对话理论",90:"元虚构",
    91:"德里达延异",92:"解构主义",93:"福柯话语理论",94:"作者之死",95:"女性主义文学批评",
    96:"后殖民主义",97:"文论失语症",98:"校勘四法",99:"辨伪学",100:"全书知识网络总览",
    101:"西方马克思主义文论",102:"芥川龙之介",103:"海明威",104:"福克纳",105:"夏目漱石",
    106:"文学自律与他律"
}

# English equivalents for cards
CARD_ENGLISH = {
    1:"Abrams' Four Elements",2:"Three Branches of Literary Studies",3:"Literary Theory Textbook System",
    4:"Literaturnost",5:"Defamiliarization",6:"Nature of Literature",7:"Yijing (Artistic Conception)",
    8:"Typicality",9:"Image & Symbol",10:"Narrative POV",11:"Literary Style",12:"Literary Schools",
    13:"Literary Movements",14:"Literary Genres",15:"Literary vs Everyday Language",
    16:"Six Principles of Shijing",17:"Chu Ci & Qu Yuan",18:"Jian'an Spirit",19:"Literary Self-Awareness",
    20:"Four Periods of Tang Poetry",21:"Li Bai & Du Fu",22:"Two Schools of Song Ci",
    23:"Tang vs Song Poetry",24:"Yuan Zaju Structure",25:"Romance of the Western Chamber & Dou E",
    26:"Typology of Four Classics",27:"Dream of the Red Chamber",28:"Lu Xun's Fiction",
    29:"May Fourth Literary Revolution",30:"Literary Research Society & Creation Society",
    31:"Mao Dun & Midnight",32:"Shen Congwen & Jingpai",33:"New Sensationalism",
    34:"Avant-Garde Literature",35:"Root-Seeking Literature",36:"Misty Poetry",
    37:"Three Stages of New Period Literature",38:"Greek Tragedy",39:"Aristotle's Poetics",
    40:"Homeric Epics",41:"Dante's Divine Comedy",42:"Chivalric Literature",
    43:"Shakespeare's Four Tragedies",44:"Don Quixote",45:"The Decameron",
    46:"Classical Three Unities",47:"Enlightenment",48:"Rousseau",49:"18th-Century English Novel",
    50:"Goethe's Faust",51:"Sturm und Drang",52:"Romanticism",53:"Victor Hugo",
    54:"Critical Realism",55:"Balzac",56:"Tolstoy",57:"Dostoevsky",
    58:"The Superfluous Man",59:"Flaubert",60:"Naturalism",61:"Symbolism",
    62:"Romanticism vs Realism",63:"19th-Century American Literature",64:"Modernism",
    65:"Stream of Consciousness",66:"Eliot's Waste Land",67:"Kafka",
    68:"Postmodernism",69:"Existentialism",70:"Theatre of the Absurd",
    71:"Magical Realism",72:"Black Humor",73:"Sartre's Engaged Literature",
    74:"Camus vs Sartre",75:"Nouveau Roman",76:"Borgess",77:"Natsume Soseki",
    78:"20th-Century Literature Overview",79:"Reception Aesthetics",
    80:"Horizon of Expectations",81:"Gaps & Implied Reader",82:"Fusion of Horizons",
    83:"Russian Formalism",84:"Structuralist Narratology",85:"Genette's Five Categories",
    86:"Story vs Discourse",87:"Propp's Morphology",88:"Greimas' Semiotic Square",
    89:"Bakhtin's Dialogism",90:"Metafiction",91:"Derrida's Différance",
    92:"Deconstruction",93:"Foucault's Discourse Theory",94:"Death of the Author",
    95:"Feminist Literary Criticism",96:"Postcolonialism",97:"Theoretical Aphasia",
    98:"Collation Methods",99:"Forgery Detection",100:"Knowledge Network Overview",
    101:"Western Marxist Literary Theory",102:"Akutagawa Ryunosuke",103:"Hemingway",
    104:"Faulkner",105:"Natsume Soseki",106:"Literary Autonomy vs Heteronomy"
}

# Year → paper_id mapping
YEAR_TO_PAPER = {
    2010:"2010-eng1", 2011:"2011-eng1", 2012:"2012-eng1", 2013:"2013-eng1",
    2014:"2014-eng1", 2015:"2015-eng1", 2016:"2016-eng1", 2017:"2017-eng1",
    2018:"2018-eng1", 2019:"2019-eng1", 2020:"2020-eng1", 2021:"2021-eng1",
    2022:"2022-eng1", 2023:"2023-eng1", 2024:"2024-eng1", 2025:"2025-eng1",
}

# Vocabulary per chapter assignment (from planning data)
VOCAB_CH = {
    1:["able","address","agree","area","blank","book","case","change","consider","draw","education","end","even","example","explain","face","group","happen","head","lead","matter","mind","name","piece","present","reason","result","role","run","seem","set","short","state","suggest"],
    2:["applicant","approach","attempt","author","campus","choose","company","condition","content","customer","decision","describe","develop","effect","essay","express","fail","following","form","goal","guide","include","issue","lack","likely","mark","message","might","notice","offer","pick","practice","promise","provide","public","purpose","receive","remain","require","research","sense","share","sign","similar","slow","social","sort","store","support","surprise"],
    3:["admission","argue","attitude","behavior","benefit","claim","comment","concern","control","cost","deal","demand","despite","due","ensure","expression","further","growth","ignore","impact","individual","influence","item","limit","means","mention","object","opinion","particular","period","position","power","prevent","process","produce","protect","prove","range","rate","recognize","reduce","reflect","refuse","regard","relate","release","rely","remove","respond","review","seek","service","specific","standard","state","statement","stress","subject","suggest"],
    4:["alter","award","bill","colleague","community","connect","current","discovery","earn","employ","expensive","expert","fund","gain","image","industry","judge","labor","national","nature","perform","positive","potential","private","program","promote","pursue","region","reject","resource","reveal","revenue","scope","sector","sheet","status","structure"],
    5:["approach","being","carve","code","convey","drawing","energy","environment","extend","function","generation","grasp","healthy","launch","mental","pattern","physical","principle","profit","propose","purchase","regulation","relevant","relief","restore","retain","route","scheme","sustain"],
    6:["analysis","bound","contest","decade","digital","era","experiment","navigate","persist","predict","reform","revenue","ruling"],
    7:["bay","drama","extreme","justice","merchant","supreme"],
    8:["civilization","nail"],
    9:["elephant","silk"],
    10:["hug"],
    13:["accord","admission","context"],
    14:["content","describe","education"],
    15:["area","change","consider"],
    16:["blank","case","even"],
    17:["book","change","draw"],
    18:["end","example","explain"],
    19:["face","group","happen"],
    20:["head","lead","matter"],
    21:["mind","name","piece"],
    22:["present","reason","result"],
    23:["role","run","seem"],
    24:["set","short","state"],
    25:["suggest","address","agree"],
    26:["able","approach","argue"],
    27:["attempt","author","behavior"],
    28:["benefit","claim","comment"],
    29:["concern","control","cost"],
    30:["deal","demand","despite"],
    31:["develop","effect","ensure"],
    32:["express","further","growth"],
    33:["impact","individual","influence"],
    34:["issue","limit","means"],
    35:["mention","object","opinion"],
    36:["particular","period","position"],
    37:["power","process","produce"],
    38:["range","rate","recognize"],
    39:["reduce","reflect","refuse"],
    40:["regard","relate","release"],
    41:["rely","remove","require"],
    42:["respond","seek","service"],
    43:["specific","standard","statement"],
    44:["stress","subject","support"],
    45:["community","connect","current"],
    46:["discovery","earn","employ"],
    47:["expensive","expert","fund"],
    48:["gain","image","industry"],
    49:["judge","labor","national"],
    50:["nature","perform","positive","potential","private","program","promote","pursue"],
}

# ============================================================
# STEP 2: Database export via psql
# ============================================================

def run_psql(sql, limit=None):
    """Execute SQL via psql and return rows as list of dicts."""
    import subprocess
    if limit:
        sql = sql.rstrip(";") + f" LIMIT {limit};"
    # Use JSON output to handle multi-line fields correctly
    wrapped = f"SELECT json_agg(t) FROM ({sql}) t;"
    cmd = ["psql", "-h", "192.168.12.48", "-U", "postgres", "-d", "kaoyan_english",
           "-t", "-A", "-c", wrapped]
    env = os.environ.copy()
    env["PGPASSWORD"] = "66ccff+1"
    env["PGCLIENTENCODING"] = "UTF8"
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=30, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            print(f"  SQL Error: {result.stderr[:200]}")
            return []
        raw = result.stdout.strip()
        if not raw or raw == "":
            return []
        data = json.loads(raw)
        return data if data else []
    except Exception as e:
        print(f"  Exception: {e}")
        return []

def export_year_data(year):
    """Export all exam data for a given year."""
    paper_id = YEAR_TO_PAPER.get(year)
    if not paper_id:
        return {}
    
    data = {"cloze": [], "reading_a": [], "reading_b": [], "translation": [], "writing": []}
    
    # Cloze
    rows = run_psql(f"SELECT q_id, passage_text, content, options_json, correct_answer, official_analysis FROM questions WHERE paper_id='{paper_id}' AND section_type='use_of_english' AND q_type='cloze' ORDER BY question_number")
    for r in rows:
        data["cloze"].append({"q_id":r.get("q_id",""),"passage":r.get("passage_text",""),"content":r.get("content",""),"options":r.get("options_json",""),"answer":r.get("correct_answer",""),"analysis":r.get("official_analysis","")})
    
    # Reading A
    rows = run_psql(f"SELECT q_id, passage_text, content, options_json, correct_answer, official_analysis, group_name FROM questions WHERE paper_id='{paper_id}' AND section_type='reading_a' AND q_type='reading' ORDER BY question_number")
    for r in rows:
        data["reading_a"].append({"q_id":r.get("q_id",""),"passage":r.get("passage_text",""),"content":r.get("content",""),"options":r.get("options_json",""),"answer":r.get("correct_answer",""),"analysis":r.get("official_analysis",""),"group":r.get("group_name","")})
    
    # Reading B
    rows = run_psql(f"SELECT q_id, passage_text, content, options_json, correct_answer, official_analysis FROM questions WHERE paper_id='{paper_id}' AND section_type='reading_b' AND q_type='reading' ORDER BY question_number")
    for r in rows:
        data["reading_b"].append({"q_id":r.get("q_id",""),"passage":r.get("passage_text",""),"content":r.get("content",""),"options":r.get("options_json",""),"answer":r.get("correct_answer",""),"analysis":r.get("official_analysis","")})
    
    # Translation
    rows = run_psql(f"SELECT q_id, passage_text, content, correct_answer, official_analysis FROM questions WHERE paper_id='{paper_id}' AND section_type='translation' AND q_type='translation' ORDER BY question_number")
    for r in rows:
        data["translation"].append({"q_id":r.get("q_id",""),"passage":r.get("passage_text",""),"content":r.get("content",""),"answer":r.get("correct_answer",""),"analysis":r.get("official_analysis","")})
    
    # Writing
    rows = run_psql(f"SELECT q_id, passage_text, content, correct_answer, official_analysis FROM questions WHERE paper_id='{paper_id}' AND section_type IN ('writing_a','writing_b') AND q_type='writing' ORDER BY section_type, question_number")
    for r in rows:
        data["writing"].append({"q_id":r.get("q_id",""),"passage":r.get("passage_text",""),"content":r.get("content",""),"answer":r.get("correct_answer",""),"analysis":r.get("official_analysis","")})
    
    return data

def parse_options(opt_json):
    """Parse options_json string into [(letter, text), ...]"""
    if not opt_json:
        return []
    try:
        d = json.loads(opt_json) if isinstance(opt_json, str) else opt_json
        return [(k, d[k]) for k in sorted(d.keys())]
    except:
        return []

# ============================================================
# STEP 3: Phonetic extraction
# ============================================================

def fetch_phonetics_batch(words):
    """Fetch IPA for a list of words from Free Dictionary API."""
    phonetics = {}
    phonetics_path = os.path.join(GLOBAL, "phonetics.json")
    
    # Load existing
    if os.path.exists(phonetics_path):
        with open(phonetics_path, "r", encoding="utf-8") as f:
            phonetics = json.load(f)
    
    to_fetch = [w for w in words if w not in phonetics]
    if not to_fetch:
        print(f"  All {len(words)} words already in phonetics cache.")
        return phonetics
    
    print(f"  Fetching phonetics for {len(to_fetch)} new words...")
    success = 0
    for i, word in enumerate(to_fetch):
        try:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.request.quote(word)}"
            req = urllib.request.Request(url, headers={"User-Agent": "WordkeeperBot/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if isinstance(data, list) and data:
                    ipa = ""
                    for p in data[0].get("phonetics", []):
                        if p.get("text"):
                            ipa = p["text"]
                            break
                    if not ipa:
                        ipa = data[0].get("phonetic", "")
                    if ipa:
                        phonetics[word] = ipa
                        success += 1
        except:
            pass
        
        if (i + 1) % 50 == 0:
            print(f"    {i+1}/{len(to_fetch)} done ({success} success)")
            # Save checkpoint
            with open(phonetics_path, "w", encoding="utf-8") as f:
                json.dump(phonetics, f, ensure_ascii=False, indent=2, sort_keys=True)
        
        time.sleep(0.12)
    
    # Final save
    with open(phonetics_path, "w", encoding="utf-8") as f:
        json.dump(phonetics, f, ensure_ascii=False, indent=2, sort_keys=True)
    
    print(f"  Done: {success}/{len(to_fetch)} new phonetics fetched. Total: {len(phonetics)}")
    return phonetics

# ============================================================
# STEP 4: Markdown generators
# ============================================================

def gen_outline(ch, info):
    """Generate outline.md for a chapter."""
    cards_str = ", ".join(f"#{c:03d} ({CARD_NAMES.get(c,'')})" for c in info["cards"])
    s = f"""# Ch.{ch} — {info['title']}

> **章节编号**: Ch.{ch} / 50
> **所属部分**: Part {'I' if ch<=12 else 'II' if ch<=26 else 'III' if ch<=40 else 'IV'}
> **年份**: {'All Years (Synthesis)' if info['year']==0 else info['year']}

---

## 知识卡片

{cards_str}

---

## 词汇 (Tier 1 Glyphs)

本章收集 {len(VOCAB_CH.get(ch,[]))} 个 Tier 1 词汇。

---

## 字数目标

**最低 5,000 词**

| 层级 | 目标字数 | 占比 |
|------|---------|------|
| 叙事 | 2,800-3,200 | ~60% |
| 嵌入真题 | 800-1,000 | ~18% |
| 教学 | 400-600 | ~10% |
| 词汇 | 200-300 | ~5% |
| 知识卡片 | 200-300 | ~5% |
| 思考题 | 100-150 | ~2% |

---
"""
    return s

def gen_cloze(year, questions):
    """Generate exam_cloze.md"""
    if not questions:
        return None
    s = f"# Ch. — 完形填空 (Use of English)\n\n> **年份**: {year} | **总分**: 10分\n\n---\n\n"
    
    # Get passage (same for all cloze questions)
    passage = questions[0].get("passage", "") if questions else ""
    if passage:
        s += f"## 原文\n\n{passage}\n\n---\n\n## 答题区\n\n"
    
    for q in questions:
        qid = q["q_id"]
        num = qid.split("-q")[-1] if "-q" in qid else "?"
        content = q.get("content", "")
        options = parse_options(q.get("options", ""))
        answer = q.get("answer", "")
        analysis = q.get("analysis", "")
        
        s += f"### Q{num}. {content}\n\n"
        if options:
            s += "**选项**:\n"
            for letter, text in options:
                s += f"- [{letter}] {text}\n"
            s += "\n"
        s += f"**答案**: {answer}\n\n"
        if analysis:
            s += f"**解析**: {analysis}\n\n"
        s += "---\n\n"
    
    return s

def gen_reading_a(year, questions):
    """Generate exam_reading.md for Part A"""
    if not questions:
        return None
    s = f"# Ch. — 阅读理解 (Reading Comprehension)\n\n> **年份**: {year} | **总分**: 40分 (Part A) + 10分 (Part B)\n\n---\n\n"
    
    # Group by passage
    passages = {}
    for q in questions:
        group = q.get("group", "Unknown")
        if group not in passages:
            passages[group] = {"passage": q.get("passage", ""), "questions": []}
        passages[group]["questions"].append(q)
    
    for group_name, group_data in passages.items():
        s += f"## {group_name}\n\n"
        passage = group_data["passage"]
        if passage:
            s += f"**Passage**:\n\n{passage}\n\n---\n\n"
        
        for q in group_data["questions"]:
            qid = q["q_id"]
            content = q.get("content", "")
            options = parse_options(q.get("options", ""))
            answer = q.get("answer", "")
            analysis = q.get("analysis", "")
            
            s += f"**{content}**\n\n"
            if options:
                s += "**选项**:\n"
                for letter, text in options:
                    s += f"- [{letter}] {text}\n"
                s += "\n"
            s += f"**答案**: {answer}\n\n"
            if analysis:
                # Truncate very long analyses
                if len(analysis) > 500:
                    analysis = analysis[:500] + "..."
                s += f"**解析**: {analysis}\n\n"
            s += "---\n\n"
    
    return s

def gen_reading_b(year, questions):
    """Generate exam_reading_b.md"""
    if not questions:
        return None
    s = f"# Ch. — 新题型 (Reading Part B)\n\n> **年份**: {year} | **总分**: 10分\n\n---\n\n"
    
    passage = questions[0].get("passage", "") if questions else ""
    if passage:
        s += f"## 原文\n\n{passage}\n\n---\n\n"
    
    for q in questions:
        qid = q["q_id"]
        content = q.get("content", "")
        options = parse_options(q.get("options", ""))
        answer = q.get("answer", "")
        
        s += f"**{content}**\n\n"
        if options:
            for letter, text in options:
                s += f"- [{letter}] {text}\n"
            s += "\n"
        s += f"**答案**: {answer}\n\n---\n\n"
    
    return s

def gen_translation(year, questions):
    """Generate exam_translation.md"""
    if not questions:
        return None
    s = f"# Ch. — 翻译 (Translation)\n\n> **年份**: {year} | **总分**: 10分\n\n---\n\n"
    
    for i, q in enumerate(questions, 46):
        content = q.get("content", "")
        analysis = q.get("analysis", "")
        
        s += f"### Q{i}. {content}\n\n"
        if analysis:
            s += f"**参考译文/解析**: {analysis}\n\n"
        s += "---\n\n"
    
    return s

def gen_writing(year, questions):
    """Generate exam_writing.md"""
    if not questions:
        return None
    s = f"# Ch. — 写作 (Writing)\n\n> **年份**: {year} | **总分**: 30分\n\n---\n\n"
    
    for q in questions:
        qid = q["q_id"]
        passage = q.get("passage", "")
        content = q.get("content", "")
        
        if "writing_a" in qid:
            s += "## Part A: 应用文写作 (10分)\n\n"
        else:
            s += "## Part B: 大作文 (20分)\n\n"
        
        if passage:
            s += f"**题目**:\n\n{passage}\n\n"
        elif content:
            s += f"**题目**: {content}\n\n"
        s += "---\n\n"
    
    return s

def gen_vocabulary(ch, words, phonetics, year_data):
    """Generate vocabulary.md for a chapter."""
    s = f"# Ch.{ch} — Tier 1 词汇表 (Core Glyphs)\n\n"
    s += f"> **词汇数量**: {len(words)} 个\n\n---\n\n"
    
    # Build lookup for example sentences from exam data
    all_passages = []
    if year_data:
        for section in ["cloze", "reading_a", "reading_b", "translation"]:
            for q in year_data.get(section, []):
                p = q.get("passage", "")
                c = q.get("content", "")
                if p:
                    all_passages.append(p)
                if c:
                    all_passages.append(c)
    passage_text = " ".join(all_passages)
    
    for i, word in enumerate(words, 1):
        ipa = phonetics.get(word, "[TODO: phonetic]")
        
        # Find example sentences from the passage text
        examples = []
        if passage_text:
            # Split into sentences and find ones containing the word
            sentences = re.split(r'(?<=[.!?])\s+', passage_text)
            for sent in sentences:
                if re.search(r'\b' + re.escape(word) + r'\b', sent, re.IGNORECASE):
                    # Bold the target word
                    bolded = re.sub(r'\b(' + re.escape(word) + r')\b', r'**\1**', sent, flags=re.IGNORECASE)
                    if len(bolded) > 200:
                        bolded = bolded[:200] + "..."
                    examples.append(f'- ({year_data.get("year","")}, Reading) "{bolded}"')
                    if len(examples) >= 2:
                        break
        
        s += f"## {i}. {word}\n\n"
        s += f"- **音标**: {ipa}\n"
        s += f"- **真题例句**:\n"
        if examples:
            for ex in examples:
                s += f"  {ex}\n"
        else:
            s += f"  - (例句待补充)\n"
        s += "\n---\n\n"
    
    return s

def gen_cards(ch, card_numbers):
    """Generate cards.md"""
    s = f"# Ch.{ch} — 知识卡片 (Knowledge Cards)\n\n"
    s += f"> **卡片数量**: {len(card_numbers)} 张\n\n---\n\n"
    
    for num in card_numbers:
        cn = CARD_NAMES.get(num, f"Card {num}")
        en = CARD_ENGLISH.get(num, "")
        card_file = f"spinoff8_card{num:03d}_{cn}.md"
        card_path = f"C:\\Users\\Administrator\\Documents\\纸上宇宙\\drafts\\spinoffs\\cards\\{card_file}"
        
        s += f"## Card #{num:03d}: {cn}\n\n"
        s += f"**英文对应**: {en}\n\n"
        
        # Try to read the card file for a summary
        try:
            with open(card_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Extract core definition (first ## section)
            match = re.search(r'## 核心定义\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
            if match:
                summary = match.group(1).strip()[:300]
                s += f"**核心要义**: {summary}\n\n"
        except:
            s += f"**核心要义**: [待补充]\n\n"
        
        s += f"**完整内容路径**: `C:\\Users\\Administrator\\Documents\\纸上宇宙\\drafts\\spinoffs\\cards\\{card_file}`\n\n---\n\n"
    
    return s

def gen_notes(ch, info):
    """Generate notes.md"""
    parts = {1:"I",2:"I",3:"I",4:"I",5:"I",6:"I",7:"I",8:"I",9:"I",10:"I",11:"I",12:"I",
             13:"II",14:"II",15:"II",16:"II",17:"II",18:"II",19:"II",20:"II",21:"II",22:"II",
             23:"II",24:"II",25:"II",26:"II",27:"III",28:"III",29:"III",30:"III",31:"III",
             32:"III",33:"III",34:"III",35:"III",36:"III",37:"III",38:"III",39:"III",40:"III",
             41:"IV",42:"IV",43:"IV",44:"IV",45:"IV",46:"IV",47:"IV",48:"IV",49:"IV",50:"IV"}
    
    part = parts.get(ch, "I")
    prev_ch = ch - 1 if ch > 1 else None
    next_ch = ch + 1 if ch < 50 else None
    
    s = f"""# Ch.{ch} — 写作注意事项

> **章节**: Ch.{ch} — {info['title']}

---

## 前后章衔接

### 前章{"（开篇章）" if ch==1 else f" Ch.{prev_ch}"}
{"无" if ch==1 else f"见 Ch.{prev_ch} 的 notes.md 中\"后章铺垫\"部分"}

### 后章 Ch.{next_ch} 铺垫
{"无（终章）" if ch==50 else "见大纲 02_chapter_outline.md 中 Ch." + str(next_ch) + " 的描述"}

---

## 字数目标

**最低 5,000 词**

---

## 写作禁忌

- ❌ 不要超过 15 个破折号（——）
- ❌ 不要让角色突然变得不符合设定
- ❌ 嵌入真题时不要破坏叙事节奏——题目要自然融入场景
- ❌ 不要在教学场景中使用过于学术化的语言——用角色的口吻讲解
"""
    if info.get("study_break"):
        s += f"\n## Study Break\n\n本章包含 Study Break: **{info['sb_topic']}**\n"
    
    return s

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("The Wordkeeper's Labyrinth — Batch Data Generator")
    print("=" * 60)
    
    # Step 1: Collect all vocabulary words
    all_words = set()
    for ch, words in VOCAB_CH.items():
        all_words.update(words)
    all_words = sorted(all_words)
    print(f"\n[1/4] Total unique vocabulary: {len(all_words)}")
    
    # Step 2: Fetch phonetics
    print(f"\n[2/4] Fetching phonetics...")
    phonetics = fetch_phonetics_batch(all_words)
    
    # Step 3: Export exam data per year
    print(f"\n[3/4] Exporting exam data from PostgreSQL...")
    year_cache = {}
    for year in range(2010, 2026):
        paper_id = YEAR_TO_PAPER.get(year)
        cache_path = os.path.join(DATA, f"exam_{year}.json")
        
        if os.path.exists(cache_path):
            with open(cache_path, "r", encoding="utf-8") as f:
                year_cache[year] = json.load(f)
            print(f"  {year}: loaded from cache")
        else:
            data = export_year_data(year)
            data["year"] = year
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
            year_cache[year] = data
            cloze_n = len(data.get("cloze", []))
            read_a = len(data.get("reading_a", []))
            read_b = len(data.get("reading_b", []))
            trans_n = len(data.get("translation", []))
            write_n = len(data.get("writing", []))
            print(f"  {year}: cloze={cloze_n} readA={read_a} readB={read_b} trans={trans_n} write={write_n}")
    
    # Step 4: Generate chapter files
    print(f"\n[4/4] Generating 50 chapter data packages...")
    
    for ch in range(1, 51):
        info = CHAPTERS[ch]
        year = info["year"]
        ch_dir = os.path.join(DATA, f"ch{ch:02d}")
        os.makedirs(ch_dir, exist_ok=True)
        
        files_written = []
        
        # outline.md
        path = os.path.join(ch_dir, "outline.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(gen_outline(ch, info))
        files_written.append("outline.md")
        
        # Exam files (only for chapters with real years)
        if year and year in year_cache:
            yd = year_cache[year]
            yd["year"] = year  # for reference in templates
            
            # cloze
            content = gen_cloze(year, yd.get("cloze", []))
            if content:
                path = os.path.join(ch_dir, "exam_cloze.md")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                files_written.append("exam_cloze.md")
            
            # reading_a + reading_b combined
            content_a = gen_reading_a(year, yd.get("reading_a", []))
            if content_a:
                path = os.path.join(ch_dir, "exam_reading.md")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content_a)
                    # Append reading_b
                    content_b = gen_reading_b(year, yd.get("reading_b", []))
                    if content_b:
                        f.write("\n\n" + content_b)
                files_written.append("exam_reading.md")
            
            # translation
            content = gen_translation(year, yd.get("translation", []))
            if content:
                path = os.path.join(ch_dir, "exam_translation.md")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                files_written.append("exam_translation.md")
            
            # writing
            content = gen_writing(year, yd.get("writing", []))
            if content:
                path = os.path.join(ch_dir, "exam_writing.md")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                files_written.append("exam_writing.md")
        
        # vocabulary.md
        words = VOCAB_CH.get(ch, [])
        if words:
            yd = year_cache.get(year, {}) if year else {}
            content = gen_vocabulary(ch, words, phonetics, yd)
            path = os.path.join(ch_dir, "vocabulary.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            files_written.append("vocabulary.md")
        
        # cards.md
        content = gen_cards(ch, info["cards"])
        path = os.path.join(ch_dir, "cards.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        files_written.append("cards.md")
        
        # notes.md
        content = gen_notes(ch, info)
        path = os.path.join(ch_dir, "notes.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        files_written.append("notes.md")
        
        print(f"  Ch.{ch:02d}: {len(files_written)} files — {', '.join(files_written)}")
    
    # Summary
    print(f"\n{'=' * 60}")
    print(f"DONE: 50 chapter data packages generated.")
    
    total_files = 0
    total_size = 0
    for ch in range(1, 51):
        ch_dir = os.path.join(DATA, f"ch{ch:02d}")
        if os.path.isdir(ch_dir):
            files = os.listdir(ch_dir)
            total_files += len(files)
            for f in files:
                total_size += os.path.getsize(os.path.join(ch_dir, f))
    
    print(f"Total files: {total_files}")
    print(f"Total size: {total_size / 1024:.1f} KB")
    print(f"Phonetics cache: {len(phonetics)} words")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
