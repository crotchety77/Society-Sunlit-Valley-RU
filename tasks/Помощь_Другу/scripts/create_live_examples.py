import os
import json
import shutil
from pathlib import Path

base_path = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]")

print("=== НАЧАЛО СОЗДАНИЯ ПРИМЕРОВ ПЕРЕВОДА ДЛЯ СБОРКИ ===")

# =========================================================================
# 1. ПРИМЕР ДЛЯ КАТЕГОРИИ 1: FTB Quests (.snbt)
# =========================================================================
quest_file = base_path / "config" / "ftbquests" / "quests" / "chapters" / "age_of_dragons.snbt"
backup_file = quest_file.with_suffix(".snbt.bak")

if quest_file.exists():
    if not backup_file.exists():
        shutil.copy2(quest_file, backup_file)
        print(f"[1. FTB Quests] Создан бэкап: {backup_file.name}")
    
    text = quest_file.read_text(encoding="utf-8")
    
    # Заменяем описание первого квеста на красивый русский перевод
    old_block = '''			description: [
				"&9Knowlwedge &fkeeps you alive."
				""
				"&aA Bestiary &fcontains information about most of the &1magical &fcreatures you may encounter possibly granting you a combat advantage."
				""
				"&2The manuscripts &fyou will need can be found within chests in caves , dragon roosts or graveyards."
			]
			id: "4B4BF1FF89C31ACA"
			rewards: [
				{
					count: 3
					id: "7299F62876C24CA1"
					item: "cisco_mod:champion_coin"
					type: "item"
				}
				{
					id: "36DFA7C739CDBDD9"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			subtitle: "Prudent Preparation"'''

    new_block = '''			description: [
				"&9Знания &fсохраняют жизнь."
				""
				"&aБестиарий &fсодержит сведения о большинстве &1магических существ&f, с которыми вы можете столкнуться, давая вам преимущество в бою."
				""
				"&2Рукописи&f, необходимые для его заполнения, можно найти в сундуках в пещерах, логовах драконов или на кладбищах."
			]
			id: "4B4BF1FF89C31ACA"
			rewards: [
				{
					count: 3
					id: "7299F62876C24CA1"
					item: "cisco_mod:champion_coin"
					type: "item"
				}
				{
					id: "36DFA7C739CDBDD9"
					type: "xp_levels"
					xp_levels: 5
				}
			]
			subtitle: "Разумная подготовка"'''

    if old_block in text:
        text = text.replace(old_block, new_block)
        quest_file.write_text(text, encoding="utf-8")
        print(f"[1. FTB Quests] Успешно переведён первый квест в '{quest_file.name}'!")
    elif new_block in text:
        print(f"[1. FTB Quests] Квест уже был переведён ранее.")
    else:
        print(f"[1. FTB Quests] Предупреждение: сигнатура квеста не найдена.")


# =========================================================================
# 2. ПРИМЕР ДЛЯ КАТЕГОРИИ 2: Происхождения (Medieval Origins)
# =========================================================================
med_origins_dir = base_path / "kubejs" / "assets" / "medievalorigins" / "lang"
med_origins_dir.mkdir(parents=True, exist_ok=True)
med_origins_file = med_origins_dir / "ru_ru.json"

med_origins_data = {
    "origin.medievalorigins.alfiq.name": "Альфик",
    "origin.medievalorigins.alfiq.description": "-§lОсновные особенности§r:\n§o§2+ Бонус без оружия§r\n§o§2+ Уникальное перемещение§r\n§o§6• Плотоядный§r\n§o§c- Защита§r\n\n§lАльфики§r — хитрая раса антропоморфных кошачьих с острыми когтями и превосходной ловкостью.",
    "origin.medievalorigins.arachnae.name": "Арахна",
    "origin.medievalorigins.arachnae.description": "-§lОсновные особенности§r:\n§o§2+ Яд и контроль толпы\n+ Лазание по стенам§r\n§o§6• Плотоядная§r\n§o§c- Голод и броня§r\n\nПричудливое слияние паука и человека с ядовитыми клыками и цепкими лапами."
}
med_origins_file.write_text(json.dumps(med_origins_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[2. Origins/Расы] Создан пример перевода: {med_origins_file.relative_to(base_path)}")


# =========================================================================
# 3. ПРИМЕР ДЛЯ КАТЕГОРИИ 3: Классы (Origins Classes)
# =========================================================================
classes_dir = base_path / "kubejs" / "assets" / "origins-classes" / "lang"
classes_dir.mkdir(parents=True, exist_ok=True)
classes_file = classes_dir / "ru_ru.json"

classes_data = {
    "layer.origins-classes.class.name": "Класс",
    "layer.origins-classes.class.missing_origin.name": "Без класса",
    "layer.origins-classes.class.missing_origin.description": "У вас пока не выбран класс персонажа."
}
classes_file.write_text(json.dumps(classes_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[3. Классы] Создан пример перевода: {classes_file.relative_to(base_path)}")


# =========================================================================
# 4. ПРИМЕР ДЛЯ КАТЕГОРИИ 4: Древо Пассивных Навыков (Passive Skill Tree)
# =========================================================================
skill_dir = base_path / "kubejs" / "assets" / "skilltree" / "lang"
skill_dir.mkdir(parents=True, exist_ok=True)
skill_file = skill_dir / "ru_ru.json"

skill_data = {
    "affix.skilltree:jewelry/attribute/experienced": "Опытный",
    "affix.skilltree:jewelry/attribute/experienced.suffix": "Опыта",
    "affix.skilltree:jewelry/attribute/hasty": "Стремительный",
    "affix.skilltree:jewelry/attribute/hasty.suffix": "Спешки",
    "affix.skilltree:jewelry/attribute/healthy": "Здоровый",
    "affix.skilltree:jewelry/attribute/healthy.suffix": "Здоровья"
}
skill_file.write_text(json.dumps(skill_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[4. Навыки] Создан пример перевода: {skill_file.relative_to(base_path)}")


# =========================================================================
# 5. ПРИМЕР ДЛЯ КАТЕГОРИИ 5: Моды без перевода (Mowzie's Cataclysm)
# =========================================================================
mowzie_dir = base_path / "kubejs" / "assets" / "mowzies_cataclysm" / "lang"
mowzie_dir.mkdir(parents=True, exist_ok=True)
mowzie_file = mowzie_dir / "ru_ru.json"

mowzie_data = {
    "item.mowzies_cataclysm.wrought_eye": "Око Кованого рыцаря",
    "item.mowzies_cataclysm.sun_eye": "Око Солнечной птицы",
    "item.mowzies_cataclysm.frostmaw_eye": "Око Ледяной пасти"
}
mowzie_file.write_text(json.dumps(mowzie_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[5. Предметы модов] Создан пример перевода: {mowzie_file.relative_to(base_path)}")


# =========================================================================
# 6. ПРИМЕР ДЛЯ КАТЕГОРИИ 6: KubeJS Client Scripts (Подсказки)
# =========================================================================
client_scripts_dir = base_path / "kubejs" / "client_scripts"
client_scripts_dir.mkdir(parents=True, exist_ok=True)
tooltip_file = client_scripts_dir / "example_custom_tooltips.js"

tooltip_code = '''// Пример кастомного описания для предмета через KubeJS
ItemEvents.tooltip(event => {
    // Добавляем красивую золотую подсказку к монете чемпиона
    event.add('cisco_mod:champion_coin', [
        Text.gold('★ Награда Чемпиона ★'),
        Text.gray('Используется для торговли с особыми торговцами и выполнения эпических квестов.')
    ])
})
'''
tooltip_file.write_text(tooltip_code, encoding="utf-8")
print(f"[6. KubeJS Tooltips] Создан скрипт подсказок: {tooltip_file.relative_to(base_path)}")

print("\n=== ВСЕ 6 ПРИМЕРОВ УСПЕШНО ВНЕДРЕНЫ В СБОРКУ! ===")
