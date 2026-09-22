@echo off
chcp 65001 >nul
echo ========================================================
echo   💿 ОБНОВЛЕНИЕ КАТАЛОГА ТМ / TR ДИСКОВ COBBLEMON 💿
echo ========================================================
echo.

set "GAME_JSON=G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\my_tms_inventory.json"
set "DOCS_JSON=%~dp0docs\my_tms_inventory.json"
set "SCRIPT_PY=%~dp0scripts\export_tms_to_excel.py"
set "EXCEL_FILE=%~dp0docs\Cobblemon_TM_TR_Inventory.xlsx"

if exist "%GAME_JSON%" (
    echo [1/3] Копирование свежего дампа бочек из игры...
    copy /Y "%GAME_JSON%" "%DOCS_JSON%" >nul
) else (
    echo [!] Файл в папке игры не найден, используется локальный дамп...
)

echo [2/3] Генерация Excel таблицы с типами и переводами...
python "%SCRIPT_PY%"

echo.
echo [3/3] Открытие таблицы в Excel...
if exist "%EXCEL_FILE%" (
    start "" "%EXCEL_FILE%"
)

echo.
echo ✔ Готово!
timeout /t 3 >nul
