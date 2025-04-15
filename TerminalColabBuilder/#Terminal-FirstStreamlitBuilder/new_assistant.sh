#!/bin/bash

# Shell wrapper for Terminal-First Streamlit Builder
# Usage: bash new_assistant.sh --name MyApp --template seo_audit

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --name) NAME="$2"; shift ;;
        --template) TEMPLATE="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [ -z "$NAME" ]; then
  echo "❌ Error: --name is required."
  exit 1
fi

python3 cli_generate.py --name "$NAME" --template "${TEMPLATE:-base_blank}"
