
# Terminal-First Streamlit Builder – System Blueprint (v1.0)

## System Objective
To create a *CLI-first workflow* that scaffolds, validates, and prepares Streamlit assistant apps with perfect structure, zero placeholders, and rapid dev cycles — feeding directly into the audit and deployment stack.

---

## 1. Execution Trigger (CLI Core)
| Layer | Description |
|-------|-------------|
| `new_assistant.sh` | Shell command that scaffolds an assistant using templates |
| `cli_generate.py` | Python backend for folder/file creation logic |
| CLI Alias | Example: `alias newassist="bash new_assistant.sh"` |

**Clarity Hack:** Keep all logic inside `cli_generate.py` and use the shell as the wrapper for flexibility. Don't bloat the shell script — it's just a trigger.

---

## 2. Scaffold Generator
| Folder/File       | Purpose                                  |
|-------------------|------------------------------------------|
| `main_app.py`     | Core Streamlit routing + multipage logic |
| `run_ui.py`       | Local dev launcher                       |
| `/pages/`         | Page-specific assistant logic            |
| `/tabs/`          | Optional modular tab components          |
| `/data/`          | Input/Output logs, CSVs, etc.            |
| `/utils/`         | Helper functions and logic separation    |
| `README.md`       | Build doc reference                      |
| `.gitignore`      | Version control hygiene                  |
| `requirements.txt`| Dependency list                          |

**Clarity Hack:** Use templates to ensure every assistant has zero missing starter files. Future-proof by adding `/docs/` if needed.

---

## 3. Template Selector
| Type | Description |
|------|-------------|
| `base_blank` | Empty structured app |
| `seo_audit` | SEO assistant template |
| `data_parser` | CSV/data cleaning UI |
| `chat_ui` | Streamlit chat-style layout |
| `multi_tab_form` | Multipage input/output form logic |

**Clarity Hack:** Templates must be versioned and stored in `/templates/` for clean diff tracking.

---

## 4. Dev Watchdog Layer (Optional)
| Feature | Behavior |
|---------|----------|
| Placeholder scanner | Flags `#TODO`, `pass`, dummy text |
| File validator | Ensures critical files exist (e.g., `run_ui.py`) |
| Structure linter | Validates presence of `/pages/`, `/tabs/` |
| Status print | Terminal readout: “✅ Audit-Ready” or “❌ Issues Found” |

**Clarity Hack:** Use this *before* running Streamlit — this prevents 80% of common UI issues and broken files.

---

## 5. Fast Iteration Launchers
| Command | Function |
|---------|----------|
| `streamlit run run_ui.py` | Launch preview in browser |
| `watchdog.py` | Auto-check structure on save (optional) |
| `log_output.txt` | Captures run metadata (optional) |

**Clarity Hack:** Make preview and logs accessible via command alias or shortcut keys for no-friction debugging.

---

## 6. Audit Pre-Pipe Output
| Output | Description |
|--------|-------------|
| `audit_ready=True` | Tag inserted in metadata or manifest |
| `v1.0_assistant/` | Fully structured folder, ready for AuditGuard |
| `.zip` optional | Compressed output for handoff |

**Clarity Hack:** Use tagging (`audit_ready=True`) to auto-skip redundant scans downstream. Use `manifest.json` if scaling.

---

## 7. Dev Acceleration Tools (Optional Add-ons)
| Tool | Role |
|------|------|
| `auto_venv.sh` | Bootstraps virtual environment |
| `.env.generator.py` | Generates starter .env files |
| `git_init_boost.sh` | Git init + README + first commit |

**Clarity Hack:** Bundle this in `/tools/` so your assistants are immediately git-ready + deploy-ready.

---

## 8. Strategic Modes (Toggle Flags)
| Mode | Use Case |
|------|----------|
| `--mode=build` | Normal build flow |
| `--mode=test` | Run watchdog + placeholder scan only |
| `--mode=dry` | Show plan without generating files |

**Clarity Hack:** Treat `--mode=test` as a preflight for audits. Allow chaining these in bash or Python CLI.

---

## 9. Output Map
| Source        | Passes To            |
|---------------|----------------------|
| `/your_app/`  | → StreamlitAuditGuard |
| `.zip export` | → AssistantLaunchPack |

**Clarity Hack:** Every output folder should be visually confirmed and pushed through placeholder-checkers *before* tagging as final.
