# 07_DIFFICULTY — Hidden Modifiers, Scaling Formulas & AI

## 🧠 Анализ факторов и модификаторов сложности

Сложность боёв в Poké Gyms определяется не одной переменной, а совокупностью **5 скрытых механик**:

---

## 📐 1. Формула расчёта эффективного уровня игрока (`getPartyLevel`)

* **Исходный код**: `kubejs/startup_scripts/cobblemon/cobblemonUtils.js` (строки 8–31)

```javascript
global.getPartyLevel = (player) => {
  const party = global.getPlayerParty(player);
  if (party == undefined) return 0;
  let partyCount = 0;
  let levelSum = 0;
  let levelHighest = 0;
  let hasBanned = false;
  party.forEach((pokemon) => {
    if (pokemon.isLegendary() || pokemon.isMythical()) hasBanned = true;
    levelSum += pokemon.level;
    if (levelHighest < pokemon.level) levelHighest = pokemon.level;
    partyCount++;
  });
  if (partyCount == 0) return 0;
  if (hasBanned) return 105;
  let levelHighestCount = 0;
  party.forEach((pokemon) => {
    if (levelHighest == pokemon.level) levelHighestCount++;
  });
  let levelAverage = Math.round(levelSum / partyCount);
  if (Math.round(levelAverage * 1.25) < levelHighest) return levelHighest;
  if (levelHighestCount >= 3) return levelHighest;
  return levelAverage;
};
```

### Разбор скрытых правил:
1. **Бан Легендарок (Level 105)**:  
   Если в группе есть хотя бы один Legendary или Mythical покемон, функция возвращает **105**. На обычном подиуме проверка `levelAverage > 100` выдает ошибку `"banned_mon"` и блокирует бой.
2. **Анти-чит на одного перекачанного покемона (Overlevel Anti-Cheese)**:  
   Если уровень самого сильного покемона превышает средний уровень группы более чем на 25% ($\text{levelAverage} \times 1.25 < \text{levelHighest}$), игра **игнорирует средний уровень и выставляет тир по максимальному покемону**!
   * *Пример*: 5 покемонов 10 уровня и 1 покемон 80 уровня (средний = 22). Так как $22 \times 1.25 = 28 < 80$, подиум установит **Tier 75 (уровень 80)**, против которого ваши слабые покемоны мгновенно погибнут.
3. **Правило большинства сильнейших**:  
   Если 3 или более покемонов имеют максимальный уровень (`levelHighestCount >= 3`), эффективным уровнем также признается максимальный.

---

## 🤖 2. Шкала уровней Искусственного Интеллекта (AI Levels)

Мод RCTMod и Cobblemon Showdown поддерживают градации боевого интеллекта:

| AI Level | Применение в сборке | Особенности поведения |
| :---: | :--- | :--- |
| **0** | Standard Tiers 10–75 | Случайный выбор атак из 4 доступных. Полное отсутствие переключений покемонов (замен). |
| **7** | League Bosses 1–8 | Базовый босс-AI: предпочитает атаки с супер-эффективным уроном, учитывает иммунитеты. |
| **9** | Elite Easy, Tier 95 | Продвинутый соревновательный AI: оценивает предсказанный урон, использует сетапные атаки (Swords Dance, Nasty Plot), защитные мувы (Protect, Substitute). |
| **11** | Elite Hard, Tier 9 Bosses | Максимальный соревновательный AI Showdown: тактические замены на резисты, предсказание переключений игрока, управление хазардами (Stealth Rock) и таймингами статусных состояний. |

---

## 📈 3. Динамика EV и IV по тирам сложности

```text
[Tier 10-75] ──► EV: 0-16%  │ 6IV: 0-16%  │ AI: 0  (Казуальные тренеры)
[Tier 80-95] ──► EV: 40-86% │ 6IV: 37-89% │ AI: 0-9 (Сложные тренеры)
[Elite Easy] ──► EV: 71%    │ 6IV: 47%    │ AI: 0-9 (Элитные тренеры 96 ур.)
[Elite Hard] ──► EV: 99.4%  │ 6IV: 99.0%  │ AI: 11  (Соревновательный турнирный уровень 100 ур.)
[Tier 9 Boss] ─► EV: 100%   │ 6IV: 100%   │ AI: 11  (Финальные боссы Лиги)
```

---

## ⚖️ 4. Эскалация рисков серии побед (Winstreak Risk Scaling)

Формула штрафа за поражение:
$$\text{Fee} = \min\Big(\text{round}(\text{balance} \times 0.05) \times (\text{wins} + 1), 10000\Big) \times (2 \text{ при trainer\_lvl\_8})$$

* С каждой победой множитель $(\text{wins} + 1)$ увеличивает финансовый риск при ошибке.
* При поражении **серия побед полностью сбрасывается в ноль**, откатывая прогресс до ближайшего сундука за 10/100 побед или медали за 15 побед.
