Майнкрафт. Сборка.
Главная папка игры: D:\ModrinthApp\profiles\Society_ Sunlit Valley

Новая директория, рабочее пространство создано для улучшения версии перевода. Сейчас в папке находится 2 файла.
1. en_us.json - оригинальный перевод для версии игры 4.1.4
Весь путь: D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_skills\lang\en_us.json
2. ru_ru.json - любительский перевод для версии 4.0.4
Весь путь: D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\society_skills\lang\ru_ru.json
3. папка puffish_skills - Навыки и узлы skills, ссылки на локализацию
D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\data\society\puffish_skills
3. Навыки и узлы (skills/): JSON-структура каждого скилла. Там прописаны:
Координаты узла в сетке GUI.
Необходимые очки опыта или зависимости (какой скилл должен быть открыт до него).
Ссылки на локализацию (title, description): например, "title": "society_skills.farming.tiller".
Награды (rewards):
Стандартные атрибуты Minecraft (например, minecraft:generic.attack_damage, minecraft:generic.movement_speed, minecraft:generic.max_health).
Уровни зачарований / эффекты.
Теги/метки (tags), выдаваемые игроку.
4. папка Server Scripts (script.js): логика выдачи и снятия эффектов.
D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\server_scripts
Там прописаны конкретные команды, которые выполняются при взятии или сбросе навыка (например, give effect, modify attribute, send message).

5. папка 
D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\server_scripts
6. папка OldVersion404 <- старые файлы для сравнения

1. В версиях могли поменяться особенности/правки баланса 
2. Обратил внимание, что цветовые теги теперь присваиваются через \n§c, а не через &c


📁 society_skills/lang/ru_ru.json — отвечает только за древо навыков (Puffish Skills) и их описания в меню прокачки (лежит в корне рабочей папки: `ru_ru.json`).
📁 society/lang/ru_ru.json — отвечает за все механизмы, блоки и сообщения в чате/на экране, включая Ящики отправки товаров, Садки, Банковские счета и утренние уведомления в 6:00 (скопирован в рабочую папку `society_lang/ru_ru.json`).