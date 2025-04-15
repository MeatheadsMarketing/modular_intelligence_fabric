import os
import csv
import argparse
from datetime import datetime

# Define simple heuristics for tagging
def infer_tags(folder):
    tags = set()
    if os.path.exists(os.path.join(folder, "tables")):
        tags.add("assistant_blueprint")
    if os.path.exists(os.path.join(folder, "prompt_logic")):
        tags.add("prompt_chaining")
    if os.path.exists(os.path.join(folder, "deepdives")):
        tags.add("strategic_insight")
    if os.path.exists(os.path.join(folder, "code_blocks")):
        tags.add("code_tool")
    return list(tags)

# Write enriched row to registry
def append_to_registry(registry_path, folder_name, base_path):
    folder_path = os.path.join(base_path, folder_name)
    tags = infer_tags(folder_path)
    summary = f"Recovered {folder_name} with {len(tags)} key asset types."

    files = ", ".join(os.listdir(folder_path)) if os.path.exists(folder_path) else "None"
    date = datetime.now().strftime("%Y-%m-%d")

    with open(registry_path, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["thread_name", "date", "files", "roles_detected", "summary"])
        writer.writerow({
            "thread_name": folder_name,
            "date": date,
            "files": files,
            "roles_detected": ";".join(tags),
            "summary": summary
        })

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enrich thread_registry.csv with tags and summary.")
    parser.add_argument("--folder", required=True, help="Recovered thread folder name")
    parser.add_argument("--base", required=True, help="Path to base recovered_threads directory")
    parser.add_argument("--registry", required=True, help="Path to thread_registry.csv")
    args = parser.parse_args()

    append_to_registry(args.registry, args.folder, args.base)
