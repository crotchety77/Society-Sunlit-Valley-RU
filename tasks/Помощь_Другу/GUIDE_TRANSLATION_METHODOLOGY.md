# 📖 Руководство по переводу сборки: Cisco's Fantasy Medieval RPG [Dragonfyre]

> 🎯 **Цель**: Понятный, безопасный и структурированный подход к переводу сборки по всем категориям (Квесты, Происхождения, Классы, Навыки, Предметы модов, Кастомные подсказки KubeJS).

---

## 🛑 1. Разбор проблемы: Почему ломались квесты от чужого русика?

В сборке **Cisco's Fantasy Medieval RPG** квесты хранятся **напрямую в файлах `.snbt`** (папка `config/ftbquests/quests/chapters/`).

* **Что произошло**: Старый русификатор просто перезаписал файлы `.snbt` файлами из старой версии сборки.
* **Результат**: В новой версии изменились ID квестов, добавились новые задачи и награды. Старые файлы перетёрли новую структуру, из-за чего квесты перестали засчитываться или сломали дерево квестов.
* **Правильное решение**: Использовать скрипты экспорта/импорта текста в `.txt` или аккуратно переводить строки `title: "..."`, `subtitle: "..."` и `description: [...]` в актуальных файлах своей версии.

---

## 🗺️ 2. Карта сборки и где что переводить

Путь к сборке: `G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]`

```text
📁 Cisco's Fantasy Medieval RPG [Dragonfyre]
├── 📁 config/ftbquests/quests/chapters/          <-- [КВЕСТЫ] 21 файл .snbt (текст прямо в файле)
└── 📁 kubejs/
    ├── 📁 assets/                                <-- [ЯЗЫКОВЫЕ ФАЙЛЫ ru_ru.json]
    │   ├── 📁 cisco_rpg_origins/lang/ru_ru.json  <-- [КАСТОМНЫЕ ПРОИСХОЖДЕНИЯ] Полубог Люкс, Афина...
    │   ├── 📁 medievalorigins/lang/ru_ru.json    <-- [РАСЫ] Альфик, Арахна и расы Medieval Origins
    │   ├── 📁 origins-classes/lang/ru_ru.json   <-- [КЛАССЫ] Профессии и классы персонажа
    │   ├── 📁 skilltree/lang/ru_ru.json         <-- [НАВЫКИ] Пассивное древо Passive Skill Tree
    │   └── 📁 <любой_мод>/lang/ru_ru.json        <-- [ПРЕДМЕТЫ] Предметы и блоки сторонних модов
    └── 📁 client_scripts/                        <-- [ПОДСКАЗКИ] Кастомные подсказки на предметах (JS)
```

---

## 💡 3. Готовые живые примеры по всем категориям (Уже в игре)

---

### Категория 1: Кастомные Происхождения и Благословения (Cisco RPG Origins)
* **Файл**: `kubejs/assets/cisco_rpg_origins/lang/ru_ru.json`
* **Живой пример (Полубог Люкс и Благословение Афины)**:
```json
{
  "layer.cisco_rpg_origins.divineblessings.name": "Божественное благословение",
  "origin.cisco_rpg_origins.demi_god_lux.name": "Полубог Люкс",
  "origin.cisco_rpg_origins.demi_god_lux.description": "Потомок священного первородного бога и смертного. Священный свет струится по вашим жилам...",
  "power.cisco_rpg_origins.divine_strength.name": "Божественная сила",
  "power.cisco_rpg_origins.divine_strength.description": "Божественное наследие наполняет вас могуществом. Вы наносите на 40% больше урона.",
  "origin.cisco_rpg_origins.athenas_blessing.name": "Благословение Афины",
  "origin.cisco_rpg_origins.athenas_blessing.description": "Вам благоволит Афина, богиня мудрости. Она дарует вам своё защитное благословение.",
  "power.cisco_rpg_origins.athenas_boon_minor.name": "Малый дар стойкости",
  "power.cisco_rpg_origins.athenas_boon_minor.description": "Афина благословляет вашу броню, увеличивая защиту на +10 единиц."
}
```

---

### Категория 2: Происхождения и Расы (Medieval Origins)
* **Файл**: `kubejs/assets/medievalorigins/lang/ru_ru.json`
* **Живой пример (Альфик, Арахна)**:
```json
{
  "origin.medievalorigins.alfiq.name": "Альфик",
  "origin.medievalorigins.alfiq.description": "-§lОсновные особенности§r:\n§o§2+ Бонус без оружия§r\n§o§2+ Уникальное перемещение§r\n§o§6• Плотоядный§r\n§o§c- Защита§r\n\n§lАльфики§r — хитрая раса антропоморфных кошачьих с острыми когтями и превосходной ловкостью.",
  "origin.medievalorigins.arachnae.name": "Арахна",
  "origin.medievalorigins.arachnae.description": "-§lОсновные особенности§r:\n§o§2+ Яд и контроль толпы\n+ Лазание по стенам§r\n§o§6• Плотоядная§r\n§o§c- Голод и броня§r"
}
```

---

### Категория 3: Классы персонажей (Origins Classes)
* **Файл**: `kubejs/assets/origins-classes/lang/ru_ru.json`
* **Живой пример**:
```json
{
  "layer.origins-classes.class.name": "Класс",
  "layer.origins-classes.class.missing_origin.name": "Без класса",
  "layer.origins-classes.class.missing_origin.description": "У вас пока не выбран класс персонажа."
}
```

---

### Категория 4: Древо Пассивных Навыков (Passive Skill Tree)
* **Файл**: `kubejs/assets/skilltree/lang/ru_ru.json`
* **Живой пример (Аффиксы бижутерии и статы)**:
```json
{
  "affix.skilltree:jewelry/attribute/experienced": "Опытный",
  "affix.skilltree:jewelry/attribute/experienced.suffix": "Опыта",
  "affix.skilltree:jewelry/attribute/hasty": "Стремительный",
  "affix.skilltree:jewelry/attribute/hasty.suffix": "Спешки",
  "affix.skilltree:jewelry/attribute/healthy": "Здоровый",
  "affix.skilltree:jewelry/attribute/healthy.suffix": "Здоровья"
}
```

---

### Категория 5: Предметы модов (на примере Mowzie's Cataclysm)
* **Файл**: `kubejs/assets/mowzies_cataclysm/lang/ru_ru.json`
* **Живой пример**:
```json
{
  "item.mowzies_cataclysm.wrought_eye": "Око Кованого рыцаря",
  "item.mowzies_cataclysm.sun_eye": "Око Солнечной птицы",
  "item.mowzies_cataclysm.frostmaw_eye": "Око Ледяной пасти"
}
```

---

### Категория 6: Кастомные подсказки на предметах (KubeJS Tooltips)
* **Файл**: `kubejs/client_scripts/example_custom_tooltips.js`
* **Живой пример**:
```javascript
ItemEvents.tooltip(event => {
    event.add('cisco_mod:champion_coin', [
        Text.gold('★ Награда Чемпиона ★'),
        Text.gray('Используется для торговли с особыми торговцами и выполнения эпических квестов.')
    ])
})
```

---

## ⚡ 4. Как проверять изменения в игре без перезапуска

1. **Для любых JSON файлов в `kubejs/assets/` и тултипов `.js`**:
   * Нажать **`F3 + T`** (Minecraft перезагрузит текстуры и язык за 5–10 секунд).
2. **Для квестов `.snbt` в `config/ftbquests/`**:
   * Нажать **`F3 + T`**, затем ввести в чате **/ftbquests reload** (или перезайти в одиночный мир).

---

## 🧰 5. Простая инструкция: Как перевести любой новый мод

1. Находишь мод в папке `mods/` (например, `irons_spellbooks-1.20.1-3.16.2.jar`).
2. Открываешь его через 7-Zip или WinRAR.
3. Заходишь внутри архива в `assets/irons_spellbooks/lang/en_us.json`.
4. Копируешь нужные строки на английском.
5. Создаёшь в сборке файл `kubejs/assets/irons_spellbooks/lang/ru_ru.json`.
6. Вставляешь туда скопированные строки и переводишь текст справа от двоеточия.
7. Сохраняешь файл в кодировке **`UTF-8`**.
8. В игре нажимаешь **`F3 + T`** — готово!

---

## 📜 6. Пошаговый план: Как переводить FTB Quests

Для квестов доступны 2 рабочих варианта перевода:

---

### Способ А: Напрямую в файлах `.snbt` (Через VS Code или Notepad++)

1. **Создай бэкап** файла главы (например, скопируй `age_of_dragons.snbt` $\rightarrow$ `age_of_dragons.snbt.bak`).
2. **Открой файл `.snbt`** в текстовом редакторе (в кодировке **UTF-8**).
3. **Найди нужный квест** по поиску (`Ctrl + F`) по английскому названию или `description:`.
4. **Переводи только строки в кавычках**:
   ```snbt
   title: "Сразить Скелетозавра"
   subtitle: "Раскалывая Скелетозавра"
   description: [
       "Огромный скелетный динозавр, сотрясающий землю..."
       ""
       "Обитает в &9Долине песка душ &fв &cНезере."
   ]
   ```
5. **Строгие запреты**:
   * ❌ Не меняй и не удаляй `id: "..."`.
   * ❌ Не трогай блоки `tasks: [...]` (условия) и `rewards: [...]` (награды).
   * ❌ Не удаляй скобки `[` `]` и `{` `}`.
6. **Сохрани файл** (`Ctrl + S`).
7. **В игре примени изменения**:
   * Нажми **`F3 + T`**.
   * Введи в чат **/ftbquests reload** — квест обновится!

---

### Способ Б: Через чистые текстовые файлы `.txt` и скрипты (Самый удобный и 100% безопасный)

В папке **[Скрипты_для_помощи_ftb_quests/](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Помощь_Другуу/Скрипты_для_помощи_ftb_quests/)** лежит готовый набор инструментов, который избавляет от необходимости видеть технический код `.snbt`.

#### Шаг 1. Открой файл нужной главы
В папке **[chapters_to_translate/](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/Помощь_Другуу/Скрипты_для_помощи_ftb_quests/chapters_to_translate/)** открой нужную главу (например, `textchampions_of_the_risencolor0be4f3_2.txt` или `age_of_dragons.txt`).

#### Шаг 2. Заполни русский перевод
Вписывай перевод в поля `RU_`:
```text
=== [КВЕСТ 1 | ID: 1F42D7C3A2431C43] ===
EN_TITLE: Slay the Skeletosaurus
RU_TITLE: Сразить Скелетозавра

EN_SUBTITLE: Splintering the Skeletosaurus
RU_SUBTITLE: Раскалывая Скелетозавра

EN_DESCRIPTION:
A massive skeletal dinosaur that stomps the ground, creating shockwaves and tail slams. 
Found roaming &9the Soul Sand Valley &fin &cthe Nether.

RU_DESCRIPTION:
Огромный скелетный динозавр, сотрясающий землю мощными ударами лап, создающий ударные волны и сокрушающий врагов хвостом.
Обитает в &9Долине песка душ &fв &cНезере.

--- КОНЕЦ КВЕСТА 1F42D7C3A2431C43 ---
```
*(Если оставить поле `RU_` пустым — квест в игре останется оригинальным).*

#### Шаг 3. Запусти импорт в игру
Сохрани файл и запусти скрипт:
```bash
python import_quests.py
```
Скрипт сам создаст бэкап `.bak`, проверит синтаксис и вставит перевод в игру.

#### Шаг 4. Обнови игру
В игре нажми **`F3 + T`** и введи **/ftbquests reload**.
