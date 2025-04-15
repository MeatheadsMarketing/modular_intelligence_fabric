
import os
import re
import argparse
import hashlib
import pandas as pd
from collections import defaultdict

def extract_tables_from_text(text, msg_id):
    """Extract markdown tables from a block of text and return them as raw text blocks with Msg ID."""
    pattern = r"(\|.+?\|(?:\n\|.+?\|)+)"
    matches = re.findall(pattern, text, re.DOTALL)
    tables = []
    for match in matches:
        rows = [line.strip() for line in match.strip().splitlines() if line.strip()]
        if len(rows) >= 2 and all('|' in row for row in rows):
            tables.append((msg_id, rows))
    return tables

def header_fingerprint(header_row):
    """Hash the header row to group tables with the same schema."""
    normalized = '|'.join([h.strip().lower() for h in header_row.split('|') if h.strip()])
    return hashlib.md5(normalized.encode('utf-8')).hexdigest()

def parse_table(rows):
    """Parse markdown table rows into headers and body rows."""
    headers = [h.strip() for h in rows[0].strip().split('|') if h.strip()]
    data = []
    for row in rows[2:]:  # Skip header and delimiter rows
        cols = [c.strip() for c in row.strip().split('|')]
        if len(cols) == len(headers):
            data.append(cols)
    return headers, data

def run_table_merge(message_blocks, output_dir):
    grouped_tables = defaultdict(list)

    for msg_id, text in message_blocks:
        for extracted_msg_id, table_rows in extract_tables_from_text(text, msg_id):
            headers, data = parse_table(table_rows)
            fingerprint = header_fingerprint(table_rows[0])
            grouped_tables[fingerprint].append({
                "msg_id": extracted_msg_id,
                "headers": headers,
                "rows": data
            })

    os.makedirs(output_dir, exist_ok=True)
    summary = []

    for i, (fp, table_group) in enumerate(grouped_tables.items(), start=1):
        if not table_group:
            continue

        headers = table_group[0]["headers"]
        all_rows = []
        for table in table_group:
            for row in table["rows"]:
                row_with_id = [table["msg_id"]] + row
                all_rows.append(row_with_id)

        out_headers = ["Msg ID"] + headers
        df = pd.DataFrame(all_rows, columns=out_headers)

        # Save CSV
        csv_name = f"master_table_{i}.csv"
        csv_path = os.path.join(output_dir, csv_name)
        df.to_csv(csv_path, index=False)

        # Optional MD output
        md_name = f"master_table_{i}.md"
        md_path = os.path.join(output_dir, md_name)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"## Master Table {i} – {len(table_group)} merged

")
            f.write("| " + " | ".join(out_headers) + " |
")
            f.write("|" + "|".join(["---"] * len(out_headers)) + "|
")
            for row in all_rows:
                f.write("| " + " | ".join(row) + " |
")

        summary.append({
            "Table Group": i,
            "Headers": headers,
            "Merged Count": len(table_group),
            "Output CSV": csv_name
        })

    # Summary file
    summary_path = os.path.join(output_dir, "merge_summary.csv")
    pd.DataFrame(summary).to_csv(summary_path, index=False)
    print(f"Generated {len(summary)} master tables.")
    print(f"Summary saved to: {summary_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Group and merge markdown tables by header structure")
    parser.add_argument("--output", type=str, required=True, help="Path to output merged tables")
    args = parser.parse_args()

    # TEMP DEMO input
    sample_messages = [
        ("MSG_004", "| Code | Name | Status | Version |\n|------|------|--------|---------|\n| A0101 | File Assistant | Ready | v1.0 |"),
        ("MSG_025", "| Code | Name | Status | Version |\n|------|------|--------|---------|\n| A0102 | Export Tool | Fixable | v1.1 |"),
        ("MSG_043", "| Module | Status | Fix Needed |\n|--------|--------|------------|\n| deploy_tab.py | FAIL | Yes |"),
        ("MSG_082", "| Module | Status | Fix Needed |\n|--------|--------|------------|\n| audit_dashboard.py | PASS | No |")
    ]

    run_table_merge(sample_messages, args.output)
