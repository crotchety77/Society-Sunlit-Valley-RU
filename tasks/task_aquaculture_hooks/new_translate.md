# Согласование локализации: Крючки Aquaculture 2

**Мод:** `aquaculture` | **Всего крючков:** 15 | **Статус:** На согласовании

---

## Блок 1: Визуальный макет (как это выглядит в игре)

### 🪝 1. Базовые металлические и минеральные крючки
```text
§fЖелезный крючок§r
§720%% шанс не потратить прочность удочки§r

§fЗолотой крючок§r
§7+1 к Удаче рыбалки§r

§fАлмазный крючок§r
§750%% шанс не потратить прочность удочки§r
```

### 🎯 2. Функциональные крючки (механики заброса и подсечки)
```text
§fОблегчённый крючок§r
§7Дальность заброса увеличена на 50%%§r

§fУтяжелённый крючок§r
§7Дальность заброса снижена на 40%% (быстрое погружение)§r

§fДвойной крючок§r
§710%% шанс поймать два предмета одновременно§r

§fРедстоуновый крючок§r
§7Увеличивает окно времени на подсечку рыбы§r

§fМузыкальный крючок§r
§7Издаёт звуковой сигнал при поклёвке§r
```

### 🌋 3. Незер-крючки (лава и особые свойства)
```text
§fКварцевый крючок§r
§730%% шанс не потратить прочность удочки§r

§fСветопылевой крючок§r
§7+1 к Удаче рыбалки§r

§fКрючок из песка душ§r
§7Увеличивает окно времени на подсечку рыбы§r

§fОбсидиановый крючок§r
§7Позволяет ловить в лаве§r

§fДвойной обсидиановый крючок§r
§7Позволяет ловить в лаве + 10%% шанс двойного улова§r

§fОбсидиановый музыкальный крючок§r
§7Позволяет ловить в лаве + звуковой сигнал при поклёвке§r

§fКрючок из звезды Незера§r
§750%% шанс не тратить прочность, +1 Удача, ловит в воде и лаве§r
```

---

## Блок 2: Точные строки и ключи локализации (`translations/mods/aquaculture.json`)

```json
{
  "item.aquaculture.iron_hook": "Железный крючок",
  "item.aquaculture.gold_hook": "Золотой крючок",
  "item.aquaculture.diamond_hook": "Алмазный крючок",
  "item.aquaculture.light_hook": "Облегчённый крючок",
  "item.aquaculture.heavy_hook": "Утяжелённый крючок",
  "item.aquaculture.double_hook": "Двойной крючок",
  "item.aquaculture.redstone_hook": "Редстоуновый крючок",
  "item.aquaculture.note_hook": "Музыкальный крючок",
  "item.aquaculture.quartz_hook": "Кварцевый крючок",
  "item.aquaculture.glowstone_hook": "Светопылевой крючок",
  "item.aquaculture.soul_sand_hook": "Крючок из песка душ",
  "item.aquaculture.obsidian_hook": "Обсидиановый крючок",
  "item.aquaculture.double_obsidian_hook": "Двойной обсидиановый крючок",
  "item.aquaculture.obsidian_note_hook": "Обсидиановый музыкальный крючок",
  "item.aquaculture.nether_star_hook": "Крючок из звезды Незера",
  "aquaculture.iron_hook.tooltip.title": "Прочный",
  "aquaculture.iron_hook.tooltip.desc": "20%% шанс не потратить прочность",
  "aquaculture.gold_hook.tooltip.title": "Удачливый",
  "aquaculture.gold_hook.tooltip.desc": "Повышает Удачу рыбалки (+1)",
  "aquaculture.diamond_hook.tooltip.title": "Сверхпрочный",
  "aquaculture.diamond_hook.tooltip.desc": "50%% шанс не потратить прочность",
  "aquaculture.light_hook.tooltip.title": "Лёгкий",
  "aquaculture.light_hook.tooltip.desc": "Летит на 50%% дальше",
  "aquaculture.heavy_hook.tooltip.title": "Тяжёлый",
  "aquaculture.heavy_hook.tooltip.desc": "Летит ближе и быстрее тонет",
  "aquaculture.double_hook.tooltip.title": "Двойной зубец",
  "aquaculture.double_hook.tooltip.desc": "10%% шанс выловить сразу два предмета",
  "aquaculture.redstone_hook.tooltip.title": "Приманивающий",
  "aquaculture.redstone_hook.tooltip.desc": "Увеличивает время на подсечку рыбы",
  "aquaculture.note_hook.tooltip.title": "Оповещение",
  "aquaculture.note_hook.tooltip.desc": "Издаёт звуковой сигнал при поклёвке",
  "aquaculture.quartz_hook.tooltip.title": "Прочный",
  "aquaculture.quartz_hook.tooltip.desc": "30%% шанс не потратить прочность",
  "aquaculture.glowstone_hook.tooltip.title": "Удачливый",
  "aquaculture.glowstone_hook.tooltip.desc": "Повышает Удачу рыбалки (+1)",
  "aquaculture.soul_sand_hook.tooltip.title": "Приманивающий",
  "aquaculture.soul_sand_hook.tooltip.desc": "Увеличивает время на подсечку рыбы",
  "aquaculture.double_obsidian_hook.tooltip.title": "Двойной зубец",
  "aquaculture.double_obsidian_hook.tooltip.desc": "10%% шанс выловить сразу два предмета в лаве и воде",
  "aquaculture.obsidian_note_hook.tooltip.title": "Оповещение",
  "aquaculture.obsidian_note_hook.tooltip.desc": "Издаёт звуковой сигнал при поклёвке",
  "aquaculture.nether_star_hook.tooltip.title": "Потусторонний",
  "aquaculture.nether_star_hook.tooltip.desc": "50%% шанс не тратить прочность, +1 Удача, ловит в воде и лаве"
}
```
