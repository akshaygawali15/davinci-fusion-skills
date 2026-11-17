# Installation & Usage Guide

This guide explains how to install and activate the **DaVinci Resolve Fusion AI Skill Suite (`fusion-scripting`)** for **Claude Code** and **Google Antigravity**.

---

## Prerequisites

1. **AI Assistant**: Either [Claude Code](https://claude.ai/code) or [Google Antigravity](https://antigravity.google).
2. **DaVinci Resolve**: DaVinci Resolve Studio or Free (v17, v18, v19, or v21+).
3. **Python**: Python 3.10+ (if running the helper automation scripts or CLI generators).

---

## 1. Quick Installation (Automatic)

Clone the repository and run the install script for your platform:

### Windows (PowerShell)
```powershell
git clone https://github.com/akshaygawali15/davinci-fusion-skills.git
cd davinci-fusion-skills
.\install.ps1
```

### macOS / Linux (Terminal)
```bash
git clone https://github.com/akshaygawali15/davinci-fusion-skills.git
cd davinci-fusion-skills
chmod +x install.sh
./install.sh
```

The script automatically detects whether Claude Code (`~/.claude`) or Google Antigravity (`~/.gemini`) is installed and copies the skill files into their global skill directories.

---

## 2. Manual Installation

If you prefer to install manually, copy the `fusion-scripting/` folder to the target directory for your AI tool:

### For Google Antigravity:
- **Global**: Copy `fusion-scripting` to `~/.gemini/config/skills/fusion-scripting/`
- **Project Specific**: Copy `fusion-scripting` to `.agents/skills/fusion-scripting/` in your project root.

### For Claude Code:
- **Global**: Copy `fusion-scripting` to `~/.claude/skills/fusion-scripting/`
- **Project Specific**: Copy `fusion-scripting` to `.claude/skills/fusion-scripting/` in your repository.

---

## 3. How to Use the Skill with AI

Once installed, your AI assistant automatically gains expert-level knowledge of the DaVinci Resolve Fusion page.

Simply ask Claude or Antigravity natural language questions or give instructions, such as:

- *"Create a motion lower third title template with auto-stretching AnimCurves for DaVinci Resolve."*
- *"Inspect my current timeline clip's Fusion composition and fix any disconnected nodes routing to MediaOut1."*
- *"Build a clean chroma key node graph using DeltaKeyer, CleanPlate, and MatteControl."*
- *"Generate a .setting file for a modern 4K split-screen generator with rounded corners."*

The AI will follow the exact node flow rules, correct input/output names, and valid `.setting` Lua table formatting documented in the skill.

---

## 4. Using the CLI Template Generator

You can also run the bundled Python CLI script directly to generate `.setting` templates:

```bash
# Generate a lower-third template in the current directory:
python fusion-scripting/scripts/generate_template.py --name "MyTitle" --title "Akshay Gawali" --subtitle "Director"

# Install directly into DaVinci Resolve's Edit Page Titles library (Windows):
python fusion-scripting/scripts/generate_template.py --name "CreatorLowerThird" --install-to-resolve
```

---

## 5. Installing Templates into DaVinci Resolve Manually

If you generate or download `.setting` templates, place them in the following paths to see them in the DaVinci Resolve **Edit Page Effects Library**:

### Windows:
`%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\`
- Subfolders: `Titles\`, `Generators\`, `Transitions\`, `Effects\`

### macOS:
`~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/`

### Linux:
`~/.local/share/DaVinciResolve/Fusion/Templates/Edit/`
