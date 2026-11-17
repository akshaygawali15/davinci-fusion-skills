# DaVinci Resolve Fusion Nodes Reference

This reference documents the exact registry IDs, primary inputs, outputs, and key scriptable parameters for commonly used tools in Fusion Studio and DaVinci Resolve Fusion page.

---

## 1. Node Categories & Registry IDs

| Category | Node Name | Registry ID | Primary Inputs | Primary Output | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **I/O** | MediaIn | `MediaIn` | None | `Output` | Imports footage from Resolve timeline track or background |
| **I/O** | MediaOut | `MediaOut` | `Input` | None | Sends final composited pixels back to Resolve timeline |
| **I/O** | Loader | `Loader` | None | `Output` | Standalone Fusion file loader (image sequences, video) |
| **I/O** | Saver | `Saver` | `Input` | None | Standalone Fusion file saver/renderer |
| **Composite** | Merge | `Merge` | `Background`, `Foreground`, `EffectMask` | `Output` | Layers foreground over background using blend modes |
| **Composite** | Dissolve | `Dissolve` | `Background`, `Foreground` | `Output` | Dissolves between two inputs with ramp/wipes |
| **Composite** | Channel Booleans | `ChannelBoolean` | `Background`, `Foreground` | `Output` | Performs mathematical/bitwise operations between channels |
| **Generator** | Background | `Background` | `EffectMask` | `Output` | Creates solid color, gradient (horizontal, vertical, radial) canvas |
| **Generator** | Text+ | `TextPlus` | `EffectMask` | `Output` | 2D/3D resolution-independent styled vector text generator |
| **Generator** | Fast Noise | `FastNoise` | `EffectMask` | `Output` | Procedural Perlin noise generator |
| **Transform** | Transform | `Transform` | `Input`, `EffectMask` | `Output` | 2D scale, move, rotate, shear, flip |
| **Transform** | Crop | `Crop` | `Input` | `Output` | Crops canvas to specific X/Y dimensions |
| **Transform** | Corner Positioner | `CornerPositioner` | `Input`, `EffectMask` | `Output` | 4-point corner pin warping |
| **Transform** | DVE | `DVE` | `Input`, `EffectMask` | `Output` | 3D plane rotation inside 2D space |
| **Filter** | Blur | `Blur` | `Input`, `EffectMask` | `Output` | Fast Gaussian / box blur |
| **Filter** | Directional Blur | `DirectionalBlur` | `Input`, `EffectMask` | `Output` | Linear / radial / zoom directional motion blur |
| **Filter** | Glow | `Glow` | `Input`, `EffectMask` | `Output` | Highlights blur/glow overlay |
| **Mask** | Rectangle Mask | `RectangleMask` | `EffectMask` | `Mask` | Rectangular vector mask with corner radius |
| **Mask** | Ellipse Mask | `EllipseMask` | `EffectMask` | `Mask` | Elliptical / circular vector mask |
| **Mask** | Polygon Mask | `PolygonMask` | `EffectMask` | `Mask` | Bezier polyline rotoscoping mask |
| **Mask** | B-Spline Mask | `BSplineMask` | `EffectMask` | `Mask` | B-Spline smooth curve mask |
| **Mask** | Bitmap Mask | `BitmapMask` | `Image`, `EffectMask` | `Mask` | Converts luminance/alpha of an image into a mask |
| **Matte / Key** | Delta Keyer | `DeltaKeyer` | `Input`, `CleanPlate`, `PreMatte` | `Output` | Advanced color difference chroma keyer |
| **Matte / Key** | Clean Plate | `CleanPlate` | `Input` | `Output` | Generates procedural clean plate from footage |
| **Matte / Key** | Matte Control | `MatteControl` | `Background`, `Foreground`, `GarbageMatte` | `Output` | Manipulates, shrinks, expands, or replaces alpha |
| **Matte / Key** | Alpha Divide | `AlphaDivide` | `Input` | `Output` | Un-premultiplies RGB by Alpha |
| **Matte / Key** | Alpha Multiply | `AlphaMultiply` | `Input` | `Output` | Re-premultiplies RGB by Alpha |
| **Tracking** | Tracker | `Tracker` | `Input`, `PatternMask` | `Output` | Multi-point pattern tracker & stabilizer |
| **Tracking** | Planar Tracker | `PlanarTracker` | `Input`, `PatternMask` | `Output` | Surface planar tracker for corner pinning / roto |
| **Tracking** | Planar Transform | `PlanarTransform` | `Input` | `Output` | Applies planar tracking data to any other layer |
| **3D** | Merge 3D | `Merge3D` | `SceneInput1`, `SceneInput2`... | `Output` | Combines 3D lights, cameras, and geometry |
| **3D** | Camera 3D | `Camera3D` | None | `Output` | Virtual 3D camera |
| **3D** | Image Plane 3D | `ImagePlane3D` | `MaterialInput`, `SceneInput` | `Output` | Projects 2D image onto a 3D planar mesh |
| **3D** | Shape 3D | `Shape3D` | `MaterialInput` | `Output` | 3D primitive geometry (Cube, Sphere, Cylinder) |
| **3D** | Text 3D | `Text3D` | None | `Output` | Extruded 3D text with beveling |
| **3D** | Directional Light | `DirectionalLight` | None | `Output` | Infinite parallel sun light |
| **3D** | Spot Light | `SpotLight` | None | `Output` | Cone spotlight with decay and penumbra |
| **3D** | Renderer 3D | `Renderer3D` | `SceneInput` | `Output` | Renders 3D scene into 2D raster pixels |
| **Shapes (s)** | Shape Render | `sRender` | `Input` | `Output` | Renders resolution-independent vector shapes |
| **Shapes (s)** | Shape Rectangle | `sRectangle` | None | `Output` | Vector rectangle primitive |
| **Shapes (s)** | Shape Ellipse | `sEllipse` | None | `Output` | Vector ellipse primitive |
| **Shapes (s)** | Shape Merge | `sMerge` | `Input1`, `Input2` | `Output` | Combines vector shape paths |
| **Shapes (s)** | Shape Outline | `sOutline` | `Input` | `Output` | Converts filled vector shapes into strokes |
| **Particles** | Particle Emitter | `pEmitter` | `Style`, `Region` | `Output` | Generates 3D/2D particle systems |
| **Particles** | Particle Render | `pRender` | `Input` | `Output` | Renders particles into 2D/3D image |
| **Particles** | Particle Turbulence | `pTurbulence` | `Input` | `Output` | Adds noise turbulence to particles |
| **Flow** | Pipe Router | `PipeRouter` | `Input` | `Output` | Passive passthrough pipe for tidying flow graphs |
| **Flow** | Underlay | `Underlay` | None | None | Visual organizational backdrop grouping nodes |

---

## 2. In-Depth Input/Output Names and Parameter Keys

### `Merge` (`Merge`)
- **Inputs**:
  - `Background` (Index 1, Orange): Bottom layer canvas. Sets canvas resolution and color space.
  - `Foreground` (Index 2, Green): Top layer composited over the background.
  - `EffectMask` (Index 3, Blue): Optional mask limiting the composite operation.
- **Key Parameters**:
  - `PerformTransform` (Boolean): Enables foreground positioning inside Merge.
  - `Center` (`{X, Y}`): Normalized `[0.0, 1.0]`. Default: `{0.5, 0.5}`.
  - `Size` (Float): Scale multiplier (1.0 = 100%).
  - `Angle` (Float): Rotation in degrees.
  - `Blend` (Float): Master opacity of foreground `[0.0, 1.0]`.
  - `ApplyMode` (String / FuID): `"Normal"`, `"Screen"`, `"Multiply"`, `"Overlay"`, `"HardLight"`, `"SoftLight"`, `"ColorDodge"`, `"ColorBurn"`.
  - `Operator` (String / FuID): `"Over"` (default), `"In"`, `"Out"`, `"Atop"`, `"XOr"`, `"Under"`.
  - `Subtractive` (Float): `0.0` = Additive blend, `1.0` = Subtractive blend.

### `Background` (`Background`)
- **Inputs**:
  - `EffectMask` (Blue): Masks the background fill.
- **Key Parameters**:
  - `Type` (String / FuID): `"Solid"`, `"Horizontal"`, `"Vertical"`, `"Four Corner"`, `"Gradient"`.
  - `TopLeftRed`, `TopLeftGreen`, `TopLeftBlue`, `TopLeftAlpha` (Float `0.0 - 1.0`): Primary color channels.
  - `TopRightRed`, `BottomLeftRed`, `BottomRightRed` (Float): Multi-corner gradient colors.
  - `Width`, `Height` (Integer): Canvas resolution (e.g., 1920, 1080).
  - `UseFrameFormatSettings` (Integer `0` or `1`): When `1`, inherits project/timeline resolution automatically.
  - `PixelAspect` (`{X, Y}`): Normalized pixel aspect (usually `{1, 1}`).
  - `Depth` (Integer): Bit depth (`1` = 8-bit int, `2` = 16-bit int, `3` = 32-bit float).

### `TextPlus` (`TextPlus`)
- **Inputs**:
  - `EffectMask` (Blue): Masks the text render.
- **Key Parameters**:
  - `StyledText` (String): The text content (e.g., `"Welcome to DaVinci Resolve"`).
  - `Font` (String): Font family (e.g., `"Open Sans"`, `"Arial"`, `"Roboto"`).
  - `Style` (String): Font style (e.g., `"Bold"`, `"Regular"`).
  - `Size` (Float): Font size relative to frame height (`0.05` to `0.2` typical).
  - `Center` (`{X, Y}`): Position anchor on screen (`{0.5, 0.5}` center).
  - `LineSpacing` (Float): Multiplier for multi-line spacing.
  - `CharacterSpacingHorizontal` (Float): Tracking / kerning offset.
  - `Red1`, `Green1`, `Blue1`, `Alpha1` (Float): Element 1 (Fill) color.
  - `Softness1` (`{X, Y}`): Text edge softness blur.
  - `VerticalTopCenterBottom` (Integer): `0` = Top, `1` = Center, `2` = Bottom alignment.
  - `HorizontalLeftCenterRight` (Integer): `0` = Left, `1` = Center, `2` = Right, `3` = Justify.

### `Transform` (`Transform`)
- **Inputs**:
  - `Input` (Orange): Image to transform.
  - `EffectMask` (Blue): Limits transformation area.
- **Key Parameters**:
  - `Center` (`{X, Y}`): Center position on canvas. Default: `{0.5, 0.5}`.
  - `Pivot` (`{X, Y}`): Anchor point around which rotation and scaling occur. Default: `{0.5, 0.5}`.
  - `Size` (Float): Uniform scale (`1.0` = 100%).
  - `XSize`, `YSize` (Float): Non-uniform scaling when `UseSizeAndAspect = 0`.
  - `Angle` (Float): Rotation in degrees (`0.0` to `360.0`).
  - `FlipHoriz`, `FlipVert` (Integer `0` or `1`): Horizontal/vertical reflection.
  - `Edges` (String / FuID): Canvas out-of-bounds treatment: `"Canvas"`, `"Wrap"`, `"Duplicate"`, `"Mirror"`.
  - `InvertTransform` (Integer `0` or `1`): Inverts transformation matrix.

### `RectangleMask` (`RectangleMask`)
- **Key Parameters**:
  - `Center` (`{X, Y}`): Center coordinates.
  - `Width`, `Height` (Float): Normalized dimensions (`0.0` to `1.0`). Note: Width and Height are independent of aspect ratio; for a square at 16:9, `Height = Width * (16 / 9)`.
  - `CornerRadius` (Float): Rounding of mask corners (`0.0` to `1.0`).
  - `Angle` (Float): Rotation of mask in degrees.
  - `Invert` (Integer `0` or `1`): Inverts mask selection.
  - `Solid` (Integer `0` or `1`): Filled mask vs hollow stroke.
  - `BorderWidth` (Float): Stroke thickness when `Solid = 0`.
  - `SoftEdge` (Float): Gaussian feathering of mask edges.

### `DeltaKeyer` (`DeltaKeyer`)
- **Inputs**:
  - `Input` (Orange): Footage containing green/blue screen.
  - `CleanPlate` (Magenta): Optional CleanPlate node for uneven lighting compensation.
  - `PreMatte` (Cyan): Optional garbage or core matte.
- **Key Parameters**:
  - `KeyColor` (`{R, G, B}`): Background screen sample color.
  - `ShadowThreshold`, `HighlightThreshold` (Float): Matte tuning controls.
  - `ColorSpillSuppression` (Float): Spill suppression intensity.
  - `Tuning` / `MatteFringe`: Edge treatment and despill controls.

### `Renderer3D` (`Renderer3D`)
- **Inputs**:
  - `SceneInput` (Orange): 3D scene from `Merge3D` or geometry node.
- **Key Parameters**:
  - `RendererType` (String / FuID): `"OpenGLRenderer"`, `"SoftwareRenderer"`.
  - `Width`, `Height` (Integer): Output 2D raster resolution.
  - `Camera` (String): Name of camera in 3D scene to render through (or `"Default"`).
  - `LightingEnabled` (Integer `0` or `1`): Enables 3D light calculations.
  - `ShadowsEnabled` (Integer `0` or `1`): Enables shadow casting.
