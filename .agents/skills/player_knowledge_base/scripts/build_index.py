#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт автоматического сканирования каталога wiki/ и генерации/обновления
главной страницы wiki/README.md со сводной навигацией, бейджами и оглавлением.
"""

import os
import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parents[4]
WIKI_DIR = ROOT_DIR / "wiki"
CATEGORY_ICONS = {
    "farming": "🌱 Земледелие и агрономия",
    "husbandry": "🐾 Животноводство и питомцы",
    "fish_ponds": "🐟 Рыбные пруды и аквакультура",
    "villagers": "👥 Отношения с жителями",
    "skills": "⚔️ Профессии и Навыки",
    "seasons_and_weather": "🍂 Сезоны и Климат",
    "entomology": "🦋 Бабочки и Насекомые",
    "automation": "⚙️ Автоматизация и механизмы",
}

def extract_title(file_path):
    """Извлекает первый H1 заголовок из markdown файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    return file_path.stem.replace("_", " ").capitalize()

def main():
    if not WIKI_DIR.exists():
        WIKI_DIR.mkdir(parents=True, exist_ok=True)

    categories = {}
    total_articles = 0

    # Сканирование подпапок
    for item in sorted(WIKI_DIR.iterdir()):
        if item.is_dir() and item.name not in ["assets", ".git"]:
            cat_key = item.name
            articles = []
            for doc in sorted(item.glob("*.md")):
                if doc.name.lower() == "readme.md":
                    continue
                title = extract_title(doc)
                rel_path = doc.relative_to(WIKI_DIR).as_posix()
                articles.append({"title": title, "path": rel_path})
                total_articles += 1
            if articles or (item / "README.md").exists():
                categories[cat_key] = articles

    # Построение главной страницы
    readme_path = WIKI_DIR / "README.md"
    content = []
    content.append("# 📚 Society: Sunlit Valley — Игровая База Знаний (Wiki)")
    content.append("> Полное иллюстрированное руководство по скрытым механикам, фермерству, жителям и прогрессии в сборке.")
    content.append("")
    content.append(f"![Статус](https://img.shields.io/badge/Статус-Активно-success) ![Статей](https://img.shields.io/badge/Статей_в_базе-{total_articles}-blue) ![Версия](https://img.shields.io/badge/Minecraft-1.20.1_Forge-orange)")
    content.append("")
    content.append("---")
    content.append("")
    content.append("## 🗺️ Быстрая навигация по разделам")
    content.append("")

    for cat_key, articles in categories.items():
        cat_title = CATEGORY_ICONS.get(cat_key, f"📁 {cat_key.replace('_', ' ').capitalize()}")
        content.append(f"### {cat_title}")
        cat_readme = WIKI_DIR / cat_key / "README.md"
        if cat_readme.exists():
            content.append(f"[📖 Перейти в раздел `{cat_key}`]({cat_key}/README.md)\n")
        
        if articles:
            for art in articles:
                content.append(f"* 📄 [{art['title']}]({art['path']})")
        else:
            content.append("* *Раздел наполняется...*")
        content.append("")

    content.append("---")
    content.append("")
    content.append("## 💡 О проекте базы знаний")
    content.append("Все гайды в этом справочнике составлены на основе **прямого реверс-инжиниринга KubeJS-скриптов** и конфигураций сборки.")
    content.append("Здесь нет устаревших догадок — только точные игровые формулы, проверенные на практике и адаптированные для приятного чтения.")
    content.append("")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n")

    print(f"База знаний успешно синхронизирована: {total_articles} статей в {len(categories)} разделах.")

if __name__ == "__main__":
    main()
