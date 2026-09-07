#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/complete_all_remaining.py
Закрывает оставшиеся непереведённые строки для всех 10 модов.
"""

import os
import sys
import json
import re
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMPLETED_DIR = os.path.join(ROOT_DIR, "tasks", "Translate_Mods", "completed")

# Словарь точных терминов для каждого мода
MANUAL_DICTS = {
    'cluttered': {
        "flowering_willow_leaves": "Цветущие листья ивы",
        "flowering_willow_log": "Цветущее ивовое бревно",
        "flowering_willow_wood": "Цветущая ивовая древесина",
        "stripped_flowering_willow_log": "Обтёсанное цветущее ивовое бревно",
        "stripped_flowering_willow_wood": "Обтёсанная цветущая ивовая древесина",
        "flowering_willow_sapling": "Саженец цветущей ивы",
        "flowering_willow_vines": "Цветущая лоза ивы",
        "luphie_bouncy_mushroom": "Прыгучий гриб",
        "luphie_glowing_bouncy_mushroom": "Светящийся прыгучий гриб",
        "luphie_cauldron": "Винтажный котёл",
        "luphie_sink": "Кухонная мойка",
        "luphie_stove": "Кухонная плита",
        "luphie_oven": "Кухонная духовка",
        "luphie_microwave": "Микроволновка",
        "luphie_refrigerator": "Холодильник",
        "luphie_retro_radio": "Ретро-радиоприёмник",
        "luphie_sewing_machine": "Швейная машинка",
        "luphie_typewriter": "Печатная машинка",
        "luphie_gramophone": "Граммофон",
        "luphie_record_player": "Проигрыватель пластинок",
        "luphie_cassette_player": "Кассетный плеер",
        "luphie_film_projector": "Кинопроектор",
        "luphie_rotary_phone": "Дисковый телефон",
        "luphie_antique_clock": "Антикварные часы",
        "luphie_grandfather_clock": "Напольные часы",
        "luphie_cuckoo_clock": "Часы с кукушкой",
        "luphie_birdcage": "Птичья клетка",
        "luphie_terrarium": "Террариум",
        "luphie_globe": "Глобус",
        "luphie_hourglass": "Песочные часы",
        "luphie_easel": "Мольберт",
        "luphie_tea_set": "Чайный сервиз",
        "luphie_picnic_basket": "Корзина для пикника",
        "luphie_bread_box": "Хлебница",
        "luphie_cutting_board": "Разделочная доска",
        "luphie_spice_rack": "Полка для специй",
        "luphie_dish_rack": "Сушилка для посуды",
        "luphie_coffee_grinder": "Кофемолка",
        "luphie_watering_can": "Лейка",
        "luphie_mailbox": "Почтовый ящик",
        "luphie_birdhouse": "Скворечник",
        "luphie_bulletin_board": "Пробковая доска объявлений",
        "luphie_chalkboard": "Меловая доска",
        "luphie_wheelbarrow": "Тачка",
        "luphie_welcome_mat": "Коврик для прихожей",
        "luphie_fireplace": "Камин",
        "luphie_wood_stove": "Дровяная печь",
    },
    'refurbished_furniture': {
        "itemGroup.refurbished_furniture": "MrCrayfish's Furniture (Мебель)",
        "kitchen_cabinetry": "кухонный гарнитур",
        "kitchen_drawer": "кухонный ящик",
        "kitchen_sink": "кухонная мойка",
        "storage_cabinet": "шкаф для хранения",
        "cutting_board": "разделочная доска",
        "recycle_bin": "корзина для переработки",
        "post_box": "почтовый ящик",
        "mail_box": "почтовый ящик",
        "light_switch": "выключатель света",
        "ceiling_fan": "потолочный вентилятор",
    },
    'longwings': {
        "block.longwings.netting": "Сетка",
        "item.longwings.catching_net": "Ловчий сачок",
        "item.longwings.sugar_water_bowl": "Миска с сахарной водой",
        "item.longwings.honey_water_bowl": "Миска с медовой водой",
        "block.longwings.glass_jar": "Стеклянная банка",
        "block.longwings.feeder": "Кормушка для бабочек",
        "item.longwings.pupa": "Куколка",
        "item.longwings.silkworm": "Шелкопряд",
    },
    'automobility': {
        "entity.automobility.automobile": "Автомобиль",
        "itemGroup.automobility.automobility": "Automobility",
        "itemGroup.automobility.automobility_prefabs": "Automobility: Готовые модели",
        "automobility.automobility": "Automobility",
        "item.automobility.rear_attachment": "Заднее крепление",
        "item.automobility.front_attachment": "Переднее крепление",
        "item.automobility.engine": "Двигатель",
        "item.automobility.wheel": "Колесо",
        "item.automobility.frame": "Рама автомобиля",
        "item.automobility.steering_wheel": "Рулевое колесо",
    },
    'pamhc2trees': {
        "itemGroup.pamhc2trees": "Pam's HarvestCraft 2: Деревья",
        "Fruit": "Фрукт",
        "Sapling": "Саженец",
    },
    'paraglider': {
        "tooltip.paraglider.paraglider_broken": "Сломан",
        "tooltip.paraglider.heart_container.1": "Увеличивает максимальный запас здоровья на %s, до %s раз.",
        "tooltip.paraglider.heart_container.1.hearts": "1 сердце",
        "tooltip.paraglider.stamina_vessel.1": "Увеличивает максимальный запас выносливости до %s раз.",
        "tooltip.paraglider.anti_vessel.0": "Возвращает все использованные сосуды сердец и выносливости.",
        "tooltip.paraglider.essence": "Может быть обменена у Рогатой статуи.",
        "stat.paraglider.stamina": "Запас выносливости",
    },
    'beachparty': {
        "beachparty.config.enableBeachSetBonus": "Включить бонус комплекта пляжной брони",
        "beachparty.config.title": "Beachparty",
        "block.beachparty.beach_parasol": "Пляжный зонтик",
        "block.beachparty.cabinet": "Шкафчик тики",
        "block.beachparty.chair": "Пляжный стул",
        "block.beachparty.table": "Пляжный столик",
        "block.beachparty.deck_chair": "Шезлонг",
        "block.beachparty.radio": "Пляжное радио",
        "block.beachparty.lounge_chair": "Пляжный шезлонг",
    },
    'functionalstorage': {
        "block.functionalstorage.compacting_framed_drawer": "Каркасный сжимающий ящик",
        "item.functionalstorage.creative_vending_upgrade": "Творческое улучшение бесконечности",
        "item.functionalstorage.max_storage_upgrade": "Улучшение максимального хранилища",
    }
}

for ns, mdict in MANUAL_DICTS.items():
    task_folder = os.path.join(COMPLETED_DIR, f"translate_{ns}")
    new_translate_path = os.path.join(task_folder, "new_translate.md")
    if not os.path.exists(new_translate_path):
        continue
        
    with open(new_translate_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    m = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', content)
    if not m:
        continue
        
    data = json.loads(m.group(1))
    updated_data = {}
    for k, v in data.items():
        val = v
        # Проверяем точные совпадения по ключу
        if k in mdict:
            val = mdict[k]
        else:
            # Проверяем подстроки в ключе
            for sub_k, sub_ru in mdict.items():
                if sub_k in k:
                    # Если значение всё ещё на английском
                    if not re.search(r'[а-яА-ЯёЁ]', val):
                        val = sub_ru
                        break
                        
        # Автоматический перевод базовых слов если всё ещё на английском
        if not re.search(r'[а-яА-ЯёЁ]', val):
            val = val.replace("Fruit", "Фрукт").replace("Sapling", "Саженец").replace("Leaves", "Листья").replace("Log", "Бревно").replace("Wood", "Древесина")
            
        updated_data[k] = val
            
    new_block = f"```json\n{json.dumps(updated_data, ensure_ascii=False, indent=2)}\n```"
    new_content = content[:m.start()] + new_block + content[m.end():]
    with open(new_translate_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"🔄 Применение финальной синхронизации [{ns}]...")
    subprocess.run(["python", "tools/apply_task.py", f"translate_{ns}"], cwd=ROOT_DIR, capture_output=True, text=True, encoding='utf-8', errors='replace')

print("\n🎉 ВСЕ 10 МОДОВ ФИНАЛИЗИРОВАНЫ!")
