import os
import csv
import argparse

# Simple keyword-based role classifier
ROLE_MAP = {
    "table": "Assistant Blueprint",
    "code": "Code Snippet",
    "deepdive": "Strategic Insight",
    "prompt": "Prompt Logic"
}

def classify_files(input_dir, output_csv):
    classifications = []
    for role_folder, system_role in ROLE_MAP.items():
        folder_path = os.path.join(input_dir, role_folder + "s")
        if not os.path.isdir(folder_path):
            continue
        for fname in os.listdir(folder_path):
            if fname.startswith("."):
                continue
            fpath = os.path.join(folder_path, fname)
            classifications.append({
                "filename": fname,
                "path": fpath,
                "assigned_role": system_role,
                "source_folder": role_folder + "s"
            })

    # Write results to CSV
    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["filename", "path", "assigned_role", "source_folder"])
        writer.writeheader()
        for row in classifications:
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify recovered files into system roles")
    parser.add_argument("--input", required=True, help="Path to recovered thread folder")
    parser.add_argument("--output", required=True, help="Path to save classification CSV")
    args = parser.parse_args()

    classify_files(args.input, args.output)
