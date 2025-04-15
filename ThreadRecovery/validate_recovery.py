import os
import argparse

def validate_folder_structure(base_path):
    expected = ['tables', 'code_blocks', 'deepdives', 'prompt_logic']
    results = {}

    for folder in expected:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            results[folder] = "Missing"
        elif not any(os.scandir(folder_path)):
            results[folder] = "Empty"
        else:
            results[folder] = "OK"

    return results

def write_validation_report(results, base_path):
    report_path = os.path.join(base_path, "recovery_validation.txt")
    with open(report_path, "w") as f:
        for k, v in results.items():
            f.write(f"{k}: {v}
")
    print(f"[VALIDATION] Report saved to {report_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate recovery folder structure.")
    parser.add_argument("--input", required=True, help="Path to recovered thread folder")
    args = parser.parse_args()

    result = validate_folder_structure(args.input)
    write_validation_report(result, args.input)
