import os
import json

# Approved translation mapping for all 62 plushies
plushie_translations = [
    # Whimsy Deco (1-7)
    ("whimsy_deco", "adv_fufu_plushie", "fufu_plushie", "Плюшевый Фуфу"),
    ("whimsy_deco", "adv_flower_pig_plushie", "flower_pig_plushie", "Плюшевая цветочная свинка"),
    ("whimsy_deco", "adv_golden_pig_plushie", "golden_pig_plushie", "Плюшевая золотая свинка"),
    ("whimsy_deco", "adv_big_panda_plushie", "big_panda_plushie", "Большая плюшевая панда"),
    ("whimsy_deco", "adv_singing_frog_plushie", "singing_frog_plushie", "Плюшевая поющая лягушка"),
    ("whimsy_deco", "adv_vocal_doll", "vocal_doll", "Кукла-вокалоид"),
    ("whimsy_deco", "adv_red_vocal_doll", "red_vocal_doll", "Красная Кукла-вокалоид"),

    # Tanuki Decor (8-9)
    ("tanukidecor", "adv_mayoral_mini_figure", "mayoral_mini_figure", "Мини-фигурка мэра"),
    ("tanukidecor", "adv_developer_mini_figure", "developer_mini_figure", "Мини-фигурка разработчика"),

    # Perfect Plushies (10-42)
    ("perfectplushies", "adv_red_fox_plushie", "red_fox_plushie", "Плюшевая рыжая лиса"),
    ("perfectplushies", "adv_snow_fox_plushie", "snow_fox_plushie", "Плюшевый песец"),
    ("perfectplushies", "adv_fennec_fox_plushie", "fennec_fox_plushie", "Плюшевый фенек"),
    ("perfectplushies", "adv_red_ruffed_lemur_plushie", "red_ruffed_lemur_plushie", "Плюшевый красный лемур"),
    ("perfectplushies", "adv_red_panda_plushie", "red_panda_plushie", "Плюшевая красная панда"),
    ("perfectplushies", "adv_raccoon_plushie", "raccoon_plushie", "Плюшевый енот"),
    ("perfectplushies", "adv_capybara_plushie", "capybara_plushie", "Плюшевая капибара"),
    ("perfectplushies", "adv_dog_plushie", "dog_plushie", "Плюшевая собака"),
    ("perfectplushies", "adv_cat_plushie", "cat_plushie", "Плюшевая кошка"),
    ("perfectplushies", "adv_dolphin_plushie", "dolphin_plushie", "Плюшевый дельфин"),
    ("perfectplushies", "adv_brown_rabbit_plushie", "brown_rabbit_plushie", "Плюшевый бурый кролик"),
    ("perfectplushies", "adv_white_rabbit_plushie", "white_rabbit_plushie", "Плюшевый белый кролик"),
    ("perfectplushies", "adv_frog_plushie", "frog_plushie", "Плюшевая лягушка"),
    ("perfectplushies", "adv_goose_plushie", "goose_plushie", "Плюшевый гусь"),
    ("perfectplushies", "adv_duck_plushie", "duck_plushie", "Плюшевая утка"),
    ("perfectplushies", "adv_rubber_duck_plushie", "rubber_duck_plushie", "Резиновая уточка"),
    ("perfectplushies", "adv_robin_plushie", "robin_plushie", "Плюшевая зарянка"),
    ("perfectplushies", "adv_hummingbird_plushie", "hummingbird_plushie", "Плюшевая колибри"),
    ("perfectplushies", "adv_hippo_plushie", "hippo_plushie", "Плюшевый бегемот"),
    ("perfectplushies", "adv_mouse_plushie", "mouse_plushie", "Плюшевая мышь"),
    ("perfectplushies", "adv_turtle_plushie", "turtle_plushie", "Плюшевая черепаха"),
    ("perfectplushies", "adv_doe_plushie", "doe_plushie", "Плюшевая лань"),
    ("perfectplushies", "adv_reindeer_plushie", "reindeer_plushie", "Плюшевый северный олень"),
    ("perfectplushies", "adv_bear_plushie", "bear_plushie", "Плюшевый медведь"),
    ("perfectplushies", "adv_koala_plushie", "koala_plushie", "Плюшевая коала"),
    ("perfectplushies", "adv_panda_plushie", "panda_plushie", "Плюшевая панда"),
    ("perfectplushies", "adv_lion_cub_plushie", "lion_cub_plushie", "Плюшевый львёнок"),
    ("perfectplushies", "adv_elephant_plushie", "elephant_plushie", "Плюшевый слон"),
    ("perfectplushies", "adv_monkey_plushie", "monkey_plushie", "Плюшевая обезьяна"),
    ("perfectplushies", "adv_seal_plushie", "seal_plushie", "Плюшевый тюлень"),
    ("perfectplushies", "adv_hedgehog_plushie", "hedgehog_plushie", "Плюшевый ёж"),
    ("perfectplushies", "adv_aye_aye_plushie", "aye_aye_plushie", "Плюшевая руконожка"),
    ("perfectplushies", "adv_quokka_plushie", "quokka_plushie", "Плюшевая квокка"),

    # Kata (43-53, 59-62)
    ("kata", "adv_ace_kata_doll", "ace_kata_doll", "Кукла Ката «Эйс»"),
    ("kata", "adv_dipp_kata_doll", "dipp_kata_doll", "Кукла Ката «Дипп»"),
    ("kata", "adv_foomin_kata_doll", "foomin_kata_doll", "Кукла Ката «Фумин»"),
    ("kata", "adv_havana_kata_doll", "havana_kata_doll", "Кукла Ката «Гавана»"),
    ("kata", "adv_honey_kata_doll", "honey_kata_doll", "Кукла Ката «Хани»"),
    ("kata", "adv_ichigo_kata_doll", "ichigo_kata_doll", "Кукла Ката «Ичиго»"),
    ("kata", "adv_johnson_kata_doll", "johnson_kata_doll", "Кукла Ката «Джонсон»"),
    ("kata", "adv_june_kata_doll", "june_kata_doll", "Кукла Ката «Джун»"),
    ("kata", "adv_jungle_kata_doll", "jungle_kata_doll", "Кукла Ката «Джангл»"),
    ("kata", "adv_prince_kata_doll", "prince_kata_doll", "Кукла Ката «Принц»"),
    ("kata", "adv_geraldine_plushie", "geraldine_plushie", "Плюшевая Джеральдина"),
    ("kata", "adv_fredbear_plushie", "fredbear_plushie", "Плюшевый Фредди"),
    ("kata", "adv_shiny_fredbear_plushie", "shiny_fredbear_plushie", "Блестящий плюшевый Фредди"),
    ("kata", "adv_princess_fredbear_plushie", "princess_fredbear_plushie", "Плюшевая принцесса Фредди"),
    ("kata", "adv_chimera", "chimera", "Плюшевая химера"),

    # Cluttered (54-58)
    ("cluttered", "adv_pastel_bunny_plushie", "pastel_bunny_plushie", "Плюшевый зайчик"),
    ("cluttered", "adv_sand_seal_plush_blue", "sand_seal_plush_blue", "Плюшевый синий песчаный котик"),
    ("cluttered", "adv_sand_seal_plush_green", "sand_seal_plush_green", "Плюшевый зелёный песчаный котик"),
    ("cluttered", "adv_sand_seal_plush_red", "sand_seal_plush_red", "Плюшевый красный песчаный котик"),
    ("cluttered", "adv_teddy_bear", "teddy_bear", "Плюшевый мишка"),
]

# Group by mod
mods_dict = {}
for mod, adv_name, base_name, ru_title in plushie_translations:
    if mod not in mods_dict:
        mods_dict[mod] = {}
    
    # Add block and item keys for both adv_ and base_
    mods_dict[mod][f"block.{mod}.{adv_name}"] = ru_title
    mods_dict[mod][f"item.{mod}.{adv_name}"] = ru_title
    mods_dict[mod][f"block.{mod}.{base_name}"] = ru_title
    mods_dict[mod][f"item.{mod}.{base_name}"] = ru_title

mods_dir = os.path.normpath("translations/mods")
os.makedirs(mods_dir, exist_ok=True)

for mod, new_keys in mods_dict.items():
    mod_file = os.path.join(mods_dir, f"{mod}.json")
    existing_data = {}
    if os.path.exists(mod_file):
        try:
            with open(mod_file, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except Exception as e:
            print(f"Error loading {mod_file}: {e}")
    
    existing_data.update(new_keys)
    with open(mod_file, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {mod}.json ({len(new_keys)} keys added/updated, total {len(existing_data)})")

print("\nAll 62 plushie translations successfully written to translations/mods/*.json!")
