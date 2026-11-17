#!/usr/bin/env python3
"""
DaVinci Resolve Fusion Automation & Utilities Library
Provides reliable, high-level helper functions for manipulating Fusion compositions,
node graphs, templates, and scripts in DaVinci Resolve Studio and Fusion Studio.
"""

import sys
import os
import json
from typing import Optional, Dict, Any, List, Tuple


def get_resolve():
    """
    Connects to the running DaVinci Resolve application instance.
    Works whether running from inside Resolve's console or as an external script.
    """
    try:
        import DaVinciResolveScript as dvr_script
        return dvr_script.scriptapp("Resolve")
    except ImportError:
        # Check standard environment variables
        resolve_script_api = os.environ.get("RESOLVE_SCRIPT_API")
        if resolve_script_api:
            modules_path = os.path.join(resolve_script_api, "Modules")
            if modules_path not in sys.path:
                sys.path.append(modules_path)
            try:
                import DaVinciResolveScript as dvr_script
                return dvr_script.scriptapp("Resolve")
            except ImportError:
                pass
    return None


def get_fusion(resolve=None):
    """
    Returns the Fusion scripting interface.
    """
    if resolve is None:
        resolve = get_resolve()
    if resolve:
        return resolve.Fusion()
    
    # Try direct fusion scriptapp
    try:
        import DaVinciResolveScript as dvr_script
        return dvr_script.scriptapp("Fusion")
    except Exception:
        return None


def get_current_comp(resolve=None, open_fusion_page: bool = True):
    """
    Retrieves the currently active Fusion composition.
    If open_fusion_page is True, switches to the Fusion page if not already there.
    """
    if resolve is None:
        resolve = get_resolve()
    
    if not resolve:
        return None

    if open_fusion_page:
        current_page = resolve.GetCurrentPage()
        if current_page != "fusion":
            resolve.OpenPage("fusion")

    fusion = resolve.Fusion()
    if fusion:
        comp = fusion.GetCurrentComp()
        if comp:
            return comp

    # Alternatively, inspect current timeline item
    proj_mgr = resolve.GetProjectManager()
    if proj_mgr:
        proj = proj_mgr.GetCurrentProject()
        if proj:
            timeline = proj.GetCurrentTimeline()
            if timeline:
                current_item = timeline.GetCurrentVideoItem()
                if current_item and current_item.GetFusionCompCount() > 0:
                    return current_item.GetFusionCompByIndex(1)

    return None


def add_tool(comp, tool_id: str, name: Optional[str] = None, x: float = 0.0, y: float = 0.0):
    """
    Adds a tool to the composition at the specified (x, y) flow coordinates
    and optionally renames it.
    """
    if not comp:
        raise ValueError("Composition object cannot be None")

    tool = comp.AddTool(tool_id, True, x, y)
    if tool and name:
        tool.SetAttrs({"TOOLS_Name": name})
    return tool


def connect_tools(target_tool, target_input_name: str, source_tool, source_output_name: str = "Output") -> bool:
    """
    Connects source_tool's output to target_tool's input.
    Handles both direct property assignment and ConnectInput method.
    """
    if not target_tool or not source_tool:
        return False

    try:
        # Method 1: ConnectInput
        output_obj = getattr(source_tool, source_output_name, None)
        if output_obj:
            res = target_tool.ConnectInput(target_input_name, output_obj)
            if res:
                return True

        # Method 2: Direct property assignment
        setattr(target_tool, target_input_name, output_obj or source_tool)
        return True
    except Exception as e:
        print(f"Warning: Failed to connect {source_tool.Name} -> {target_tool.Name}.{target_input_name}: {e}")
        return False


def set_tool_input(tool, input_name: str, value: Any, time: Optional[float] = None) -> bool:
    """
    Sets a tool input parameter with type coercion and error checking.
    """
    if not tool:
        return False

    try:
        if time is not None:
            tool.SetInput(input_name, value, time)
        else:
            setattr(tool, input_name, value)
        return True
    except Exception as e:
        print(f"Warning: Failed to set input {input_name} on {tool.Name}: {e}")
        return False


def ensure_media_out_connected(comp) -> bool:
    """
    Inspects the composition, finds MediaOut1, and if disconnected,
    locates the last upstream merge or effect node and connects it.
    Prevents black screen glitches in DaVinci Resolve Edit page!
    """
    if not comp:
        return False

    comp.StartUndo("Ensure MediaOut Connected")

    mout = comp.FindTool("MediaOut1")
    if not mout:
        mout = comp.AddTool("MediaOut", True, 5.0, 0.0)
        mout.SetAttrs({"TOOLS_Name": "MediaOut1"})

    # Check if mout already has an active input
    input_link = mout.FindMainInput(1)
    if input_link and input_link.GetConnectedOutput() is not None:
        comp.EndUndo(True)
        return True

    # Search for candidates to connect
    tool_list = comp.GetToolList(False)
    candidates = []
    for tool in tool_list.values():
        if tool.ID in ["Merge", "Transform", "DeltaKeyer", "MatteControl", "ColorCorrector", "TextPlus", "Background"]:
            if tool.Name != "MediaOut1":
                candidates.append(tool)

    if candidates:
        # Take the last added or rightmost node
        final_tool = candidates[-1]
        connect_tools(mout, "Input", final_tool, "Output")
        mout.SetAttrs({"TOOLB_Selected": True})
        comp.EndUndo(True)
        return True

    comp.EndUndo(True)
    return False


def build_text_lower_third(comp, title: str = "Title Here", subtitle: str = "Subtitle Here") -> Dict[str, Any]:
    """
    Procedurally creates a clean motion lower-third title card in the active comp.
    """
    if not comp:
        raise ValueError("Invalid composition")

    comp.StartUndo("Create Motion Lower Third")

    # 1. Dark pill background
    bg_pill = comp.AddTool("Background", True, -2.0, 1.0)
    bg_pill.SetAttrs({"TOOLS_Name": "Pill_Background"})
    bg_pill.TopLeftRed = 0.08
    bg_pill.TopLeftGreen = 0.08
    bg_pill.TopLeftBlue = 0.1
    bg_pill.TopLeftAlpha = 0.88

    # Mask for pill
    mask_pill = comp.AddTool("RectangleMask", True, -2.0, 0.0)
    mask_pill.SetAttrs({"TOOLS_Name": "Pill_Mask"})
    mask_pill.Center = [0.25, 0.2]
    mask_pill.Width = 0.35
    mask_pill.Height = 0.12
    mask_pill.CornerRadius = 0.3
    bg_pill.EffectMask = mask_pill.Output

    # 2. Main Title Text+
    title_text = comp.AddTool("TextPlus", True, 0.0, 0.5)
    title_text.SetAttrs({"TOOLS_Name": "Title_Text"})
    title_text.StyledText = title
    title_text.Font = "Open Sans"
    title_text.Style = "Bold"
    title_text.Size = 0.045
    title_text.Center = [0.25, 0.23]
    title_text.HorizontalLeftCenterRight = 1  # Center

    # 3. Subtitle Text+
    sub_text = comp.AddTool("TextPlus", True, 0.0, 1.5)
    sub_text.SetAttrs({"TOOLS_Name": "Subtitle_Text"})
    sub_text.StyledText = subtitle
    sub_text.Font = "Open Sans"
    sub_text.Style = "Regular"
    sub_text.Size = 0.026
    sub_text.Center = [0.25, 0.17]
    sub_text.Red1 = 0.75
    sub_text.Green1 = 0.75
    sub_text.Blue1 = 0.8
    sub_text.HorizontalLeftCenterRight = 1

    # 4. Merge text elements
    merge_texts = comp.AddTool("Merge", True, 1.5, 1.0)
    merge_texts.SetAttrs({"TOOLS_Name": "Merge_Texts"})
    merge_texts.Background = title_text.Output
    merge_texts.Foreground = sub_text.Output

    # 5. Merge text over pill
    merge_all = comp.AddTool("Merge", True, 3.0, 1.0)
    merge_all.SetAttrs({"TOOLS_Name": "Merge_Card"})
    merge_all.Background = bg_pill.Output
    merge_all.Foreground = merge_texts.Output

    # 6. Connect to MediaIn / MediaOut pipeline if present
    media_in = comp.FindTool("MediaIn1")
    media_out = comp.FindTool("MediaOut1")
    if not media_out:
        media_out = comp.AddTool("MediaOut", True, 5.0, 0.0)

    if media_in:
        final_merge = comp.AddTool("Merge", True, 4.0, 0.0)
        final_merge.SetAttrs({"TOOLS_Name": "Merge_Final"})
        final_merge.Background = media_in.Output
        final_merge.Foreground = merge_all.Output
        media_out.Input = final_merge.Output
    else:
        media_out.Input = merge_all.Output

    comp.EndUndo(True)
    return {
        "pill": bg_pill,
        "mask": mask_pill,
        "title": title_text,
        "subtitle": sub_text,
        "output": media_out
    }


def paste_setting_string(comp, setting_lua_string: str) -> bool:
    """
    Pastes a raw .setting Lua string or dictionary into the active composition.
    """
    if not comp:
        return False
    try:
        # If string, use comp.Paste()
        return comp.Paste(setting_lua_string)
    except Exception as e:
        print(f"Error pasting setting: {e}")
        return False


if __name__ == "__main__":
    print("DaVinci Resolve Fusion Utilities Library initialized.")
    res = get_resolve()
    if res:
        print(f"Connected to DaVinci Resolve (Current page: {res.GetCurrentPage()})")
    else:
        print("DaVinci Resolve is not currently running. Offline helper functions ready.")
