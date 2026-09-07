---
name: ui_formatting_and_layout
description: Стандарты оформления текста, вёрстка UI, переносы строк, цветовое кодирование, тултипы и раскрывающийся [SHIFT] в KubeJS.
---

# Навык: Вёрстка UI, тултипы и типографика (ui_formatting_and_layout)

Навык регламентирует стандарты оформления текстов, физические ограничения окон интерфейса (GUI) в Minecraft / KubeJS / FTB Quests и правила визуальной подачи информации игроку.

---

## 1. Физические ограничения и специфика GUI

| Элемент интерфейса | Физический лимит / Специфика | Правило оформления |
| :--- | :--- | :--- |
| **Записки Candlelight** (`candlelight:note_paper_written`) | Высота GUI строго **128px** (~10 строк) | Не более **6–8 строк** текста. Длинные тексты обрезаются снизу. |
| **FTB Quests (окно квеста)** | Ограничение высоты карточки | Не более **4–6 строк** на страницу. Разделять длинные тексты тегом `{@pagebreak}`. |
| **Всплывающие подсказки (Tooltips)** | Загромождение экрана при наведении | **1–2 лаконичные строки** в основном тултипе. Детали, формулы и рецепты прятать под `[SHIFT]`. |
| **Диалоги жителей** | Скорость чтения и комфорт | Абзацы до 3 строк. Ключевые термины подсвечивать `&6`. |

---

## 2. Цветовая палитра и форматирование

### Цветовые коды (в FTB Quests и JSON):
* `&6` / `§6` — **Золотой/Оранжевый**: ключевые термины, имена персонажей, названия предметов, механики.
* `&e` / `§e` — **Жёлтый**: числа, значения, проценты, награды, горячие клавиши.
* `&a` / `§a` — **Зелёный**: положительные эффекты, завершённые условия, бонусы.
* `&c` / `§c` — **Красный**: предупреждения, штрафы, ограничения, опасности.
* `&b` / `§b` — **Голубой/Аква**: особые свойства, кристаллы, магия, алмазное качество.
* `&d` / `§d` — **Фиолетовый/Розовый**: иридиевое качество, легендарные свойства.
* `&7` / `§7` — **Серый**: лор, второстепенные примечания, цитаты, подсказки по управлению.
* `&r` / `§r` — **Сброс цвета**: обязательно ставить после каждого окрашенного слова или фразы!

### Спецсимволы:
* Монета: строго `§e●` (`\u25CF`) с жёлтым цветом в чате, HUD и тултипах.
* Маркеры списков: `▪` или длинное тире `—`.

### 🚨 Экранирование процентов в строках с String.format (FTB Quests и Puffish Skills):
* В **FTB Quests** (`translations/ftbquests/ru_ru.json`) и **Puffish Skills** (`translations/skills/ru_ru.json`) знак процента **ВСЕГДА экранируется как `%%`**:
  * ✅ Правильно: `шанс &e0,5%%&r`, `бонус §a+10%%§7`
  * ❌ Ошибка (вызывает `Format Error` в игре): `шанс &e0,5%&r`

---

## 3. Добавление и кастомизация подсказок к предметам (Tooltips в KubeJS)

Подробное руководство по стандартам тултипов см. в [docs/TOOLTIPS-AND-LOCALIZATION-ARCHITECTURE.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/docs/TOOLTIPS-AND-LOCALIZATION-ARCHITECTURE.md).

### Вариант А: Обычный тултип с трансляцией или аргументами (%s)
Используется для коротких подсказок к механике или рецепту (1–2 строки):
1. **Файл скрипта KubeJS:** `kubejs/client_scripts/tooltips/addTooltips.js` (или отдельный файл в `tooltips/`)
   ```javascript
   tooltip.add(
     "namespace:item_name",
     Text.translatable("item.namespace.item_name.description").gray()
   );
   // С динамическим аргументом станка/блока:
   tooltip.add(
     "society:upgrade_item",
     Text.translatable(
       "item.society.upgrade_item.description",
       Text.translatable("block.society.machine").darkGreen()
     ).green()
   );
   ```
2. **Языковые ключи:** в `kubejs/assets/<namespace>/lang/ru_ru.json` и `translations/mods/<namespace>.json`.

---

### Вариант Б: Раскрывающийся тултип под клавишу [SHIFT] и чтение NBT
Используется для подробных инструкций, формул, уровней прокачки и NBT:
1. **Файл скрипта KubeJS:** `kubejs/client_scripts/tooltips/addTooltips.js`
   ```javascript
   tooltip.addAdvanced("namespace:item_name", (item, advanced, text) => {
     if (tooltip.shift) {
       text.add(1, Text.translatable("tooltip.namespace.item_name.details").gray());
       if (item.nbt && item.nbt.contains("level")) {
         text.add(2, Text.translatable("tooltip.namespace.item_name.level", item.nbt.getInt("level")).gold());
       }
     } else {
       text.add(1, Text.translatable("tooltip.society.hold_shift"));
     }
   });
   ```
2. **Языковые ключи:** `tooltip.namespace.item_name.details` и `tooltip.society.hold_shift` в языковых файлах `ru_ru.json`.

---

### Вариант В: Кастомная рамка тултипа (Tooltip Overhaul через ресурспак)
Мод `Tooltip Overhaul` поддерживает загрузку кастомных рамок напрямую из ресурспаков (`kubejs/assets/`), что исключает необходимость править системную папку `config/` игры.

1. **Файл конфигурации в проекте:**
   `translations/society/tooltipoverhaul/custom_frames.json` (автоматически синхронизируется в `kubejs/assets/society/tooltipoverhaul/custom_frames.json`).

2. **Формат записи:**
   ```json
   {
     "frames": [
       {
         "texture": "tooltipoverhaul:textures/overlay/diamond_frame.png",
         "items": [
           "quark:diamond_heart"
         ],
         "gradientType": "custom",
         "borderType": "auto_gradient"
       }
     ]
   }
   ```

3. **Доступные текстуры рамок и эффекты:**
   * `diamond_frame.png` — Алмазная рамка (голубая/aqua).
   * `king_frame.png` (+ `"specialEffect": "metal_shining"`) — Королевская золотая рамка с переливом (как у `society:prismatic_shard`).
   * `amethyst_frame.png` — Аметистовая рамка (фиолетовая).
   * `gear_frame.png` — Механическая шестерёнчатая рамка (стимпанк/Create).
   * `amber_frame.png` — Янтарная/медовая рамка.
   * `silver_frame.png` — Серебряная рамка.

4. **Перезагрузка:** применяется на лету по **`F3 + T`**.

---

## 4. Стандарты разметки в файлах согласования (`new_translate`)

В файле `tasks/<task_name>/new_translate` текст всегда представляется в двух блоках:

### Блок 1. Визуальный макет (как видит игрок в игре)
```text
==================================================
  Вкус к жизни
==================================================
Мод Spice of Life: Onion Edition поощряет разнообразный рацион.

Открывая новые блюда и расширяя меню, вы будете получать приятные бонусы из кулинарной книги — и главное, увеличите максимальный запас здоровья!
--------------------------------------------------
[✓] Понятно!
==================================================
```

### Блок 2. Исходный код / Ключи локализации
```json
{
  "ftbquests.chapter.welcome.title": "Вкус жизни",
  "ftbquests.chapter.welcome.description1": "Мод Spice of Life: Onion Edition поощряет разнообразный рацион.",
  "ftbquests.chapter.welcome.description2": "Открывая новые блюда и расширяя меню, вы будете получать приятные бонусы из кулинарной книги — и главное, увеличите максимальный запас здоровья!"
}
```
