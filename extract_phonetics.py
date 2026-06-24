#!/usr/bin/env python3
"""Fetch IPA phonetics from Free Dictionary API for all Tier 1 words."""
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
GLOBAL = os.path.join(DATA, "_global")
PHONETICS_PATH = os.path.join(GLOBAL, "phonetics.json")

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

def load_existing():
    if os.path.exists(PHONETICS_PATH):
        with open(PHONETICS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_phonetics(phonetics):
    os.makedirs(GLOBAL, exist_ok=True)
    with open(PHONETICS_PATH, "w", encoding="utf-8") as f:
        json.dump(phonetics, f, ensure_ascii=False, indent=2, sort_keys=True)

def fetch_ipa(word):
    """Fetch IPA phonetic from Free Dictionary API."""
    url = API_URL.format(word=word)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "WordkeeperBot/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if isinstance(data, list) and len(data) > 0:
                phonetics = data[0].get("phonetics", [])
                for p in phonetics:
                    text = p.get("text", "")
                    if text:
                        return text
                # Fallback: check top-level phonetic
                top_phonetic = data[0].get("phonetic", "")
                if top_phonetic:
                    return top_phonetic
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, KeyError) as e:
        pass
    return None

def main():
    # Load word list from vocabulary JSONL
    vocab_path = os.path.join(DATA, "vocab_ch01.jsonl")
    if not os.path.exists(vocab_path):
        print("ERROR: vocab_ch01.jsonl not found")
        sys.exit(1)
    
    with open(vocab_path, "r", encoding="utf-8") as f:
        words = [json.loads(line)["word"] for line in f if line.strip()]
    
    # Also load from data tables if available
    # For now, use the vocab file
    
    phonetics = load_existing()
    total = len(words)
    fetched = 0
    skipped = 0
    failed = 0
    
    print(f"Fetching phonetics for {total} words...")
    print(f"Already cached: {len(phonetics)}")
    
    for i, word in enumerate(words, 1):
        if word in phonetics:
            skipped += 1
            continue
        
        ipa = fetch_ipa(word)
        if ipa:
            phonetics[word] = ipa
            fetched += 1
            if fetched % 20 == 0:
                print(f"  [{i}/{total}] Fetched {fetched} so far... (last: {word} -> {ipa})")
        else:
            failed += 1
            phonetics[word] = "[TODO: not in Free Dictionary API]"
            if failed % 10 == 0:
                print(f"  [{i}/{total}] Failed {failed} so far... (last: {word})")
        
        # Save every 50 words
        if (fetched + failed) % 50 == 0:
            save_phonetics(phonetics)
        
        time.sleep(0.12)  # 120ms between requests
    
    save_phonetics(phonetics)
    
    print(f"\nDone!")
    print(f"  Total words: {total}")
    print(f"  Fetched: {fetched}")
    print(f"  Skipped (cached): {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Saved to: {PHONETICS_PATH}")

if __name__ == "__main__":
    main()
