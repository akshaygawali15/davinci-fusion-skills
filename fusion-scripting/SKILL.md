---
name: fusion-scripting
description: Comprehensive expert guide and runbook for DaVinci Resolve Fusion compositing, node graphs, Lua/Python scripting, template (.setting) creation, expressions, modifiers, and pipeline debugging. Use whenever creating or modifying Fusion node networks, writing scripts for Fusion/Resolve, building motion graphics templates, or troubleshooting black screens, inverted masks, or broken node connections.
---

# DaVinci Resolve Fusion Compositing & Scripting Guide (Resolve 21.1+)

Fusion is a procedural, node-based 2D/3D compositing engine embedded inside DaVinci Resolve. Unlike layer-based editors, Fusion executes as a directed acyclic image-processing graph where operations propagate from upstream nodes (left) to downstream nodes (right) and culminate in an output.

---

## 1. Golden Rules of Fusion

1. **Left-to-Right Flow Direction**:
   - Media enters on the left (e.g. `MediaIn1`, `Loader`, `Background`, `TextPlus`).
   - Processing flows rightwards through filters, transforms, and merges.
   - Pixels must exit through `MediaOut1` (in Resolve timeline clips) or `Saver` (in Fusion Studio).
2. **The Merge Rule (Never Invert Foreground & Background)**:
   - **Background Input** (Orange / Yellow arrow): Base canvas. Sets the output resolution, bit depth, and color space.
   - **Foreground Input** (Green arrow): Layer placed *on top* of the background.
   - **EffectMask Input** (Blue arrow): Vector or raster mask restricting the blend.
   - *Trap*: Connecting Foreground to Background places graphics underneath footage!
3. **The Timeline Clip Media Contract**:
   - In DaVinci Resolve timeline clips, `MediaIn1` receives source pixels from the edit track.
   - `MediaOut1` delivers the final rendered composite back to the Edit page.
   - **If `MediaOut1.Input` is disconnected, the clip renders solid black in the Edit and Deliver pages.** Always verify `MediaOut1` has an active upstream connection.
4. **Normalized Coordinate System**:
   - Fusion positions are normalized `0.0` to `1.0`.
   - Bottom-Left is `(0.0, 0.0)`. Top-Right is `(1.0, 1.0)`. Center is `(0.5, 0.5)`.
   - Shapes are aspect-ratio independent: on a 16:9 frame, setting `Width = 0.5` and `Height = 0.5` on a rectangle or ellipse creates an ellipse/rectangle elongated by `16/9`. For an exact circle or square, scale height by the frame aspect ratio: `Height = Width * (width_px / height_px)`.
5. **Always Wrap Scripted Changes in Undo Blocks**:
   - Always open with `comp:StartUndo("Operation Name")` (Lua) or `comp.StartUndo("Operation Name")` (Python).
   - Always close with `comp:EndUndo(true)`. Failing to close undo blocks corrupts the undo stack and can crash Resolve.
6. **Prefer Procedural AnimCurves Over Fixed Keyframe Numbers**:
   - Hardcoded frame numbers break when editors change clip durations on the Edit page.
7. **TextPlus Alignment Values (Crucial Rule)**:
   - In TextPlus, `HorizontalLeftCenterRight` is a float slider:
     - `-1.0` = **Left Aligned**
     - `0.0` = **Center Aligned** (Standard for titles)
     - `1.0` = **Right Aligned**
   - Setting `1.0` right-aligns text to `Center.X`, causing long titles to spill off the left edge of the display! Always use `0.0` for centered motion graphic titles.
8. **Playhead Keyframe Capture Rule**:
   - Calling `tool.AddModifier(input, "BezierSpline")` automatically captures the value at `comp.CurrentTime` as the initial keyframe.
   - Always reset `comp.CurrentTime = 0.0` *before* adding animated modifiers.

---

## 2. Scripting Fusion: Python & Lua

### Accessing the Composition Object
In Python (external script or console):
```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
# Ensure we are on the Fusion page
resolve.OpenPage("fusion")

fusion = resolve.Fusion()
comp = fusion.GetCurrentComp()
```

From a specific Timeline Clip:
```python
timeline = project.GetCurrentTimeline()
clip = timeline.GetCurrentVideoItem()
comp = clip.GetFusionCompByIndex(1)
```

In Lua (internal Fusion script):
```lua
local comp = app:GetCurrentComp() or fusion:GetCurrentComp()
if not comp then
    print("Error: No active Fusion comp!")
    return
end
```

### Essential Composition Methods
| Method (Python) | Method (Lua) | Description |
| :--- | :--- | :--- |
| `comp.AddTool(id, defsettings, x, y)` | `comp:AddTool(id, defsettings, x, y)` | Adds tool at flow position `(x, y)` |
| `comp.FindTool(name)` | `comp:FindTool(name)` | Returns tool by name (e.g. `"MediaOut1"`) |
| `comp.FindToolByID(id)` | `comp:FindToolByID(id)` | Returns first tool matching registry ID |
| `comp.GetToolList(selected, regid)` | `comp:GetToolList(selected, regid)` | Returns dictionary/table of tools in comp |
| `comp.StartUndo(name)` | `comp:StartUndo(name)` | Starts an undo event |
| `comp.EndUndo(keep)` | `comp:EndUndo(keep)` | Closes undo event (`keep = True`) |
| `comp.Copy(tool_or_list)` | `comp:Copy(tool_or_list)` | Copies tools to system clipboard as ASCII |
| `comp.Paste(setting_dict_or_str)` | `comp:Paste(setting_dict_or_str)` | Pastes tools from ASCII table / clipboard |
| `comp.CurrentTime = frame` (Property) | `comp:SetCurrentTime(frame)` | Moves playhead to target frame |

### Essential Tool / Operator Methods
| Method (Python) | Method (Lua) | Description |
| :--- | :--- | :--- |
| `tool.SetAttrs({"TOOLS_Name": "NewName"})` | `tool:SetAttrs({ TOOLS_Name = "NewName" })` | Renames tool |
| `tool.ConnectInput(input_name, target)` | `tool:ConnectInput(input_name, target)` | Connects target output to input |
| `tool.SetInput(id, value, time)` | `tool:SetInput(id, value, time)` | Sets input value (optional keyframe time) |
| `tool.GetInput(id, time)` | `tool:GetInput(id, time)` | Reads input value at frame |
| `tool.AddModifier(input, modifier_id)` | `tool:AddModifier(input, modifier_id)` | Attaches modifier (e.g. `"AnimCurves"`) |
| `tool.Delete()` | `tool:Delete()` | Removes tool from composition |

---

## 3. High-Speed 1-Minute Motion Graphics Fast Track (< 60s Execution)

When the user asks for a motion graphic sequence, title card, or promo cut, **DO NOT** write 400 lines of boilerplate scratch scripts from scratch.
Use the pre-engineered, benchmarked, zero-defect functions in `fusion_utils.py` and `quick_promo.py`:

```python
import sys
sys.path.insert(0, r"fusion-scripting/scripts")
from fusion_utils import create_fusion_timeline, create_motion_graphics_promo, validate_comp_sanity

# 1. Instant Timeline & Fusion Clip setup (Under 2 seconds)
timeline, comp = create_fusion_timeline(project, "Motion_Graphic_30s", duration_seconds=30.0)

# 2. Multi-Scene Motion Graphic Generator (Under 2 seconds)
scenes = [
    {
        "tag": "INTRO // HIGHLIGHT",
        "title": "PRIMARY TITLE HERE",
        "subtitle": "Clear, concise supporting text explaining the benefit",
        "accent_color": (0.0, 0.88, 0.82)
    },
    {
        "tag": "KEY BENEFIT 01",
        "title": "FLAWLESS COMPOSITING",
        "subtitle": "Strict Input Contracts & Zero Black Screens",
        "accent_color": (0.98, 0.72, 0.15)
    }
]
create_motion_graphics_promo(comp, scenes, duration_frames=720)

# 3. Automated Zero-Defect Title Safe Validator (Under 0.5 seconds)
# Automatically checks DoD, corrects any font scale breaches, and verifies MediaOut1
validation = validate_comp_sanity(comp, auto_fix=True)
print("Validated:", validation["status"])
```

**Total Execution Time**: **< 3 seconds** end-to-end directly in DaVinci Resolve Studio!

---

## 4. Creating and Connecting Nodes in Script

### Python Example: Building a Red Canvas with Centered Circle
```python
comp.StartUndo("Add Red Canvas with Circle")

# 1. Background (Red)
bg = comp.AddTool("Background", True, 0.0, 0.0)
bg.SetAttrs({"TOOLS_Name": "RedBackground"})
bg.TopLeftRed = 1.0
bg.TopLeftGreen = 0.0
bg.TopLeftBlue = 0.0
bg.TopLeftAlpha = 1.0

# 2. Ellipse Mask
mask = comp.AddTool("EllipseMask", True, 0.0, -1.0)
mask.SetAttrs({"TOOLS_Name": "CircleMask"})
mask.Center = [0.5, 0.5]
mask.Width = 0.3
mask.Height = 0.3 * (1920.0 / 1080.0) # Aspect ratio correction for circle
mask.Solid = 1.0

# Connect mask to background
bg.EffectMask = mask.Output

# 3. Route to MediaOut1
mout = comp.FindTool("MediaOut1")
if not mout:
    mout = comp.AddTool("MediaOut", True, 2.0, 0.0)
mout.Input = bg.Output

comp.EndUndo(True)
```

---

## 5. The `.setting` Clipboard Magic (Instant ASCII Node Generation)

Every Fusion tool, group, and macro can be serialized to an ASCII Lua table.
To programmatically generate clean node graphs without hundreds of individual `AddTool` calls, build a `.setting` string and call `comp.Paste(setting_string)`!

### Example Setting String:
```lua
{
    Tools = ordered() {
        GlowCard = Merge {
            Inputs = {
                Background = Input { SourceOp = "MediaIn1", Source = "Output", },
                Foreground = Input { SourceOp = "TextPlus1", Source = "Output", },
            },
            ViewInfo = OperatorInfo { Pos = { 300, 100 } },
        },
        TextPlus1 = TextPlus {
            Inputs = {
                StyledText = Input { Value = "HEADLINE TEXT", },
                Font = Input { Value = "Open Sans", },
                Style = Input { Value = "Bold", },
                Size = Input { Value = 0.08, },
                Center = Input { Value = { 0.5, 0.5 }, },
                HorizontalLeftCenterRight = Input { Value = 0, },
            },
            ViewInfo = OperatorInfo { Pos = { 150, 150 } },
        }
    }
}
```

---

## 6. Templates & Macros for the Edit Page

To create reusable drag-and-drop templates for video editors:
1. Wrap tools in a `MacroOperator`.
2. Expose user-configurable parameters via `InstanceInput`.
3. Expose output via `InstanceOutput`.
4. Save the `.setting` file in:
   - **Titles**: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Titles\`
   - **Generators**: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Generators\`
   - **Transitions**: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Transitions\`
   - **Effects**: `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Effects\`

---

## 7. Procedural Animation: `AnimCurves` & `KeyStretcher`

Never hardcode keyframe frame numbers in templates!
- **`AnimCurves`**: Evaluates animation across normalized clip duration (`0.0` to `1.0`).
  - Attach `AnimCurves` to any input (`Size`, `Angle`, `Blend`, `Center`).
  - Set `Source = "Duration"` and `Curve = "Easing"`.
- **`KeyframeStretcher`**:
  - Insert between your animated graphics and the final merge.
  - Set `SourceStart = 0`, `SourceEnd = 100`, `StretchStart = 25`, `StretchEnd = 75`.
  - The intro (0-25) and outro (75-100) maintain 100% full speed; the middle holds to match any clip length on the timeline!

---

## 8. Troubleshooting & Failure Recovery

| Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| **Solid black screen on Edit page** | `MediaOut1.Input` disconnected or MediaOut index mismatch | Run `ensure_media_out_connected(comp)` to re-pipe the downstream merge into `MediaOut1.Input`. |
| **Text spills outside display bounds** | `HorizontalLeftCenterRight = 1.0` right-aligned text to screen center | Always use `HorizontalLeftCenterRight = 0.0` (Center) and run `validate_comp_sanity(comp, auto_fix=True)`. |
| **Keyframes overshoot or play simultaneous scenes** | Playhead was not at frame 0 when modifiers were attached | Always reset `comp.CurrentTime = 0.0` before creating BezierSpline modifiers. |
| **Graphics appear behind footage** | Swapped Merge inputs | Verify footage is connected to `Merge.Background` (orange) and graphics to `Merge.Foreground` (green). Swap with `Merge.Background, Merge.Foreground = Merge.Foreground, Merge.Background`. |
| **Circle is rendered as an oval** | Normalized coords without aspect correction | Scale mask height: `Height = Width * (1920.0 / 1080.0)`. Or enable `UseFrameFormatSettings = 1` and `PixelAspect = {1, 1}`. |
| **Animation plays too fast/slow on different clips** | Hardcoded keyframe numbers | Replace fixed spline keyframes with `AnimCurves` modifier or insert `KeyframeStretcher`. |
| **Script runs without error but nothing changes** | Calling setter without saving/undo end, or wrong page | Check if `comp.StartUndo` had matching `comp.EndUndo(True)`. Switch to Fusion page (`resolve.OpenPage("fusion")`). |
| **Mask hides everything outside instead of inside** | `Invert` parameter flipped | Set `mask.Invert = 1` (or `0`). |
