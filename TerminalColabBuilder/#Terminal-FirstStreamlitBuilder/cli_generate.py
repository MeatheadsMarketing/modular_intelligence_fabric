#!/usr/bin/env python3
"""
CLI Builder – Terminal-First Streamlit Assistant Scaffolder
"""

import os
import argparse
import shutil

def scaffold_project(project_name, template_type):
    base_dir = os.path.join(os.getcwd(), project_name)
    if os.path.exists(base_dir):
        print("❌ Project already exists.")
        return

    os.makedirs(base_dir)
    os.makedirs(os.path.join(base_dir, 'pages'))
    os.makedirs(os.path.join(base_dir, 'tabs'))
    os.makedirs(os.path.join(base_dir, 'data'))
    os.makedirs(os.path.join(base_dir, 'utils'))

    open(os.path.join(base_dir, 'main_app.py'), 'w').write("# main_app entry")
    open(os.path.join(base_dir, 'run_ui.py'), 'w').write("# local dev launcher")
    open(os.path.join(base_dir, 'requirements.txt'), 'w').write("streamlit
")
    open(os.path.join(base_dir, 'README.md'), 'w').write(f"# {project_name} Assistant")
    open(os.path.join(base_dir, '.gitignore'), 'w').write(".DS_Store
__pycache__
.venv
")

    print(f"✅ Scaffolding complete for: {project_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Streamlit Assistant Scaffolder")
    parser.add_argument("--name", type=str, required=True, help="Project name")
    parser.add_argument("--template", type=str, default="base_blank", help="Template type")
    args = parser.parse_args()

    scaffold_project(args.name, args.template)
