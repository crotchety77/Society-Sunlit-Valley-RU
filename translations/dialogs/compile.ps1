# PowerShell 5.1+ compiler
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$reviewDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $reviewDir) { $reviewDir = Get-Location }

$ruData = [ordered]@{}
$qaErrors = [System.Collections.Generic.List[string]]::new()

$files = Get-ChildItem -Path $reviewDir -Filter "*.md" | Where-Object { $_.Name -notmatch "^README" } | Sort-Object Name

$totalParsed = 0
$translatedCount = 0

foreach ($file in $files) {
    $lines = Get-Content -Path $file.FullName -Encoding UTF8
    $lineIdx = 0
    foreach ($line in $lines) {
        $lineIdx++
        $trimmed = $line.Trim()
        if ($trimmed.StartsWith('|') -and $trimmed.Contains('`dialog.npc.')) {
            $parts = $trimmed.Split('|')
            if ($parts.Count -ge 4) {
                $p1 = $parts[1].Trim()
                $ruVal = $parts[3].Trim()
                if ($p1 -match '`([^`]+)`') {
                    $key = $Matches[1]
                    $totalParsed++
                    
                    if ($ruVal.Length -gt 0) {
                        if ($ruVal -match '(?<!%)%(?!%)') {
                            $fname = $file.Name
                            $qaErrors.Add("[ERROR %] $fname (line $lineIdx): key '$key' has unescaped %. Use %%!")
                        }
                        $ruData[$key] = $ruVal
                        $translatedCount++
                    }
                }
            }
        }
    }
}

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "         SOCIETY DIALOG TRANSLATION COMPILER        " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "Total dialog lines found : $totalParsed"
Write-Host "Translated lines         : $translatedCount / $totalParsed"
Write-Host "----------------------------------------------------"

if ($qaErrors.Count -gt 0) {
    Write-Host "`n[WARNING] Formatting errors detected:" -ForegroundColor Red
    foreach ($err in $qaErrors) {
        Write-Host " $err" -ForegroundColor Yellow
    }
    Write-Host "----------------------------------------------------"
}

$outRuPath = Join-Path $reviewDir "ru_ru.json"
$jsonString = ConvertTo-Json $ruData -Depth 10
[System.IO.File]::WriteAllText($outRuPath, $jsonString, [System.Text.UTF8Encoding]::new($false))

Write-Host "Done! Saved ru_ru.json to:`n  $outRuPath" -ForegroundColor Green

$modpackPath = "D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\dialog\lang\ru_ru.json"
try {
    $modpackDir = [System.IO.Path]::GetDirectoryName($modpackPath)
    if ([System.IO.Directory]::Exists($modpackDir)) {
        [System.IO.File]::WriteAllText($modpackPath, $jsonString, [System.Text.UTF8Encoding]::new($false))
        Write-Host "`n[SYNC] Successfully copied to modpack:`n  $modpackPath" -ForegroundColor Magenta
        Write-Host "  (Press F3 + T in game to reload translations)" -ForegroundColor Gray
    }
} catch {
}

Write-Host "====================================================`n" -ForegroundColor Cyan
