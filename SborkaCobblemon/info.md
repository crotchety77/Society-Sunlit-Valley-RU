# ⚡ Society: Sunlit Cobblemon — Рабочее пространство перевода и аудита

> **Путь к установленной сборке:**  
> `G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon`

---

## 🚨 Железный регламент изоляции (Правило 15 AGENTS.md)

1. **Полная изоляция от основной сборки:**
   - Основная сборка **Society: Sunlit Valley** (`D:\ModrinthApp\profiles\Society_ Sunlit Valley`) и её файлы в корневой папке `translations/` являются независимыми.
   - **Запрещено** переносить Cobblemon-специфичные файлы, переводы или квесты в корень `translations/` или синхронизировать их в `D:\ModrinthApp\...`.
   - Вся работа над сборкой Cobblemon ведётся **СТРОГО внутри папки `SborkaCobblemon/`**.

2. **Защита целостности FTB Quests (`en_us.json`):**
   - В сборке Cobblemon файл `kubejs/assets/ftbquestlocalizer/lang/en_us.json` содержит **2317 ключей** (включая 673 уникальных квеста тренеров и покемонов).
   - **Запрещено** перезаписывать `en_us.json` файлом из базовой сборки Sunlit Valley (иначе пропадут тексты 673 квестов и они превратятся в битые сырые ключи `ftbquests.chapter...`).

3. **Отдельный скрипт синхронизации:**
   - Все изменения для сборки Cobblemon применяются исключительно скриптами из `SborkaCobblemon/scripts/`, нацеленными на `G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon`.

---

## 🗂 Структура директории `SborkaCobblemon/`

```text
SborkaCobblemon/
├── info.md                     # Этот документ (манифест, реестр нововведений и регламент)
├── tasks/                      # Папки задач (аудит механик, квесты, тултипы, перевод)
│   ├── 01_cobblemon_skills/    # 7 новых книг навыков и интеграция с Puffish Skills
│   │   └── docs/               # Аудиты механик:
│   │       ├── MECHANICS-AUDIT.md # Аудит 8 рангов и 7 книг навыков
│   │       ├── workers.md      # Формулы и математика Cobblemon Farmers
│   │       ├── ranching_guide.md # Полный гайд по Ранчо (Ranching Station)
│   │       ├── friendship_guide.md # Полный гайд по Дружбе покемонов
│   │       ├── sun_raid_statue.md # Полный гайд по Статуям Солнечного Рейда
│   │       └── gem_box_guide.md # Полный гайд по Шкатулке самоцветов и Реджи-Титанам
│   ├── 02_ftb_quests/          # 673 новых квеста тренеров и покемонов
│   ├── 03_sunlit_cobblemon/    # Мод sunlit_cobblemon (покеболы, рейды, гачамоны, значки)
│   ├── 04_cobblemon_farmers/   # Мод cobblemon_farmers (блюда и продукты)
│   └── 05_tooltips_and_jei/    # Покемон-тултипы и рецепты KubeJS
├── translations/               # Изолированные файлы переводов для Cobblemon
│   ├── ftbquests/              # Дополнения к квестам ru_ru.json
│   ├── skills/                 # Навыки и книги
│   └── mods/                   # sunlit_cobblemon, cobblemon_farmers, simpletms и др.
├── scripts/                    # Скрипты применения, валидации и синхронизации
│   └── sync_cobblemon.py       # Синхронизация в G:\curseforge\...\Society Sunlit Cobblemon
└── dist/                       # Готовый пакет русификатора для сборки Cobblemon
```

---

## 🔍 Реестр нововведений сборки Cobblemon

### 1. Новые книги навыков (7 литературных книг в `skillBooks.js`)
По аналогии с базовыми книгами Sunlit Valley, автор сборки добавил 7 книг навыков с каламбурными названиями мировой классики:

| ID предмета | Skill ID | Литературный первоисточник / Англ. название | Механика и эффект в игре |
| :--- | :--- | :--- | :--- |
| `sunlit_cobblemon:the_art_of_battle` | `5bh79ul0je3425c5` | Сунь-цзы: *Искусство войны* (*The Art of Battle*) | Лига Sunlit выплачивает на **+25%% больше монет** за победу в битвах. |
| `sunlit_cobblemon:berry_labor_and_capital` | `l9v5igsptrxg1o7w` | К. Маркс: *Капитал* (*Berry, Labor, and Capital*) | **+5 слотов** для покемонов-работников на ферме. |
| `sunlit_cobblemon:bottlecaps_and_nothingness` | `yi3sssvxzz4h5ufn` | Ж.-П. Сартр: *Бытие и ничто* (*Bottlecaps and Nothingness*) | Небольшой шанс найти **Крышки от бутылок** (Bottlecaps) в сундуках с лутом. |
| `sunlit_cobblemon:braiding_surprisegrass` | `7qievsed72hmchf4` | Р. У. Киммерер: *Плетение травы* (*Braiding Surprisegrass*) | **В 2 раза выше шанс** встретить покемона при добыче руд и сборе урожая / плодов деревьев. |
| `sunlit_cobblemon:the_gachamonbler` | `fqdq5o5mfwl2uaeg` | Ф. М. Достоевский: *Игрок* (*The Gachamonbler*) | В капсулах Гачамонов шанс на шайни-покемона **удвоен**. Капсулы золотого качества и выше спавнят покемонов только из бонусного пула. |
| `sunlit_cobblemon:mukbeth` | `imv02rfzfi83dndp` | У. Шекспир: *Макбет* (*Mukbeth* — игра слов с покемоном Muk) | Граймер, Траббиш и их эволюции больше **не клюют на Поке-поплавки** при рыбалке. |
| `sunlit_cobblemon:savage_sun` | `ecwqhex344gxang8` | *Дикое солнце* (*Savage Sun*) | Статуи Солнечных рейдов имеют **15%% шанс проигнорировать кулдаун** активации. |

---

### 2. Главы и квесты FTB Quests (673 новых квеста)
- **Иерархия рангов тренеров (8 тиров прогрессии):**
  - 🌿 **Twig** (Прут)
  - 🪨 **Rock** (Камень)
  - ⛓️ **Iron** (Железо)
  - 🟡 **Gold** (Золото)
  - 💎 **Diamond** (Алмаз)
  - 🟣 **Iridium** (Иридий)
  - 🏺 **Ancient** (Древний)
  - 🌈 **Prismatic** (Призматический)
- **Новые главы квестов:**
  - `ic__cobblemon.snbt` — Введение в мир Cobblemon и ловля покемонов.
  - `rare_pokmon.snbt` — Редкие и легендарные покемоны (Mew, Rayquaza, Tao Trio, Darkrai).
  - `cobble_berries.snbt` — Ягоды Cobblemon, мутации и крафты.
  - `hunting_legends.snbt` — Охота за легендами, алтари биокуполов, червоточины Ультра-чудовищ.

---

### 3. Пространства имён (Namespaces) Cobblemon
- `sunlit_cobblemon` (**508 ключей**):
  - Покеболы (Poké Ball, Great Ball, Ultra Ball, Master Ball, Beast Ball и др.).
  - Значки тренеров, алтари, статуи рейдов, капсулы Гачамонов, солнечные кристаллы.
  - Поке-руда, снаряжение тренера, приманки и скоупы (Silph Scope).
- `sunlit_cobblemon_tips` (**17 ключей**): советы на экранах загрузки по механике покемонов.
- `cobblemon_farmers` (**36 ключей**): фермерские блюда, поке-лакомства, нарезки и выпечка.
- `simpletms` (**15 ключей**): диски TM для обучения атакам.

---

## 🚀 Дорожная карта (Roadmap) работ

1. **Этап 1: Инфраструктура и скрипт синхронизации (`SborkaCobblemon/scripts/sync_cobblemon.py`).**
2. **Этап 2: Книги навыков и ветка Puffish Skills (7 книг, формулы, экранирование `%%`, регистрация в глоссарии).**
3. **Этап 3: Полная локализация и аудит мода `sunlit_cobblemon` (508 ключей + 17 tips).**
4. **Этап 4: Локализация мода `cobblemon_farmers` и `simpletms`.**
5. **Этап 5: Локализация и форматирование 673 квестов FTB Quests (`&6`, `&a`, `{@pagebreak}`).**
6. **Этап 6: Тултипы `[Shift]` для предметов Cobblemon и сборка единого дистрибутива `SborkaCobblemon/dist/`.**
