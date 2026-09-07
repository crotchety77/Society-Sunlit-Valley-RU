# Задача: Полный аудит и подсказки системы рыбалки (task_aquaculture_hooks)

**Моды:** Aquaculture 2, Crabber's Delight, Stardew Fishing, Society KubeJS  
**Область:** Удочки, 15 крючков, лески, приманки, крабовые ловушки, поплавки, KubeJS-триггеры, пределы зачарований (Hard Caps) и игровые подсказки.

---

## 🎯 Цели задачи:
1. **Глубокий технический аудит всей механики:**
   * Проверить байткод Java-классов модов (`Hooks`, `HookItem`, `AquaFishingRodItem`, `BaitItem`, `CrabTrapBlockEntity`).
   * Проверить KubeJS-скрипты сборки (`fishingRodLeveling.js`, `fishingLoot.js`, `fishingSkills.js`, `baitMaker.js`, `modifyItems.js`).
   * Зафиксировать точные формулы, скрытые шансы, дропы, лимиты прокачки (Lure IV, Luck of the Sea VI) в едином файле [MECHANICS-AUDIT.md](file:///c:/Users/Foxi8/OneDrive/Рабочий%20стол/СозданиеПеревода/tasks/task_aquaculture_hooks/docs/MECHANICS-AUDIT.md).
2. **Создание файла согласования `new_translate.md`:**
   * Сформировать Блок 1 (визуальный макет в игре) и Блок 2 (точные строки JSON и подсказок для `addTooltips.js` и `translations/`).
3. **Скрипт синхронизации и физической верификации `apply_and_sync.py`:**
   * Автоматическое применение изменений и проверка физических файлов в `D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\`.
