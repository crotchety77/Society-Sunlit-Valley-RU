#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Комплексная замена терминов 'Слизень' -> 'Слайм' по сборке:
1. Мод splendid_slimes (блоки, инкубатор, кормушка, загон, сердца)
2. FTB Quests (Инкубация слаймов, квесты похищения, счастья, пресса, рецепты сердец)
3. Книги навыков Puffish Skills и Society
4. Синхронизация и прямая верификация физических файлов игры.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NEW_TRANSLATE_MD = os.path.join(TASK_DIR, "new_translate.md")
QUESTS_TRANSLATE_MD = os.path.join(TASK_DIR, "quests_translate.md")

# Файлы проекта
SPLENDID_JSON = os.path.join(ROOT_DIR, "translations", "mods", "splendid_slimes.json")
FTB_RU_JSON = os.path.join(ROOT_DIR, "translations", "ftbquests", "ru_ru.json")
SOCIETY_RU_JSON = os.path.join(ROOT_DIR, "translations", "society", "ru_ru.json")
SKILLS_RU_JSON = os.path.join(ROOT_DIR, "translations", "skills", "ru_ru.json")

# Файлы игры
GAME_SPLENDID = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\splendid_slimes\lang\ru_ru.json"
GAME_FTB = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json"
GAME_SOCIETY = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society\lang\ru_ru.json"
GAME_SKILLS = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_skills\lang\ru_ru.json"

def update_splendid():
    print("--- 1. Обновление splendid_slimes ---")
    with open(SPLENDID_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["block.splendid_slimes.corral_block"] = "Блок загона для слаймов"
    data["block.splendid_slimes.slime_feeder"] = "Кормушка для слаймов"
    data["block.splendid_slimes.slime_incubator"] = "Инкубатор слаймов"
    data["item.splendid_slimes.default_heart"] = "Сердце слайма"
    data["info.splendid_slimes.slime_heart"] = "Поместите в инкубатор для выведения слайма"
    data["item.splendid_slimes.slime_heart"] = "Сердце слайма: %s"

    with open(SPLENDID_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ translations/mods/splendid_slimes.json обновлен.")

def update_ftbquests():
    print("--- 2. Обновление FTB Quests ---")
    with open(FTB_RU_JSON, "r", encoding="utf-8") as f:
        ftb = json.load(f)

    # 1. Инкубация слаймов (iii__advanced_farming)
    ftb["ftbquests.chapter.iii__advanced_farming.quest139B02AFBCBBF350.title"] = "Инкубация слаймов"
    ftb["ftbquests.chapter.iii__advanced_farming.quest139B02AFBCBBF350.description1"] = "Во время странствий вы могли наткнуться на &6Сердце слайма&r. Это ценный предмет, который можно использовать для инкубации слаймов!"
    ftb["ftbquests.chapter.iii__advanced_farming.quest139B02AFBCBBF350.description2"] = "Для начала нажмите ПКМ по &6Инкубатору слаймов&r с сердцем в руке."

    # 2. Инкубация слаймов (iv__prismatic_farming)
    ftb["ftbquests.chapter.iv__prismatic_farming.quest62CB7BAB9BBB4030.title"] = "Инкубация слаймов"
    ftb["ftbquests.chapter.iv__prismatic_farming.quest62CB7BAB9BBB4030.description1"] = "Во время странствий вы могли наткнуться на &6Сердце слайма&r. Это ценный предмет, который можно использовать для инкубации слаймов!"
    ftb["ftbquests.chapter.iv__prismatic_farming.quest62CB7BAB9BBB4030.description2"] = "Для начала нажмите ПКМ по &6Инкубатору слаймов&r с сердцем в руке."

    # 3. Пресс плортов (iv__prismatic_farming)
    ftb["ftbquests.chapter.iv__prismatic_farming.quest4ABFC024D15BFC10.description1"] = "Слаймы не размножаются обычным скрещиванием. Вместо этого их &6Плорты&r спрессовываются в новое &6Сердце слайма&r с помощью &6Пресса плортов&r."

    # 4. Кормушка для слаймов (iii__advanced_farming)
    ftb["ftbquests.chapter.iii__advanced_farming.quest54E81642A0E67042.title"] = "Кормушка для слаймов"
    ftb["ftbquests.chapter.iii__advanced_farming.quest54E81642A0E67042.description1"] = "&6Кормушка для слаймов&r автоматически кормит слаймов в загоне подходящей едой."
    ftb["ftbquests.chapter.iii__advanced_farming.quest54E81642A0E67042.description2"] = "Это можно сделать более удобным способом с помощью &6Кормушки для слаймов&r, которая кормит ближайших слаймов едой из их рациона."

    # 5. Похищение слаймов (iii__advanced_farming)
    ftb["ftbquests.chapter.iii__advanced_farming.quest5C9C7A5A88613109.title"] = "Похищение слаймов"
    ftb["ftbquests.chapter.iii__advanced_farming.quest5C9C7A5A88613109.description1"] = "Слаймов можно найти по всему миру. С помощью вакуумного сборщика их можно засосать в инвентарь, нажав &6Shift + ПКМ&r."
    ftb["ftbquests.chapter.iii__advanced_farming.quest5C9C7A5A88613109.description2"] = "Затем вы можете выстрелить ими, нажав ПКМ, если слайм в банке находится в другой руке. Вы также можете засасывать и выстреливать предметы!"
    ftb["ftbquests.chapter.iii__advanced_farming.quest5C9C7A5A88613109.description3"] = "&oЕсли вы посмотрите рецепт в JEI, используя иконку слайма, вы можете найти подсказки о том, где могут прятаться некоторые виды.&r"

    # 6. Блоки загона (iii__advanced_farming)
    ftb["ftbquests.chapter.iii__advanced_farming.quest648FD0A599A54A0F.description1"] = "&6Блоки загона&r в основном защищают ваших слаймов, удерживая их внутри, но позволяя всему остальному входить и выходить."
    ftb["ftbquests.chapter.iii__advanced_farming.quest648FD0A599A54A0F.description2"] = "При подаче редстоун-сигнала они также не позволят выходить мобам, не являющимся слаймами."

    # 7. Анализатор слаймов (iii__advanced_farming)
    ftb["ftbquests.chapter.iii__advanced_farming.quest66C1440EFF12DC66.description1"] = "Разведение слаймов может быть непростым! У всех них разные мечты и желания, и одно неверное движение может заставить их разрушить вашу ферму..."
    ftb["ftbquests.chapter.iii__advanced_farming.quest66C1440EFF12DC66.description2"] = "К счастью, &6Анализатор слаймов&r здесь, чтобы помочь! Нажав им ПКМ по слайму, вы узнаете, мешает ли что-нибудь их счастью и вашей прибыли!"

    # 8. Счастье слаймов (iii__advanced_farming)
    ftb["ftbquests.chapter.iii__advanced_farming.quest7A551F04BB9A117.title"] = "Счастье слаймов"
    ftb["ftbquests.chapter.iii__advanced_farming.quest7A551F04BB9A117.task.4037539672589303441.title"] = "Я буду заботиться о слаймах"
    ftb["ftbquests.chapter.iii__advanced_farming.quest7A551F04BB9A117.description1"] = "Счастье слаймов зависит от их голода и условий жизни. Каждый раз, когда они едят, их &6счастье&r увеличивается. Если они окружены слаймами того же типа, они становятся счастливее!"
    ftb["ftbquests.chapter.iii__advanced_farming.quest7A551F04BB9A117.description2"] = "Счастье уменьшается, когда слаймы голодны или находятся в тесноте (более &67&r в одной области)."
    ftb["ftbquests.chapter.iii__advanced_farming.quest7A551F04BB9A117.description3"] = "Когда слаймы несчастны, они могут накладывать статусные эффекты на окружение. Чем ценнее их плорты, тем смертоноснее они могут быть..."

    # 9. Субтитры создаваемых сердец слаймов (slimes)
    heart_quests = [
        "quest1254F6F99ABB36D5", "quest321F14C492AF6793", "quest365B720FB6A9BCF3",
        "quest376A606EF1F9E850", "quest3A108FB6BA7E60D6", "quest610689180666C83A"
    ]
    for q in heart_quests:
        k = f"ftbquests.chapter.slimes.{q}.subtitle"
        if k in ftb:
            ftb[k] = "Создаваемое сердце слайма"

    with open(FTB_RU_JSON, "w", encoding="utf-8") as f:
        json.dump(ftb, f, ensure_ascii=False, indent=2)
    print(f"✅ translations/ftbquests/ru_ru.json обновлен.")

def update_society_and_skills():
    print("--- 3. Обновление Society & Skills ---")
    # Skills
    with open(SKILLS_RU_JSON, "r", encoding="utf-8") as f:
        skills = json.load(f)
    book_desc = ("§7Инкубация Сердца слайма может выдать Слизневый билет.\n"
                 "После получения книги шанс выпадения Слизневого билета также составляет (§715.0%).§8\n\n"
                 "§8Основной способ получения: инкубация Сердца слайма в Инкубаторе слаймов (§715.0%§8).\n\n"
                 "§8Другие способы: §7Призовой автомат§8 (шанс §71/23§8 в категории «Тип приза: Книга»).\n"
                 "Книжная ярмарка в конце любого сезона (§624 576 §e●§8).\n"
                 "Обмен у Странствующего торговца (§620 480 §e●§8).§r")
    skills["society_skills.books.slime_contain_protect.description"] = book_desc
    with open(SKILLS_RU_JSON, "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)

    # Society
    with open(SOCIETY_RU_JSON, "r", encoding="utf-8") as f:
        soc = json.load(f)
    soc["item.society.slime_contain_protect.description"] = book_desc
    soc["tooltip.society.slime_ticket"] = "Используйте на слайме, чтобы узнать его любимую еду."
    soc["tooltip.society.slime_feeder"] = "Автоматически кормит ближайших слаймов. Учитывает сложные черты характера."
    soc["society.trofers.slimes"] = "Трофей коллекции слаймов"
    soc["society.slime_ticket.favorite.item"] = "Любимая еда слайма (%s) :pink_heart:"
    soc["society.slime_ticket.favorite.entity"] = "Любимая добыча слайма (%s) :pink_heart:"
    with open(SOCIETY_RU_JSON, "w", encoding="utf-8") as f:
        json.dump(soc, f, ensure_ascii=False, indent=2)
    print("✅ translations/society/ru_ru.json и skills/ru_ru.json обновлены.")

def update_markdown_docs():
    print("--- 4. Обновление new_translate.md и quests_translate.md ---")
    with open(NEW_TRANSLATE_MD, "r", encoding="utf-8") as f:
        nt = f.read()

    nt = nt.replace("Инкубатор слизней", "Инкубатор слаймов")
    nt = nt.replace("Кормушка для слизней", "Кормушка для слаймов")
    nt = nt.replace("Блок загона для слизней", "Блок загона для слаймов")
    nt = nt.replace("выстрел слизнями", "выстрел слаймами")
    nt = nt.replace("Виды слизней", "Виды слаймов")
    nt = nt.replace("Информация о слизнях", "Информация о слаймах")
    nt = nt.replace("Черты слизней", "Черты слаймов")
    nt = nt.replace("Инкубация слизней", "Инкубация слаймов")

    with open(NEW_TRANSLATE_MD, "w", encoding="utf-8") as f:
        f.write(nt)

    if os.path.exists(QUESTS_TRANSLATE_MD):
        with open(QUESTS_TRANSLATE_MD, "r", encoding="utf-8") as f:
            qt = f.read()
        qt = qt.replace("Инкубация слизней", "Инкубация слаймов")
        qt = qt.replace("инкубатору слизней", "Инкубатору слаймов")
        qt = qt.replace("инкубатор слизней", "Инкубатор слаймов")
        qt = qt.replace("Кормушка для слизней", "Кормушка для слаймов")
        qt = qt.replace("сердце слизня", "сердце слайма")
        qt = qt.replace("Сердце слизня", "Сердце слайма")
        qt = qt.replace("Похищение слизней", "Похищение слаймов")
        qt = qt.replace("Счастье слизней", "Счастье слаймов")
        with open(QUESTS_TRANSLATE_MD, "w", encoding="utf-8") as f:
            f.write(qt)
    print("✅ new_translate.md и quests_translate.md обновлены.")

def sync_and_verify():
    print("--- 5. Синхронизация с игрой ---")
    sync_js = os.path.join(ROOT_DIR, "sync_all_to_game.js")
    if os.path.exists(sync_js):
        res = subprocess.run(["node", sync_js], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8')
        print(f"🔄 Результат sync_all_to_game.js:\n{res.stdout}")

    print("\n🔍 ОБЯЗАТЕЛЬНАЯ ВЕРИФИКАЦИЯ ФАЙЛОВ ИГРЫ:")

    print("\n[Splendid Slimes (assets/splendid_slimes/lang/ru_ru.json)]:")
    with open(GAME_SPLENDID, "r", encoding="utf-8") as f:
        sp_v = json.load(f)
    for k in ["block.splendid_slimes.slime_feeder", "block.splendid_slimes.slime_incubator", "block.splendid_slimes.corral_block", "item.splendid_slimes.default_heart", "info.splendid_slimes.slime_heart"]:
        print(f"   ▪ [{k}]: {sp_v.get(k)}")

    print("\n[FTB Quests (assets/ftbquestlocalizer/lang/ru_ru.json)]:")
    with open(GAME_FTB, "r", encoding="utf-8") as f:
        ftb_v = json.load(f)
    ftb_keys = [
        "ftbquests.chapter.iii__advanced_farming.quest139B02AFBCBBF350.title",
        "ftbquests.chapter.iii__advanced_farming.quest139B02AFBCBBF350.description1",
        "ftbquests.chapter.iii__advanced_farming.quest139B02AFBCBBF350.description2",
        "ftbquests.chapter.iv__prismatic_farming.quest62CB7BAB9BBB4030.title",
        "ftbquests.chapter.iv__prismatic_farming.quest4ABFC024D15BFC10.description1",
        "ftbquests.chapter.iii__advanced_farming.quest54E81642A0E67042.title",
        "ftbquests.chapter.iii__advanced_farming.quest5C9C7A5A88613109.title",
        "ftbquests.chapter.iii__advanced_farming.quest7A551F04BB9A117.title",
        "ftbquests.chapter.slimes.quest1254F6F99ABB36D5.subtitle"
    ]
    for k in ftb_keys:
        print(f"   ▪ [{k}]: {ftb_v.get(k)}")

    print("\n[Society & Skills (assets/society/ and assets/society_skills/)]:")
    with open(GAME_SOCIETY, "r", encoding="utf-8") as f:
        soc_v = json.load(f)
    print(f"   ▪ [tooltip.society.slime_feeder]: {soc_v.get('tooltip.society.slime_feeder')}")
    print(f"   ▪ [tooltip.society.slime_ticket]: {soc_v.get('tooltip.society.slime_ticket')}")
    with open(GAME_SKILLS, "r", encoding="utf-8") as f:
        sk_v = json.load(f)
    print(f"   ▪ [society_skills.books.slime_contain_protect.description]:\n{sk_v.get('society_skills.books.slime_contain_protect.description')}")

if __name__ == "__main__":
    update_splendid()
    update_ftbquests()
    update_society_and_skills()
    update_markdown_docs()
    sync_and_verify()
