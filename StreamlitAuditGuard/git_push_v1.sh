
#!/bin/bash

REPO_NAME="streamlit_audit_guard"
VERSION_TAG="v1.0-final"
REMOTE_URL="git@github.com:MeatheadsMarketing/$REPO_NAME.git"

echo "==> Committing and tagging release: $VERSION_TAG"

# Ensure repo initialized
git init
git remote add origin $REMOTE_URL 2>/dev/null

git add .
git commit -m "Release: $VERSION_TAG – Full audit + recovery system"
git tag -a $VERSION_TAG -m "Version $VERSION_TAG - full system release"
git push origin main --tags

echo "==> Release pushed to GitHub with tag: $VERSION_TAG"
