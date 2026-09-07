# Технический аудит механик мода Legendary Creatures (Level 1)

**Мод:** `Legendary Creatures` (`legendarycreatures`)  
**Версия JAR:** `legendarycreatures-1.20.1-1.1.1.3.jar`  
**Статус локализации:** ✅ 100% (102/102 строк)

---

## 1. Сводный реестр механик и доступность мобов в сборке

| Сущность / Предмет | ID объекта | Статус в сборке | Где появляется / Механика |
| :--- | :--- | :---: | :--- |
| **Пожиратель трупов** | `legendarycreatures:corpse_eater` | 🟢 **АКТИВЕН (БОСС-МОБ)** | 💀 Спавнится в **Пещере Черепа** (`society:skull_cavern`) в шахтах с баффами (Здоровье ×7, Урон ×3) |
| **Пустынный моджо** | `legendarycreatures:desert_mojo` | 🟢 **АКТИВЕН** | 🏜️ Спавнится в подземных биомах Society (`desert_caves`, `desert_fault`) |
| **Лесной моджо** | `legendarycreatures:forest_mojo` | 🟢 **АКТИВЕН** | 🌿 Спавнится в биоме пышных пещер Society (`lush_caverns`) |
| **Пугало** | `legendarycreatures:scarecrow` | 🔴 **ВЫКЛЮЧЕНО** | Отключён спавн на полях в `legendarycreatures-common.toml` и заблокирован в Overworld |
| **Соломенная шляпа** | `legendarycreatures:straw_hat` | ⚠️ **ОТКЛЮЧЕНО** | Скрыта автором в `globalRemovedItems.js` (защита от пугала не требуется) |
| **Гончая** | `legendarycreatures:hound` | 🔴 **ВЫКЛЮЧЕНО** | Спавн в Overworld заблокирован в `incontrol/spawn.json` |
| **Скорпионы (3 вида)** | `...:scorpion`, `...:scorpion2/baby` | 🔴 **ВЫКЛЮЧЕНО** | Спавн в Overworld заблокирован в `incontrol/spawn.json` |
| **Павлиньи пауки (3 вида)**| `...:peacock_spider*` | 🔴 **ВЫКЛЮЧЕНО** | Спавн в Overworld заблокирован в `incontrol/spawn.json` |
| **Лягушки-быки (3 вида)** | `...:bullfrog*` | 🔴 **ВЫКЛЮЧЕНО** | Спавн в Overworld заблокирован в `incontrol/spawn.json` |
| **Виспы (Огоньки)** | `...:wisp`, `...:nether_wisp` | 🟡 **ТОЛЬКО ЧАСТИЦЫ** | Сами сущности выключены; частицы `wisp_particle` используются в механизмах Society |
| **Эффект «Судороги»** | `effect.legendarycreatures.convulsion` | 🟢 **АКТИВЕН** | Применён в ядах Society и у Пыльных слаймов (`dusty.json`) |
| **Эффект «Опутывание»** | `effect.legendarycreatures.root` | 🟡 **ТЕХНИЧЕСКИЙ** | Механика сковывания движений игрока |

---

## 2. Глубокий реверс-инжиниринг настроек сборки Society

### 🚫 Тотальная блокировка спавна мода в Обычном мире (Overworld)
В файле `config/incontrol/spawn.json` разработчик сборки прописал жёсткое глобальное правило:
```json
{
  "mod": "legendarycreatures",
  "dimension": "minecraft:overworld",
  "result": "deny"
}
```
> **Вывод:** Ни один моб мода Legendary Creatures **НЕ появляется** в обычном мире на поверхности.

---

### 🌾 Механика Пугала и Соломенной шляпы (Scarecrow)
1. В `config/legendarycreatures/legendarycreatures-common.toml` параметр ломания блоков полностью отключён:
   `"Scarecrow Breaking Block Spawn " = false`
2. Конфиг `config/legendarycreatures/json/scarecrow-spawn.json` полностью пуст (`{ "block_names": {}, ... }`).
3. **Пугало не появляется при сборе урожая.**
4. В связи с этим Соломенная шляпа (`straw_hat`), предотвращавшая спавн пугала, потеряла смысл и была отключена автором сборки в `startup_scripts/globalRemovedItems.js:L518`.

---

### 💀 Элитный монстр: Пожиратель трупов (`corpse_eater`)
В `config/incontrol/spawn.json` Пожиратель трупов настроен как элитный опасный моб пещерного эндгейма:
* **Локация:** Только в измерении **Пещера Черепа (`society:skull_cavern`)** внутри заброшенных шахт (`hopo:mineshaft/*`).
* **Модификаторы In Control:**
  - Здоровье: **`×7`** (семикратный запас HP).
  - Урон: **`×3`** (тройной урон).
  - Броня: **`+5`**.
  - Скорость: **`0.4`** (медленный, но сокрушительный).
* **Кастомный лут:** Модифицирован в `server_scripts/loot/generalLoot.js:L30`.

---

### 🏜️ Подземные големы: Моджо (`desert_mojo` и `forest_mojo`)
* **Пустынный моджо (`desert_mojo`):** Прописан в генераторах кастомных подземных биомов `data/society/worldgen/biome/desert_caves.json` и `desert_fault.json`.
* **Лесной моджо (`forest_mojo`):** Прописан в генераторе биома пышных пещер `data/society/worldgen/biome/lush_caverns.json`.
