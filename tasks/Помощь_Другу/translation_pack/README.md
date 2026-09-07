# 📦 Папка готового перевода (Translation Pack Template)

Эта папка полностью повторяет структуру инстанса Minecraft сборки **Cisco's Fantasy Medieval RPG [Dragonfyre]**.

---

## 🗂️ Структура папки

```text
📁 translation_pack/
├── 📁 config/
│   └── 📁 ftbquests/
│       └── 📁 quests/
│           └── 📁 chapters/
│               └── 📄 age_of_dragons.snbt  <-- Пример перевода квеста «Бестиарий»
└── 📁 kubejs/
    ├── 📁 assets/
    │   ├── 📁 medievalorigins/lang/ru_ru.json  <-- Расы и происхождения (Альфик, Арахна)
    │   ├── 📁 origins-classes/lang/ru_ru.json   <-- Классы (Без класса, Класс)
    │   ├── 📁 skilltree/lang/ru_ru.json         <-- Пассивное древо навыков (Аффиксы и статы)
    │   └── 📁 mowzies_cataclysm/lang/ru_ru.json <-- Предметы мода без встроенного перевода
    └── 📁 client_scripts/
        └── 📄 example_custom_tooltips.js       <-- Кастомные подсказки на предметах
```

---

## 🚀 Как пользоваться этим шаблоном

1. **Редактирование / Добавление новых переводов**:
   * Для нового мода: создать папку `kubejs/assets/<имя_мода>/lang/ru_ru.json` и вставить туда переводы.
   * Для нового квеста: открыть нужную главу в `config/ftbquests/quests/chapters/<имя_главы>.snbt` и перевести текст в `description` / `title`.

2. **Перенос в игру**:
   * Просто скопировать всё содержимое папки `translation_pack` (папки `config` и `kubejs`) прямо в корень папки своего инстанса сборки в CurseForge:
     `G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]` с заменой файлов.

3. **Обновление в игре**:
   * Нажать **`F3 + T`** (для lang-файлов и тултипов).
   * Ввести **/ftbquests reload** (для квестов).
