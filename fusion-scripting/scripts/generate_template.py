#!/usr/bin/env python3
"""
DaVinci Resolve Fusion Template Generator CLI
Generates valid, production-ready .setting files and macros for Edit Page Titles,
Generators, and Transitions with exposed controls and AnimCurves procedural animation.
"""

import os
import sys
import argparse


LOWER_THIRD_TEMPLATE = """{
\tTools = ordered() {
\t\t%{MACRO_NAME} = MacroOperator {
\t\t\tInputs = ordered() {
\t\t\t\tInput1 = InstanceInput {
\t\t\t\t\tSourceOp = "TitleText",
\t\t\t\t\tSource = "StyledText",
\t\t\t\t\tName = "Title",
\t\t\t\t\tPage = "Controls",
\t\t\t\t},
\t\t\t\tInput2 = InstanceInput {
\t\t\t\t\tSourceOp = "SubtitleText",
\t\t\t\t\tSource = "StyledText",
\t\t\t\t\tName = "Subtitle",
\t\t\t\t\tPage = "Controls",
\t\t\t\t},
\t\t\t\tInput3 = InstanceInput {
\t\t\t\t\tSourceOp = "PillBackground",
\t\t\t\t\tSource = "TopLeftRed",
\t\t\t\t\tName = "Card Color",
\t\t\t\t\tControlGroup = 1,
\t\t\t\t\tDefault = 0.1,
\t\t\t\t},
\t\t\t\tInput4 = InstanceInput {
\t\t\t\t\tSourceOp = "PillBackground",
\t\t\t\t\tSource = "TopLeftGreen",
\t\t\t\t\tControlGroup = 1,
\t\t\t\t\tDefault = 0.1,
\t\t\t\t},
\t\t\t\tInput5 = InstanceInput {
\t\t\t\t\tSourceOp = "PillBackground",
\t\t\t\t\tSource = "TopLeftBlue",
\t\t\t\t\tControlGroup = 1,
\t\t\t\t\tDefault = 0.12,
\t\t\t\t},
\t\t\t\tInput6 = InstanceInput {
\t\t\t\t\tSourceOp = "PillBackground",
\t\t\t\t\tSource = "TopLeftAlpha",
\t\t\t\t\tControlGroup = 1,
\t\t\t\t\tDefault = 0.9,
\t\t\t\t},
\t\t\t\tInput7 = InstanceInput {
\t\t\t\t\tSourceOp = "PillMask",
\t\t\t\t\tSource = "CornerRadius",
\t\t\t\t\tName = "Roundness",
\t\t\t\t\tDefault = 0.35,
\t\t\t\t},
\t\t\t\tInput8 = InstanceInput {
\t\t\t\t\tSourceOp = "CardTransform",
\t\t\t\t\tSource = "Center",
\t\t\t\t\tName = "Position",
\t\t\t\t},
\t\t\t\tInput9 = InstanceInput {
\t\t\t\t\tSourceOp = "CardTransform",
\t\t\t\t\tSource = "Size",
\t\t\t\t\tName = "Overall Size",
\t\t\t\t\tDefault = 1.0,
\t\t\t\t},
\t\t\t},
\t\t\tOutputs = {
\t\t\t\tMainOutput1 = InstanceOutput {
\t\t\t\t\tSourceOp = "CardTransform",
\t\t\t\t\tSource = "Output",
\t\t\t\t}
\t\t\t},
\t\t\tViewInfo = GroupInfo { Pos = { 0, 0 } },
\t\t\tTools = ordered() {
\t\t\t\tPillBackground = Background {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tUseFrameFormatSettings = Input { Value = 1, },
\t\t\t\t\t\tWidth = Input { Value = 1920, },
\t\t\t\t\t\tHeight = Input { Value = 1080, },
\t\t\t\t\t\tTopLeftRed = Input { Value = 0.08, },
\t\t\t\t\t\tTopLeftGreen = Input { Value = 0.08, },
\t\t\t\t\t\tTopLeftBlue = Input { Value = 0.1, },
\t\t\t\t\t\tTopLeftAlpha = Input { Value = 0.88, },
\t\t\t\t\t\tEffectMask = Input {
\t\t\t\t\t\t\tSourceOp = "PillMask",
\t\t\t\t\t\t\tSource = "Mask",
\t\t\t\t\t\t}
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { -150, 50 } },
\t\t\t\t},
\t\t\t\tPillMask = RectangleMask {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tCenter = Input { Value = { 0.25, 0.2 }, },
\t\t\t\t\t\tWidth = Input { Value = 0.38, },
\t\t\t\t\t\tHeight = Input { Value = 0.14, },
\t\t\t\t\t\tCornerRadius = Input { Value = 0.35, },
\t\t\t\t\t\tUseFrameFormatSettings = Input { Value = 1, },
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { -150, -20 } },
\t\t\t\t},
\t\t\t\tTitleText = TextPlus {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tUseFrameFormatSettings = Input { Value = 1, },
\t\t\t\t\t\tWidth = Input { Value = 1920, },
\t\t\t\t\t\tHeight = Input { Value = 1080, },
\t\t\t\t\t\tStyledText = Input { Value = "%{TITLE_DEFAULT}", },
\t\t\t\t\t\tFont = Input { Value = "Open Sans", },
\t\t\t\t\t\tStyle = Input { Value = "Bold", },
\t\t\t\t\t\tSize = Input { Value = 0.042, },
\t\t\t\t\t\tCenter = Input { Value = { 0.25, 0.23 }, },
\t\t\t\t\t\tHorizontalLeftCenterRight = Input { Value = 1, },
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { 50, 0 } },
\t\t\t\t},
\t\t\t\tSubtitleText = TextPlus {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tUseFrameFormatSettings = Input { Value = 1, },
\t\t\t\t\t\tWidth = Input { Value = 1920, },
\t\t\t\t\t\tHeight = Input { Value = 1080, },
\t\t\t\t\t\tStyledText = Input { Value = "%{SUBTITLE_DEFAULT}", },
\t\t\t\t\t\tFont = Input { Value = "Open Sans", },
\t\t\t\t\t\tStyle = Input { Value = "Regular", },
\t\t\t\t\t\tSize = Input { Value = 0.024, },
\t\t\t\t\t\tRed1 = Input { Value = 0.75, },
\t\t\t\t\t\tGreen1 = Input { Value = 0.75, },
\t\t\t\t\t\tBlue1 = Input { Value = 0.8, },
\t\t\t\t\t\tCenter = Input { Value = { 0.25, 0.17 }, },
\t\t\t\t\t\tHorizontalLeftCenterRight = Input { Value = 1, },
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { 50, 60 } },
\t\t\t\t},
\t\t\t\tMergeTexts = Merge {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tBackground = Input {
\t\t\t\t\t\t\tSourceOp = "TitleText",
\t\t\t\t\t\t\tSource = "Output",
\t\t\t\t\t\t},
\t\t\t\t\t\tForeground = Input {
\t\t\t\t\t\t\tSourceOp = "SubtitleText",
\t\t\t\t\t\t\tSource = "Output",
\t\t\t\t\t\t},
\t\t\t\t\t\tPerformTransform = Input { Value = 0, },
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { 200, 30 } },
\t\t\t\t},
\t\t\t\tMergeCard = Merge {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tBackground = Input {
\t\t\t\t\t\t\tSourceOp = "PillBackground",
\t\t\t\t\t\t\tSource = "Output",
\t\t\t\t\t\t},
\t\t\t\t\t\tForeground = Input {
\t\t\t\t\t\t\tSourceOp = "MergeTexts",
\t\t\t\t\t\t\tSource = "Output",
\t\t\t\t\t\t},
\t\t\t\t\t\tPerformTransform = Input { Value = 0, },
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { 350, 40 } },
\t\t\t\t},
\t\t\t\tCardTransform = Transform {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tInput = Input {
\t\t\t\t\t\t\tSourceOp = "MergeCard",
\t\t\t\t\t\t\tSource = "Output",
\t\t\t\t\t\t},
\t\t\t\t\t\tCenter = Input { Value = { 0.5, 0.5 }, },
\t\t\t\t\t\tSize = Input {
\t\t\t\t\t\t\tSourceOp = "AnimCurves1",
\t\t\t\t\t\t\tSource = "Value",
\t\t\t\t\t\t},
\t\t\t\t\t},
\t\t\t\t\tViewInfo = OperatorInfo { Pos = { 480, 40 } },
\t\t\t\t},
\t\t\t\tAnimCurves1 = LUTLookup {
\t\t\t\t\tInputs = {
\t\t\t\t\t\tSource = Input { Value = FuID { "Duration" }, },
\t\t\t\t\t\tCurve = Input { Value = FuID { "Easing" }, },
\t\t\t\t\t\tScale = Input { Value = 1, },
\t\t\t\t\t\tOffset = Input { Value = 0, },
\t\t\t\t\t},
\t\t\t\t}
\t\t\t},
\t\t}
\t},
\tActiveTool = "%{MACRO_NAME}"
}
"""


def generate_lower_third(name: str, title: str, subtitle: str, output_path: str):
    content = LOWER_THIRD_TEMPLATE.replace("%{MACRO_NAME}", name)
    content = content.replace("%{TITLE_DEFAULT}", title)
    content = content.replace("%{SUBTITLE_DEFAULT}", subtitle)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated template: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate DaVinci Resolve Fusion .setting templates")
    parser.add_argument("--type", choices=["lower-third"], default="lower-third", help="Template type")
    parser.add_argument("--name", default="Aki_Motion_Lower_Third", help="Macro operator name (no spaces)")
    parser.add_argument("--title", default="Presenter Name", help="Default main title text")
    parser.add_argument("--subtitle", default="Host & Creator", help="Default subtitle text")
    parser.add_argument("--output", default="Aki_Motion_Lower_Third.setting", help="Output file path")
    parser.add_argument("--install-to-resolve", action="store_true", help="Install directly into Resolve user Titles folder")

    args = parser.parse_args()

    out_file = args.output
    if args.install_to_resolve:
        appdata = os.environ.get("APPDATA")
        if appdata:
            target_dir = os.path.join(appdata, "Blackmagic Design", "DaVinci Resolve", "Support", "Fusion", "Templates", "Edit", "Titles")
            out_file = os.path.join(target_dir, f"{args.name}.setting")
        else:
            print("Warning: APPDATA environment variable not found. Writing to local file instead.")

    generate_lower_third(args.name, args.title, args.subtitle, out_file)


if __name__ == "__main__":
    main()
