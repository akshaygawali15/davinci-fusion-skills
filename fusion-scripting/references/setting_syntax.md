# Fusion `.setting` File Syntax & Template Packaging Guide

Every node graph, macro, and motion-graphic template in DaVinci Resolve Fusion is stored in a clean, human-readable Lua table format known as the `.setting` file.

---

## 1. Top-Level Structure of a `.setting` File

A `.setting` file contains a single root dictionary:

```lua
{
    Tools = ordered() {
        -- Node definitions or MacroOperator definitions go here
    },
    ActiveTool = "FinalToolName"
}
```

### Types of Containers
1. **Raw Node Group**: A list of standard nodes connected together directly.
2. **`GroupOperator`**: A visual group that can be expanded or collapsed in the Node Editor.
3. **`MacroOperator`**: A compiled reusable node whose internals are encapsulated and only specifically selected controls are exposed to the Inspector. **This is the standard format for Edit Page Templates (Titles, Generators, Transitions, Effects)**.

---

## 2. Anatomy of a `MacroOperator`

A macro packages multiple internal nodes into a single custom tool:

```lua
{
    Tools = ordered() {
        MyCustomTitle = MacroOperator {
            Inputs = ordered() {
                -- Expose selected controls from internal nodes to the Inspector
                TitleText = InstanceInput {
                    SourceOp = "TextPlus1",
                    Source = "StyledText",
                    Name = "Title",
                    Page = "Controls",
                },
                TitleColor = InstanceInput {
                    SourceOp = "TextPlus1",
                    Source = "Red1",
                    Name = "Color",
                    ControlGroup = 1,
                    Default = 1.0,
                },
                BoxColor = InstanceInput {
                    SourceOp = "Background1",
                    Source = "TopLeftRed",
                    Name = "Box Color",
                    ControlGroup = 2,
                    Default = 0.1,
                },
            },
            Outputs = {
                MainOutput1 = InstanceOutput {
                    SourceOp = "Merge1",
                    Source = "Output",
                }
            },
            ViewInfo = GroupInfo { Pos = { 0, 0 } },
            Tools = ordered() {
                -- All internal nodes that make up the composition
                Background1 = Background {
                    Inputs = {
                        Width = Input { Value = 1920, },
                        Height = Input { Value = 1080, },
                        UseFrameFormatSettings = Input { Value = 1, },
                        TopLeftRed = Input { Value = 0.1, },
                        TopLeftGreen = Input { Value = 0.1, },
                        TopLeftBlue = Input { Value = 0.1, },
                        TopLeftAlpha = Input { Value = 0.85, },
                    },
                    ViewInfo = OperatorInfo { Pos = { 100, 50 } },
                },
                TextPlus1 = TextPlus {
                    Inputs = {
                        Width = Input { Value = 1920, },
                        Height = Input { Value = 1080, },
                        UseFrameFormatSettings = Input { Value = 1, },
                        StyledText = Input { Value = "Sample Title", },
                        Font = Input { Value = "Open Sans", },
                        Style = Input { Value = "Bold", },
                        Size = Input { Value = 0.08, },
                    },
                    ViewInfo = OperatorInfo { Pos = { 100, 150 } },
                },
                Merge1 = Merge {
                    Inputs = {
                        Background = Input {
                            SourceOp = "Background1",
                            Source = "Output",
                        },
                        Foreground = Input {
                            SourceOp = "TextPlus1",
                            Source = "Output",
                        },
                        PerformTransform = Input { Value = 0, },
                    },
                    ViewInfo = OperatorInfo { Pos = { 300, 100 } },
                }
            },
        }
    },
    ActiveTool = "MyCustomTitle"
}
```

---

## 3. InstanceInput Specifications

`InstanceInput` exposes an internal parameter to the host application (e.g. DaVinci Resolve Inspector):

| Property | Type | Description |
| :--- | :--- | :--- |
| `SourceOp` | String | Name of internal node containing the parameter (e.g. `"TextPlus1"`) |
| `Source` | String | Internal parameter key (e.g. `"StyledText"`, `"Size"`, `"Center"`) |
| `Name` | String | User-facing display name in the Inspector |
| `Page` | String | Target tab page in Inspector (e.g. `"Controls"`, `"Text"`, `"Layout"`) |
| `Default` | Value | Default value when reset |
| `ControlGroup` | Integer | Groups R, G, B, A sliders into a unified color picker widget |

---

## 4. Where Templates Must Be Saved in DaVinci Resolve

To make templates appear in the DaVinci Resolve **Edit Page Effects Library**:

### Windows:
- **User Specific**:
  - Titles: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Titles\`
  - Generators: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Generators\`
  - Transitions: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Transitions\`
  - Effects: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Effects\`
- **System-Wide (All Users)**:
  - `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Templates\Edit\`

### macOS:
- `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/{Titles, Generators, Transitions, Effects}/`

### Linux:
- `~/.local/share/DaVinciResolve/Fusion/Templates/Edit/{Titles, Generators, Transitions, Effects}/`

---

## 5. Transition Template Rules

In Fusion transition templates:
- `MediaIn1` automatically represents the **outgoing clip** from track V1 (left clip).
- `MediaIn2` automatically represents the **incoming clip** from track V1 (right clip).
- The transition is driven by a `Dissolve` node or an animated mask.
- Never delete `MediaIn1` or `MediaIn2` in a transition template.
- Connect `MediaOut1.Input` to the final composite node.

---

## 6. How to Build a `.drfx` Bundle

A `.drfx` (DaVinci Resolve Fusion Extension) file is a standard **ZIP archive** with the `.zip` extension renamed to `.drfx`.

Directory structure inside the zip:
```
MyBundle.drfx (ZIP)
└── Edit/
    ├── Titles/
    │   └── MyTitle.setting
    ├── Generators/
    │   └── MyGenerator.setting
    ├── Transitions/
    │   └── MyTransition.setting
    └── Effects/
        └── MyEffect.setting
```
Double-clicking a `.drfx` file on any computer running DaVinci Resolve automatically prompts the user to install all included templates into their system!
