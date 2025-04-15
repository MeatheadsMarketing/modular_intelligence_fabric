
# GPT Thread Recovery – Colab Lab (Phase 1)

## 1. Upload Your GPT Thread File (.md or .txt)

from google.colab import files
uploaded = files.upload()

## 2. Run the Recovery Script

import os
import subprocess

# Create output directory
output_dir = "/content/recovered_outputs"
os.makedirs(output_dir, exist_ok=True)

# Find uploaded file
uploaded_file = list(uploaded.keys())[0]

# Run recovery
!python3 gpt_thread_recovery.py --output {output_dir} --input {uploaded_file}

## 3. Preview Outputs

import os

tables = os.listdir(f"{output_dir}/tables") if os.path.exists(f"{output_dir}/tables") else []
code_blocks = os.listdir(f"{output_dir}/code_blocks") if os.path.exists(f"{output_dir}/code_blocks") else []
deepdives = os.listdir(f"{output_dir}/deepdives") if os.path.exists(f"{output_dir}/deepdives") else []
prompt_logic = os.listdir(f"{output_dir}/prompt_logic") if os.path.exists(f"{output_dir}/prompt_logic") else []

print("Tables Extracted:", tables)
print("Code Blocks Extracted:", code_blocks)
print("Deep Dives Extracted:", deepdives)
print("Prompt Logic Extracted:", prompt_logic)

## 4. Download Outputs (Optional)

from google.colab import files
import shutil

shutil.make_archive("recovery_outputs", 'zip', output_dir)
files.download("recovery_outputs.zip")
