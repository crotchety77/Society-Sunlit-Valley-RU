# Очередь аудита и перевода товаров NPC (trades_items_NPC)

Регламент аудита: «То, что видит игрок — то и переводим».
Для каждого NPC создаётся отдельная папка `tasks/trades_items_NPC/<Имя>/` с детальным файлом анализа `<Имя>.md` и рабочими файлами `new_translate.md` / `scripts/apply_and_sync.py`.

---

## 📊 Статус очереди NPC

| # | Папка / NPC | Роль / Описание | Файл магазина | Товаров | Статус |
| :-: | :--- | :--- | :--- | :-: | :-: |
| **01** | [`Carlos`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Carlos) | **Карлос** (Странствующий торговец) | `trader.json` | 35 | 🟢 **Завершено** (5 проблемных исправлено) |
| **02** | [`Blacksmith`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Blacksmith) | **Кузнец** (Жеоды, руды, инструменты) | `blacksmith.json` | 20 | 🟢 **Завершено** (Статуя Лунного гнома, цвета, тултипы) |
| **03** | [`Librarian`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Librarian) | **Вероника** (Библиотекарь, ящики, RS, хранилища) | `librarian.json` | 50 | 🟢 **Завершено** (50/50 проверено) |
| **04** | [`Book_Fair`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Book_Fair) | **Книжная ярмарка** (Вероника 20–30 числа) | `book_fair.json` | 30 | ⏳ **На согласовании** (Описание в телефоне обновлено) |
| **05** | [`Market`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Market) | **Торговец с Рынка** (Семена, урожай, удобрения) | `market.json` | 66 | ⚪ Ожидает |
| **06** | [`Carpenter`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Carpenter) | **Плотник** (Стройматериалы, верстаки, декор) | `carpenter.json` | 55 | ⚪ Ожидает |
| **07** | [`Shepherd`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Shepherd) | **Пастух** (Животноводство, лассо, корма) | `shepherd.json` | 20 | ⚪ Ожидает |
| **08** | [`Fisher`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Fisher) | **Рыбак** (Снасти, поплавки, наживки, рыба) | `fisher.json` | 29 | ⚪ Ожидает |
| **09** | [`Banker`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Banker) | **Банкир** (Карты, монеты, чеки, сейфы) | `banker.json` | 18 | ⚪ Ожидает |
| **10** | [`Barkeeper`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Barkeeper) | **Бармен** (Таверна, напитки, блюда) | `barkeeper.json` | 32 | ⚪ Ожидает |
| **11** | [`Witch`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Witch) | **Эвелин** (Ведьма / Травница, зелья, алхимия) | `witch.json` | 38 | ⚪ Ожидает |
| **12** | [`Wise_Oak`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Wise_Oak) | **Мудрый Дуб** (Древнее древо, реликвии) | `wise_oak.json` | 12 | ⚪ Ожидает |
| **13** | [`Wanderer`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Wanderer) | **Странник** (Уникальный редкий лут) | `wanderer.json` | 5 | ⚪ Ожидает |
| **14** | [`Wandering_Baker`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Wandering_Baker) | **Странствующий пекарь** (Выпечка, десерты) | `wandering_baker.json` | 12 | ⚪ Ожидает |
| **15** | [`Wandering_Winemaker`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Wandering_Winemaker) | **Странствующий винодел** (Вино, лозы) | `wandering_winemaker.json` | 10 | ⚪ Ожидает |
| **16** | [`Ribbit_Merchant`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Ribbit_Merchant) | **Лягушонок-торговец** (Болотные редкости) | `ribbit_merchant.json` | 8 | ⚪ Ожидает |
| **17** | [`Ribbit_Fisher`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Ribbit_Fisher) | **Лягушонок-рыбак** (Болотная рыбалка) | `ribbit_fisher.json` | 8 | ⚪ Ожидает |
| **18** | [`Guild`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Guild) | **Гильдия приключений** (Награды гильдии) | `guild.json` | 18 | ⚪ Ожидает |
| **19** | [`Invitations`](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/trades_items_NPC/Invitations) | **Приглашения жителей** (Письма новоселья) | `invitations.json` | 10 | ⚪ Ожидает |
