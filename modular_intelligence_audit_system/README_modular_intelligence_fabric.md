
# Modular Intelligence Fabric

A complete system of assistant lifecycle threads — from extraction and recovery to validation and deployment.  
Each folder is a modular, audit-ready assistant workspace connected to a system-wide flow.

---

## 🧠 Thread Overview

| Folder                   | Role |
|--------------------------|------|
| `ThreadFullSpecExtractor` | Verbatim extraction from GPT threads, shortcut parsing, and table recovery |
| `ThreadRecovery`          | Recovery logic for tables, prompts, code blocks with thread clarity metadata |
| `ThreadRecoveryEngine`    | Matrix-based routing and role classifier for recovery logic |
| `TerminalColabBuilder`    | CLI + terminal scaffolding system for new assistants |
| `AssistantLaunchPack`     | Packaging, routing, and deployment layer for agent-based assistants |
| `StreamlitAuditGuard`     | Final validator for assistant readiness: launch score, structure check, fix tagging |

---

## ✅ Structure

Each assistant folder may contain:
- `/audit/` – validator scripts, dashboards
- `/data/` – registry files, trackers, tables
- `/docs/` – changelogs, handoff files
- `/tabs/` – UI logic for dashboards
- `main_app.py` – Streamlit launcher (optional)
- `README.md` – assistant-specific overview

---

## 🧰 Shared Toolkit (Cross-Thread)

- `gpt_thread_recovery.py` – Full recovery extractor
- `table_group_merge.py` – Header-matching table merger
- `file_role_clarifier.py` – Classify file by recovery or launch stage
- `streamlit_log_viewer.py` – Visual registry/launch history explorer

---

## 🚀 Deployment

To run any assistant or tool:
```bash
cd assistant_folder
streamlit run main_app.py
```

Install requirements first:
```bash
pip install -r requirements.txt
```

---

## 🔁 Cross-Thread Flow Diagram

```text
ThreadFullSpecExtractor
      ↓
ThreadRecovery → ThreadRecoveryEngine
      ↓
TerminalColabBuilder
      ↓
AssistantLaunchPack
      ↓
StreamlitAuditGuard ← (reinject failed builds)
```

---

System designed for modular evolution and clarity.  
Use `structure_audit_summary.csv` and `folder_fix_manifest.csv` to maintain consistency.

