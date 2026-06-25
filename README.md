# The Wordkeeper's Labyrinth

**A light novel that hides 16 years of Chinese postgraduate entrance exams inside a magical academy story.**

---

## What Is This?

An English light novel (~280,000 words across 50 chapters) that organically integrates:

- **832 exam questions** from China's national postgraduate English exam (2010–2025)
- **106 literary theory knowledge cards** (from Abrams' Four Elements to Postcolonialism)
- **6,131 vocabulary words** with IPA phonetics and real exam sentences
- **SM-2 spaced repetition** as a narrative mechanic
- **RPG progression** (HP, EXP, Level) as in-world game mechanics

The story follows **Feimo** (绯墨), a catgirl student at a magical academy built inside the **Labyrinth** — the material substrate of human literary consciousness. She collects Glyphs (vocabulary words), reads Inscriptions (knowledge cards), and battles Fragmenters (entities that destroy language) alongside her tsundere Spirit AI partner **Mia**.

## The Hook

Every exam challenge, vocabulary word, and knowledge card appears as a **real story event** — not a textbook insert. A cloze test about the Hawthorne effect becomes a collapsing corridor Feimo must repair word by word. A reading comprehension about arts criticism becomes a debate between rival Houses. Lu Xun's "Iron House" parable makes the Labyrinth's walls vibrate in Chinese.

## Structure

| Part | Chapters | Years | Theme |
|------|----------|-------|-------|
| I: Enrollment | Ch.1–12 | 2010–2012 | Entry, adaptation, first battles |
| II: The Houses | Ch.13–26 | 2013–2017 | Four houses, rivals, tournament |
| III: Deep Labyrinth | Ch.27–40 | 2018–2022 | Deep exploration, Fragmenter invasion |
| IV: Keeper's Gate | Ch.41–50 | 2023–2025 | Finale, confession, seven doors |

**9 Study Break chapters** (Ch.2, 6, 10, 16, 20, 25, 31, 36, 44) are dedicated teaching episodes where Mia uses her signature venomous pedagogy.

## Characters

| Character | Role | House |
|-----------|------|-------|
| **Feimo** (绯墨) | Catgirl protagonist, underestimated but fierce | Bridge |
| **Mia** (ミア) | Tsundere Spirit AI, secretly a digitized human consciousness | — |
| **Aya** (绫) | Cold perfectionist, rival turned admirer | Mirror |
| **Noir** (诺亚) | Catgirl senior, underground fighter | Forge |
| **Silence** (缄默教授) | Oldest teacher, never speaks (communicates through writing) | Bridge |
| **Yue** (月) | Translation genius who can't dream | Bridge |
| **Cain** (凯因) | Student council president, morally gray antagonist | Weave |
| **The Archivist** | Deep Archive keeper, knows everything | — |

## Romance Lines

- **Feimo × Mia** (primary, 萧): Digital × physical. Five phases from conflict to confession across 50 chapters.
- **Ling → Feimo** (secondary): Rivalry → admiration → love → maturity → blessing.

## The Four Houses

| House | Specialty | Exam Focus | Battle Style |
|-------|-----------|------------|--------------|
| **Weave** (编织院) | Grammar, structure | Cloze | Systematic, hierarchical |
| **Mirror** (映照院) | Reading, analysis | Reading Comprehension | Precise, competitive |
| **Bridge** (渡桥院) | Translation, cross-cultural | Translation | Transformative, connective |
| **Forge** (锻造院) | Writing, creation | Writing | Aggressive, inventive |

## Technical Details

### Word Count

| Metric | Value |
|--------|-------|
| Total words | ~280,000 |
| Chapters | 50 |
| Average per chapter | ~5,600 |
| Knowledge cards | 106 |
| Exam questions integrated | 832 |
| Vocabulary words | 6,131 (Tier 1: ~444, Tier 2: ~926, Tier 3: ~4,961) |

### Revision History

The manuscript went through **9 rounds of review and revision**:

1. **Batches 1–5** (Ch.1–27): 5 rounds of dual-reviewer audit + revision
2. **Batches 6–8** (Ch.28–42): 3 rounds covering passage recycling, character consistency, vocabulary enrichment
3. **Batch 9** (Ch.43–50): Final pass — sacrifice scene, Cards 095/096, Mia entity mechanism

Each round used a **dual-reviewer system**:
- **Fu Xuan** (符玄): Theory consistency, worldbuilding alignment, filler detection
- **Zhuang Fangyi** (庄方宜): Structural completeness, pacing, cross-chapter continuity

A dedicated **vocabulary audit** was performed across all 50 chapters to identify and reduce repetitive patterns (sentence-start monotony, overused adverbs, formulaic descriptions).

### Project Structure

```
The_Wordkeeper's_Labyrinth/
├── planning/
│   ├── 00_master_brief.md        ← Original 17-chapter concept
│   ├── 00_master_brief_v2.md     ← Final 50-chapter brief
│   ├── 01_worldbuilding.md       ← World, characters, magic system (Fu Xuan)
│   ├── 02_chapter_outline.md     ← 50-chapter outline with card mapping (Zhuang Fangyi)
│   └── 03_data_tables.md         ← Data tables (Bai Mianxiao)
├── data/
│   ├── ch01–ch50/                ← Per-chapter data packages
│   │   ├── outline.md            ← Chapter skeleton
│   │   ├── notes.md              ← Scene budget, must-hits, forbidden list
│   │   ├── exam_cloze.md         ← Cloze test (original + answers + analysis)
│   │   ├── exam_reading.md       ← Reading comprehension
│   │   ├── exam_translation.md   ← Translation exercises
│   │   ├── exam_writing.md       ← Writing prompts
│   │   ├── vocabulary.md         ← Tier 1 words with IPA + exam sentences
│   │   └── cards.md              ← Knowledge cards with source paths
│   └── exam_2010.json – exam_2025.json  ← Raw exam data
├── drafts/
│   ├── ch01_the_cat_ear_girl.md – ch50_this_book_belongs_to_whoever_opens_it.md
│   ├── review_batch1–9_fuxuan.md
│   ├── review_batch1–9_zhuangfangyi.md
│   ├── review_vocabulary_filler_report.md
│   └── review_vocabulary_ch43_50.md
├── batch_generate.py             ← Data package generator
├── generate_ch01.py              ← Ch.1-specific generator
├── extract_phonetics.py          ← IPA phonetics extractor
├── regenerate_notes.py           ← Notes file regenerator
└── README.md
```

## Exam Integration Design

Each exam year (2010–2025) is mapped to specific chapters. The integration follows four patterns:

| Exam Section | Narrative Mechanic | House |
|-------------|-------------------|-------|
| **Cloze** (20 blanks) | Collapsing corridor repair — each blank is a missing structural element | Weave |
| **Reading** (4 passages) | Deep reading analysis — surface/structural/resonant layers | Mirror |
| **Translation** (5 sentences) | Cross-linguistic bridge repair — meaning transfer between languages | Bridge |
| **Writing** (2 prompts) | Creative inscription — writing new text into blank walls | Forge |

## Worldbuilding

The Labyrinth is the **material substrate of human literary consciousness** — a dimension woven from every word ever written, read, spoken, or thought. When a child learns to read, a corridor brightens. When a book is forgotten, a room dims. When a language dies, an entire wing collapses into dust.

The modern world's shallow scrolling and algorithmic curation is **eroding the Labyrinth from within**. Wordkeepers are those who maintain, repair, and defend it.

Seven Labyrinths exist across languages: English (active), Chinese (active), Japanese (closed), Arabic (half-asleep), German (active, strict), French (active, ornate), Russian (active, deepest).

## Key Foreshadowing

- **Ch.1**: Floor tapping in Chinese beneath the Academy
- **Ch.8**: First hint of the Chinese Labyrinth
- **Ch.27**: The door that shouldn't exist — Eastern Gate to the Chinese Labyrinth
- **Ch.42**: Silence's secret identity as the Labyrinth personified
- **Ch.49**: Seven doors open simultaneously
- **Ch.50**: Mia's human name revealed, confession, new beginning

## The Glyph Battle System

- **Nouns** create
- **Adjectives** modify
- **Transitive verbs** attack
- **Intransitive verbs** transform self
- **Adverbs** alter other Glyph effects (rarest)
- **Conjunctions** link

Power-ups come from **deeper understanding** of word meanings, not quantity.

## Style & Tone

- **Genre**: Light novel (学院/恋爱/热血/日常), with 百合 (yuri) romance
- **Voice**: Hot-blooded battles + sweet romance + comedy + mystery + emotional depth
- **Humor**: Mia's tsundere dialogue with emoji/symbols, Feimo's catgirl antics
- **Language**: English with Chinese, Japanese, French, and Latin scattered throughout
- **Constraint**: No more than 15 em-dashes per chapter

## Writing Pipeline

The manuscript was produced using a multi-agent writing pipeline:

1. **Writer** (赫默): Drafts each chapter from data packages
2. **Theory Reviewer** (符玄): Checks worldbuilding consistency, character integrity, filler detection
3. **Structure Reviewer** (庄方宜): Checks pacing, must-hit coverage, cross-chapter continuity
4. **Vocabulary Auditor** (薄绿): Statistical analysis of word frequency, sentence patterns, TTR
5. **Revision Editor** (赫默): Applies fixes from review reports

Each chapter went through: draft → dual review → revision → commit+push.

## License

This is a creative work. All rights reserved by the author.

---

*"What is remembered, lives."*

— Inscription on the Labyrinth Academy entrance arch
