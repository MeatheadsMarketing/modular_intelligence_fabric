
import os
import shutil

ROOT = os.path.dirname(__file__)

FOLDER_MAP = {
    "audit": [
        "run_audit.py",
        "run_batch_audit.py",
        "audit_dashboard.py",
        "audit_dashboard_all.py",
        "recovery_tab.py",
        "fix_summary_tab.py",
        "deploy_tab.py"
    ],
    "audit/checks": [
        "file_structure_check.py",
        "placeholder_scan.py",
        "ui_integrity_check.py",
        "streamlit_run_check.py",
        "manifest_validator.py",
        "performance_check.py"
    ],
    "audit/utils": [
        "logger.py",
        "fixer.py"
    ],
    "data": [
        "../data/assistant_registry.csv",
        "../data/fix_tracker.csv",
        "../v1_master_registry.csv"
    ],
    "deploy_ready": [
        "../deploy_ready/fixed_assistants_bundle.zip",
        "../deploy_ready/CHANGELOG.md"
    ],
    "docs": [
        "../reflection_v1.0.md"
    ]
}

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

def move_file(file_path, dest_folder):
    dest_path = os.path.join(ROOT, dest_folder, os.path.basename(file_path))
    if os.path.exists(file_path):
        shutil.move(file_path, dest_path)
        print(f"Moved: {file_path} -> {dest_path}")

def organize_project():
    for folder, files in FOLDER_MAP.items():
        full_folder = os.path.join(ROOT, folder)
        ensure_folder(full_folder)
        for file_rel in files:
            file_path = os.path.join(ROOT, file_rel) if not file_rel.startswith("..") else os.path.abspath(os.path.join(ROOT, file_rel))
            move_file(file_path, full_folder)

if __name__ == "__main__":
    organize_project()
