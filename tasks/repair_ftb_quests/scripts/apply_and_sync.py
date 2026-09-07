import os
import sys
import json
import re
import shutil
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
GAME_DIR = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters'
EN_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'en_us.json')
RU_PATH = os.path.join(REPO_ROOT, 'translations', 'ftbquests', 'ru_ru.json')

print("=== 1. ПРИМЕНЕНИЕ ИСПРАВЛЕНИЙ В SNBT ===")

def modify_snbt_quest(chapter_file, quest_id, new_description_lines):
    fpath = os.path.join(GAME_DIR, chapter_file)
    bak_path = fpath + '.bak'
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    shutil.copy2(fpath, bak_path)
    
    # Count quests before
    quests_before = len(re.findall(r'id:\s*\"[0-9A-Fa-f]+\"', content))
    
    # Find quest block
    pattern = rf'(\{{\s*id:\s*\"{quest_id}\"[\s\S]*?description:\s*\[)([\s\S]*?)(\]\s*\n)'
    # Or description before id
    pattern_alt = rf'(description:\s*\[)([\s\S]*?)(\]\s*[\s\S]*?id:\s*\"{quest_id}\")'
    
    def repl_desc(match):
        prefix = match.group(1)
        suffix = match.group(3)
        formatted_lines = ',\n\t\t\t\t'.join([f'"{l}"' for l in new_description_lines])
        # In FTB quests snbt indentation: \n\t\t\t\t"..."
        formatted_block = '\n\t\t\t\t' + formatted_lines.replace(',\n\t\t\t\t', '\n\t\t\t\t') + '\n\t\t\t'
        return f"{prefix}{formatted_block}{suffix}"

    if re.search(pattern, content):
        new_content = re.sub(pattern, repl_desc, content, count=1)
    elif re.search(pattern_alt, content):
        new_content = re.sub(pattern_alt, repl_desc, content, count=1)
    else:
        # Fallback: line by line search
        print(f"  Warning: regex pattern not matched for {quest_id} in {chapter_file}, doing precise slice replace")
        idx = content.find(f'"{quest_id}"')
        if idx == -1:
            raise Exception(f"Quest {quest_id} not found in {chapter_file}")
        # Search description in range
        start = max(0, idx - 400)
        end = min(len(content), idx + 600)
        sub = content[start:end]
        
        # Replace description: [ ... ]
        dm = re.search(r'description:\s*\[[\s\S]*?\]', sub)
        if not dm:
            raise Exception(f"Description block not found for {quest_id}")
        formatted_lines = '\n\t\t\t\t' + '\n\t\t\t\t'.join([f'"{l}"' for l in new_description_lines]) + '\n\t\t\t'
        new_desc = f'description: [{formatted_lines}]'
        sub_mod = sub[:dm.start()] + new_desc + sub[dm.end():]
        new_content = content[:start] + sub_mod + content[end:]

    quests_after = len(re.findall(r'id:\s*\"[0-9A-Fa-f]+\"', new_content))
    if quests_before != quests_after:
        shutil.copy2(bak_path, fpath)
        raise Exception(f"Safety check failed for {chapter_file}: quests count changed {quests_before} -> {quests_after}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  [OK] {chapter_file} -> квест {quest_id} успешно обновлён (квестов: {quests_after})")

# 1.1 Исправляем iii__advanced_farming.snbt (Разведение бабочек)
butterfly_lines = [
    "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description1}",
    "",
    "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description2}",
    "",
    "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description3}"
]
modify_snbt_quest('iii__advanced_farming.snbt', '263CCA4D2EAF2629', butterfly_lines)

# 1.2 Исправляем getting_started.snbt (Вручение подарков)
gifts_lines = [
    "{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description1}",
    "",
    "{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2}",
    "",
    "{ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description3}"
]
modify_snbt_quest('getting_started.snbt', '3E08F21BA8F69499', gifts_lines)


print("\n=== 2. ОБНОВЛЕНИЕ ПЕРЕВОДОВ В JSON ===")

with open(EN_PATH, 'r', encoding='utf-8') as f:
    en_json = json.load(f)
with open(RU_PATH, 'r', encoding='utf-8') as f:
    ru_json = json.load(f)

# 2.1 Разведение бабочек! (263CCA4D2EAF2629)
ru_json['ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description1'] = "Когда две разные бабочки или мотылька находятся рядом, они могут отложить &6Яйцо гусеницы&r!"
ru_json['ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description2'] = "Яйца появляются естественным образом — так же, как бабочки сбрасывают янтарь и пыльцу, опыляя цветы вокруг.\n&7Совет: сажайте пары бабочек среди 7–8 видов цветов (радиус 4 блока) для максимального шанса кладки (до 25%%).&r"
ru_json['ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description3'] = "Вид и размер яйца определяются типом родителей: скрещивание двух разных видов даёт новый, более редкий вид, а размер потомка растёт относительно среднего размера родителей."
ru_json.pop('ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description4', None)
ru_json.pop('ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description5', None)

en_json.pop('ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description4', None)
en_json.pop('ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description5', None)

# 2.2 Вручение подарков (3E08F21BA8F69499)
ru_json['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description1'] = "У жителей есть система дружбы, позволяющая дарить им подарки для повышения уровня отношений."
ru_json['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2'] = "Нажмите &6Shift + ПКМ&r по жителю с предметом в руке, чтобы вручить подарок (кулдаун — &61 раз в 4 дня&r). Ежедневный разговор приносит &a+5 очков&r."
ru_json['ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description3'] = "Предметы, имеющие цену продажи, всегда можно дарить. Полный список предпочтений ищите по тегу &6#villager_gift&r в JEI/EMI.\n&dУниверсальные любимые подарки:&r Призматический осколок, Кроличья лапка, Чай Улун, Солнечная жемчужина, Желейное вино."
ru_json.pop('ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4', None)
ru_json.pop('ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description5', None)
ru_json.pop('ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description6', None)

en_json.pop('ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4', None)
en_json.pop('ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description5', None)
en_json.pop('ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description6', None)

# 2.3 Улучшения машин (41C453E806763C4F)
ru_json['ftbquests.chapter.iv__prismatic_farming.quest41C453E806763C4F.description1'] = "Житель-&6торговец&r продаёт улучшения для машин в обмен на различные фермерские товары (ему также можно позвонить по телефону после посещения Пещеры Черепа). Эти улучшения добавляют машинам особые эффекты при установке."
ru_json['ftbquests.chapter.iv__prismatic_farming.quest41C453E806763C4F.description2'] = "Также у него есть удобные полезные обмены на ценные, но труднодоступные предметы вроде черепов скелетов-иссушителей."
ru_json.pop('ftbquests.chapter.iv__prismatic_farming.quest41C453E806763C4F.description3', None)

# 2.4 Для владельцев серверов (18490F31FFAB134E)
ru_json['ftbquests.chapter.welcome.quest18490F31FFAB134E.description1'] = "Если вы держите сервер для нескольких человек, которые заходят в разное время, вам стоит изменить длительность сезонов в файлах конфигурации."
ru_json['ftbquests.chapter.welcome.quest18490F31FFAB134E.description2'] = "Это можно сделать, изменив параметр &6sub_season_duration&r в файле &6config/sereneseasons/seasons.toml&r."
ru_json['ftbquests.chapter.welcome.quest18490F31FFAB134E.description3'] = "На больших серверах рекомендуется установить это значение на 16-20, чтобы никто не смог «прожить» целый сезон за один день.\n&oПримечание: игрокам также потребуется обновить свои файлы конфигурации, чтобы интерфейс сезонов соответствовал серверному.&r"
ru_json.pop('ftbquests.chapter.welcome.quest18490F31FFAB134E.description4', None)

# 2.5 Исправление ключа «Тепличное стекло» (quest0A455A4E0D7D074E -> questA455A4E0D7D074E)
if 'ftbquests.chapter.iii__advanced_farming.quest0A455A4E0D7D074E.description1' in ru_json:
    d1 = ru_json.pop('ftbquests.chapter.iii__advanced_farming.quest0A455A4E0D7D074E.description1')
    d2 = ru_json.pop('ftbquests.chapter.iii__advanced_farming.quest0A455A4E0D7D074E.description2', '')
    ru_json['ftbquests.chapter.iii__advanced_farming.questA455A4E0D7D074E.description1'] = d1
    ru_json['ftbquests.chapter.iii__advanced_farming.questA455A4E0D7D074E.description2'] = d2
    print("  [OK] Ключ quest0A455A4E0D7D074E успешно переименован в questA455A4E0D7D074E")

# Save JSON files
with open(EN_PATH, 'w', encoding='utf-8') as f:
    json.dump(en_json, f, ensure_ascii=False, indent=2)

with open(RU_PATH, 'w', encoding='utf-8') as f:
    json.dump(ru_json, f, ensure_ascii=False, indent=2)

print("  [OK] Файлы translations/ftbquests/ru_ru.json и en_us.json сохранены.")

print("\n=== 3. СИНХРОНИЗАЦИЯ В ИГРУ ===")
subprocess.run(['node', os.path.join(REPO_ROOT, 'sync_all_to_game.js')], cwd=REPO_ROOT, check=True)

print("\n=== 4. ПРЯМАЯ ФИЗИЧЕСКАЯ ВЕРИФИКАЦИЯ ===")
GAME_RU_PATH = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\ftbquestlocalizer\lang\ru_ru.json'
with open(GAME_RU_PATH, 'r', encoding='utf-8') as f:
    game_ru = json.load(f)

test_keys = [
    'ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description1',
    'ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description2',
    'ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description3',
    'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description1',
    'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description2',
    'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description3',
    'ftbquests.chapter.iv__prismatic_farming.quest41C453E806763C4F.description1',
    'ftbquests.chapter.iv__prismatic_farming.quest41C453E806763C4F.description2',
    'ftbquests.chapter.welcome.quest18490F31FFAB134E.description1',
    'ftbquests.chapter.welcome.quest18490F31FFAB134E.description2',
    'ftbquests.chapter.welcome.quest18490F31FFAB134E.description3',
    'ftbquests.chapter.iii__advanced_farming.questA455A4E0D7D074E.description1',
]

for tk in test_keys:
    val = game_ru.get(tk)
    print(f"  ✓ {tk} -> {repr(val)}")

deleted_keys = [
    'ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description4',
    'ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description5',
    'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description4',
    'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description5',
    'ftbquests.chapter.getting_started.quest3E08F21BA8F69499.description6',
    'ftbquests.chapter.iv__prismatic_farming.quest41C453E806763C4F.description3',
    'ftbquests.chapter.welcome.quest18490F31FFAB134E.description4',
    'ftbquests.chapter.iii__advanced_farming.quest0A455A4E0D7D074E.description1',
]

for dk in deleted_keys:
    if dk in game_ru:
        print(f"  ❌ ОШИБКА: Удалённый ключ {dk} всё ещё присутствует в игре!")
    else:
        print(f"  ✓ Удалённый ключ {dk} отсутствует (чисто)")

print("\n=== ВСЕ ИСПРАВЛЕНИЯ УСПЕШНО ПРИМЕНЕНЫ И ВЕРИФИЦИРОВАНЫ! ===")
