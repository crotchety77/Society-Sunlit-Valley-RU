# Отчёт аудита FTB Quests — Society: Sunlit Valley 4.1.4

## 1. Общая статистика

| Параметр | Значение | Описание |
| -------- | -------- | -------- |
| **Квестов в 4.0.4** | **1227** | Исходное количество квестов |
| **Квестов в 4.1.4** | **1142** | Текущее количество квестов |
| **Новых квестов** | **20** | Появились только в 4.1.4 (`new_in_4.1.4`) |
| **Изменённых квестов** | **14** | Существовали в 4.0.4, но изменились в 4.1.4 |
| **Удалённых квестов** | **105** | 104 квеста из главы `building_shop` + 1 квест из `crops` |
| **Полностью переведённых** | **181** | Все тексты имеют кириллическую русскую локализацию |
| **Частично переведённых** | **332** | Переведено название или часть описаний |
| **Полностью непереведённых** | **17** | Только английский текст |
| **Пустых (чисто иконки/предметы)** | **612** | Квесты сдачи предметов без кастомного текста |

---

## 2. Главы и таблицы наград

### Главы (29 глав в 4.1.4 vs 30 в 4.0.4)
- **Удалённая глава**: `building_shop.snbt` (104 квеста магазина строительных блоков, перенесены/упразднены разработчиком в 4.1.4).
- **Все остальные 29 глав** сохранены: `abandoned_farm`, `armor_weapons__tools`, `artifacts`, `banners`, `boiler_room`, `botania`, `crafts_room`, `creatures`, `crops`, `drinks`, `fishing`, `fish_tank`, `gems`, `getting_started`, `iii__advanced_farming`, `ii__building_up_the_farm`, `ivi__mechanical_farming`, `iv__prismatic_farming`, `longwings`, `minerals`, `pantry`, `perfection`, `relics`, `slimes`, `tools`, `transportation`, `vault`, `villagers`, `welcome`.

### Таблицы наград (20 в 4.1.4 vs 11 в 4.0.4)
Появилось **9 новых таблиц наград** для домов жителей:
1. `villager_home__banker`
2. `villager_home__blacksmith`
3. `villager_home__carpenter`
4. `villager_home__fisher`
5. `villager_home__librarian_2`
6. `villager_home__market`
7. `villager_home__shepherd`
8. `villager_home__trader`
9. `villager_home__witch`

---

## 3. Новые квесты в 4.1.4 (20 квестов)

| Глава | ID | Название EN | Название RU | Статус |
| ----- | -- | ----------- | ----------- | ------ |
| `artifacts` | `4A88F30DE9250181` | — (Item Task) | — | `empty` |
| `artifacts` | `54E20BA869846944` | — (Item Task) | — | `empty` |
| `banners` | `3315CF66A6C33A02` | — (Item Task) | — | `empty` |
| `ii__building_up_the_farm` | `1F12BF72B966E0CC` | Free Geode Busting | — | `untranslated` |
| `ii__building_up_the_farm` | `42C8E1F0D9A5B2BD` | — (Item Task) | — | `untranslated` |
| `ii__building_up_the_farm` | `62129A6009E60E0F` | Finding Menu Items | — | `untranslated` |
| `ii__building_up_the_farm` | `6F3FC6227213B886` | Crop Quality | — | `untranslated` |
| `ii__building_up_the_farm` | `723A5C8DB06D8C36` | Opening a Cozy Cafe | — | `untranslated` |
| `ii__building_up_the_farm` | `7C30FC21953CF7D3` | Plating Up | — | `untranslated` |
| `ii__building_up_the_farm` | `7FFED918C5367350` | Eggs of the King | — | `untranslated` |
| `iii__advanced_farming` | `0A455A4E0D7D074E` | — (Item Task) | — | `untranslated` |
| `iii__advanced_farming` | `17C8B0197B8636E7` | — (Item Task) | — | `untranslated` |
| `iii__advanced_farming` | `263CCA4D2EAF2629` | Butterfly Breeding! | — | `untranslated` |
| `iii__advanced_farming` | `3DE36C9FBCB58800` | Magic in the Valley | — | `untranslated` |
| `iv__prismatic_farming` | `4CCA31DA0B782830` | — (Item Task) | — | `empty` |
| `iv__prismatic_farming` | `7037A26BF990653E` | Bartering? | — | `untranslated` |
| `iv__prismatic_farming` | `73D3DF7A58D2112A` | — (Item Task) | — | `empty` |
| `longwings` | `48AE61B7C8084142` | — (Item Task) | — | `empty` |
| `longwings` | `59F65B3F0935DB5B` | — (Item Task) | — | `empty` |
| `welcome` | `238702B124895A0A` | Finding Answers! | — | `untranslated` |

---

## 4. Изменённые квесты (14 квестов)

| Глава | ID | Название EN | Что изменилось |
| ----- | -- | ----------- | -------------- |
| `getting_started` | `24C86673E1F57A3E` | — (Item Task) | Tasks / requirements changed<br>Rewards modified |
| `getting_started` | `3E08F21BA8F69499` | Giving Gifts | Description pages updated |
| `getting_started` | `4DB169DA4B4CCFBA` | — (Item Task) | Tasks / requirements changed<br>Rewards modified |
| `getting_started` | `66D159252C70D5F2` | Starting Your Village | Tasks / requirements changed<br>Rewards modified |
| `ii__building_up_the_farm` | `429FEBEC239B975F` | Fishing | Tasks / requirements changed<br>Rewards modified |
| `ii__building_up_the_farm` | `6ADD884F3FFE5D42` | Starting Farming | Tasks / requirements changed<br>Rewards modified |
| `ii__building_up_the_farm` | `6EEBD017839FF628` | Raising Farm Animals | Tasks / requirements changed<br>Rewards modified |
| `iii__advanced_farming` | `1AA78CF8A14DEE76` | Smarter Selling | Rewards modified |
| `iii__advanced_farming` | `3B6640956F047EC8` | The Butterfly Effect | Rewards modified |
| `iii__advanced_farming` | `44A512703C4A9990` | Making Real Money | Tasks / requirements changed |
| `iv__prismatic_farming` | `41C453E806763C4F` | Machine Upgrades | Description pages updated |
| `tools` | `100B4D3BEEE9C433` | Furniture Catalogs | Rewards modified |
| `villagers` | `7B2AB58CA9C1C19B` | Barkeeper | Tasks / requirements changed |
| `welcome` | `18490F31FFAB134E` | For Server Owners | Description pages updated |

---

## 5. Аудит квеста о подарках жителям (`3E08F21BA8F69499`)

В соответствии с правилом 11:
- В оригинале 4.0.4 квест содержал только 3 строки описания (`description1..3`).
- В 4.1.4 добавлено описание кулдауна и наград.
- Зафиксировано форматирование оригинала:
  - `&6Shift + Right Click&r` $\rightarrow$ `&6Shift + ПКМ&r`
  - `&6once every 4 days&r` $\rightarrow$ `&61 раз в 4 дня&r`
  - `&a+5 points&r` $\rightarrow$ `&a+5 очков&r`
  - `&6#villager_gift&r` $\rightarrow$ `&6#villager_gift&r`
- Декоративная радужная раскраска устранена; соблюдены смысловые акценты оригинала.

---

## 6. Рабочая очередь и приоритеты

1. **Priority 1 — Новые квесты 4.1.4 (20 шт.)**: `work_queue/priority1_new.md`
2. **Priority 2 — Изменённые квесты (14 шт.)**: `work_queue/priority2_changed.md`
3. **Priority 3 — Частично переведённые квесты (320 шт.)**: `work_queue/priority3_partially_translated.md`
4. **Priority 4 — Непереведённые квесты (3 шт.)**: `work_queue/priority4_untranslated.md`

Все рабочие файлы структурированы блоками вида:
```text
ID: <id>
Глава: <chapter>

EN title: ...
RU title: ...

EN description1: ...
RU description1: ...

EN reward: ...
RU reward: ...

Source: ...
Status: ...
```
