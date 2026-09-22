@echo off
chcp 65001 >nul
echo ========================================================
echo   [PC] POKEMON PC EXCEL CATALOG GENERATOR
echo ========================================================
echo.

set "GAME_JSON=G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\my_cobblemon_pc.json"
set "DOCS_JSON=%~dp0docs\my_cobblemon_pc.json"
set "SCRIPT_PY=%~dp0scripts\export_pokemon_pc_to_excel.py"
set "EXCEL_FILE=%~dp0docs\Cobblemon_PC_Catalog.xlsx"
set "EXCEL_UPDATED=%~dp0docs\Cobblemon_PC_Catalog_updated.xlsx"

if exist "%GAME_JSON%" (
    echo [1/3] Copying fresh PC dump from game folder...
    copy /Y "%GAME_JSON%" "%DOCS_JSON%" >nul
) else (
    echo [!] Game JSON dump not found, using cached docs file...
)

echo [2/3] Generating Excel table with stats, moves, IV colors...
python "%SCRIPT_PY%"

echo.
echo [3/3] Opening table in Excel...
if exist "%EXCEL_UPDATED%" (
    start "" "%EXCEL_UPDATED%"
) else if exist "%EXCEL_FILE%" (
    start "" "%EXCEL_FILE%"
)

echo.
echo [OK] Done!
ping 127.0.0.1 -n 4 >nul
