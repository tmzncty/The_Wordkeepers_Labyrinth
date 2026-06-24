#!/usr/bin/env python3
"""Generate Ch.1 data files from JSONL sources."""
import json
import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
CH01 = os.path.join(DATA, "ch01")

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def parse_options(options_field):
    """Parse options from JSON string or dict."""
    if not options_field:
        return None
    if isinstance(options_field, str):
        return json.loads(options_field)
    return options_field

def format_options(options):
    """Format options as markdown list."""
    if not options:
        return "**选项**: *(无选项 — 简答/翻译题)*"
    lines = ["**选项**:"]
    for letter in sorted(options.keys()):
        lines.append(f"- [{letter}] {options[letter]}")
    return "\n".join(lines)

def format_vocab_sentence(sentence, target_word):
    """Format a single vocabulary example sentence."""
    year = sentence.get("year", "?")
    source = sentence.get("source", "?")
    en = sentence.get("en", "")
    
    # Extract clean source label: remove leading year, keep section type
    # "2011 English I · Section II Part C" -> "Section II Part C"
    # "2010 English I · Section I Use of English" -> "Use of English"
    source_label = source
    if source:
        # Remove year prefix
        source_label = re.sub(r'^\d{4}\s*English\s*I\s*[·•]\s*', '', source)
        if not source_label:
            source_label = source  # fallback
    
    # Bold the target word in the sentence (case-insensitive, word boundary)
    pattern = re.compile(r'\b(' + re.escape(target_word) + r')\b', re.IGNORECASE)
    en_bolded = pattern.sub(r'**\1**', en)
    
    # Truncate very long sentences
    if len(en_bolded) > 200:
        en_bolded = en_bolded[:197] + "..."
    
    return f"- ({year}, {source_label}) \"{en_bolded}\""


# ============================================================
# 1. Generate exam_cloze.md
# ============================================================
def generate_exam_cloze():
    all_q = load_jsonl(os.path.join(DATA, "kaoyan_2010.jsonl"))
    cloze = [q for q in all_q if q["section_type"] == "use_of_english"]
    cloze.sort(key=lambda q: q["question_number"])
    
    # Also load from cloze_2010.jsonl for supplementary data
    cloze_local = load_jsonl(os.path.join(DATA, "cloze_2010.jsonl"))
    cloze_local_map = {q["qnum"]: q for q in cloze_local}
    
    lines = []
    lines.append("# Ch.1 — 完形填空 (Use of English)")
    lines.append("")
    lines.append("> **年份**: 2010 | **题号**: Q1-Q20 | **总分**: 10分（每题0.5分）")
    lines.append("> **主题**: Hawthorne experiments — 霍桑实验与\"霍桑效应\"")
    lines.append("> **叙事用途**: Weave (编织院) — 绯墨必须将撕裂的段落重新编织完整")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Part A: 完形填空原文")
    lines.append("")
    
    # Build passage from cloze_local data (reconstruct)
    passage_paras = [
        'In 1924 America\'s National Research Council sent two engineers to supervise a series of experiments at a telephone-parts factory called the Hawthorne Plant near Chicago. It hoped they would learn how shop-floor lighting _1_ workers\' productivity. Instead, the studies ended _2_ giving their name to the "Hawthorne effect," the extremely influential idea that the very _3_ of being experimented upon changed subjects\' behavior.',
        '',
        'The idea arose because of the _4_ behavior of the women in the plant. According to _5_ of the experiments, their hourly output rose when lighting was increased, but also when it was dimmed. It did not _6_ what was done in the experiment; _7_ something was changed, productivity rose. A(n) _8_ that they were being experimented upon seemed to be _9_ to alter workers\' behavior _10_ itself.',
        '',
        'After several decades, the same data were _11_ to econometric analysis. The Hawthorne experiments had another surprise in store. _12_ the descriptions on record, no systematic _13_ was found that levels of productivity were related to changes in lighting.',
        '',
        'It turns out that the peculiar way of conducting the experiments may have led to _14_ interpretations of what happened. _15_, lighting was always changed on a Sunday. When work started again on Monday, output _16_ rose compared with the previous Saturday and _17_ to rise for the next couple of days. _18_, a comparison with data for weeks when there was no experimentation showed that output always went up on Mondays. Workers _19_ to be diligent for the first few days of the week in any case, before _20_ a plateau and then slackening off. This suggests that the alleged "Hawthorne effect" is hard to pin down.'
    ]
    for p in passage_paras:
        lines.append(p)
    lines.append("")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 答题区")
    lines.append("")
    
    for q in cloze:
        qnum = q["question_number"]
        content = q["content"]
        options = parse_options(q.get("options"))
        answer = q.get("answer", "?")
        
        # Merge analysis from local file if available
        local = cloze_local_map.get(qnum, {})
        analysis = q.get("analysis", "") or local.get("analysis", "")
        
        lines.append(f"### Q{qnum}. {content}")
        lines.append("")
        lines.append(format_options(options))
        lines.append("")
        lines.append(f"**答案**: {answer}")
        lines.append("")
        if analysis:
            lines.append(f"**解析**: {analysis}")
        lines.append("")
        lines.append("---")
        lines.append("")
    
    path = os.path.join(CH01, "exam_cloze.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] exam_cloze.md: {len(cloze)} questions with options")


# ============================================================
# 2. Generate exam_reading.md
# ============================================================
def generate_exam_reading():
    all_q = load_jsonl(os.path.join(DATA, "kaoyan_2010.jsonl"))
    
    # Reading A
    reading_a = [q for q in all_q if q["section_type"] == "reading_a"]
    reading_a.sort(key=lambda q: q["question_number"])
    
    # Reading B
    reading_b = [q for q in all_q if q["section_type"] == "reading_b"]
    reading_b.sort(key=lambda q: q["question_number"])
    
    # Group reading_a by Text
    texts = {}
    for q in reading_a:
        g = q.get("group_name", "Unknown")
        if g not in texts:
            texts[g] = []
        texts[g].append(q)
    
    lines = []
    lines.append("# Ch.1 — 阅读理解 (Reading Comprehension)")
    lines.append("")
    lines.append("> **年份**: 2010 | **题号**: Q21-Q40 (Part A) + Q41-Q45 (Part B) | **总分**: 40分")
    lines.append("> **叙事用途**: Mirror (映照院) — 文本映照在镜面上，绯墨必须选择正确的\"倒影\"来解答")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Part A: 传统阅读理解 (每题2分)")
    lines.append("")
    
    for text_name in sorted(texts.keys()):
        qs = texts[text_name]
        lines.append(f"### {text_name}")
        lines.append("")
        lines.append("**Passage**:")
        lines.append("")
        # Use passage from first question of group
        passage = qs[0].get("passage_text", "")
        for para in passage.split("\n\n"):
            lines.append(para.strip())
            lines.append("")
        lines.append("---")
        lines.append("")
        
        for q in qs:
            qnum = q["question_number"]
            content = q["content"]
            options = parse_options(q.get("options"))
            answer = q.get("answer", "?")
            analysis = q.get("analysis", "")
            
            lines.append(f"**Q{qnum}.** {content}")
            lines.append("")
            if options:
                lines.append(format_options(options))
                lines.append("")
            lines.append(f"**答案**: {answer}")
            lines.append("")
            if analysis:
                lines.append(f"**解析**: {analysis}")
            lines.append("")
            lines.append("---")
            lines.append("")
    
    # Reading B
    if reading_b:
        lines.append("## Part B: 新题型 (每题2分)")
        lines.append("")
        
        # Get passage from first reading_b question
        rb_passage = reading_b[0].get("passage_text", "")
        if rb_passage:
            lines.append("**Passage**:")
            lines.append("")
            for para in rb_passage.split("\n\n"):
                lines.append(para.strip())
                lines.append("")
            lines.append("---")
            lines.append("")
        
        for q in reading_b:
            qnum = q["question_number"]
            content = q.get("content", f"Q{qnum}")
            answer = q.get("answer", "?")
            analysis = q.get("analysis", "")
            
            lines.append(f"**Q{qnum}.** {content}")
            lines.append("")
            lines.append(f"**答案**: {answer}")
            lines.append("")
            if analysis:
                lines.append(f"**解析**: {analysis}")
            lines.append("")
            lines.append("---")
            lines.append("")
    
    path = os.path.join(CH01, "exam_reading.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] exam_reading.md: {len(reading_a)} Part A + {len(reading_b)} Part B questions")


# ============================================================
# 3. Generate vocabulary.md
# ============================================================
def generate_vocabulary():
    vocab = load_jsonl(os.path.join(DATA, "vocab_ch01.jsonl"))
    
    lines = []
    lines.append("# Ch.1 — Tier 1 词汇表 (Core Glyphs)")
    lines.append("")
    lines.append("> **章节**: Ch.1 — The Cat-Ear Girl and the Cruelest Spirit")
    lines.append(f"> **词汇数量**: {len(vocab)} 个 Tier 1 词汇（数据库确认 ≥3 次真题出现）")
    lines.append("> **用途**: 绯墨在迷宫中收集的第一批\"字形\"(Glyphs)")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    for i, entry in enumerate(vocab, 1):
        word = entry["word"]
        meaning = entry["meaning"]
        pos = entry["pos"]
        freq = entry["frequency"]
        sentences = entry.get("example_sentences") or []
        
        lines.append(f"## {i}. {word}")
        lines.append("")
        lines.append(f"- **音标**: [TODO: 待补充]")
        lines.append(f"- **词性**: {pos}")
        
        # Format meaning (handle multiline)
        meaning_lines = meaning.strip().split("\n")
        if len(meaning_lines) == 1:
            lines.append(f"- **释义**: {meaning}")
        else:
            lines.append(f"- **释义**: {meaning_lines[0]}")
            for ml in meaning_lines[1:]:
                lines.append(f"  {ml}")
        
        lines.append(f"- **真题出现次数**: {freq} 次")
        lines.append(f"- **真题例句**:")
        
        for sent in sentences:
            lines.append(format_vocab_sentence(sent, word))
        
        lines.append("")
        lines.append("---")
        lines.append("")
    
    path = os.path.join(CH01, "vocabulary.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] vocabulary.md: {len(vocab)} words with formatted sentences")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("Generating Ch.1 data files...\n")
    generate_exam_cloze()
    generate_exam_reading()
    generate_vocabulary()
    print("\n[OK] All Ch.1 files regenerated.")
