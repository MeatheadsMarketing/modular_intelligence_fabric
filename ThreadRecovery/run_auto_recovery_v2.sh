#!/bin/bash

WATCH_FOLDER="./watched_threads"
OUTPUT_BASE="./recovered_threads"
LOG_FOLDER="./logs"
RECOVERY_SCRIPT="gpt_thread_recovery.py"
MERGE_SCRIPT="table_group_merge.py"
ROLE_SCRIPT="file_role_clarifier.py"
SUMMARY_SCRIPT="write_summary.py"
VALIDATE_SCRIPT="validate_recovery.py"

mkdir -p "$WATCH_FOLDER" "$OUTPUT_BASE" "$LOG_FOLDER"

echo "[INFO] Monitoring $WATCH_FOLDER for .md files..."

for file in "$WATCH_FOLDER"/*.md; do
    [ -e "$file" ] || continue  # Skip if no .md files found

    THREAD_NAME=$(basename "$file" .md)
    TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
    OUTPUT_FOLDER="$OUTPUT_BASE/${TIMESTAMP}_${THREAD_NAME}"
    mkdir -p "$OUTPUT_FOLDER"

    echo "[INFO] Processing: $file"
    python3 "$RECOVERY_SCRIPT" --input "$file" --output "$OUTPUT_FOLDER" >> "$LOG_FOLDER/thread_log.csv" 2>> "$LOG_FOLDER/error_log.txt"

    echo "[INFO] Merging tables..."
    python3 "$MERGE_SCRIPT" --input "$OUTPUT_FOLDER/tables/" --output "$OUTPUT_FOLDER/merged_tables/" >> "$LOG_FOLDER/thread_log.csv" 2>> "$LOG_FOLDER/error_log.txt"

    echo "[INFO] Classifying files..."
    python3 "$ROLE_SCRIPT" --input "$OUTPUT_FOLDER/" --output "$OUTPUT_FOLDER/file_role_audit.csv" >> "$LOG_FOLDER/thread_log.csv" 2>> "$LOG_FOLDER/error_log.txt"

    echo "[INFO] Writing summary..."
    python3 "$SUMMARY_SCRIPT" --input "$OUTPUT_FOLDER" --name "$THREAD_NAME"

    echo "[INFO] Validating output..."
    python3 "$VALIDATE_SCRIPT" --input "$OUTPUT_FOLDER"

    echo "[DONE] Finished: $file"
done
