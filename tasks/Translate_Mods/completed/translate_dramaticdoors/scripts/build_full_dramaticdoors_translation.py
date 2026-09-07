import json, os, re

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_PATH = os.path.join(TASK_DIR, "en_us_all.json")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(TASK_DIR))))
RU_TARGET = os.path.join(BASE_DIR, "translations", "mods", "dramaticdoors.json")
GAME_TARGET = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\dramaticdoors\lang\ru_ru.json"

WORDS_MAP = {
    'Abyssal': 'бездны', 'Acacia': 'акациевая', 'Acorn': 'жёлудевая', 'Aerfin': 'аэрфиновая', 'Aerogel': 'аэрогелевая', 'Aeronos': 'аэроносовая',
    'Agathoxylon': 'агатоксилоновая', 'Aged': 'состаренная', 'Alarmed': 'сигнальная', 'Alder': 'ольховая', 'Aluminium': 'алюминиевая',
    'Aluminum': 'алюминиевая', 'Amber': 'янтарная', 'Amethyst': 'аметистовая', 'Anchor': 'якорная', 'Ancient': 'древняя',
    'Andesite': 'андезитовая', 'Apple': 'яблоневая', 'Apricorn': 'априкорновая', 'Araucaria': 'араукариевая', 'Arcane': 'тайная',
    'Archwood': 'арочнодревесная', 'Aroma': 'ароматная', 'Ash': 'ясеневая', 'Ashen': 'пепельная', 'Aspen': 'осиновая',
    'Aster': 'астрового дерева', 'Astral': 'астральная', 'Atlas': 'атласная', 'Aurora': 'северного сияния', 'Autumn': 'осенняя',
    'Autumnal': 'осенняя', 'Avocado': 'авокадовая', 'Azalea': 'азалиевая', 'Azul': 'лазурная', 'Azurite': 'азуритовая',
    'Bamboo': 'бамбуковая', 'Banana': 'банановая', 'Baobab': 'баобабовая', 'Bark': 'коровая', 'Barn': 'амбарная',
    'Basalt': 'базальтовая', 'Bay': 'лаврового дерева', 'Beach': 'пляжная', 'Beech': 'буковая', 'Beeswax': 'пчелиновосковая',
    'Bell': 'колокольная', 'Bioluminescent': 'биолюминесцентная', 'Bioshroom': 'биогрибная', 'Birch': 'берёзовая', 'Black': 'чёрная',
    'Blackstone': 'чернокаменная', 'Blackwood': 'чернодревесная', 'Blank': 'гладкая', 'Blaze': 'всполоховая', 'Bleached': 'отбеленная',
    'Blossom': 'цветущая', 'Blue': 'синяя', 'Bluebright': 'ярко-синяя', 'Bog': 'болотная', 'Bone': 'костяная',
    'Bookshelf': 'книжная', 'Brachyphyllum': 'брахифиллумовая', 'Brass': 'латунная', 'Breeze': 'ветерочная', 'Brimwood': 'сернодревесная',
    'Brittle': 'хрупкая', 'Bronze': 'бронзовая', 'Brown': 'коричневая', 'Bubbler': 'пузырчатая', 'Bulbis': 'бульбисовая',
    'Burnt': 'обожжённая', 'Cacao': 'какао', 'Cactus': 'кактусовая', 'Calcite': 'кальцитовая', 'Candle': 'свечная',
    'Canopy': 'купольная', 'Cardboard': 'картонная', 'Carnelian': 'сердоликовая', 'Carved': 'резная', 'Casing': 'кожуховая',
    'Cassette': 'кассетная', 'Cast': 'чугунная', 'Cavern': 'пещерная', 'Cedar': 'кедровая', 'Celestite': 'целеститовая',
    'Cell': 'тюремная', 'Ceramic': 'керамическая', 'Cerise': 'светло-вишнёвая', 'Chalk': 'меловая', 'Charred': 'обугленная',
    'Checkered': 'клетчатая', 'Cherry': 'вишнёвая', 'Chestnut': 'каштановая', 'Chiseled': 'резная', 'Chlorophyte': 'хлорофитовая',
    'Chrome': 'хромированная', 'Cika': 'цикасовая', 'Cinder': 'пепельная', 'Cinnamon': 'коричная', 'Citrine': 'цитриновая',
    'Citron': 'цитроновая', 'Classic': 'классическая', 'Clay': 'глиняная', 'Cloud': 'облачная', 'Cobalt': 'кобальтовая',
    'Cobblestone': 'булыжниковая', 'Cocoa': 'какао', 'Coconut': 'кокосовая', 'Colored': 'цветная', 'Comberry': 'комберриевая',
    'Constantan': 'константановая', 'Copper': 'медная', 'Corail': 'коралловая', 'Coral': 'коралловая', 'Corrupted': 'осквернённая',
    'Cottage': 'коттеджная', 'Cragroot': 'скалокорневая', 'Crimson': 'багровая', 'Cracked': 'треснувшая', 'Crystal': 'кристаллическая',
    'Crystalline': 'кристаллическая', 'Cyan': 'бирюзовая', 'Cypress': 'кипарисовая', 'Dark': 'тёмная', 'Darkwood': 'темнодревесная',
    'Dead': 'мёртвая', 'Decayed': 'гнилая', 'Deepslate': 'глубинносланцевая', 'Delight': 'изысканная', 'Demon': 'демоническая',
    'Diamond': 'алмазная', 'Diorite': 'диоритовая', 'Distorted': 'искажённая', 'Double': 'двойная', 'Dragon': 'драконья',
    'Dream': 'сновиденческая', 'Dreamwood': 'древесно-сновиденческая', 'Driftwood': 'плавниковая', 'Dripstone': 'капельниковая',
    'Dusk': 'сумеречная', 'Dust': 'пыльная', 'Ebony': 'эбеновая', 'Echo': 'эхо', 'Edelwood': 'эдельвейсовая',
    'Elder': 'бузинная', 'Eldritch': 'жуткая', 'Electric': 'электрическая', 'Electrum': 'электрумовая', 'Elm': 'вязовая',
    'Embur': 'тлеющая', 'Emerald': 'изумрудная', 'Empyreal': 'эмпирейная', 'Enchanted': 'чародейская', 'End': 'энда',
    'Ender': 'эндер', 'Endstone': 'эндерняковая', 'Ether': 'эфирная', 'Eucalyptus': 'эвкалиптовая', 'Exotic': 'экзотическая',
    'Exposed': 'потускневшая', 'Eye': 'глазная', 'Fairy': 'сказочная', 'Fallen': 'поваленная', 'Fancy': 'изящная',
    'Festive': 'праздничная', 'Fiber': 'волоконная', 'Fig': 'инжирная', 'Fine': 'тонкая', 'Fir': 'пихтовая',
    'Flax': 'льняная', 'Flaxen': 'льняная', 'Flesh': 'плотская', 'Floral': 'цветочная', 'Florus': 'флорусовая',
    'Fluorescent': 'люминесцентная', 'Foam': 'пенная', 'Forest': 'лесная', 'Forged': 'кованая', 'Fossil': 'ископаемая',
    'Fossilized': 'окаменелая', 'Four': 'четырёх', 'Framed': 'обрамлённая', 'French': 'французская', 'Frost': 'морозная',
    'Frostbright': 'ярко-морозная', 'Frosted': 'матовая застеклённая', 'Fungal': 'грибная', 'Fungus': 'грибная', 'Galax': 'галактическая',
    'Gilded': 'позолоченная', 'Ginger': 'имбирная', 'Ginkgo': 'гинкговая', 'Glass': 'стеклянная', 'Glassed': 'застеклённая',
    'Glow': 'светящаяся', 'Glowing': 'светящаяся', 'Glowshroom': 'светогрибная', 'Gold': 'золотая', 'Golden': 'золотая',
    'Gothic': 'готическая', 'Granite': 'гранитная', 'Gray': 'серая', 'Green': 'зелёная', 'Greenheart': 'зеленосердечная',
    'Grim': 'мрачная', 'Grimwood': 'мрачнодеревная', 'Grongle': 'гронгловая', 'Grounded': 'заземлённая', 'Grove': 'рощевая',
    'Hardened': 'закалённая', 'Haunted': 'призрачная', 'Hawthorn': 'боярышниковая', 'Hazel': 'лещиновая', 'Heart': 'с сердечком',
    'Hearth': 'очаговая', 'Hearthgrove': 'очагово-рощевая', 'Heavy': 'тяжёлая', 'Heidiphyllum': 'хейдифиллумовая', 'Hell': 'адская',
    'Hellbark': 'адскокорая', 'Hidden': 'скрытая', 'Highland': 'высокогорная', 'Holly': 'падубовая', 'Hollow': 'полая',
    'Holo': 'голографическая', 'Honeycomb': 'сотовая', 'Hornbeam': 'грабовая', 'Horse': 'лошадиная', 'Hydra': 'гидры',
    'Ice': 'ледяная', 'Icy': 'ледяная', 'Illager': 'разбойничья', 'Imperial': 'имперская', 'Imparius': 'непарная',
    'Industrial': 'индустриальная', 'Infernal': 'адская', 'Infused': 'насыщенная', 'Inlaid': 'инкрустированная', 'Invar': 'инваровая',
    'Iron': 'железная', 'Ironwood': 'железнодеревная', 'Ivory': 'слоновой кости', 'Jacaranda': 'жакарандовая', 'Jail': 'решётчатая тюремная',
    'Jasper': 'яшмовая', 'Joshua': 'джошуа', 'Jungle': 'тропическая', 'Kapok': 'капоковая', 'Kelp': 'ламинариевая',
    'Knightmetal': 'рыцарского металла', 'Kousa': 'кусовая', 'Lacquered': 'лакированная', 'Lantern': 'фонарная', 'Lapis': 'лазуритовая',
    'Larch': 'лиственничная', 'Laser': 'лазерная', 'Lattice': 'решётчатая', 'Laurel': 'лавровая', 'Lava': 'лавовая',
    'Lead': 'свинцовая', 'Leaf': 'лиственная', 'Leafy': 'лиственная', 'Leather': 'кожаная', 'Light': 'светлая',
    'Lighted': 'освещённая', 'Limestone': 'известняковая', 'Linden': 'липовая', 'Liriodendrites': 'лириодендритовая', 'Living': 'живая',
    'Livingwood': 'живодревесная', 'Log': 'бревенчатая', 'Loom': 'ткацкая', 'Lotus': 'лотосовая', 'Lunar': 'лунная',
    'Lush': 'пышная', 'Luxurious': 'роскошная', 'Macaw': 'макао', 'Magic': 'магическая', 'Magma': 'магматическая',
    'Magnolia': 'магнолиевая', 'Mahogany': 'краснодеревная', 'Malachite': 'малахитовая', 'Mangrove': 'мангровая', 'Maple': 'кленовая',
    'Marble': 'мраморная', 'Marsh': 'топяная', 'Masonry': 'каменнокладочная', 'Mauve': 'розовато-лиловая', 'Meadow': 'луговая',
    'Melon': 'арбузная', 'Metal': 'металлическая', 'Metallic': 'металлическая', 'Metasequoia': 'метасеквойная', 'Midnight': 'полуночная',
    'Miner': 'шахтёрская', 'Minewood': 'шахтодеревная', 'Mirage': 'миражная', 'Mirror': 'зеркальная', 'Mist': 'туманная',
    'Modern': 'современная', 'Moon': 'лунная', 'Moonlight': 'лунносветная', 'Morado': 'морадская', 'Mosaic': 'мозаичная',
    'Moss': 'мшистая', 'Mossy': 'мшистая', 'Mud': 'саманная', 'Mushroom': 'грибная', 'Mystic': 'мистическая',
    'Mythril': 'мифриловая', 'Nebula': 'туманностная', 'Neocalamites': 'неокаламитовая', 'Neon': 'неоновая', 'Nether': 'незерская',
    'Netherite': 'незеритовая', 'Netherrack': 'незеритово-камневая', 'Nickel': 'никелевая', 'Night': 'ночная', 'Nightfall': 'сумеречная',
    'Nightshade': 'паслёновая', 'Nox': 'нокс', 'Nut': 'ореховая', 'Nutmeg': 'мускатная', 'Oak': 'дубовая',
    'Oasis': 'оазисная', 'Obsidian': 'обсидиановая', 'Ocean': 'океаническая', 'Ochre': 'охристая', 'Old': 'старая',
    'Olive': 'оливковая', 'Onyx': 'ониксовая', 'Opal': 'опаловая', 'Orange': 'оранжевая', 'Orchard': 'садовая',
    'Origin': 'первозданная', 'Ornate': 'витиеватая', 'Overgrown': 'заросшая', 'Oxidized': 'окисленная', 'Painted': 'окрашенная',
    'Pale': 'бледно-дубовая', 'Palm': 'пальмовая', 'Panel': 'панельная', 'Paneled': 'панельная', 'Paper': 'бумажная',
    'Paradise': 'райская', 'Park': 'парковая', 'Patterned': 'узорчатая', 'Pearl': 'жемчужная', 'Peat': 'торфяная',
    'Pecan': 'пекановая', 'Persimmon': 'хурмовая', 'Petrified': 'окаменелая', 'Phantom': 'фантомная', 'Piglin': 'пиглинская',
    'Pine': 'сосновая', 'Pink': 'розовая', 'Piston': 'поршневая', 'Pistachio': 'фисташковая', 'Plain': 'простая',
    'Plank': 'дощатая', 'Plasma': 'плазменная', 'Plated': 'пластинчатая', 'Platinum': 'платиновая', 'Plum': 'сливовая',
    'Pneumatic': 'пневматическая', 'Poison': 'ядовитая', 'Poise': 'равновесная', 'Polished': 'полированная', 'Polyp': 'полиповая',
    'Ponderosa': 'желтососновая', 'Poplar': 'тополевая', 'Poppy': 'маковая', 'Porcelain': 'фарфоровая', 'Porphyry': 'порфировая',
    'Portcullis': 'герсовая', 'Prismatic': 'призматическая', 'Prismarine': 'призмариновая', 'Protojuniperoxylon': 'протоюнипероксилоновая',
    'Protopiceoxylon': 'протопицеоксилоновая', 'Prunepost': 'черносливовая', 'Pulp': 'мякотная', 'Pumpkin': 'тыквенная',
    'Pure': 'чистая', 'Purple': 'фиолетовая', 'Purpur': 'пурпурная', 'Pyrite': 'пиритовая', 'Quartz': 'кварцевая',
    'Radiant': 'сияющая', 'Rainbow': 'радужная', 'Rambler': 'вьющаяся', 'Rattan': 'ротанговая', 'Raw': 'сырая',
    'Red': 'красная', 'Redstone': 'редстоуновая', 'Redwood': 'секвойная', 'Reed': 'тростниковая', 'Refined': 'очищенная',
    'Reinforced': 'укреплённая', 'Rift': 'разломная', 'Rim': 'ободковая', 'River': 'речная', 'Rock': 'скальная',
    'Root': 'корневая', 'Rooted': 'укоренённая', 'Rose': 'розовая', 'Roseroot': 'розовокорневая', 'Rosewood': 'розоводеревная',
    'Rowan': 'рябиновая', 'Royal': 'королевская', 'Ruin': 'руинная', 'Runic': 'руническая', 'Rust': 'ржавая',
    'Rustic': 'деревенская', 'Rusty': 'ржавая', 'Sacred': 'священная', 'Sakura': 'сакуровая', 'Saloon': 'салунная',
    'Sand': 'песчаная', 'Sandstone': 'песчаниковая', 'Sapphire': 'сапфировая', 'Sassafras': 'сассафрасовая', 'Savage': 'дикая',
    'Scaffold': 'строительных лесов', 'Scattered': 'рассеянная', 'Scenic': 'живописная', 'Schilderia': 'шильдериевая',
    'Scorched': 'обожжённая', 'Screen': 'сетчатая', 'Sculk': 'скалковая', 'Seagrass': 'морской травы', 'Sealed': 'запечатанная',
    'Secret': 'потайная', 'Security': 'защитная', 'Serene': 'безмятежная', 'Shadow': 'теневая', 'Shaded': 'затенённая',
    'Shell': 'ракушечная', 'Shimmer': 'мерцающая', 'Shimmerwood': 'мерцающая', 'Shinestone': 'сияющекаменная', 'Shiny': 'блестящая',
    'Shoji': 'сёдзи', 'Silk': 'шёлковая', 'Silky': 'шелковистая', 'Silver': 'серебряная', 'Simple': 'простая',
    'Single': 'одинарная', 'Skeletal': 'скелетная', 'Sky': 'небесная', 'Skyris': 'небесная', 'Skyroot': 'небеснокорневая',
    'Slanted': 'наклонная', 'Slate': 'сланцевая', 'Sliding': 'раздвижная', 'Slime': 'слизистая', 'Smokey': 'дымчатая',
    'Smogstem': 'смогстебельная', 'Smooth': 'гладкая', 'Snail': 'улиточная', 'Snow': 'снежная', 'Snowy': 'снежная',
    'Socotra': 'сокотрийская', 'Solid': 'сплошная', 'Sorting': 'сортировочная', 'Sortingwood': 'сортировочная', 'Soul': 'душ',
    'Spark': 'искристая', 'Spectral': 'спектральная', 'Spike': 'шипастая', 'Spire': 'шпилевая', 'Spirit': 'духовная',
    'Spotted': 'пятнистая', 'Spring': 'весенняя', 'Spruce': 'еловая', 'Stable': 'конюшенная', 'Stained': 'витражная',
    'Starlight': 'звездносветная', 'Starlit': 'звёздная', 'Steel': 'стальная', 'Stitched': 'сшитая', 'Stone': 'каменная',
    'Storm': 'штормовая', 'Straw': 'соломенная', 'Striped': 'полосатая', 'Stripped': 'обтёсанная', 'Strong': 'прочная',
    'Studded': 'обитая', 'Sturdy': 'крепкая', 'Submerged': 'погружённая', 'Sugar': 'сахарная', 'Sun': 'солнечная',
    'Sunken': 'затонувшая', 'Sunlight': 'солнечносветная', 'Sunroot': 'солнцекорневая', 'Sunset': 'закатная', 'Swamp': 'болотная',
    'Sweet': 'сладкая', 'Sweetgum': 'ликвидамбаровая', 'Sycamore': 'платанная', 'Sylvan': 'лесная', 'Synthetic': 'синтетическая',
    'Sythian': 'сифиевая', 'Tallow': 'сальная', 'Tan': 'желтовато-коричневая', 'Tangle': 'запутанная', 'Tar': 'дегтярная',
    'Teak': 'тиковая', 'Temple': 'храмовая', 'Terracotta': 'терракотовая', 'Thatch': 'соломенная', 'Thermal': 'термальная',
    'Thorn': 'шипастая', 'Thorny': 'терновая', 'Thunder': 'грозовая', 'Timber': 'бревенчатая', 'Time': 'времени',
    'Timewood': 'дерева времени', 'Tin': 'оловянная', 'Titanium': 'титановая', 'Topaz': 'топазовая', 'Torch': 'факельная',
    'Tower': 'башенная', 'Towerwood': 'башенная', 'Traditional': 'традиционная', 'Train': 'поездная', 'Tranquil': 'спокойная',
    'Translucent': 'полупрозрачная', 'Transmuting': 'трансформирующая', 'Transwood': 'трансформирующая', 'Trap': 'люковая',
    'Treated': 'обработанная', 'Tree': 'древесная', 'Treasure': 'сокровищная', 'Trochodendroides': 'троходендроидная',
    'Tropical': 'тропическая', 'Tuff': 'туфовая', 'Twilight': 'сумеречная', 'Umbran': 'сумрачная', 'Underground': 'подземная',
    'Underworld': 'подземного мира', 'Universal': 'универсальная', 'Uranium': 'урановая', 'Urban': 'городская', 'Valiant': 'доблестная',
    'Valley': 'долинная', 'Vanilla': 'ванильная', 'Vapor': 'паровая', 'Vault': 'сейфовая', 'Velvet': 'бархатная',
    'Verdant': 'зеленеющая', 'Victorian': 'викторианская', 'Vine': 'лианная', 'Vintage': 'винтажная', 'Violet': 'фиалковая',
    'Void': 'пустотная', 'Volcanic': 'вулканическая', 'Waffle': 'вафельная', 'Walnut': 'ореховая', 'Warped': 'искажённая',
    'Water': 'водяная', 'Waterlogged': 'затопленная', 'Wattle': 'плетёная', 'Wave': 'волновая', 'Waxed': 'вощёная',
    'Weathered': 'состаренная', 'Weeping': 'плакучая', 'Western': 'ковбойская', 'Wetland': 'топкая', 'White': 'белая',
    'Wigwarp': 'вихрестебельная', 'Wild': 'дикая', 'Wildwood': 'дикодревесная', 'Willow': 'ивовая', 'Wind': 'ветровая',
    'Wired': 'проволочная', 'Wisp': 'блуждающего огонька', 'Wisteria': 'глициниевая', 'Witch': 'ведьмина', 'Wither': 'визерная',
    'Wood': 'деревянная', 'Wooden': 'деревянная', 'Woodworthia': 'вудвортиевая', 'Wool': 'шерстяная', 'Woven': 'тканая',
    'Wrought': 'кованая', 'Yagroot': 'ягкорневая', 'Yellow': 'жёлтая', 'Yew': 'тисовая', 'Yucca': 'юкковая',
    'Zamites': 'замитовая', 'Zelkova': 'дзельквовая', 'Zinc': 'цинковая',
    'Barred': 'решётчатая', 'Boarded': 'дощатая', 'Dual': 'двойная', 'Fortified': 'укреплённая', 'Gated': 'калиточная',
    'Pressed': 'прессованная', 'Shack': 'хижины', 'Supported': 'с подпорками', 'Tile': 'плиточная', 'Tiled': 'плиточная',
    'Windowed': 'с окном', 'Store': 'магазинная', 'Hospital': 'больничная', 'Warning': 'предупреждающая', 'Stem': 'стеблевая',
    'Bar': 'решётчатая', 'Barrel': 'бочечная', 'Brick': 'кирпичная', 'Corrugated': 'гофрированная', 'Factory': 'фабричная',
    'Ship': 'корабельная', 'Steampunk': 'стимпанк', 'Dwarf': 'дворфийская', 'Fantasy': 'фэнтезийная',
    'Laboratory': 'лабораторная', 'Rusted': 'ржавая', 'Safe': 'сейфовая', 'Space': 'космическая', 'Paneled': 'панельная',
    'Chipped': 'чиппинг', 'Macaw': 'макао', 'ManyIdeas': 'мэниидейс'
,
    'Amaranth': 'амарантовая',
    'Artichoke': 'артишоковая',
    'Auritis': 'ауритисовая',
    'Aurum': 'золотая',
    'Azule': 'лазурная',
    'Azure': 'лазурная',
    'Balloon': 'шариковая',
    'Balsa': 'бальсовая',
    'Banyin': 'баньяновая',
    'Bedrock': 'бедроковая',
    'Beladon': 'белладонновая',
    'Blaru': 'бларовая',
    'Blighted': 'зачумлённая',
    'Blightwillow': 'чумноивовая',
    'Blood': 'кровавая',
    'Bloodshroom': 'кровавогрибная',
    'Bloom': 'цветущая',
    'Blooming': 'цветущая',
    'Bone': 'костяная',
    'Brain': 'мозговая',
    'Breath': 'дыхания',
    'Bright': 'яркая',
    'Bubble': 'пузырьковая',
    'Ceilinum': 'сейлинумовая',
    'Ceiltrunk': 'сейлствольная',
    'Celestial': 'небесная',
    'Cerulean': 'лазурная',
    'Chain': 'цепная',
    'Cincinnasite': 'цинцинназитовая',
    'Cindered': 'пепельная',
    'Citrus': 'цитрусовая',
    'Cloudcap': 'облачношляпочная',
    'Coal': 'угольная',
    'Cobbled': 'булыжниковая',
    'Conberry': 'хвойноягодная',
    'Concrete': 'бетонная',
    'Cork': 'пробковая',
    'Cradlewood': 'колыбельнодревесная',
    'Cruderoot': 'грубокорневая',
    'Cruxite': 'крукситовая',
    'Crystallized': 'кристаллизованная',
    'Deadwood': 'мертводревесная',
    'Decadent': 'декадентская',
    'Demonic': 'демоническая',
    'Dense': 'плотная',
    'Deorum': 'деорумовая',
    'Distortic': 'искажённая',
    'Doom': 'роковая',
    'Dragon': 'драконья',
    'Dry': 'сухая',
    'Edified': 'назидательная',
    'Enigma': 'загадочная',
    'Etyr': 'этировая',
    'Fan': 'веерная',
    'Fieldsproot': 'полеростковая',
    'Fiss': 'трещинная',
    'Fleshkin': 'плотская',
    'Flowering': 'цветущая',
    'FoamDoor': 'пенная дверь',
    'Frozen': 'замороженная',
    'Fuchsia': 'фуксиевая',
    'Fungyss': 'грибная',
    'Generic': 'обычная',
    'Ghaf': 'гафовая',
    'Giant': 'гигантская',
    'Gingerbread': 'пряничная',
    'Glacia': 'ледяная',
    'Glacian': 'гляциановая',
    'Glaciated': 'оледенелая',
    'Glowood': 'светодревесная',
    'GoldenWood': 'золотодревесная',
    'Goopy': 'липкая',
    'Gourdrot': 'тыквенногнилая',
    'Grape': 'виноградная',
    'Grey': 'серая',
    'HearthgroveDoor': 'очагово-рощевая дверь',
    'Helix': 'спиральная',
    'Hellwood': 'адскодревесная',
    'Hemlock': 'болиголовая',
    'Highsproot': 'высокоростковая',
    'Hoary': 'седая',
    'Honey': 'медовая',
    'Hope': 'надежды',
    'Indigo': 'индиговая',
    'Inverted': 'перевёрнутая',
    'Jabuticaba': 'жабутикабовая',
    'Japanese': 'японская',
    'Jellyshroom': 'желегрибная',
    'Jinglestem': 'звенестебельная',
    'Juniper': 'можжевеловая',
    'Lacugrove': 'лакурощевая',
    'Large': 'большая',
    'Lavic': 'лавовая',
    'Lazuli': 'лазуритовая',
    'Lemon': 'лимонная',
    'Leppa': 'леппа',
    'Life': 'жизни',
    'Lime': 'лаймовая',
    'Link': 'звеньевая',
    'Lockable': 'запираемая',
    'Locked': 'запертая',
    'Lucernia': 'люцерниевая',
    'Luzawood': 'лузадревесная',
    'Lychee': 'личи',
    'Magenta': 'пурпурная',
    'Mango': 'манговая',
    'Maroon': 'бордовая',
    'Menril': 'менриловая',
    'Mesh': 'сетчатая',
    'Mind': 'разума',
    'Mint': 'мятная',
    'Mold': 'плесневая',
    'Muddy': 'илистая',
    'Mulberry': 'шелковичная',
    'Murushroom': 'муругрибная',
    'Mystical': 'мистическая',
    'Nanab': 'нанабовая',
    'Navy': 'тёмно-синяя',
    'Netherwood': 'незеродревесная',
    'Nibbletwig': 'грызоветочная',
    'Northland': 'северная',
    'Oran': 'орановая',
    'Padded': 'мягкая',
    'Palo': 'пало',
    'Peach': 'персиковая',
    'Pear': 'грушевая',
    'Pecha': 'печевая',
    'Penumbral': 'полутеневая',
    'Perfectly': 'идеально',
    'Periwinkle': 'барвинковая',
    'Perturbed': 'возмущённая',
    'Pewen': 'певеновая',
    'Planks': 'дощатая',
    'Poisonous': 'ядовитая',
    'Powdery': 'порошковая',
    'Pream': 'примовая',
    'Primordial': 'первозданная',
    'Pulse': 'пульсирующая',
    'Pyrowood': 'пиродревесная',
    'Pythadendron': 'питодендроновая',
    'Rage': 'ярости',
    'Rambutan': 'рамбутановая',
    'Redbud': 'багряниковая',
    'Redlove': 'красноплодная',
    'Reed': 'тростниковая',
    'Reeds': 'тростниковая',
    'Ring': 'кольцевая',
    'Rotten': 'гнилая',
    'Roze': 'розовая',
    'Rubber': 'каучуковая',
    'Rubberwood': 'каучукодревесная',
    'Rubeus': 'рубиновая',
    'Runewood': 'рунодревесная',
    'Sage': 'шалфейная',
    'Sal': 'саловая',
    'Sap': 'смоляная',
    'Saxaul': 'саксауловая',
    'Scabyst': 'скабистовая',
    'Scarlet': 'алая',
    'Sea': 'морская',
    'Shadewood': 'тенедревесная',
    'Shamrock': 'клеверная',
    'Sheet': 'листовая',
    'Silverbell': 'сереброколокольчиковая',
    'Sitrus': 'цитрусовая',
    'Slimed': 'ослизлая',
    'Small': 'малая',
    'Snowman': 'снеговика',
    'Soulblight': 'душечумная',
    'Soulcopper': 'душемедная',
    'Soulwood': 'душедревесная',
    'Sourcestone': 'камня источника',
    'Sponge': 'губчатая',
    'Stalagnate': 'сталагнатная',
    'Strawberry': 'клубничная',
    'Strophar': 'строфариевая',
    'Sugi': 'криптомериевая',
    'Syrmorite': 'сирморитовая',
    'Tecal': 'текаловая',
    'Temporal': 'временная',
    'Tenanea': 'тенанейская',
    'Terminite': 'терминитовая',
    'Thallasium': 'талласиевая',
    'Thornwood': 'тернодревесная',
    'Tiger': 'тигровая',
    'Tigerwood': 'тигродревесная',
    'Tinted': 'тонированная',
    'Tooth': 'зубная',
    'Torreya': 'торреевая',
    'Trumpet': 'трубная',
    'Twisted': 'витая',
    'Umbral': 'теневая',
    'Umbrella': 'зонтичная',
    'Verde': 'зелёная',
    'Vermilion': 'киноварная',
    'Vigilant': 'бдительная',
    'Wart': 'наростная',
    'Weedwood': 'сорнякодревесная',
    'Whistlecane': 'свистотростниковая',
    'Wide': 'широкая',
    'Wigglewood': 'извиводревесная',
    'Wormwood': 'полынная'}

PHRASES = {
    'Dark Oak': 'тёмно-дубовая',
    'Pale Oak': 'бледно-дубовая',
    'Rainbow Eucalyptus': 'радужно-эвкалиптовая',
    'White Mangrove': 'беломангровая',
    'Witch Hazel': 'гамамелисовая',
    'Blue Enchanted': 'синяя чародейская',
    'Green Enchanted': 'зелёная чародейская',
    'Exposed Copper': 'потускневшая медная',
    'Weathered Copper': 'состаренная медная',
    'Oxidized Copper': 'окисленная медная',
    'Waxed Copper': 'вощёная медная',
    'Waxed Exposed Copper': 'вощёная потускневшая медная',
    'Waxed Weathered Copper': 'вощёная состаренная медная',
    'Waxed Oxidized Copper': 'вощёная окисленная медная',
    'Twilight Oak': 'сумеречно-дубовая',
    'Ancient Oak': 'древнедубовая',
    'Golden Oak': 'золотодубовая',
    'Cast Iron': 'чугунная',
    'Four Panel': 'четырёхпанельная',
    'Shoji Whole': 'цельная сёдзи',
    'Barn Glassed': 'застеклённая амбарная',
    'Bark Glass': 'застеклённая коровая',
    'Stable Horse': 'лошадиная конюшенная'
}

def translate_phrase(text):
    for en_p, ru_p in sorted(PHRASES.items(), key=lambda x: -len(x[0])):
        text = re.sub(r'\b' + re.escape(en_p) + r'\b', ru_p, text)
    
    words = text.split()
    translated_words = []
    for w in words:
        if w in WORDS_MAP:
            translated_words.append(WORDS_MAP[w])
        else:
            translated_words.append(w)
    return " ".join(translated_words)

def translate_full_entry(en_name):
    if en_name == "Dramatic Doors": return "Dramatic Doors"
    if en_name == "Dramatic Doors: Chipped": return "Dramatic Doors: Chipped"
    if en_name == "Dramatic Doors: Macaw's Doors": return "Dramatic Doors: Macaw's Doors"
    if en_name == "Dramatic Doors: ManyIdeas Doors": return "Dramatic Doors: ManyIdeas Doors"
    if en_name == "Waterloggable Doors": return "Затопляемые двери"
    if en_name == "Waterloggable Fence Gates": return "Затопляемые калитки"
    if "Allow doors to be waterlogged" in en_name:
        return "Позволяет дверям находиться под водой. Включите для разрешения затопления водой. Отключите для совместимости с некоторыми модами. Требуется перезапуск после изменения. По умолчанию: включено"
    if "Allow fence gates to be waterlogged" in en_name:
        return "Позволяет калиткам находиться под водой. Включите для разрешения затопления водой. Отключите для совместимости с некоторыми модами. Требуется перезапуск после изменения. По умолчанию: включено"

    prefix = ""
    if en_name.startswith("Tall "):
        prefix = "Высокая "
        core = en_name[5:]
    elif en_name.startswith("Short "):
        prefix = "Низкая "
        core = en_name[6:]
    else:
        return en_name

    is_placeholder = "(Placeholder)" in core
    is_legacy = "(Legacy)" in core
    core = re.sub(r'\s*\((Placeholder|Legacy)\)', '', core).strip()

    suffix = " дверь"
    if core.endswith(" Door"):
        core = core[:-5].strip()
    elif core.endswith(" Trapdoor"):
        prefix = "Высокий " if prefix.startswith("Высокая") else "Низкий "
        suffix = " люк"
        core = core[:-9].strip()
    elif core.endswith(" Fence Gate"):
        suffix = " калитка"
        core = core[:-11].strip()

    translated_core = translate_phrase(core)
    result = prefix + translated_core + suffix

    if is_legacy:
        result += " (Устаревшая)"
    if is_placeholder:
        result += " (Заполнитель)"

    # Clean double spaces
    result = re.sub(r'\s+', ' ', result).strip()
    return result

def main():
    with open(EN_PATH, "r", encoding="utf-8") as f:
        en_data = json.load(f)

    ru_data = {}
    for k, v in en_data.items():
        ru_data[k] = translate_full_entry(v)

    os.makedirs(os.path.dirname(RU_TARGET), exist_ok=True)
    with open(RU_TARGET, "w", encoding="utf-8") as f:
        json.dump(ru_data, f, ensure_ascii=False, indent=2)

    os.makedirs(os.path.dirname(GAME_TARGET), exist_ok=True)
    with open(GAME_TARGET, "w", encoding="utf-8") as f:
        json.dump(ru_data, f, ensure_ascii=False, indent=2)

    print(f"Translated and saved {len(ru_data)} keys successfully!")

if __name__ == "__main__":
    main()
