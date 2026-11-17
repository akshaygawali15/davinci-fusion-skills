# DaVinci Resolve Fusion AI Skills (for Claude Code & Antigravity)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DaVinci Resolve](https://img.shields.io/badge/DaVinci%20Resolve-Studio%2021%2B-blue)](https://www.blackmagicdesign.com/products/davinciresolve)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![AI Assistants](https://img.shields.io/badge/AI-Claude%20Code%20%7C%20Antigravity-orange)](https://github.com/akshaygawali15/davinci-fusion-skills)

Production-grade skills, runbooks, and automation scripts that empower AI coding assistants (**Claude Code** and **Google Antigravity**) to accurately construct, script, and troubleshoot **DaVinci Resolve Fusion** node graphs, `.setting` macros, and motion graphics templates.

---

## The Problem: Why Video Editing AIs Struggle with Fusion

Recent AI video editing assistants excel at cut detection, audio transcription, and EDL/timeline assembly. However, when asked to build or modify effects on DaVinci Resolve's **Fusion Page**, they almost invariably fail:

1. **Inverted Merge Logic**: AIs frequently swap `Background` (Orange) and `Foreground` (Green) inputs, rendering graphics *underneath* footage instead of on top.
2. **The Black Screen Bug**: In timeline clips, if a node graph is disconnected from `MediaOut1.Input`, DaVinci Resolve renders a solid black screen on the Edit page without an error message.
3. **Hardcoded Keyframe Breakage**: AIs place static keyframe numbers (e.g. frame 0 to 30) that break whenever a creator trims or extends clip duration on the timeline.
4. **Normalized Coordinate Distortion**: Fusion uses normalized coordinates `[0.0, 1.0]` where aspect ratios affect shapes (e.g. circles distort into ovals at 16:9 unless height is properly scaled).
5. **API & Serialization Hallucinations**: Calling non-existent methods or failing to use Fusion's ASCII Lua table (`.setting`) clipboard format.

---

## The Solution: What This Skill Provides

This skill suite transforms your AI assistant into a senior Fusion compositing TD with deep domain knowledge:

- **Strict Flow Contracts**: Explicit input/output rules for all primary tools (`Merge`, `Transform`, `TextPlus`, `DeltaKeyer`, `Background`).
- **Pipeline Doctor / Health Checks**: Scripts to automatically detect disconnected nodes and route them to `MediaOut1`.
- **Procedural Animation Mastery**: Patterns for `AnimCurves` (`LUTLookup`) and `KeyframeStretcher` (`KfS`), ensuring motion graphics auto-scale across any clip duration.
- **Official API Stubs**: Decompressed Python `.pyi` stubs (`fusion_api.pyi` and `ui_api.pyi`) from DaVinci Resolve Studio 21.1.2.
- **Edit Page Template Generator**: CLI tools and syntax specifications for generating installable `.setting` macros and `.drfx` bundles.

---

## Repository Structure

```
davinci-fusion-skills/
├── README.md                          # Main project documentation
├── INSTALL.md                         # Detailed multi-platform installation guide
├── LICENSE                            # MIT License
├── install.ps1                        # One-command installer for Windows
├── install.sh                         # One-command installer for macOS & Linux
│
└── fusion-scripting/                  # The core AI Skill package
    ├── SKILL.md                       # Master AI runbook and operational instructions
    │
    ├── references/                    # Deep reference documents
    │   ├── nodes_reference.md         # Exhaustive dictionary of node IDs, inputs, and outputs
    │   ├── setting_syntax.md          # Anatomy of .setting files, MacroOperators & .drfx bundles
    │   ├── expressions_and_modifiers.md # SimpleExpressions, Lua functions, AnimCurves guide
    │   └── stubs/                     # Official DaVinci Resolve Studio 21.1.2 type stubs
    │       ├── fusion_api.pyi         # FusionScript API stubs
    │       └── ui_api.pyi             # DaVinci Resolve UI API stubs
    │
    └── scripts/                       # Production helper utilities & CLI generators
        ├── fusion_utils.py            # Python automation module (auto-connect, undo blocks)
        └── generate_template.py       # CLI template generator for Edit page titles & generators
```

---

## Quick Start: Installation

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

*For manual installation steps, see [INSTALL.md](INSTALL.md).*

---

## How to Prompt Your AI Assistant

Once installed in `~/.claude/skills/fusion-scripting` or `~/.gemini/config/skills/fusion-scripting`, simply instruct your AI:

### Example 1: Creating a Motion Lower Third
> *"Create a modern motion lower third title template in DaVinci Resolve with an auto-stretching AnimCurves animation and exposed controls for text and colors."*

### Example 2: Fixing a Broken Fusion Clip
> *"Check the Fusion page of my current timeline clip. If any nodes are disconnected from MediaOut1, auto-route the final merge into MediaOut1 so the clip doesn't render black."*

### Example 3: Chroma Keying Green Screen
> *"Generate a complete green-screen keying node graph in Python using DeltaKeyer, CleanPlate, and MatteControl, with spill suppression enabled."*

---

## Included CLI Tools

### Generate DaVinci Resolve Edit Page Templates
You can generate production-ready `.setting` macro templates directly from the command line:

```bash
# Generate a lower-third template locally:
python fusion-scripting/scripts/generate_template.py --name "CreatorLowerThird" --title "Akshay Gawali" --subtitle "Host"

# Install directly into DaVinci Resolve's Edit Page Titles library:
python fusion-scripting/scripts/generate_template.py --name "ChannelIntro" --install-to-resolve
```

---

## Contributing

Contributions, bug reports, and additional node recipe templates are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
