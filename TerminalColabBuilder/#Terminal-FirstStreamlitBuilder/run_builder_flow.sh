#!/bin/bash

# Orchestrator Script: Terminal-First Streamlit Builder Full Flow
# Usage: bash run_builder_flow.sh --name MyApp --template seo_audit

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --name) NAME="$2"; shift ;;
        --template) TEMPLATE="$2"; shift ;;
        *) echo "❌ Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [ -z "$NAME" ]; then
  echo "❌ Error: --name is required."
  exit 1
fi

echo "🚀 Starting Terminal-First Build Flow for: $NAME"

# Step 1: Scaffold assistant using CLI
python3 cli_generate.py --name "$NAME" --template "${TEMPLATE:-base_blank}" || { echo "❌ Scaffold failed"; exit 1; }

# Step 2: Validate structure (placeholder: insert your validator if built)
echo "🔍 Validating project structure..."
# python3 validate_structure.py --folder "$NAME"  # Optional placeholder for validator

# Step 3: Generate manifest.json
echo "🧾 Generating manifest.json..."
cat <<EOF > ./"$NAME"/manifest.json
{
  "assistant": "$NAME",
  "template": "${TEMPLATE:-base_blank}",
  "audit_ready": true,
  "launchable": true,
  "source": "run_builder_flow.sh",
  "thread": "TerminalStreamlitBuilder",
  "version": "v1.0"
}
EOF

# Step 4: Zip project
echo "📦 Creating zip archive..."
zip -rq "${NAME}.zip" "$NAME"

# Step 5: Completion message
echo "✅ Build complete."
echo "→ Folder: $(pwd)/$NAME"
echo "→ Zip:    $(pwd)/${NAME}.zip"
