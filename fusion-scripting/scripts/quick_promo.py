#!/usr/bin/env python3
"""
Turnkey 1-Minute Motion Graphics Generator for DaVinci Resolve Fusion
Generates a broadcast-quality, Title Safe, 30-second multi-scene text motion
graphic directly inside DaVinci Resolve Studio in under 5 seconds.
"""

import sys
import os
import time
import json

# Ensure scripts dir is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fusion_utils import get_resolve, create_fusion_timeline, create_motion_graphics_promo, validate_comp_sanity

DEFAULT_SCENES = [
    {
        "tag": "DAVINCI RESOLVE  •  CLAUDE  •  ANTIGRAVITY",
        "title": "FUSION AI SKILLS",
        "subtitle": "Flawless Node-Based Compositing with AI",
        "accent_color": (0.0, 0.88, 0.82)  # Cyan
    },
    {
        "tag": "BENEFIT 01  //  FLOW ARCHITECTURE",
        "title": "ZERO INVERTED MERGES",
        "subtitle": "Strict Input Contracts: Foreground, Background & Masks\nAutomated Routing Prevents Solid Black Screens",
        "accent_color": (0.98, 0.72, 0.15)  # Amber
    },
    {
        "tag": "BENEFIT 02  //  PROCEDURAL ANIMATION",
        "title": "SMART ANIMCURVES",
        "subtitle": "Duration-Independent Motion Graphics That Never Break\nAuto-Stretches Seamlessly When You Trim on Timeline",
        "accent_color": (0.15, 0.90, 0.45)  # Mint Green
    },
    {
        "tag": "BENEFIT 03  //  TEMPLATE EXPORT",
        "title": "1-CLICK .SETTING MACROS",
        "subtitle": "Build Reusable Edit Page Titles, Transitions & Generators",
        "cta": "github.com/akshaygawali15/davinci-fusion-skills",
        "accent_color": (0.40, 0.75, 1.0)  # Bright Blue
    }
]

def generate_promo(project=None, timeline_name="Fusion_AI_Promo_30s", scenes=None, duration_seconds=30.0):
    start_time = time.time()
    
    if project is None:
        resolve = get_resolve()
        if not resolve:
            raise RuntimeError("Cannot connect to DaVinci Resolve. Please ensure DaVinci Resolve Studio is running.")
        project_mgr = resolve.GetProjectManager()
        project = project_mgr.GetCurrentProject()
        if not project:
            raise RuntimeError("No project is currently open in DaVinci Resolve.")
    else:
        resolve = get_resolve()

    if scenes is None:
        scenes = DEFAULT_SCENES

    print(f"[1/3] Setting up timeline '{timeline_name}' ({duration_seconds}s @ 24fps)...")
    timeline, comp = create_fusion_timeline(project, timeline_name, duration_seconds=duration_seconds, fps=24)

    print(f"[2/3] Constructing {len(scenes)}-scene text motion graphic with Title Safe typography...")
    total_frames = int(duration_seconds * 24)
    promo_result = create_motion_graphics_promo(comp, scenes, duration_frames=total_frames)

    print("[3/3] Running zero-defect Title Safe & node health validation...")
    validation = validate_comp_sanity(comp, auto_fix=True)

    elapsed = time.time() - start_time
    print(f"\nSUCCESS! 30-second motion graphic generated and validated in {elapsed:.2f} seconds!")
    print(f"Status: {validation.get('status')} | Text Nodes: {validation.get('textNodesValidated')} | Fixes Applied: {len(validation.get('fixesApplied'))}")

    # Switch to Fusion page so user sees result immediately
    if resolve:
        resolve.OpenPage("fusion")

    return {
        "elapsedSeconds": elapsed,
        "timeline": timeline.GetName() if timeline else None,
        "promoResult": promo_result,
        "validation": validation
    }

if __name__ == "__main__":
    generate_promo()
