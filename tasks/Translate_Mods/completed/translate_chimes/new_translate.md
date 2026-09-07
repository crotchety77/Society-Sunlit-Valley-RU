# Локализация мода: Chimes (Музыка ветра) (`chimes`)

**JAR:** `Chimes-v2.1.1-1.20.1-Forge.jar` | **Всего строк:** 49 | **Готово к применению:** 49

## 1. Визуальный контекст и оформление

### Основные колокольчики и фурины:
* **Японский стеклянный колокольчик (Бамбуковый Фурин)** (`block.chimes.bamboo_chimes`)
* **Японский стеклянный колокольчик (Резной Бамбуковый Фурин)** (`block.chimes.carved_bamboo_chimes`)
* **Японский стеклянный колокольчик (Железный Фурин)** (`block.chimes.iron_chimes`)
* **Японский стеклянный колокольчик (Медный Фурин)** (`block.chimes.copper_chimes`)
* **Японский стеклянный колокольчик (Аметистовый Фурин)** (`block.chimes.amethyst_chimes`)
* **Японский стеклянный колокольчик (Стеклянный Фурин)** (`block.chimes.glass_bells`)
* **Японский стеклянный колокольчик (Настраиваемый Фурин)** (`item.glass_wind_bell.customizable`)

### Кастомизация стеклянного колокольчика (16 цветов):
* **Язычок (вымпел ветра):** *Белый язычок*, *Оранжевый язычок*, *Пурпурный язычок*, *Голубой язычок*, *Жёлтый язычок*, *Лаймовый язычок*, *Розовый язычок*, *Серый язычок*, *Светло-серый язычок*, *Бирюзовый язычок*, *Фиолетовый язычок*, *Синий язычок*, *Коричневый язычок*, *Зелёный язычок*, *Красный язычок*, *Чёрный язычок*.
* **Основание (купол):** *Белое основание*, *Оранжевое основание*, *Пурпурное основание*, *Голубое основание*, *Жёлтое основание*, *Лаймовое основание*, *Розовое основание*, *Серое основание*, *Светло-серое основание*, *Бирюзовое основание*, *Фиолетовое основание*, *Синее основание*, *Коричневое основание*, *Зелёное основание*, *Красное основание*, *Чёрное основание*.

---

## 2. Предлагаемый перевод (JSON)

```json
{
  "block.chimes.bamboo_chimes": "Японский стеклянный колокольчик (Бамбуковый Фурин)",
  "block.chimes.carved_bamboo_chimes": "Японский стеклянный колокольчик (Резной Бамбуковый Фурин)",
  "block.chimes.iron_chimes": "Японский стеклянный колокольчик (Железный Фурин)",
  "block.chimes.copper_chimes": "Японский стеклянный колокольчик (Медный Фурин)",
  "block.chimes.amethyst_chimes": "Японский стеклянный колокольчик (Аметистовый Фурин)",
  "block.chimes.glass_bells": "Японский стеклянный колокольчик (Стеклянный Фурин)",
  "item.chimes.glass_bells.description": "Покрасьте верх и низ отдельно. Краситель — сверху и снизу в верстаке",
  "item.glass_wind_bell.customizable": "Японский стеклянный колокольчик (Настраиваемый Фурин)",
  "block.glass_wind_bell.white.tag": "Белый язычок",
  "block.glass_wind_bell.orange.tag": "Оранжевый язычок",
  "block.glass_wind_bell.magenta.tag": "Пурпурный язычок",
  "block.glass_wind_bell.light_blue.tag": "Голубой язычок",
  "block.glass_wind_bell.yellow.tag": "Жёлтый язычок",
  "block.glass_wind_bell.lime.tag": "Лаймовый язычок",
  "block.glass_wind_bell.pink.tag": "Розовый язычок",
  "block.glass_wind_bell.gray.tag": "Серый язычок",
  "block.glass_wind_bell.light_gray.tag": "Светло-серый язычок",
  "block.glass_wind_bell.cyan.tag": "Бирюзовый язычок",
  "block.glass_wind_bell.purple.tag": "Фиолетовый язычок",
  "block.glass_wind_bell.blue.tag": "Синий язычок",
  "block.glass_wind_bell.brown.tag": "Коричневый язычок",
  "block.glass_wind_bell.green.tag": "Зелёный язычок",
  "block.glass_wind_bell.red.tag": "Красный язычок",
  "block.glass_wind_bell.black.tag": "Чёрный язычок",
  "block.glass_wind_bell.white.base": "Белое основание",
  "block.glass_wind_bell.orange.base": "Оранжевое основание",
  "block.glass_wind_bell.magenta.base": "Пурпурное основание",
  "block.glass_wind_bell.light_blue.base": "Голубое основание",
  "block.glass_wind_bell.yellow.base": "Жёлтое основание",
  "block.glass_wind_bell.lime.base": "Лаймовое основание",
  "block.glass_wind_bell.pink.base": "Розовое основание",
  "block.glass_wind_bell.gray.base": "Серое основание",
  "block.glass_wind_bell.light_gray.base": "Светло-серое основание",
  "block.glass_wind_bell.cyan.base": "Бирюзовое основание",
  "block.glass_wind_bell.purple.base": "Фиолетовое основание",
  "block.glass_wind_bell.blue.base": "Синее основание",
  "block.glass_wind_bell.brown.base": "Коричневое основание",
  "block.glass_wind_bell.green.base": "Зелёное основание",
  "block.glass_wind_bell.red.base": "Красное основание",
  "block.glass_wind_bell.black.base": "Чёрное основание",
  "chimes.configGui.title": "Настройки Chimes",
  "chimes.configGui.animations.button": "Музыка ветра",
  "chimes.configGui.bamboo_leaf.button": "Падающие листья бамбука",
  "chimes.configGui.options.animated": "Анимированные",
  "chimes.configGui.options.static": "Статичные",
  "chimes.configGui.options.on": "Вкл.",
  "chimes.configGui.options.off": "Выкл.",
  "chimes.subtitles.wind_chime.chimes": "Музыка ветра звенит",
  "chimes.subtitles.wind_chime.shimmers": "Музыка ветра переливается",
  "chimes.subtitles.wind_chime.tie": "Музыка ветра закреплена"
}
```
