#!/bin/bash

# Colors
G='\033[0;32m'
R='\033[0;31m'
B='\033[0;34m'
Y='\033[1;33m'
C='\033[0;36m'
NC='\033[0m'

clear

# Header
echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${C}                 T-SETUP INSTALLER${NC}"
echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo

# Install Font
echo -ne "${B}[1/2]${NC} Installing Fonts... "
mkdir -p "$HOME/.termux"
if [ -f "$HOME/T-SETUP/files/font.ttf" ]; then
    cp "$HOME/T-SETUP/files/font.ttf" "$HOME/.termux/font.ttf"
    echo -e "${G}DONE${NC}"
else
    echo -e "${R}FAILED${NC}"
    echo -e "${Y}  Font file not found!${NC}"
fi

# Reload Settings
echo -ne "${B}[2/2]${NC} Reloading Settings... "
termux-reload-settings 2>/dev/null
echo -e "${G}DONE${NC}"

echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo

# Run Python Interface
if [ -f "$HOME/T-SETUP/files/tsetup.py" ]; then
    python3 "$HOME/T-SETUP/files/tsetup.py"
else
    echo -e "${R}Error: tsetup.py not found!${NC}"
    exit 1
fi