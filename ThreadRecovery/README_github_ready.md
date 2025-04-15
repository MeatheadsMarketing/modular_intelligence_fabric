
# 🧠 ThreadRecoveryOrganizer

This repo is the second link in a multi-thread GPT intelligence pipeline. It transforms raw GPT thread exports into structured, labeled, and indexable components, preparing them for assistant generation, dashboard visualization, or Streamlit-based launching.

---

## 🔁 Workflow Role

| Position | Thread Name               |
|----------|---------------------------|
| 1️⃣       | ThreadFullSpectrumExtraction |
| **2️⃣**   | **ThreadRecoveryOrganizer**     |
| 3️⃣       | TerminalStreamlitBuilder   |
| 4️⃣       | AssistantLaunchPack        |
| 5️⃣       | StreamlitAuditSystem       |

---

## 🚀 What It Does

- Extracts tables, deep dives, prompt chains, and code from GPT `.md` logs
- Merges matching tables into unified master tables
- Classifies files with system-level roles (blueprints, snippets, logic, insights)
- Generates summaries, logs, and metadata registries
- Prepares all output for visual exploration in Streamlit or routing to builders

---

## 📁 Key Folders

| Folder        | Purpose |
|---------------|---------|
| `/scripts/`   | All recovery, classification, merge, and summary scripts |
| `/logs/`      | Execution and error tracking logs |
| `/specs/`     | System specs, boot guides, templates |
| `/templates/` | Markdown templates (e.g. summary format) |
| `/outputs/`   | Merged tables and CSVs |
| `/streamlit/` | Log viewing interface (`streamlit_log_viewer.py`) |
| `/zip_files/` | Archived input and output bundles |

---

## 🧪 Test Instructions

```bash
cd scripts/
chmod +x run_auto_recovery_v2.sh
./run_auto_recovery_v2.sh
```

Place your `.md` GPT thread logs in `/watched_threads/` before running.

---

## 📈 Optional Streamlit UI

Launch the log viewer:
```bash
streamlit run streamlit/streamlit_log_viewer.py
```

---

## ✅ System Outputs

Each thread run will create:
- `/tables/`, `/deepdives/`, `/code_blocks/`, `/prompt_logic/`
- `recovery_summary.md`
- `recovery_validation.txt`
- `file_role_audit.csv`
- Updated `thread_log.csv` and `thread_registry.csv`

---

## 🧭 Sync Card

See: `ThreadRecoveryOrganizer_SYNC_CARD.md`

---

## 📌 Status

> Version: `v1.1-final`  
> Author: Recovery Systems Architect  
> Last Updated: 2025-04-14

---

**Ready to be consumed by: [`TerminalStreamlitBuilder`](#)**  
