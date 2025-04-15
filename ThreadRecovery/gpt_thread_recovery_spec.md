
# GPT Thread Recovery Engine – System Specification

**Version:** v1.0  
**Component:** `gpt_thread_recovery.py`  
**Purpose:** Extract critical intelligence from GPT threads (tables, deep dives, code, prompt logic) and store it in structured, reusable formats.

---

## ✅ Features

| Feature                  | Description |
|--------------------------|-------------|
| **Full Verbatim Capture** | All messages extracted exactly as written (no truncation) |
| **Structured Output Folders** | Saves into `/tables/`, `/deepdives/`, `/code_blocks/`, `/prompt_logic/` |
| **Metadata Injection**   | Msg ID, Type, Tags, Value Score, Date, Thread ID |
| **Recovery Index**       | Auto-generates `recovery_index.csv` with all extracted files |
| **CLI Compatible**       | Run from terminal using `--output` to define save folder |
| **Extensible**           | Can plug into future Notion sync, changelog engines, assistant registries |

---

## Folder Output Example

```
/extracted/
├── tables/
│   └── MSG_004_registry_table.md
├── deepdives/
│   └── MSG_026_tagging_strategy.md
├── code_blocks/
│   └── MSG_057_audit_structure.txt
├── prompt_logic/
│   └── MSG_072_resume_shortcut.md
├── recovery_index.csv
```

---

## How It Works

1. Load messages from thread history
2. Categorize each message:
   - Table: Markdown tables
   - Deep Dive: >150 words
   - Code Block: uses ``` format
   - Prompt Logic: uses `#CH-RESUME`, `#TASK:`, or similar
3. Save each message to a file with full metadata
4. Index the results in a CSV for future analysis

---

## CLI Usage

```bash
python gpt_thread_recovery.py --output ./extracted/
```

**Parameters:**
- `--output`: Path to output folder for recovery results

---

## Metadata Injected Per File

```yaml
---
Msg ID: MSG_026
Type: Deep Dive
Thread: streamlit_audit_system_v1
Tags: ["Strategy", "Tagging"]
Value Score: 5
Date Extracted: 2025-04-14
---
```

---

## Notes

- Can be extended to:
  - Filter by `--min-value-score` or `--min-words`
  - Integrate with `thread_chapter_log.md`
  - Sync into Notion or external dashboards

---

**Author:** GPT System Recovery Designer  
**Date:** 2025-04-14
