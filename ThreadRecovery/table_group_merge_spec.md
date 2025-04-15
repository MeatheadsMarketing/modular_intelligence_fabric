
# Table Group Merge Engine – Specification

**Script:** `table_group_merge.py`  
**Purpose:** Automatically group and merge Markdown tables extracted from GPT threads based on identical header structures.

---

## ✅ Core Features

| Feature             | Description |
|---------------------|-------------|
| Header-Based Grouping | Tables are grouped by normalized header row (exact match, same order, same casing) |
| Verbatim Row Merge  | Rows are merged exactly as written, with no reformatting or shifting |
| Msg ID Traceability | Each row includes the source message ID |
| Output Formats      | Exports to `.csv` and `.md` |
| Summary Index       | Outputs `merge_summary.csv` with schema and file reference |
| CLI Compatible      | Simple run with `--output` path argument |

---

## Example Output Structure

```
/master_tables/
├── master_table_1.csv
├── master_table_1.md
├── master_table_2.csv
├── master_table_2.md
├── merge_summary.csv
```

---

## Sample Merged Table (.md)

```markdown
## Master Table 1 – 3 merged

| Msg ID | Code | Name | Status | Version |
|--------|------|------|--------|---------|
| MSG_004 | A0101 | File Assistant | Ready | v1.0 |
| MSG_025 | A0102 | Export Tool | Fixable | v1.1 |
```

---

## CLI Usage

```bash
python table_group_merge.py --output ./master_tables/
```

---

## Requirements

- Input must be a list of tuples like:  
```python
[("MSG_004", "| Code | Name | Status | Version |\n|------|------|--------|---------|\n| A0101 | File Assistant | Ready | v1.0 |"), ...]
```

- Can be piped directly from `gpt_thread_recovery.py` outputs

---

## Versioning

**Spec Version:** v1.0  
**Author:** GPT Table Recovery Architect  
**Use Case:** Thread intelligence extraction, assistant registry aggregation, audit consolidation

