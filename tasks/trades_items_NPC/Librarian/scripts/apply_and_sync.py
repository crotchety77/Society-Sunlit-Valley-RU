#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт применения и синхронизации локализации товаров Вероники (Librarian Trades).
"""

import os
import sys
import json
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets"

def main():
    print("🚀 Запуск синхронизации для Библиотекаря (Вероника)...")
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        subprocess.run(["node", sync_js], cwd=ROOT_DIR, check=True)
    print("✅ Синхронизация завершена успешно.")

if __name__ == "__main__":
    main()
