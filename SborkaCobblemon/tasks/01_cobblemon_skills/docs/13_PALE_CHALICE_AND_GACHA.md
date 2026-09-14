# Бледная чаша, Гачамон и Лут-боксы (Pale Chalice & Gacha System)

> **Глубокий технический аудит ритуалов Чаши, Гача-капсул, TM-паков и Лут-боксов**  
> *Содержит формулы шансов, разбор скриптов `cobblemonFillChalice.js`, `cobblemonGachaPools.js`, `cobblemonLootOpening.js` и скрытые таланты.*

---

## 1. Бледная чаша и Ритуал Гиратины (Pale Chalice)

**Бледная чаша (`sunlit_cobblemon:pale_chalice`)** — мистический алтарный сосуд, используемый для наполнения жидкостями Бледного мира и вызова рейдового босса Искажённого мира.

### 1.1. Логика скрипта `cobblemonFillChalice.js`
Взаимодействие с чашей требует обязательного ношения Очков Силф в слоте Curios:
```javascript
BlockEvents.rightClicked("sunlit_cobblemon:pale_chalice", (e) => {
    const { block, hand, player, level, item, server } = e;
    if (hand !== "MAIN_HAND") return;
    if (!['sunlit_cobblemon:liquid_pale', 'sunlit_cobblemon:liquid_antimatter'].includes(item.id)) return;
    if (!global.hasScope(player)) {
        player.tell(Text.translatable("sunlit_cobblemon.need_scope").red());
        return;
    }
    if (player.isFake()) return;
    if (item.id == 'sunlit_cobblemon:liquid_antimatter') {
        block.set("windswept:chiseled_cut_lunalite_bricks");
        summonRaidLegendary(level, server, player, item, block, "giratina", 100)
    } else {
        if (block.properties.get("full") == "true") return;
        block.set(block.id, { full: "true" });
    }
    item.shrink(1)
    server.runCommandSilent(`playsound minecraft:item.bottle.fill block @a ${block.x} ${block.y} ${block.z}`);
});
```

### 1.2. Эффекты жидкостей в чаше:
1. **Жидкая бледность (`liquid_pale`)**:
   - Наполняет чашу (устанавливает состояние `full = true`). Служит источником эссенции для крафтов и ритуалов.
2. **Жидкая антиматерия (`liquid_antimatter`)**:
   - Мгновенно трансформирует чашу в блок луналитовых кирпичей (`windswept:chiseled_cut_lunalite_bricks`).
   - **Призывает Рейдового Босса:** **Giratina (100 Уровень)** с полным набором рейдовых характеристик и уникальным лутом победы!

---

## 2. Гачамон: Капсулы покемонов (Gachamon Capsules)

**Капсула Гачамона (`sunlit_cobblemon:gachamon_capsule`)** — предмет для случайного призыва покемонов с механикой качества еды, редких форм (Magikarp Jump, Alolan, Galarian, Hisuian) и блестящих шансов.

### 2.1. Формула шанса блестящего (Shiny Chance)
Шанс появления Shiny-покемона из капсулы зависит от NBT-качества привязанной еды (`quality_food`):

$$\text{Base Shiny Chance} = \begin{cases} 0.1\% & (0.001) & \text{Обычное / Без качества} \\ 0.25\% & (0.0025) & \text{Качество ★ (1.0)} \\ 0.5\% & (0.005) & \text{Качество ★★ (2.0)} \\ 1.0\% & (0.01) & \text{Качество ★★★ (3.0)} \end{cases}$$

### 2.2. Модификаторы талантов (Stages):
- **Талант «The Gachamonbler» (`the_gachamonbler`)**:
  - **Удваивает шанс Shiny:** $0.1\% \rightarrow 0.2\%$, $1.0\% \rightarrow 2.0\%$!
  - **Снижает требование к спешл-пулу:** Специальный пул открывается уже при качестве $\ge 2.0$ (вместо $3.0$).
  - При открытии капсулы без таланта есть **1% шанс** мгновенно получить предмет таланта `sunlit_cobblemon:the_gachamonbler`!
- **Талант «The Red and The Black» (`the_red_and_the_black`)**:
  - Совершает **двойной спавн (Double Roll)** — за одну капсулу призываются сразу 2 покемона, каждый с независимой проверкой на Shiny!
- **Защита от лагов (Anti-Lag Guard):**
  - Если в радиусе 12 блоков уже находится $> 40$ покемонов, капсула не откроется и выдаст предупреждение `sunlit_cobblemon.gachamon_capsule.addiction`!

---

## 3. Наборы технических машин (TM & TR Packs)

При открытии кликом правой кнопкой мыши генерируют диски технических машин:

```javascript
// Обычный TM-пак: 3 дропа (6 с талантом the_red_and_the_black)
Math.random() < 0.12 ? TM : TR;

// Большой TM-пак (Greater TM Pack): 3 дропа (6 с талантом)
Math.random() < 0.20 || index == 2 ? TM : TR; // 3-й слот ВСЕГДА гарантированный TM!

// Призматический TM-пак (Prismatic TM Pack): 3 дропа (6 с талантом)
100% TM (только постоянные многоразовые TM)!
```

### Сводная таблица паков:
| Тип пака | Кол-во дисков (База) | Кол-во с талантом Red&Black | Вероятность TM / TR | Особенности |
| :--- | :---: | :---: | :--- | :--- |
| **TM Pack** | 3 шт. | 6 шт. | $12\%$ TM / $88\%$ TR | Базовый набор |
| **Greater TM Pack** | 3 шт. | 6 шт. | $20\%$ TM / $80\%$ TR | **3-й слот: 100% гарантированный TM** |
| **Prismatic TM Pack** | 3 шт. | 6 шт. | $100\%$ TM | Только многоразовые ценные TM |

---

## 4. Ягодные капсулы и Коробка Поффлетов (Loot Boxes)

1. **Ягодная капсула (`sunlit_cobblemon:berry_capsule`)**:
   - Дропает 1 случайную ягоду из пула `#cobblemon_farmers:common_berries`.
   - При наличии таланта `the_red_and_the_black` дропает **2 ягоды**.
2. **Коробка Поффлетов (`sunlit_cobblemon:pofflet_box`)**:
   - Дропает **4 Поффлета** случайного типа из `#sunlit_cobblemon:pofflet`.
   - При наличии таланта `the_red_and_the_black` дропает **8 Поффлетов**!

---

## 5. Резюме для игрока
1. **Призыв Гиратины:** Наденьте Очки Силф, возьмите колбу `liquid_antimatter` и кликните по `pale_chalice`. Подготовьте сильную команду 100 уровня!
2. **Фарм Shiny из Гачамона:** Всегда используйте капсулы качества ★★★ вместе с разблокированным талантом *The Gachamonbler* и *The Red and The Black* для шанса блестящего $2.0\%$ на каждого из двух призываемых покемонов.
3. **Многоразовые диски атак:** Открывайте *Prismatic TM Pack* под действием *The Red and The Black*, чтобы получать по 6 премиальных TM за раз.
