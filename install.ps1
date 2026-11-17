# Automated Installer for DaVinci Resolve Fusion AI Skill (Windows)
# Supports Claude Code and Google Antigravity

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Installing DaVinci Resolve Fusion Skill for AI Assistants" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$CurrentDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$SkillSource = Join-Path $CurrentDir "fusion-scripting"

if (-not (Test-Path $SkillSource)) {
    Write-Error "Source folder 'fusion-scripting' not found in $CurrentDir"
}

# 1. Install for Google Antigravity
$GeminiSkillsPath = Join-Path $HOME ".gemini\config\skills\fusion-scripting"
try {
    if (Test-Path (Join-Path $HOME ".gemini")) {
        New-Item -ItemType Directory -Path $GeminiSkillsPath -Force | Out-Null
        Copy-Item -Path "$SkillSource\*" -Destination $GeminiSkillsPath -Recurse -Force
        Write-Host "[OK] Installed for Google Antigravity: $GeminiSkillsPath" -ForegroundColor Green
    } else {
        Write-Host "[SKIP] Antigravity directory (~/.gemini) not detected." -ForegroundColor Yellow
    }
} catch {
    Write-Warning "Could not copy to Antigravity directory: $_"
}

# 2. Install for Claude Code
$ClaudeSkillsPath = Join-Path $HOME ".claude\skills\fusion-scripting"
try {
    if (Test-Path (Join-Path $HOME ".claude")) {
        New-Item -ItemType Directory -Path $ClaudeSkillsPath -Force | Out-Null
        Copy-Item -Path "$SkillSource\*" -Destination $ClaudeSkillsPath -Recurse -Force
        Write-Host "[OK] Installed for Claude Code: $ClaudeSkillsPath" -ForegroundColor Green
    } else {
        Write-Host "[SKIP] Claude directory (~/.claude) not detected." -ForegroundColor Yellow
    }
} catch {
    Write-Warning "Could not copy to Claude directory: $_"
}

Write-Host ""
Write-Host "Installation Complete! Claude Code and Antigravity can now use 'fusion-scripting'." -ForegroundColor Green
