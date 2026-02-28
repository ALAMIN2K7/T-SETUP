#!/bin/bash

# ===============================================
# 🌟 T-SETUP Installer Script
# ===============================================

# Colors for messages
GREEN="\033[0;32m"
RED="\033[0;31m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
NC="\033[0m"  # No Color

echo -e "${BLUE}【•】Starting Setup in 3 seconds...${NC}"
sleep 3
echo

# 1️⃣ Font Copy
FONT_SRC="$HOME/T-SETUP/files/font.ttf"
FONT_DEST="$HOME/.termux/font.ttf"
mkdir -p "$HOME/.termux"

if cp "$FONT_SRC" "$FONT_DEST"; then
    echo -e "${GREEN}✔ Font copied successfully!${NC}"
else
    echo -e "${RED}✘ Failed to copy font. Check if $FONT_SRC exists.${NC}"
    exit 1
fi

# 2️⃣ Reload Termux Settings
if command -v termux-reload-settings >/dev/null 2>&1; then
    termux-reload-settings
    echo -e "${GREEN}✔ Termux settings reloaded.${NC}"
else
    echo -e "${YELLOW}⚠ termux-reload-settings command not found. You may need to reload settings manually.${NC}"
fi

# 3️⃣ Run Python setup.py
PYTHON_SCRIPT="$HOME/T-SETUP/files/setup.py"

if [ -f "$PYTHON_SCRIPT" ]; then
    echo -e "${BLUE}【•】Running setup.py...${NC}"
    python3 "$PYTHON_SCRIPT"
    exit 1
fi