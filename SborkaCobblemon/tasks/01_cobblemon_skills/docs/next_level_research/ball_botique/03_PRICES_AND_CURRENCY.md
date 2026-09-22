# 💰 03_PRICES_AND_CURRENCY — Цены и валютная система Ball Boutique

## 1. Валютная система мода Numismatics

Все цены в моде `society_trading` и магазине Ball Boutique задаются в базовых числовых единицах (центах / минимальных единицах Numismatics).

### Номиналы монет Numismatics:
| Монета | Предмет ID | Номинал в единицах | Коэффициент конвертации |
| :--- | :--- | :---: | :--- |
| **Spur** (Шпора) | `numismatics:spur` | **1** | 1 Spur = 1 ед. |
| **Bevel** (Фаска) | `numismatics:bevel` | **8** | 1 Bevel = 8 Spur |
| **Sprocket** (Звёздочка) | `numismatics:sprocket` | **64** | 1 Sprocket = 8 Bevel |
| **Cog** (Шестерня) | `numismatics:cog` | **512** | 1 Cog = 8 Sprocket |
| **Crown** (Корона) | `numismatics:crown` | **4,096** | 1 Crown = 8 Cog |
| **Sun** (Солнце) | `numismatics:sun` | **4,096** | Эквивалент Crown (тематическая монета сборки) |
| **Neptunium Coin** | `numismatics:neptunium_coin` | **65,536** | 1 Neptunium = 16 Sun (16 × 4,096) |

---

## 2. Структура ценообразования капсул

Цены капсул строго фиксированы в JSON-файле магазина `ball_boutique.json`. Они разбиты на 3 чёткие ценовые категории в зависимости от редкости пула:

### Категория А: Стандартные капсулы типов и регионов (10 типов)
*Dragon, Steel, Fairy, Ghost, Rock, Pika, Alolan, Hisuian, Galarian, Magikarp*

| Качество (Tier) | Цена (ед.) | Расчёт в монетах | Множитель от базы |
| :---: | :---: | :--- | :---: |
| **Regular (Q0)** | **8,192** | 2× Sun Coin | $1.0\times$ (База) |
| **Silver (Q1)** | **16,384** | 4× Sun Coin | $2.0\times$ |
| **Gold (Q2)** | **24,576** | 6× Sun Coin | $3.0\times$ |
| **Iridium (Q3)** | **32,768** | 8× Sun Coin | $4.0\times$ |

> **Формула Категории А**: $\text{Price}(Q) = 8192 \times (Q + 1)$

---

### Категория Б: Бюджетные капсулы (2 типа)
*Baby, Common*

| Качество (Tier) | Цена (ед.) | Расчёт в монетах | Множитель от базы |
| :---: | :---: | :--- | :---: |
| **Regular (Q0)** | **4,096** | 1× Sun Coin | $1.0\times$ (База) |
| **Silver (Q1)** | **8,192** | 2× Sun Coin | $2.0\times$ |
| **Gold (Q2)** | **16,384** | 4× Sun Coin | $4.0\times$ |
| **Iridium (Q3)** | **24,576** | 6× Sun Coin | $6.0\times$ |

> **Формула Категории Б**: Прогрессия $4096 \rightarrow 8192 \rightarrow 16384 \rightarrow 24576$.

---

### Категория В: Премиум-набор Стартовиков (Starter Pack)
*Starter Pack (все 27 стартовиков)*

| Качество (Tier) | Цена (ед.) | Расчёт в монетах | Наблюдаемое значение |
| :---: | :---: | :--- | :--- |
| **Regular (Q0)** | **49,152** | 12× Sun Coin | Базовый стартовый набор |
| **Silver (Q1)** | **81,920** | 20× Sun Coin | Серебряный стартер |
| **Gold (Q2)** | **131,072** | 2× Neptunium Coin (32 Sun) | Золотой стартер |
| **Iridium (Q3)** | **245,760** | 3.75× Neptunium (60 Sun) | **245,760 монет** |

> **Разгадка наблюдения игрока**:
> Наблюдение игрока (`Starter Pack, Quality: Iridium, Price: 245,760`) **полностью подтверждено кодом**. Это ровно $60$ Sun монет ($60 \times 4096 = 245760$), что является максимальной ценой среди всех предложений в игре.

---

## 3. Цены постоянных товаров (Permanent Offers)

| Предмет | Цена (число) | Валюта | Дневной лимит |
| :--- | :---: | :--- | :---: |
| **Pofflet Box** (`society:pofflet_box`) | 4,096 | 1× Sun Coin | 4 |
| **Premier Ball** | 192 | 3× Sprocket | $\infty$ (без лимита) |
| **Heal Ball** | 320 | 5× Sprocket | $\infty$ |
| **Lure Ball** | 1,536 | 3× Cog | $\infty$ |
| **Friend Ball** | 1,536 | 3× Cog | $\infty$ |
| **Nest Ball** | 3,072 | 6× Cog | $\infty$ |
| **Dive Ball** | 3,072 | 6× Cog | $\infty$ |
| **Sword Ball** | 3,072 | 6× Cog | $\infty$ |
| **Shield Ball** | 3,072 | 6× Cog | $\infty$ |
| **Dusk Ball** | 4,096 | 1× Sun Coin | $\infty$ |
| **Quick Ball** | 4,096 | 1× Sun Coin | $\infty$ |
| **Repeat Ball** | 4,096 | 1× Sun Coin | $\infty$ |
| **Timer Ball** | 8,192 | 2× Sun Coin | $\infty$ |

---

## 4. Цены случайных технических дисков (TMs — Random Set 0)
* Каждый из 593 дисков ТМ (`simpletms:tr_*`) продаётся по единой фиксированной цене:
  * **2,048 ед.** (4× Cog / 0.5 Sun Coin)
  * **Лимит**: 4 покупки в день на выпавший диск.
