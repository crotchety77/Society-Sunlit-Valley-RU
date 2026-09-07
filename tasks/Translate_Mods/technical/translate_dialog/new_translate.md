# Локализация мода: dialog

**JAR:** `SVDialog-0.6.jar` | **Всего строк:** 67 | **Не переведено:** 67

## 1. Визуальный контекст и оформление
* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.
* Валюта: использовать значок монеты `§e●` (`U+25CF`).
* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.

## 2. Непереведённые строки (требуют перевода)

```json
{
  "dialog.command.show.success": "TODO: Showing dialog: %s",
  "dialog.command.show.player_only": "TODO: This command can only be executed by a player",
  "dialog.command.show.entity_not_found": "TODO: Entity not found: %s",
  "dialog.command.show.target_not_found": "TODO: Target player not found: %s",
  "dialog.command.show.dialog_not_found": "TODO: Dialog not found: %s",
  "dialog.command.show.help": "TODO: Usage: /dialog <entity_selector> show <player> <dialog_id> or /dialog show <dialog_id> (backward compatible)",
  "dialog.command.show.success_with_entity": "TODO: Entity %s is showing dialog %s to player %s",
  "dialog.command.reload.start": "TODO: Reloading dialog files...",
  "dialog.command.reload.success_server": "TODO: Dialog files reloaded successfully",
  "dialog.command.reload.sync_sent_all": "TODO: Dialogs synchronized to all clients",
  "dialog.command.reload.no_dialogs_to_sync": "TODO: No dialogs to synchronize",
  "dialog.command.list.header": "TODO: Available dialogs:",
  "dialog.command.help": "TODO: Dialog System Command Help:\n/dialog <entity_selector> show <player> <dialog_id> - Make specified entity show dialog to specified player\n/dialog show <dialog_id> - Show dialog (backward compatible)\n/dialog reload - Reload dialog files\n/dialog list - List all available dialogs",
  "dialog.ui.continue": "TODO: Continue",
  "dialog.ui.back": "TODO: Back",
  "dialog.ui.exit": "TODO: Exit",
  "dialog.ui.auto_play": "TODO: Auto Play",
  "dialog.ui.history": "TODO: History",
  "dialog.ui.close_history": "TODO: Close History",
  "dialog.ui.esc": "TODO: Exit Dialog",
  "dialog.ui.confirm_esc": "TODO: Do you want to skip the entire dialog?",
  "dialog.manager.requesting_from_server": "TODO: Requesting dialog files from server...",
  "dialog.manager.loading": "TODO: Loading dialog files, path: %s",
  "dialog.manager.files_found": "TODO: Found %s dialog files",
  "dialog.manager.sequence_loaded": "TODO: Successfully loaded dialog sequence: %s",
  "dialog.manager.sequence_empty": "TODO: Dialog sequence is empty or ID is null: %s",
  "dialog.manager.load_failed": "TODO: Failed to load dialog file %s: %s",
  "dialog.manager.total_loaded": "TODO: Total loaded dialog sequences: %s",
  "dialog.manager.no_sequences": "TODO: No dialog sequences found, please check resource path and file format",
  "dialog.manager.parse_null": "TODO: Failed to parse dialog JSON: result is null",
  "dialog.manager.parse_failed": "TODO: Failed to parse dialog JSON: %s",
  "dialog.manager.read_failed": "TODO: Failed to read dialog JSON file: %s",
  "dialog.manager.sequence_not_found": "TODO: Dialog sequence not found: %s",
  "dialog.manager.no_entries": "TODO: No entries found in dialog sequence: %s",
  "dialog.manager.target_not_found": "TODO: Target dialog entry not found: %s",
  "dialog.test_dialog.speaker.tlipoca": "TODO: Tlipoca",
  "dialog.test_dialog.speaker.leaf": "TODO: Little Leaf",
  "dialog.test_dialog.entry.start.text": "TODO: Welcome, @i, to this mod! This is a dialog system example.",
  "dialog.test_dialog.entry.1.text": "TODO: This dialog system can display multiple characters simultaneously and show portraits in left, center, and right positions. (In order to save space, the corresponding resource files for the portraits are not attached to the mod)",
  "dialog.test_dialog.entry.2.text": "TODO: You can configure dialog content via JSON files, including text, speaker, portraits and their positions, opacity, etc., allowing for simple, efficient, and comprehensive customization.",
  "dialog.test_dialog.entry.3.text.0": "TODO: Of course, things like ",
  "dialog.test_dialog.entry.3.text.1": "TODO: colored ",
  "dialog.test_dialog.entry.3.text.2": "TODO: text ",
  "dialog.test_dialog.entry.3.text.3": "TODO: and ",
  "dialog.test_dialog.entry.3.text.4": "TODO: formatting",
  "dialog.test_dialog.entry.3.text.5": "TODO: , ",
  "dialog.test_dialog.entry.3.text.6": "TODO: bold",
  "dialog.test_dialog.entry.3.text.7": "TODO: , ",
  "dialog.test_dialog.entry.3.text.8": "TODO: italic",
  "dialog.test_dialog.entry.3.text.9": "TODO:  and other formatting codes are also supported.",
  "dialog.test_dialog.entry.4.text": "TODO: You can even freely choose from preset portrait entrance animations, like...",
  "dialog.test_dialog.entry.5.text": "TODO: Fade In",
  "dialog.test_dialog.entry.6.text": "TODO: Slide In",
  "dialog.test_dialog.entry.7.text": "TODO: Bounce, and various other animations.",
  "dialog.test_dialog.entry.8.text": "TODO: Of course, you can also customize branch options. Now you can choose what to do next:",
  "dialog.test_dialog.entry.more_info.text": "TODO: The two buttons in the bottom right are for auto-play and history. Also, if you want to skip the plot, long-press the Ctrl key to quickly skip dialog to the options.",
  "dialog.test_dialog.entry.command.text": "TODO: You can also execute specific commands after selecting an option or after a line of dialog, to trigger events or change affection levels, etc. Here’s an example using weather changes:",
  "dialog.test_dialog.entry.item.text": "TODO: Rendered items can be customized at the top of the dialog, including NBT and quantity.",
  "dialog.test_dialog.entry.end.text": "TODO: Thank you for using this mod! Use the /dialog show test_dialog command to open this dialog again.",
  "dialog.test_dialog.entry.hidden_entry.text": "TODO: This entry is hidden from players in survival mode",
  "dialog.test_dialog.entry.background_cg.text": "TODO: You can also add custom images as CG to the background",
  "dialog.test_dialog.option.more_info": "TODO: Learn more about the dialog system",
  "dialog.test_dialog.option.end_dialog": "TODO: End dialog",
  "dialog.test_dialog.option.hidden_option": "TODO: Hidden option, only visible to players in survival mode",
  "dialog.test_dialog.option.weather_rain": "TODO: Set weather to rain",
  "dialog.test_dialog.option.weather_clear": "TODO: Set weather to clear",
  "dialog.test_dialog.option.weather_thunder": "TODO: Set weather to thunder"
}
```

