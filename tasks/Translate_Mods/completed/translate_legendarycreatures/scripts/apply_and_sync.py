import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TRANSLATIONS_FILE = os.path.join(BASE_DIR, 'translations', 'mods', 'legendarycreatures.json')
GAME_LANG_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\legendarycreatures\lang"
GAME_LANG_FILE = os.path.join(GAME_LANG_DIR, "ru_ru.json")

TRANSLATIONS = {
  "itemGroup.legendarycreatures": "Легендарные существа",
  "block.legendarycreatures.doom_fire": "Огонь рока",
  "item.legendarycreatures.straw_hat": "Соломенная шляпа",
  "item.legendarycreatures.straw_hat.description": "Предотвращает появление Пугала",
  "item.legendarycreatures.desert_mojo_spawn_egg": "Яйцо призыва пустынного моджо",
  "item.legendarycreatures.forest_mojo_spawn_egg": "Яйцо призыва лесного моджо",
  "item.legendarycreatures.hound_spawn_egg": "Яйцо призыва гончей",
  "item.legendarycreatures.scarecrow_spawn_egg": "Яйцо призыва пугала",
  "item.legendarycreatures.scorpion_spawn_egg": "Яйцо призыва скорпиона",
  "item.legendarycreatures.scorpion_baby_spawn_egg": "Яйцо призыва детёныша скорпиона",
  "item.legendarycreatures.wisp_spawn_egg": "Яйцо призыва виспа",
  "item.legendarycreatures.nether_wisp_spawn_egg": "Яйцо призыва незерского виспа",
  "item.legendarycreatures.ender_wisp_spawn_egg": "Яйцо призыва эндер-виспа",
  "item.legendarycreatures.corpse_eater_spawn_egg": "Яйцо призыва пожирателя трупов",
  "item.legendarycreatures.peacock_spider_spawn_egg": "Яйцо призыва павлиньего паука",
  "item.legendarycreatures.bullfrog_spawn_egg": "Яйцо призыва лягушки-быка",
  "item.legendarycreatures.butterfly_spawn_egg": "Яйцо призыва бабочки",
  "item.legendarycreatures.dragonfly_spawn_egg": "Яйцо призыва стрекозы",
  "item.legendarycreatures.ladybug_spawn_egg": "Яйцо призыва божьей коровки",
  "item.legendarycreatures.scarab_spawn_egg": "Яйцо призыва скарабея",
  "item.legendarycreatures.mantis_spawn_egg": "Яйцо призыва богомола",
  "item.legendarycreatures.hermit_crab_spawn_egg": "Яйцо призыва рака-отшельника",
  "effect.legendarycreatures.root": "Опутывание",
  "effect.legendarycreatures.root.description": "Сковывает движения игрока",
  "effect.legendarycreatures.convulsion": "Судороги",
  "effect.legendarycreatures.convulsion.description": "Заставляет игрока хаотично двигаться",
  "death.attack.legendarycreatures.root_attack": "%1$s был насмерть искусан",
  "death.attack.legendarycreatures.root_attack.player": "%1$s был насмерть искусан игроком %2$s",
  "entity.legendarycreatures.desert_mojo": "Пустынный моджо",
  "entity.legendarycreatures.forest_mojo": "Лесной моджо",
  "entity.legendarycreatures.hound": "Гончая",
  "entity.legendarycreatures.scarecrow": "Пугало",
  "entity.legendarycreatures.scorpion": "Скорпион",
  "entity.legendarycreatures.scorpion2": "Багровый скорпион",
  "entity.legendarycreatures.scorpion_baby": "Детёныш скорпиона",
  "entity.legendarycreatures.wisp": "Висп",
  "entity.legendarycreatures.wisp_purse": "",
  "entity.legendarycreatures.nether_wisp": "Незерский висп",
  "entity.legendarycreatures.nether_wisp_purse": "",
  "entity.legendarycreatures.ender_wisp": "Эндер-висп",
  "entity.legendarycreatures.ender_wisp_purse": "",
  "entity.legendarycreatures.corpse_eater": "Пожиратель трупов",
  "entity.legendarycreatures.peacock_spider": "Павлиний паук",
  "entity.legendarycreatures.peacock_spider2": "Лиственный павлиний паук",
  "entity.legendarycreatures.peacock_spider3": "Смертоносный павлиний паук",
  "entity.legendarycreatures.bullfrog": "Лягушка-бык",
  "entity.legendarycreatures.bullfrog2": "Земляная лягушка-бык",
  "entity.legendarycreatures.bullfrog3": "Багровая лягушка-бык",
  "entity.legendarycreatures.butterfly": "Бабочка",
  "entity.legendarycreatures.dragonfly": "Стрекоза",
  "entity.legendarycreatures.ladybug": "Божья коровка",
  "entity.legendarycreatures.scarab": "Скарабей",
  "entity.legendarycreatures.mantis": "Богомол",
  "entity.legendarycreatures.hermit_crab": "Рак-отшельник",
  "sounds.legendarycreatures.geonach_idle": "Геонах ворчит",
  "sounds.legendarycreatures.geonach_hurt": "Геонах ранен",
  "sounds.legendarycreatures.geonach_death": "Геонах погибает",
  "sounds.legendarycreatures.mojo_step": "Моджо шагает",
  "sounds.legendarycreatures.mojo_death": "Моджо погибает",
  "sounds.legendarycreatures.mojo_spawn": "Моджо появляется",
  "sounds.legendarycreatures.mojo_idle": "Моджо рычит",
  "sounds.legendarycreatures.mojo_hurt": "Моджо ранен",
  "sounds.legendarycreatures.mojo_base_attack_hit": "Моджо атакует",
  "sounds.legendarycreatures.hound_hurt": "Гончая ранена",
  "sounds.legendarycreatures.hound_death": "Гончая погибает",
  "sounds.legendarycreatures.hound_idle": "Гончая рычит",
  "sounds.legendarycreatures.hound_step": "Гончая бежит",
  "sounds.legendarycreatures.hound_base_attack_hit": "Гончая кусает",
  "sounds.legendarycreatures.hound_root_attack": "Гончая хватает зубами",
  "sounds.legendarycreatures.scarecrow_spawn": "Пугало оживает",
  "sounds.legendarycreatures.scarecrow_death": "Пугало погибает",
  "sounds.legendarycreatures.scarecrow_step": "Пугало шагает",
  "sounds.legendarycreatures.scarecrow_base_attack_hit": "Пугало атакует",
  "sounds.legendarycreatures.scorpion_hurt": "Скорпион ранен",
  "sounds.legendarycreatures.scorpion_death": "Скорпион погибает",
  "sounds.legendarycreatures.scorpion_idle": "Скорпион шипит",
  "sounds.legendarycreatures.scorpion_step": "Скорпион ползёт",
  "sounds.legendarycreatures.scorpion_claws_hit": "Скорпион щёлкает клешнями",
  "sounds.legendarycreatures.scorpion_tail_hit": "Скорпион бьёт жалом",
  "sounds.legendarycreatures.wisp_idle": "Висп мерцает",
  "sounds.legendarycreatures.wisp_death": "Висп угасает",
  "sounds.legendarycreatures.corpse_eater_spawn": "Пожиратель трупов появляется",
  "sounds.legendarycreatures.corpse_eater_hurt": "Пожиратель трупов ранен",
  "sounds.legendarycreatures.corpse_eater_run": "Пожиратель трупов бежит",
  "sounds.legendarycreatures.corpse_eater_death": "Пожиратель трупов погибает",
  "sounds.legendarycreatures.corpse_eater_idle": "Пожиратель трупов воет",
  "sounds.legendarycreatures.corpse_eater_step": "Пожиратель трупов шагает",
  "sounds.legendarycreatures.corpse_eater_attack": "Пожиратель трупов нападает",
  "sounds.legendarycreatures.corpse_eater_attack_hit": "Пожиратель трупов бьёт",
  "sounds.legendarycreatures.peacock_spider_hurt": "Павлиний паук ранен",
  "sounds.legendarycreatures.peacock_spider_run": "Павлиний паук бежит",
  "sounds.legendarycreatures.peacock_spider_death": "Павлиний паук погибает",
  "sounds.legendarycreatures.peacock_spider_step": "Павлиний паук перебирает лапками",
  "sounds.legendarycreatures.peacock_spider_attack": "Павлиний паук нападает",
  "sounds.legendarycreatures.peacock_spider_hiss": "Павлиний паук шипит",
  "sounds.legendarycreatures.bullfrog_death": "Лягушка-бык погибает",
  "sounds.legendarycreatures.bullfrog_idle": "Лягушка-бык квакает",
  "sounds.legendarycreatures.bullfrog_step": "Лягушка-бык прыгает",
  "sounds.legendarycreatures.bullfrog_attack": "Лягушка-бык атакует",
  "sounds.legendarycreatures.bullfrog_tongue_attack": "Лягушка-бык выбрасывает язык",
  "sounds.legendarycreatures.dragonfly_idle": "Стрекоза стрекочет",
  "sounds.legendarycreatures.scarab_idle": "Скарабей шуршит"
}

def main():
    os.makedirs(os.path.dirname(TRANSLATIONS_FILE), exist_ok=True)
    with open(TRANSLATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(TRANSLATIONS, f, ensure_ascii=False, indent=2)
    print(f"✅ Сохранено в проект: {TRANSLATIONS_FILE} ({len(TRANSLATIONS)} ключей)")

    os.makedirs(GAME_LANG_DIR, exist_ok=True)
    with open(GAME_LANG_FILE, 'w', encoding='utf-8') as f:
        json.dump(TRANSLATIONS, f, ensure_ascii=False, indent=2)
    print(f"✅ Скопировано в игру: {GAME_LANG_FILE} ({len(TRANSLATIONS)} ключей)")

    sync_script = os.path.join(BASE_DIR, 'sync_all_to_game.js')
    if os.path.exists(sync_script):
        os.system(f"node \"{sync_script}\"")

if __name__ == '__main__':
    main()
