# Локализация мода: Cozy Cafe (Уютное кафе и менеджмент кофейни) (`cozycafe`)

**JAR:** `cozycafe-1.8-all.jar` | **Всего строк:** 63 | **Готово к применению:** 63

## 1. Визуальный контекст и оформление

### Основные блоки и предметы кафе:
* **Менеджер кафе** (`block.cozycafe.cafe_manager`) — главный блок управления кофейней
* **Меню кафе** (`block.cozycafe.cafe_menu`) — стенд с доступными блюдами и ценами
* **Станция сервировки** (`block.cozycafe.plating_station`) — стол для выкладки блюд
* **Вывеска кафе** (`block.cozycafe.cafe_sign`) — маркер спавна посетителей
* **Сервировочная тарелка** (`item.cozycafe.serving_plate`) / **Грязная сервировочная тарелка** (`item.cozycafe.dirty_serving_plate`)
* **Посетитель** (`entity.cozycafe.customer`)

### Категории блюд:
* **Основное блюдо** (`category.cozycafe.main`)
* **Десерт** (`category.cozycafe.dessert`)
* **Напиток** (`category.cozycafe.drink`)

### Кнопки GUI и цены:
* Кнопки: *«Открыть кафе»*, *«Закрыть кафе»*, *«Редактировать меню»*, *«Показать зону кафе»*, *«Сбросить данные кафе (Зажмите Shift)»*.
* Цены: `§e●%s` (символ монеты).

---

## 2. Предлагаемый перевод (JSON)

```json
{
  "itemGroup.cozycafe": "«Уютное кафе»",
  "itemGroup.cozycafe.creative_tab": "«Уютное кафе»",
  "block.cozycafe.cafe_manager": "Менеджер кафе",
  "block.cozycafe.cafe_menu": "Меню кафе",
  "block.cozycafe.plating_station": "Станция сервировки",
  "block.cozycafe.cafe_sign": "Вывеска кафе",
  "block.cozycafe.any.cannot_break": "Вы не можете сломать это, пока кафе открыто!",
  "item.cozycafe.serving_plate": "Сервировочная тарелка",
  "item.cozycafe.serving_plate.served": "Сервированное %s",
  "item.cozycafe.dirty_serving_plate": "Грязная сервировочная тарелка",
  "item.cozycafe.cafe_sign.linked": "Позиция менеджера кафе сохранена в вывеске!",
  "entity.cozycafe.customer": "Посетитель",
  "tooltip.cozycafe.cafe_manager": "Позволяет создать и развивать своё уютное кафе",
  "tooltip.cozycafe.cafe_manager.cafe_name": "Название: %s",
  "tooltip.cozycafe.cafe_manager.no_reputation": "Репутация пока отсутствует! Обслужите больше посетителей!",
  "tooltip.cozycafe.cafe_manager.reputation": "Репутация: %s",
  "tooltip.cozycafe.cafe_manager.error": "Не удалось открыть кафе!",
  "tooltip.cozycafe.cafe_manager.cannot_edit": "Нельзя менять меню во время работы кафе!",
  "tooltip.cozycafe.cafe_manager.0": "Разместите Меню кафе в рабочей зоне Менеджера кафе",

  "tooltip.cozycafe.cafe_manager.1": "Привяжите вывеску кафе перед открытием",
  "tooltip.always.cozycafe.cafe_sign.0": "§7Указывает место появления посетителей в вашем кафе.",
  "tooltip.cozycafe.cafe_sign.0": "§6Shift + ПКМ§7 по Менеджеру кафе,",
  "tooltip.cozycafe.cafe_sign.1": "§7чтобы привязать вывеску перед установкой.",
  "tooltip.always.cozycafe.plating_station.0": "§7Позволяет сервировать основные блюда для подачи посетителям.",
  "tooltip.cozycafe.plating_station.0": "§6ПКМ§7 с сервировочной тарелкой, чтобы начать сервировку",
  "tooltip.cozycafe.plating_station.1": "§6ПКМ§7 с блюдом из меню, чтобы выложить его на тарелку",
  "tooltip.cozycafe.plating_station.2": "§6ПКМ§7 пустой рукой, чтобы забрать готовую тарелку",
  "tooltip.cozycafe.cafe_menu.0": "§7Разместите в рабочей зоне вашего Менеджера кафе.",
  "tooltip.always.cozycafe.serving_plate.0": "§7Используется для подачи основных блюд на станции сервировки.",
  "tooltip.cozycafe.serving_plate.0": "§6Shift + ПКМ§7, чтобы убрать удерживаемый предмет",
  "tooltip.always.cozycafe.dirty_serving_plate.0": "§7Остаётся после трапезы довольных посетителей!",
  "tooltip.cozycafe.dirty_serving_plate.0": "§6Зажмите ПКМ§7 по губке или раковине, чтобы помыть",
  "block.cozycafe.cafe_manager.no_sign": "Необходимо привязать Вывеску кафе к этому Менеджеру кафе",
  "block.cozycafe.cafe_manager.menu_too_small": "В меню должно быть как минимум 3 позиции!",
  "block.cozycafe.cafe_manager.menu_too_small_for_stars": "Требуется как минимум на 3 позиции больше для каждой звезды!",
  "block.cozycafe.cafe_manager.already_opened": "Вы уже открывали кафе сегодня! Приходите завтра!",
  "block.cozycafe.cafe_manager.nearby_manager": "Поблизости уже есть другое открытое кафе!",
  "block.cozycafe.cafe_menu.payment": "§e●%s добавлено на банковский счёт",

  "block.cozycafe.cafe_menu.not_plated": "Это блюдо необходимо сервировать на Станции сервировки!",
  "block.cozycafe.plating_station.not_main": "Этот тип блюд из меню не требует сервировки!",
  "block.cozycafe.plating_station.not_menu_item": "Этот предмет нельзя подавать посетителям!",
  "block.cozycafe.plating_station.already_plated": "На этой тарелке уже лежит блюдо!",
  "category.cozycafe.main": "Основное блюдо",
  "category.cozycafe.dessert": "Десерт",
  "category.cozycafe.drink": "Напиток",
  "container.cozycafe.cafe_manager": "Менеджер кафе",
  "gui.cozycafe.cafe_manager.edit_menu": "Редактировать меню",
  "gui.cozycafe.cafe_manager.open": "Открыть кафе",
  "gui.cozycafe.cafe_manager.close": "Закрыть кафе",
  "gui.cozycafe.cafe_manager.show_area": "Показать зону кафе",
  "gui.cozycafe.cafe_manager.clear_data": "Сбросить данные кафе (Зажмите Shift)",
  "gui.cozycafe.cafe_manager.edit_name": "Изменить название кафе",
  "gui.cozycafe.menu_selector.name": "Меню",
  "gui.cozycafe.menu_selector.invalid": "Нельзя добавить!",
  "gui.cozycafe.menu_selector.added": "Добавлено!",
  "gui.cozycafe.menu_selector.price": "Цена: §e●%s",
  "gui.cozycafe.menu_selector.item_category": "Категория: %s",
  "gui.cozycafe.menu_selector.inline_price": "§e●%s",
  "gui.cozycafe.menu_selector.remove": "Нажмите, чтобы удалить",
  "gui.cozycafe.menu_selector.bowl_food": "Блюдо в миске (сервировка не требуется)",
  "gui.cozycafe.menu_selector.bottle_drink": "Оставляет бутылочку после употребления",
  "gui.cozycafe.menu_selector.stars_required": "Минимум позиций в меню: %s",
  "gui.cozycafe.menu_selector.place_items": "Поместите предмет для добавления"
}
```
