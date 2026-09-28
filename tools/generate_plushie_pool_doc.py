import json, os

with open('tools/plushie_pool_detailed.json', 'r', encoding='utf-8') as f:
    plushies = json.load(f)

# Translation dictionary mapping english name / item id to high quality Russian translation and rationale
# Categories:
# 1. Whimsy Deco (7): Fufu, Flower Pig, Golden Pig, Big Panda, Singing Frog, Vocal Doll, Red Vocal Doll
# 2. Tanuki Decor (2): Mayoral Mini Figure, Developer Mini Figure
# 3. Perfect Plushies (34): Red Fox, Snow Fox, Fennec Fox, Red Ruffed Lemur, Red Panda, Raccoon, Capybara, Dog, Cat, Dolphin, Brown Rabbit, White Rabbit, Frog, Goose, Duck, Rubber Duck, Robin, Hummingbird, Hippo, Mouse, Turtle, Doe, Reindeer, Bear, Koala, Panda, Lion Cub, Elephant, Monkey, Seal, Hedgehog, Aye Aye, Quokka
# 4. Kata (15): Ace Kata Doll, Dipp Kata Doll, Foomin Kata Doll, Havana Kata Doll, Honey Kata Doll, Ichigo Kata Doll, Johnson Kata Doll, June Kata Doll, Jungle Kata Doll, Prince Kata Doll, Geraldine Plushie, Fredbear Plushie, Shiny Fredbear Plushie, Princess Fredbear Plushie, Chimera Plushie
# 5. Cluttered (4/5): Pastel Bunny Plush, Blue Sandseal Plush, Green Sandseal Plush, Red Sandseal Plush, Teddy Bear

translations_map = {
    # Whimsy Deco
    "whimsy_deco:adv_fufu_plushie": ("Fufu Plushie", "Плюшевый Фуфу", "Персонаж/маскот Fufu (Whimsy Deco)"),
    "whimsy_deco:adv_flower_pig_plushie": ("Flower Pig Plushie", "Плюшевая цветочная свинка", "Свинка с цветком"),
    "whimsy_deco:adv_golden_pig_plushie": ("Golden Pig Plushie", "Плюшевая золотая свинка", "Золотая свинка-копилка"),
    "whimsy_deco:adv_big_panda_plushie": ("Big Panda Plushie", "Большая плюшевая панда", "Большая панда"),
    "whimsy_deco:adv_singing_frog_plushie": ("Singing Frog Plushie", "Плюшевая поющая лягушка", "Поющая лягушка (имеет пасхалку проигрывания музыки)"),
    "whimsy_deco:adv_vocal_doll": ("Vocal Doll", "Вокальная кукла", "Вокалоидная кукла"),
    "whimsy_deco:adv_red_vocal_doll": ("Red Vocal Doll", "Красная вокальная кукла", "Красная вокалоидная кукла"),
    
    # Tanuki Decor
    "tanukidecor:adv_mayoral_mini_figure": ("Mayoral Mini Figure", "Мини-фигурка мэра", "Фигурка мэра (Tanuki Decor / Animal Crossing референс)"),
    "tanukidecor:adv_developer_mini_figure": ("Developer Mini Figure", "Мини-фигурка разработчика", "Фигурка разработчика мода"),
    
    # Perfect Plushies
    "perfectplushies:adv_red_fox_plushie": ("Red Fox Plushie", "Плюшевая рыжая лиса", "Рыжая лиса"),
    "perfectplushies:adv_snow_fox_plushie": ("Snow Fox Plushie", "Плюшевая песчанка / снежная лиса", "Снежная лиса (песец)"),
    "perfectplushies:adv_fennec_fox_plushie": ("Fennec Fox Plushie", "Плюшевый фенек", "Лисица фенек"),
    "perfectplushies:adv_red_ruffed_lemur_plushie": ("Red Ruffed Lemur Plushie", "Плюшевый красный вари", "Красный вари (краснобрюхий/красный хохлатый лемур)"),
    "perfectplushies:adv_red_panda_plushie": ("Red Panda Plushie", "Плюшевая красная панда", "Красная панда (малая панда)"),
    "perfectplushies:adv_raccoon_plushie": ("Raccoon Plushie", "Плюшевый енот", "Енот"),
    "perfectplushies:adv_capybara_plushie": ("Capybara Plushie", "Плюшевая капибара", "Капибара"),
    "perfectplushies:adv_dog_plushie": ("Dog Plushie", "Плюшевая собака", "Собака"),
    "perfectplushies:adv_cat_plushie": ("Cat Plushie", "Плюшевая кошка", "Кошка"),
    "perfectplushies:adv_dolphin_plushie": ("Dolphin Plushie", "Плюшевый дельфин", "Дельфин"),
    "perfectplushies:adv_brown_rabbit_plushie": ("Brown Rabbit Plushie", "Плюшевый бурый кролик", "Бурый кролик"),
    "perfectplushies:adv_white_rabbit_plushie": ("White Rabbit Plushie", "Плюшевый белый кролик", "Белый кролик"),
    "perfectplushies:adv_frog_plushie": ("Frog Plushie", "Плюшевая лягушка", "Лягушка"),
    "perfectplushies:adv_goose_plushie": ("Goose Plushie", "Плюшевый гусь", "Гусь"),
    "perfectplushies:adv_duck_plushie": ("Duck Plushie", "Плюшевая утка", "Утка"),
    "perfectplushies:adv_rubber_duck_plushie": ("Rubber Duck Plushie", "Резиновая уточка", "Классическая резиновая уточка"),
    "perfectplushies:adv_robin_plushie": ("Robin Plushie", "Плюшевая зарянка", "Птица зарянка (малиновка)"),
    "perfectplushies:adv_hummingbird_plushie": ("Hummingbird Plushie", "Плюшевая колибри", "Птица колибри"),
    "perfectplushies:adv_hippo_plushie": ("Hippo Plushie", "Плюшевый бегемот", "Бегемот / гиппопотам"),
    "perfectplushies:adv_mouse_plushie": ("Mouse Plushie", "Плюшевая мышь", "Мышь"),
    "perfectplushies:adv_turtle_plushie": ("Turtle Plushie", "Плюшевая черепаха", "Черепаха"),
    "perfectplushies:adv_doe_plushie": ("Doe Plushie", "Плюшевая олениха", "Самка оленя (лань/олениха)"),
    "perfectplushies:adv_reindeer_plushie": ("Reindeer Plushie", "Плюшевый северный олень", "Северный олень"),
    "perfectplushies:adv_bear_plushie": ("Bear Plushie", "Плюшевый медведь", "Медведь"),
    "perfectplushies:adv_koala_plushie": ("Koala Plushie", "Плюшевая коала", "Коала"),
    "perfectplushies:adv_panda_plushie": ("Panda Plushie", "Плюшевая панда", "Большая панда"),
    "perfectplushies:adv_lion_cub_plushie": ("Lion Cub Plushie", "Плюшевый львёнок", "Детёныш льва"),
    "perfectplushies:adv_elephant_plushie": ("Elephant Plushie", "Плюшевый слон", "Слон"),
    "perfectplushies:adv_monkey_plushie": ("Monkey Plushie", "Плюшевая обезьяна", "Обезьяна"),
    "perfectplushies:adv_seal_plushie": ("Seal Plushie", "Плюшевый тюлень", "Тюлень"),
    "perfectplushies:adv_hedgehog_plushie": ("Hedgehog Plushie", "Плюшевый ёж", "Ёж"),
    "perfectplushies:adv_aye_aye_plushie": ("Aye Aye Plushie", "Плюшевая руконожка ай-ай", "Мадагаскарская руконожка ай-ай"),
    "perfectplushies:adv_quokka_plushie": ("Quokka Plushie", "Плюшевая квокка", "Квокка (короткохвостый кенгуру)"),

    # Kata Dolls & Plushies (Katatroll Dolls & FNaF Easter Eggs)
    "kata:adv_ace_kata_doll": ("Ace Kata Doll", "Кукла Ката «Эйс»", "Именная кукла кузена Ace (Katatroll / Katamari референс)"),
    "kata:adv_dipp_kata_doll": ("Dipp Kata Doll", "Кукла Ката «Дипп»", "Именная кукла кузена Dipp"),
    "kata:adv_foomin_kata_doll": ("Foomin Kata Doll", "Кукла Ката «Фумин»", "Именная кукла кузины Foomin"),
    "kata:adv_havana_kata_doll": ("Havana Kata Doll", "Кукла Ката «Гавана»", "Именная кукла кузины Havana"),
    "kata:adv_honey_kata_doll": ("Honey Kata Doll", "Кукла Ката «Хани»", "Именная кукла кузины Honey"),
    "kata:adv_ichigo_kata_doll": ("Ichigo Kata Doll", "Кукла Ката «Ичиго»", "Именная кукла кузины Ichigo"),
    "kata:adv_johnson_kata_doll": ("Johnson Kata Doll", "Кукла Ката «Джонсон»", "Именная кукла кузена Johnson"),
    "kata:adv_june_kata_doll": ("June Kata Doll", "Кукла Ката «Джун»", "Именная кукла кузины June"),
    "kata:adv_jungle_kata_doll": ("Jungle Kata Doll", "Кукла Ката «Джангл»", "Именная кукла кузена Jungle"),
    "kata:adv_prince_kata_doll": ("Prince Kata Doll", "Кукла Ката «Принц»", "Именная кукла Принца Всей Вселенной (Katamari)"),
    "kata:adv_geraldine_plushie": ("Geraldine Plushie", "Плюшевая Джеральдина", "Именная плюшевая игрушка жирафа Джеральдина"),
    "kata:adv_fredbear_plushie": ("Fredbear Plushie", "Плюшевый Фредбер", "Плюшевый Фредбер (Five Nights at Freddy's)"),
    "kata:adv_shiny_fredbear_plushie": ("Shiny Fredbear Plushie", "Блестящий плюшевый Фредбер", "Сияющий/Шайни Фредбер"),
    "kata:adv_princess_fredbear_plushie": ("Princess Fredbear Plushie", "Плюшевая принцесса Фредбер", "Принцесса Фредбер (FNaF: Princess Quest)"),
    "kata:adv_chimera": ("Chimera Plushie", "Плюшевая Химера", "Плюшевая химера"),

    # Cluttered
    "cluttered:adv_pastel_bunny_plushie": ("Pastel Bunny Plush", "Пастельный плюшевый кролик", "Пастельный плюшевый зайчик/кролик"),
    "cluttered:adv_sand_seal_plush_blue": ("Blue Sandseal Plush", "Синий плюшевый песчаный котик", "Песчаный котик (The Legend of Zelda: BotW)"),
    "cluttered:adv_sand_seal_plush_green": ("Green Sandseal Plush", "Зелёный плюшевый песчаный котик", "Песчаный котик (The Legend of Zelda: BotW)"),
    "cluttered:adv_sand_seal_plush_red": ("Red Sandseal Plush", "Красный плюшевый песчаный котик", "Песчаный котик (The Legend of Zelda: BotW)"),
    "cluttered:adv_teddy_bear": ("Teddy Bear", "Плюшевый мишка Тедди", "Классический плюшевый мишка Тедди")
}

output_rows = []
for p in plushies:
    adv_id = p['adv_id']
    if adv_id in translations_map:
        en_n, ru_n, rat = translations_map[adv_id]
        p['en_canonical'] = en_n
        p['ru_proposed'] = ru_n
        p['rationale'] = rat
    else:
        p['en_canonical'] = p['en_name']
        p['ru_proposed'] = p['ru_name'] or "[UNKNOWN]"
        p['rationale'] = "[UNKNOWN]"
    output_rows.append(p)

with open('tools/plushie_pool_final.json', 'w', encoding='utf-8') as f:
    json.dump(output_rows, f, ensure_ascii=False, indent=2)

print(f'Total final rows: {len(output_rows)}')
