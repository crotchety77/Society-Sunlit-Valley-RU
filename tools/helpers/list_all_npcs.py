import os
import json
import re

shops_dir = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\data\society_trading\shops"
dialog_dir = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\dialog\lang"
society_lang = r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\translations\society\ru_ru.json"

with open(society_lang, "r", encoding="utf-8") as f:
    society_data = json.load(f)

# NPC mapping from society_trading shops and dialogs
# Let's map filename to NPC name / profession
npc_info = {
    "trader": {"ru_name": "Карлос (Carlos)", "role": "Странствующий торговец (Trader)", "file": "trader.json"},
    "blacksmith": {"ru_name": "Кузнец (Blacksmith)", "role": "Кузнец", "file": "blacksmith.json"},
    "librarian": {"ru_name": "Вероника (Veronica)", "role": "Библиотекарь (Librarian)", "file": "librarian.json"},
    "book_fair": {"ru_name": "Книжная ярмарка (Book Fair)", "role": "Вероника (27-28 числа)", "file": "book_fair.json"},
    "market": {"ru_name": "Торговец с Рынка (Market)", "role": "Рынок семян и продуктов", "file": "market.json"},
    "carpenter": {"ru_name": "Плотник (Carpenter)", "role": "Плотник и строитель", "file": "carpenter.json"},
    "shepherd": {"ru_name": "Пастух (Shepherd)", "role": "Животноводство и корма", "file": "shepherd.json"},
    "fisher": {"ru_name": "Рыбак (Fisher)", "role": "Снасти, наживка и рыбалка", "file": "fisher.json"},
    "banker": {"ru_name": "Банкир (Banker)", "role": "Финансы и хранилище", "file": "banker.json"},
    "barkeeper": {"ru_name": "Бармен (Barkeeper)", "role": "Таверна и напитки", "file": "barkeeper.json"},
    "witch": {"ru_name": "Эвелин (Evelyne / Witch)", "role": "Ведьма / Травница", "file": "witch.json"},
    "wise_oak": {"ru_name": "Мудрый Дуб (Wise Oak)", "role": "Древнее древо", "file": "wise_oak.json"},
    "wanderer": {"ru_name": "Странник (Wanderer)", "role": "Странствующий торговец редким лутом", "file": "wanderer.json"},
    "wandering_baker": {"ru_name": "Странствующий пекарь (Wandering Baker)", "role": "Выпечка и сладости", "file": "wandering_baker.json"},
    "wandering_winemaker": {"ru_name": "Странствующий винодел (Wandering Winemaker)", "role": "Виноделие и саженцы", "file": "wandering_winemaker.json"},
    "ribbit_merchant": {"ru_name": "Лягушонок-торговец (Ribbit Merchant)", "role": "Торговец Риббит", "file": "ribbit_merchant.json"},
    "ribbit_fisher": {"ru_name": "Лягушонок-рыбак (Ribbit Fisher)", "role": "Рыбак Риббит", "file": "ribbit_fisher.json"},
    "guild": {"ru_name": "Гильдия приключений (Guild)", "role": "Награды и контракты гильдии", "file": "guild.json"},
    "invitations": {"ru_name": "Приглашения жителей (Invitations)", "role": "Покупка писем приглашений", "file": "invitations.json"},
}

print("=== СПИСОК ВСЕХ NPC И ИХ МАГАЗИНОВ ===")
for key, info in npc_info.items():
    shop_path = os.path.join(shops_dir, info["file"])
    trades_count = 0
    if os.path.exists(shop_path):
        data = json.load(open(shop_path, "r", encoding="utf-8"))
        trades_count = len(data.get("trades", []))
    print(f"[{key}] {info['ru_name']} | {info['role']} | Товаров: {trades_count}")
