#!/usr/bin/env bash
# Automated Installer for DaVinci Resolve Fusion AI Skill (macOS / Linux)
# Supports Claude Code and Google Antigravity

set -e

echo "=========================================================="
echo " Installing DaVinci Resolve Fusion Skill for AI Assistants"
echo "=========================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SOURCE="$SCRIPT_DIR/fusion-scripting"

if [ ! -d "$SKILL_SOURCE" ]; then
    echo "Error: Source folder 'fusion-scripting' not found in $SCRIPT_DIR"
    exit 1
fi

# 1. Install for Google Antigravity
GEMINI_DIR="$HOME/.gemini"
if [ -d "$GEMINI_DIR" ]; then
    TARGET="$GEMINI_DIR/config/skills/fusion-scripting"
    mkdir -p "$TARGET"
    cp -R "$SKILL_SOURCE/"* "$TARGET/"
    echo "[OK] Installed for Google Antigravity: $TARGET"
else
    echo "[SKIP] Antigravity directory (~/.gemini) not detected."
fi

# 2. Install for Claude Code
CLAUDE_DIR="$HOME/.claude"
if [ -d "$CLAUDE_DIR" ]; then
    TARGET="$CLAUDE_DIR/skills/fusion-scripting"
    mkdir -p "$TARGET"
    cp -R "$SKILL_SOURCE/"* "$TARGET/"
    echo "[OK] Installed for Claude Code: $TARGET"
else
    echo "[SKIP] Claude directory (~/.claude) not detected."
fi

echo ""
echo "Installation Complete! Claude Code and Antigravity can now use 'fusion-scripting'."
