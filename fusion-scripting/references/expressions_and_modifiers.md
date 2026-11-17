# Fusion Expressions and Modifiers Guide

Expressions and modifiers give Fusion its procedural power. Instead of hardcoding keyframe numbers on every shot, procedural tools allow animations to automatically adapt to clip duration, resolution, and external parameters.

---

## 1. SimpleExpressions Syntax & Functions

SimpleExpressions can be added to any number, point, or text input by right-clicking the control in the Inspector and choosing **Expression**, or by pressing `=` in the field.

### Available Variables & Constants
| Variable | Meaning | Example |
| :--- | :--- | :--- |
| `time` | Current frame number | `sin(time * 0.1)` |
| `comp.CurrentTime` | Current composition frame | `comp.CurrentTime` |
| `comp.RenderStart` | First render frame of the comp | `time - comp.RenderStart` |
| `comp.RenderEnd` | Last render frame of the comp | `comp.RenderEnd - time` |
| `width`, `height` | Resolution of current tool input | `width / height` (aspect ratio) |
| `pi` | Math constant π (3.14159...) | `cos(time * pi / 30)` |

### Math Functions
- Basic math: `+`, `-`, `*`, `/`, `%` (modulo), `^` (exponent)
- Trigonometry: `sin(rad)`, `cos(rad)`, `tan(rad)`, `asin(x)`, `acos(x)`, `atan2(y, x)`
- Rounding: `floor(x)`, `ceil(x)`, `abs(x)`
- Min / Max / Clamp: `min(a, b)`, `max(a, b)`, `clamp(val, low, high)`
- Randomness: `rand(low, high)` (evaluates per-frame)

### Conditional Operator (`iif`)
Fusion uses Lua's inline conditional expression:
```lua
iif(condition, true_value, false_value)
```
Examples:
- Toggle visibility based on time:
  ```lua
  iif(time > 50, 1.0, 0.0)
  ```
- Flash effect (alternating every 5 frames):
  ```lua
  iif((time % 10) < 5, 1.0, 0.2)
  ```

### Point Expressions
For 2D coordinates (`Center`, `Pivot`, `Offset`), return a 2D point vector using `Point(x, y)`:
```lua
Point(0.5 + sin(time * 0.05) * 0.1, 0.5)
```

### String Expressions (for Text+ StyledText)
Wrap text and concatenate using Lua's `..` operator:
```lua
Text("Timecode: " .. time .. " / " .. comp.RenderEnd)
```
Formatted time:
```lua
Text("Rendering: " .. os.date("%H:%M:%S"))
```

### Pick-Whip Syntax (Referencing Other Nodes)
You can directly read any parameter or output of another node in the graph:
- `Merge1.Foreground.Width` (reads width of Foreground input image)
- `Transform1.Center.X` (reads X coordinate of Transform1's center)
- `Background1.TopLeftRed` (links color to Background1)

---

## 2. The `AnimCurves` Modifier (Resolution & Duration Independent Animation)

**Why AnimCurves is Essential for Templates**:
If you keyframe a title to animate in from frame 0 to frame 30 and out from frame 120 to frame 150, when an editor drops the title onto a 3-second or 10-second clip on the Edit page, the out-animation either cuts off or triggers at the wrong time!

`AnimCurves` solves this by calculating animation curves based on normalized **Duration** (`0.0` to `1.0`), not fixed frames.

### How to Apply `AnimCurves` via Script or `.setting`
In `.setting` syntax:
```lua
Size = Input {
    SourceOp = "AnimCurves1",
    Source = "Value",
}
```

### Key Parameters of `AnimCurves` (Registry ID: `LUTLookup` / `AnimCurves`)
- `Source`:
  - `Duration`: Scales animation across the full length of the clip.
  - `Transition`: Used for transition templates (`0.0` to `1.0` across the edit point).
- `Curve`:
  - `"Linear"`, `"Ease In"`, `"Ease Out"`, `"Easing"`, `"Custom"`.
- `Scale`: Multiplier for the value swing (e.g., `0.2` size expansion).
- `Offset`: Baseline value (e.g., `1.0` base scale).
- `Invert`: Reverses direction (e.g., zoom in vs zoom out).

---

## 3. The `KeyStretcher` Modifier & Node

The `KeyStretcher` node (`KeyframeStretcher` / `KfS`) preserves fixed-length intro and outro animations while stretching the middle hold period to match any clip length on the timeline!

### Parameters:
- `SourceStart`: First frame of original animation (e.g. `0`).
- `SourceEnd`: Last frame of original animation (e.g. `100`).
- `Keyframes`:
  - `StretchStart`: Frame where intro animation finishes and hold begins (e.g. `25`).
  - `StretchEnd`: Frame where hold finishes and outro animation begins (e.g. `75`).

When the editor stretches a 4-second title into a 15-second title on the Edit page, frames 0-25 play at normal speed, frames 75-100 play at normal speed, and the freeze frame between 25-75 is stretched across the difference!
