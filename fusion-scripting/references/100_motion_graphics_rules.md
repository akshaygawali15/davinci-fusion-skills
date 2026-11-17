# 100 Rules for Professional Motion Graphics in DaVinci Resolve Fusion

A comprehensive engineering, design, and editorial standard for creating high-impact, broadcast-grade motion graphics inside DaVinci Resolve Studio Fusion.

---

## Category A: Pre-Production & Strategic Planning (Rules 1 – 10)

1. **Define the Singular Objective**: Determine whether the graphic is meant to explain complex data, introduce a subject (title card), highlight an essential metric/statistic, or establish narrative context.
2. **Design for the Target Audience & Platform**: Tailor typography scale, pacing, and layout to the target viewing environment (mobile vertical 9:16, desktop 16:9, or broadcast television).
3. **Harmonize with Narrative Mood & Tone**: Align the visual aesthetic, typography weight, and color palette with the documentary's thematic identity (investigative, historical, corporate, or cinematic).
4. **Enforce One Primary Focal Point per Shot**: Maintain a single primary message or visual hero element per shot to prevent cognitive overload.
5. **Pre-Edit On-Screen Copy for Brevity**: Ruthlessly condense text copy before designing. Keep phrases short, punchy, and instantly understandable.
6. **Storyboard the Three-Act Temporal Arc**: Structure every motion graphic into a defined In (build/intro), Hold (readability window), and Out (transition/dissolve).
7. **Verify Project Resolution & Frame Rate Upfront**: Confirm timeline resolution (e.g., 1080p, 4K) and frame rate (e.g., 24fps, 30fps, 60fps) before creating Fusion node networks to avoid scaling artifacts.
8. **Lock Color Space & Management Settings**: Standardize color science (DaVinci YRGB Color Managed or Rec.709 Gamma 2.4) before shading tools to prevent color shifts between pages.
9. **Analyze Live Footage Lighting & Contrast**: Sample background footage exposure and color temperature so motion overlays feel integrated rather than superimposed.
10. **Establish Visual Reference & Styleframes**: Prepare styleframes or moodboard references before building complex node networks to maintain visual consistency across all video sequences.

---

## Category B: Text & Typography Standards (Rules 11 – 25)

11. **Select High-Legibility Typefaces**: Use clean, modern grotesque or geometric sans-serif typefaces (Open Sans, Inter, Montserrat, Roboto) for all user interface, informational, and motion graphics elements.
12. **Reserve Display Typefaces for Short Titles Only**: Never use decorative, script, or distressed display typefaces for multi-line subtitles or explanatory body text.
13. **Mobile Screen Legibility Standard**: Ensure all on-screen body text has a minimum vertical size of `0.022` (at 1080p, ~24px height) so it remains effortlessly readable on mobile devices.
14. **Enforce Clear Typographic Hierarchy**: Differentiate Title, Subtitle, and Metadata through distinct scale ratios (e.g., `0.068` vs `0.026`), weights (ExtraBold vs Regular), and luminance contrast.
15. **Limit Font Families to Two Maximum**: Restrict the entire project to at most one primary headline font and one complementary body font.
16. **Verify Non-Latin & Multilingual Glyphs in Viewer**: Confirm that all complex scripts (such as Marathi, Devanagari, Hindi, Japanese) render correct conjuncts, vowel matras, and diacritics in Fusion TextPlus without missing glyphs.
17. **Inspect Ligatures and Punctuation**: Verify ligatures (`fi`, `fl`), quotation marks, em-dashes, and currency symbols render cleanly without overlapping adjacent letterforms.
18. **Constrain Line Length (Character Count)**: Never allow a single text line to exceed 50-60 characters; wrap longer sentences into balanced 2-3 line blocks.
19. **Generous Line Spacing (Leading)**: Maintain generous line spacing (`LineSpacing = 1.25` to `1.35`) in TextPlus to prevent multi-line descenders and ascenders from colliding.
20. **Inspect Character Spacing (Tracking)**: Use subtle kerning adjustments (`CharacterSpacingHorizontal = 1.05` to `1.10`) for uppercase titles; avoid exaggerated tracking that degrades legibility.
21. **Title Safe Boundary Enforcement**: Keep all typography within the SMPTE Title Safe zone (minimum 10% margin on all sides, `X: 0.10` to `0.90`). Never place text near outer display edges.
22. **Audience Reading Time Formula**: Provide sufficient screen duration based on human reading speed: minimum 1.5 seconds for initial recognition plus 0.3 seconds per word.
23. **Restrained Text Animation**: Animate text as cohesive lines or phrase blocks; avoid chaotic letter-by-letter or word-by-word jitter unless deliberately stylizing a typewriter effect.
24. **Avoid Redundant On-Screen Transcription**: Do not duplicate verbatim speech onto the screen unless specifically creating subtitles; on-screen text should summarize or provide new visual evidence.
25. **Double-Check All Factual Data**: Cross-check names, titles, dates, geographical locations, and numerical statistics twice before rendering.

---

## Category C: Visual Design, Composition & Layout (Rules 26 – 40)

26. **Establish a Clear Visual Anchor**: Position the hero element with deliberate weight so the viewer's eye instantly knows where to look first.
27. **Visual Priority via Scale, Contrast & Placement**: Use size, luminance contrast, or framing accents to establish which graphic element is most important.
28. **Balance Footage and Graphic Elements**: Position graphics in natural negative space (e.g., lower thirds, opposite the subject's eyeline) to create visual harmony.
29. **Stagger Concurrent Graphic Entrances**: Avoid bringing multiple disparate graphic elements onto the screen on the exact same frame; stagger entrances by 4-8 frames.
30. **Embrace Negative Space (Breathing Room)**: Leave ample uncrowded canvas; never clutter the screen edge-to-edge with excessive boxes, arrows, or decorative shapes.
31. **Strict 3-Color Palette Restriction**: Limit color schemes to 1 dark canvas tone, 1 neutral readable text tone (white/light gray), and 1-2 vivid accent tones (cyan, amber, mint).
32. **Harmonize with Overall Project Palette**: Sample accent colors from project art direction or footage grades rather than choosing random neon hues.
33. **Guaranteed Luminance Contrast**: Ensure a minimum 4.5:1 luminance contrast ratio between foreground typography and background plates for effortless readability.
34. **Use Underlays or Scrims Over Busy Footage**: Place a subtle dark gradient, blur, or tinted pill underlay behind text when overlaying busy, detailed video footage.
35. **Action Safe & Title Safe Adherence**: Position all critical visual information inside Action Safe (90%) and all text inside Title Safe (80%).
36. **Face-Safe & Eyeline-Safe Clearance**: Never allow lower thirds, charts, or labels to collide with or obstruct human faces, eyes, or primary documentary action.
37. **Clear Directional Indicators**: When using arrows, leader lines, or callout pins, ensure they terminate precisely on the intended subject without ambiguity.
38. **Universally Understood Iconography**: Use intuitive, recognized icons; avoid obscure symbols that require mental decoding.
39. **Curate Data Visualizations**: In maps, line charts, and bar graphs, strip away chartjunk, gridlines, and superfluous ticks; display only the key inflection point or metric.
40. **Consistent Color Coding Semantics**: If a color denotes a specific category or meaning (e.g. green for increase, red for decrease), keep that semantic mapping 100% consistent across all graphics.

---

## Category D: Animation Dynamics, Timing & Easing (Rules 41 – 60)

41. **Purpose-Driven Motion**: Every motion vector must have narrative or communicative justification; eliminate motion added merely to keep things moving.
42. **Eliminate Motion Noise**: Avoid continuous jitter, oscillating wiggle, or endless secondary loops that distract from reading comprehension.
43. **Natural Momentum & Deceleration**: Objects should enter with rapid momentum and smoothly decelerate to their resting position as if governed by real-world inertia.
44. **Avoid Linear Keyframing**: Never use linear interpolation (`Linear`) on visual transforms; linear start/stop motion looks robotic and amateur.
45. **Universal Bezier Easing**: Apply smooth Bezier easing (`BezierSpline`) on all translation, scale, and blend keyframes.
46. **Inspect Spline Curves in Fusion Spline Editor**: Always open the Spline Editor panel to inspect the velocity curve; ensure acceleration curves are smooth without kinks or overshoots.
47. **Symmetric or Snappy Bezier Handles**: Use `T` (Smooth) and adjust spline handles to create a snappy 60-80% ease-in and gradual ease-out.
48. **Match Motion Velocity to Narrative Pacing**: Fast energetic cuts require rapid 8-12 frame graphic builds; contemplative documentaries require 20-30 frame elegant drifts.
49. **Avoid Hyperactive Bouncing in Serious Contexts**: In historical, investigative, or serious documentary scenes, avoid playful spring or elastic bounces.
50. **Adequate Read-Hold Duration**: Once animated in, allow graphics to remain completely stationary (or with only ultra-subtle 1-2% scale drift) long enough for comfortable reading.
51. **Stylistic Consistency with Variable Entrances**: Maintain consistent easing curves and visual hierarchy across the project, even when varying entrance directions (slide-up, mask-reveal, scale-pop).
52. **Hierarchical Motion Staggering**: Secondary elements (subtitles, accent bars, badges) should inherit or follow the primary title's motion with a 4-6 frame delay.
53. **Coordinated Multi-Element Choreography**: When animating multi-node layouts, organize entrances logically: Base Background -> Hero Graphic -> Supporting Text -> Accent Details.
54. **Judicious Motion Blur Usage**: Apply Motion Blur (`Settings -> Motion Blur`) only on fast translation and scale transitions; avoid blurring static or slow-drifting elements.
55. **Motion Blur Quality & Shutter Angle**: When enabling Motion Blur, use `Quality = 4` or `8` and match the timeline camera shutter angle (typically `180.0` degrees).
56. **Sync Entrances to Audio Beats & Dialogue**: Anchor motion graphic in-points to spoken narration cues, music downbeats, or cuts in the edit timeline.
57. **Clean Exit Transitions Before Shot Cuts**: Transition out on-screen graphics 8-12 frames before the underlying video cut to avoid jarring visual collision.
58. **Provide Visual Stillness**: Do not animate continuously; provide resting periods where the eye can settle and absorb information.
59. **Pacing Prioritizes Comprehension**: Graphic timing must serve the viewer's cognitive processing speed above aesthetic flair.
60. **Avoid Premature Transitions**: Ensure transitions do not whisk text away while the narrator is still speaking about that topic.

---

## Category E: Fusion Node Graph Architecture & Hygiene (Rules 61 – 75)

61. **Clean, Structured Left-to-Right Flow**: Organize nodes in a strictly linear left-to-right DAG (Directed Acyclic Graph) trunk with branches organized logically above.
62. **Explicit Semantic Node Naming**: Never leave default tool names (`Merge1`, `Transform4`, `TextPlus2`); immediately rename nodes to semantic names (`Title_Text`, `Merge_Scene1`, `Glow_Mask`).
63. **Group & Cluster Related Operations**: Place related nodes into Underlays or GroupOperators to modularize the node network.
64. **Use Underlays and Color Labels for Navigation**: In complex compositions (20+ nodes), wrap functional blocks in Underlays with distinct colors (e.g. Blue for Background, Yellow for Text, Green for Masks).
65. **Single Clear Purpose per Node**: Do not overload nodes; separate layout transforms (`Transform` for layout positioning) from animated motion transforms (`Transform` for animation).
66. **Master the Merge Input Contract (Green vs Yellow)**:
    - `Background` (Orange/Yellow): The canvas / under layer.
    - `Foreground` (Green): The layer placed *on top*.
    - `EffectMask` (Blue): Vector or raster mask limiting the merge operation.
67. **Modular Multi-Scene Architecture**: Build multi-section motion graphics with isolated scene branches merged sequentially onto a single master trunk.
68. **Export Reusable Macros (.setting & .drfx)**: Encapsulate recurring titles and lower thirds into `MacroOperator` `.setting` files for instant reuse across the Edit page.
69. **Inspect Transform Pivots & Anchors**: Always set the `Pivot` (`{X, Y}`) to the logical center of rotation and scaling before adding animated modifiers.
70. **Strict MediaOut1 Connection Contract**: Always ensure the downstream merge or effect terminates into `MediaOut1.Input` to prevent black screens on the Edit page.
71. **Inspect Mask Softness & Bounding**: Always verify `SoftEdge` and mask limits to avoid clipping glowing borders or hard edges cutting through ambient gradients.
72. **Prune Disconnected & Orphaned Tools**: Delete unused tools, disabled experiments, and orphaned nodes before finalizing compositions.
73. **Inspect Broken Tool Links & Red Indicators**: Check node flow for broken tool links or invalid Lua expressions (marked with red node outlines or console warnings).
74. **Double Viewer Verification**: Use Dual Viewers (Key 1 for Viewer 1 / Key 2 for Viewer 2) to monitor upstream elements while inspecting the final `MediaOut1` output.
75. **Always Enclose Scripted Modifications in Undo Blocks**: In Python/Lua scripting, wrap all graph mutations in `comp.StartUndo("Description")` and `comp.EndUndo(True)`.

---

## Category F: Color, Shading, Effects & Graphic Assets (Rules 76 – 88)

76. **Subtle, Restrained Optical Effects**: Use Glow, Drop Shadow, and Blur with restraint; avoid blown-out nuclear glows that degrade professional fidelity.
77. **Preserve Typography Edge Sharpness**: Ensure glow and blur effects do not bleed into letterforms and destroy character edge crispness.
78. **Consistent Directional Lighting & Shadows**: Maintain consistent shadow offset angle and soft edge blur across all elements on screen (e.g., top-left light source casting bottom-right shadow).
79. **Footage Color Gamut Harmony**: Ensure graphic RGB values do not conflict with footage color grading (e.g., avoid hyper-saturated pure greens over graded teal-orange footage).
80. **Broadcast Safe Color Compliance**: Keep RGB values within standard broadcast legal limits (`16-235` in 8-bit equivalent / Rec.709 legal) to avoid clipping on calibrated displays.
81. **Subtle Background Gradients**: When using gradient canvas backgrounds, use smooth, low-contrast gradients to avoid distracting the eye from foreground information.
82. **Flat & 2.5D Restraint Over Unnecessary 3D**: Do not force complex 3D scenes when clean, crisp 2D or 2.5D typography communicates the message faster and cleaner.
83. **Coordinated 3D Lighting & Cameras**: If using Fusion 3D nodes (`Shape3D`, `Camera3D`, `SpotLight`), ensure light coordinates, shadows, and focal length match the footage camera.
84. **Keep Particle Systems Subdued**: Treat particle systems (`pEmitter`, `pRender`) as atmospheric background dust or subtle ambient depth, never as loud screen-filling distractions.
85. **Dual-Coding for Data Graphics (Color + Label)**: In charts and data graphics, never rely solely on color to convey data; always provide text labels, percentages, or shape cues.
86. **Color-Blind Accessibility (WCAG 2.1)**: Avoid red-green only distinctions; use shape, line styling, or high luminance contrast so color-blind viewers easily understand the data.
87. **High-Resolution Vector & Lossless Raster Assets**: When importing external logos or maps, use vector SVG/EPS or high-res lossless PNGs with clean alpha channels; never upscale compressed JPEGs.
88. **Preserve Subtitle & Lower-Third Clearance**: When placing graphics, reserve the bottom 15-20% of the screen for subtitles and YouTube UI playhead controls.

---

## Category G: Quality Assurance, Verification & Delivery (Rules 89 – 100)

89. **Full Real-Time Scrub & Playback in Fusion**: Play the entire composition from frame 0 to the final frame in Fusion viewer to verify caching, timing, and smooth motion.
90. **Playback Verification on Edit Timeline**: Switch to the Edit page and verify playback in timeline context against background audio, dialogue, and adjacent video cuts.
91. **Low-Resolution Proxy / Thumbnail Check**: Test legibility at 25% preview scale or small thumbnail size to ensure the core message remains readable on small screens.
92. **Mobile Device Field Verification**: Inspect the exported frame on a real smartphone screen to verify text scale and contrast under ambient lighting.
93. **Cross-Display Color Calibration Verification**: Check colors across calibrated Rec.709 display, standard sRGB monitor, and mobile OLED to ensure consistent color rendition.
94. **Frame-by-Frame Artifact & Flicker Audit**: Step through cut boundaries frame-by-frame (`Left`/`Right` arrow keys) to eliminate single-frame glitches, keyframe overshoots, or mask clipping.
95. **Spelling, Numerical Data & Typography Proofreading**: Perform a rigorous final pass to verify spelling, grammar, numbers, units, and punctuation.
96. **Temporal Audio-Visual Synchronization Audit**: Verify that animations, sound effects (whooshes, hits), and voiceover narration align to the exact frame.
97. **Alpha Channel & Premultiplication Verification**: If exporting graphics with transparency, ensure the alpha channel is exported as Straight or Premultiplied according to the editing pipeline contract.
98. **Verify Render Resolution, Codec & Frame Rate**: Confirm Deliver page settings match exact timeline delivery specifications (e.g., ProRes 4444 for master graphics, ProRes 422 or H.264/H.265 for web).
99. **Black-Frame & Drop-Frame Elimination**: Ensure zero black frames at clip start/end, no missing media offline badges, and no dropped render frames.
100. **The Golden Narrative Test**: Ask the final essential question: *"Does this motion graphic serve the story, enhance understanding, and elevate the film's authority?"* If it distracts or confuses, simplify it until it is pure, effortless communication.
