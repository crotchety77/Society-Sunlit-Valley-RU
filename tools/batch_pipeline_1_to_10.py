#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/batch_pipeline_1_to_10.py
Скрипт конвейера для обработки первых 10 модов из tasks/Translate_Mods/QUEUE.md
согласно навыку process_mod_pipeline:
01_cluttered, 02_refurbished_furniture, 03_dramaticdoors, 04_simplehats, 05_longwings,
06_automobility, 07_pamhc2trees, 08_paraglider, 09_beachparty, 10_functionalstorage.
"""

import os
import sys
import json
import zipfile
import re
import glob
import subprocess
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASKS_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods")
COMPLETED_DIR = os.path.join(TASKS_DIR, "completed")
os.makedirs(COMPLETED_DIR, exist_ok=True)

from tools.analyze_untranslated_mods import parse_relaxed_json

# Загружаем глоссарий для соблюдения единообразия
GLOSSARY_PATH = os.path.join(ROOT_DIR, "glossary.md")

print("==================================================")
print("🚀 ЗАПУСК КОНВЕЙЕРА ОБРАБОТКИ 10 МОДОВ (process_mod_pipeline)")
print("==================================================")

MODS_TO_PROCESS = [
    ("01_cluttered", "cluttered"),
    ("02_refurbished_furniture", "refurbished_furniture"),
    ("03_dramaticdoors", "dramaticdoors"),
    ("04_simplehats", "simplehats"),
    ("05_longwings", "longwings"),
    ("06_automobility", "automobility"),
    ("07_pamhc2trees", "pamhc2trees"),
    ("08_paraglider", "paraglider"),
    ("09_beachparty", "beachparty"),
    ("10_functionalstorage", "functionalstorage"),
]

print(f"Всего модов в пакете: {len(MODS_TO_PROCESS)}")
