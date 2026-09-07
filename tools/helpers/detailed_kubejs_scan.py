import os, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

kubejs_dir = r'D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs'

books = [
  'alias_moss', 'animal_fancy', 'banana_karenina', 'brine_and_punishment', 'bluegill_meridian',
  'bullfish_jobs', 'canadian_and_famous', 'first_aid_guide', 'hitting_hard_and_soft', 'no_name_for_the_sheep',
  'intro_to_algorithms', 'paradise_crop', 'slouching_towards_artistry', 'debt_caverns', 'frogs_bounty_bazaar',
  'phenomenology_of_treasure', 'slime_contain_protect', 'the_spark_also_rises', 'universal_methods_of_farming',
  'wuthering_logs', 'pond_house_five', 'the_quality_of_the_earth', 'the_red_and_the_black',
  'women_who_run_with_the_plushies', 'the_metamorphosize'
]

book_analysis = {b: {'shops': [], 'drops': [], 'rewards': [], 'others': []} for b in books}

for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith(('.js', '.json', '.snbt')):
            path = os.path.join(root, f)
            rel = os.path.relpath(path, kubejs_dir)
            if 'assets' in rel and 'lang' in rel:
                continue # skip pure translations for now
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                for b in books:
                    if b in content:
                        if 'shops' in rel or 'trading' in rel:
                            book_analysis[b]['shops'].append((rel, content))
                        elif 'loot' in rel or 'blockEvents' in rel or 'playerEvents' in rel or 'entities' in rel:
                            book_analysis[b]['drops'].append((rel, content))
                        elif 'prizeMachine' in rel or 'slotMachine' in rel or 'lootOpening' in rel:
                            book_analysis[b]['rewards'].append((rel, content))
                        else:
                            book_analysis[b]['others'].append((rel, content))
            except Exception as e:
                pass

with open('tools/helpers/book_analysis_detailed.json', 'w', encoding='utf-8') as out:
    json.dump(book_analysis, out, ensure_ascii=False, indent=2)

print('Detailed analysis written!')
