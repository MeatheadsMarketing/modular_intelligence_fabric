
# GPT Thread Recovery Engine (Terminal Edition)

This system allows you to run full GPT thread recovery, merging, classification, and logging locally on your machine — fully automated once a `.md` file is dropped in.

---

## 📁 Folder Structure

```
gpt_thread_recovery_engine/
├── run_auto_recovery.sh           # Main runner script
├── gpt_thread_recovery.py         # Extracts tables, code, deep dives, prompts
├── table_group_merge.py           # Merges similar tables into master sets
├── file_role_clarifier.py         # Classifies files into system-level roles
├── watched_threads/               # DROP your `.md` threads here
├── recovered_threads/             # Output folder for recovered assets
├── logs/
│   ├── thread_log.csv             # Records each run and result
│   └── error_log.txt              # Captures failures or warnings
├── thread_registry.csv            # Master registry of all recovered threads
```

---

## ⚙️ Setup Instructions

1. **Install Python if needed:**
```bash
brew install python3
```

2. **Navigate to the folder:**
```bash
cd ~/gpt_thread_recovery_engine
```

3. **Make the runner script executable:**
```bash
chmod +x run_auto_recovery.sh
```

4. **Drop your `.md` thread files into:**
```
watched_threads/
```

5. **Run the script:**
```bash
./run_auto_recovery.sh
```

---

## 🧠 Output

After execution, each recovered thread is stored in:
```
recovered_threads/YYYY-MM-DD_threadname/
```

Includes:
- `/tables/`
- `/deepdives/`
- `/code_blocks/`
- `/prompt_logic/`
- `recovery_index.csv`
- `file_role_audit.csv`
- `merged_tables/`
- Full logs and summaries

---

## ✅ What's Next

- [ ] Add Notion or GitHub sync (Phase 3)
- [ ] Build a Streamlit Viewer Dashboard (Optional UI)
- [ ] Set up a cron job for continuous monitoring

---

**Author:** GPT System Recovery Architect  
**Version:** v1.0-final
