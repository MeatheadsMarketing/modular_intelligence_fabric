
import os
import re
import json
import argparse
from datetime import datetime

# Simulate loading from thread (in production, this will be parsed or provided as structured JSON)
THREAD_ID = "streamlit_audit_system_v1"

def sanitize_filename(text):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', text.strip())[:50]

def extract_and_save(data, out_dir, category, extension="md"):
    os.makedirs(out_dir, exist_ok=True)
    index = []
    for msg_id, content, meta in data:
        file_id = f"{msg_id}_{sanitize_filename(meta.get('title', category))}"
        filename = f"{file_id}.{extension}"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\n")
            f.write(f"Msg ID: {msg_id}\n")
            f.write(f"Type: {meta['type']}\n")
            f.write(f"Thread: {THREAD_ID}\n")
            f.write(f"Tags: {json.dumps(meta.get('tags', []))}\n")
            f.write(f"Value Score: {meta['value_score']}\n")
            f.write(f"Date Extracted: {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"---\n\n")
            f.write(content.strip())
        index.append({
            "Msg ID": msg_id,
            "Type": meta["type"],
            "Value Score": meta["value_score"],
            "Tags": ", ".join(meta.get("tags", [])),
            "Filename": filename
        })
    return index

def run_recovery(messages, output_dir, min_words=0, min_score=1):
    tables, deepdives, codeblocks, prompts = [], [], [], []

    for msg_id, content in messages:
        word_count = len(content.split())

        if re.search(r"\|.*\|", content) and "\n|" in content:
            tables.append((msg_id, content, {
                "type": "Table",
                "title": "table",
                "value_score": 4,
                "tags": ["Structured", "Audit"]
            }))

        if word_count > max(min_words, 150):
            deepdives.append((msg_id, content, {
                "type": "Deep Dive",
                "title": "deep_dive",
                "value_score": 5,
                "tags": ["Strategy", "Insight"]
            }))

        if "```" in content:
            codeblocks.append((msg_id, content, {
                "type": "Code Block",
                "title": "code_block",
                "value_score": 3,
                "tags": ["Code", "Utility"]
            }))

        if "#CH-RESUME" in content or "#TASK:" in content:
            prompts.append((msg_id, content, {
                "type": "Prompt Logic",
                "title": "prompt_logic",
                "value_score": 4,
                "tags": ["Prompt", "Shortcut"]
            }))

    full_index = []
    full_index += extract_and_save(tables, os.path.join(output_dir, "tables"))
    full_index += extract_and_save(deepdives, os.path.join(output_dir, "deepdives"))
    full_index += extract_and_save(codeblocks, os.path.join(output_dir, "code_blocks"), extension="txt")
    full_index += extract_and_save(prompts, os.path.join(output_dir, "prompt_logic"))

    # Save index
    index_path = os.path.join(output_dir, "recovery_index.csv")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("Msg ID,Type,Value Score,Tags,Filename\n")
        for row in full_index:
            f.write(f"{row['Msg ID']},{row['Type']},{row['Value Score']},{row['Tags']},{row['Filename']}\n")

    print(f"Recovery complete. {len(full_index)} items saved.")
    print(f"Index: {index_path}")

# Example structure to test script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GPT Thread Recovery")
    parser.add_argument("--output", type=str, required=True, help="Path to save extracted content")
    args = parser.parse_args()

    # TEMP EXAMPLE INPUT (replace with thread loader)
    sample_messages = [
        ("MSG_004", "| Table | Description |\n|---|---|\n| A | B |"),
        ("MSG_026", "Longform discussion about tagging assistants...\n\nAnd why they must be recovered..."),
        ("MSG_057", "```\naudit/\n├── run_audit.py\n├── deploy_tab.py\n```"),
        ("MSG_072", "Use `#CH-RESUME:1` to return to audit system chapter")
    ]

    run_recovery(sample_messages, args.output)
