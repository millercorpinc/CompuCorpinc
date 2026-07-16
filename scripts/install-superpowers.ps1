param(
    [string]$Ref = "main"
)

$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Vendor = Join-Path $Root ".vendor/superpowers"
$Target = Join-Path $Root ".agents/skills"
$Manifest = Join-Path $Target ".superpowers-installed.txt"
$Version = Join-Path $Target ".superpowers-version"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "git is required"
}

New-Item -ItemType Directory -Force -Path (Join-Path $Root ".vendor") | Out-Null
New-Item -ItemType Directory -Force -Path $Target | Out-Null

if (-not (Test-Path (Join-Path $Vendor ".git"))) {
    git clone https://github.com/obra/superpowers.git $Vendor
} else {
    git -C $Vendor fetch --all --tags --prune
}

git -C $Vendor checkout --force $Ref
if ($Ref -eq "main") {
    git -C $Vendor pull --ff-only origin main
}

if (Test-Path $Manifest) {
    Get-Content $Manifest | ForEach-Object {
        $Skill = $_.Trim()
        if ($Skill -and -not $Skill.StartsWith("company-")) {
            $OldPath = Join-Path $Target $Skill
            if (Test-Path $OldPath) {
                Remove-Item -Recurse -Force $OldPath
            }
        }
    }
}

$Installed = @()
Get-ChildItem (Join-Path $Vendor "skills") -Directory | ForEach-Object {
    $Skill = $_.Name
    if ($Skill.StartsWith("company-")) {
        throw "Upstream skill uses reserved company- prefix: $Skill"
    }

    $Destination = Join-Path $Target $Skill
    if (Test-Path $Destination) {
        Remove-Item -Recurse -Force $Destination
    }
    Copy-Item -Recurse -Force $_.FullName $Destination
    $Installed += $Skill
}

$Installed | Set-Content -Encoding UTF8 $Manifest
$Commit = (git -C $Vendor rev-parse HEAD).Trim()
$Commit | Set-Content -Encoding UTF8 $Version

$License = Join-Path $Vendor "LICENSE"
if (Test-Path $License) {
    Copy-Item -Force $License (Join-Path $Target "SUPERPOWERS-LICENSE")
}

Write-Host "Installed Superpowers skills at commit $Commit"
Write-Host "Open Codex from the repository root and run /skills."
