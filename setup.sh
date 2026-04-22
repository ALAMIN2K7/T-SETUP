#!/bin/bash

# ===============================================
# 🌟 T-SETUP ULTIMATE INSTALLER
# ===============================================

G='\033[0;32m' # Green
R='\033[0;31m' # Red
B='\033[0;34m' # Blue
Y='\033[1;33m' # Yellow
C='\033[0;36m' # Cyan
NC='\033[0m'   # No Color

clear

# টাইপিং ইফেক্ট
type_text() {
    local text="$1"
    local delay="$2"
    for (( i=0; i<${#text}; i++ )); do
        echo -ne "${text:$i:1}"
        sleep $delay
    done
    echo
}

# স্পিনার লোডার
spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ -d /proc/$pid ]; do
        local temp=${spinstr#?}
        printf " [${Y}%c${NC}]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# হেডার
echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
type_text "It would be better if you zoomed out and the box fit nicely inside the screen." 0.02
echo -e "${C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo

# ধাপ ১: ফন্ট কপি (সঠিকভাবে চেক করা)
echo -ne "${B}【•】${NC} Installing System Fonts... "
(
    FONT_SRC="$HOME/T-SETUP/files/font.ttf"
    FONT_DEST="$HOME/.termux/font.ttf"
    mkdir -p "$HOME/.termux"
    
    # ফাইল থাকলে কপি করবে
    if [ -f "$FONT_SRC" ]; then
        cp "$FONT_SRC" "$FONT_DEST" > /dev/null 2>&1
        sleep 2 # এনিমেশন দেখার জন্য
    else
        sleep 1
        exit 1 # ফাইল না থাকলে এরর কোড দিবে
    fi
) & spinner

# আগের প্রসেসটির এক্সিট স্ট্যাটাস চেক
if [ $? -eq 0 ] && [ -f "$HOME/.termux/font.ttf" ]; then
    echo -e "${G}DONE!${NC}"
else
    echo -e "${R}FAILED!${NC}"
    echo -e "${Y}  [!] Error: Font file not found in T-SETUP/files/${NC}"
    exit 1
fi

# ধাপ ২: সেটিংস রিলোড
echo -ne "${B}【•】${NC} Optimizing Termux Settings... "
(
    if command -v termux-reload-settings >/dev/null 2>&1; then
        termux-reload-settings
    fi
    sleep 1.5
) & spinner
echo -e "${G}SUCCESS!${NC}"

echo -e "\n${Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
type_text " ✔ Setup Complete! Launching Python Interface..." 0.03
echo -e "${Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
sleep 1

# মেইন পাইথন ফাইল রান
PYTHON_SCRIPT="$HOME/T-SETUP/files/setup.py"
if [ -f "$PYTHON_SCRIPT" ]; then
    python3 "$PYTHON_SCRIPT"
else
    echo -e "${R}✘ Error: setup.py not found!${NC}"
    exit 1
fi
