# Локализация мода: aitranslator

**JAR:** `aitranslator-1.0.1.jar` | **Всего строк:** 30 | **Не переведено:** 30

## 1. Визуальный контекст и оформление
* Форматирование: Названия предметов/блоков начинаются с Заглавной буквы.
* Валюта: использовать значок монеты `§e●` (`U+25CF`).
* Тултипы: подсветка клавиш `§6Shift + ПКМ§7`.

## 2. Непереведённые строки (требуют перевода)

```json
{
  "screen.aitranslator.title": "TODO: AI Translator",
  "screen.aitranslator.config": "TODO: AI Translator - Config",
  "screen.aitranslator.result": "TODO: Translation",
  "key.aitranslator.open": "TODO: Open Translator",
  "key.aitranslator.config": "TODO: Open Config",
  "key.categories.aitranslator": "TODO: AI Translator",
  "button.aitranslator.copy": "TODO: Copy",
  "aitranslator.reading": "TODO: Reading text",
  "aitranslator.translating": "TODO: Translating",
  "aitranslator.copied": "TODO: Copied!",
  "config.aitranslator.api_key": "TODO: API Key",
  "config.aitranslator.endpoint": "TODO: API Endpoint",
  "config.aitranslator.model": "TODO: OCR Model",
  "config.aitranslator.translation_model": "TODO: Translation Model",
  "config.aitranslator.translation_model_hint": "TODO: (optional — same as OCR Model if blank)",
  "config.aitranslator.timeout": "TODO: Timeout (seconds)",
  "config.aitranslator.target_lang": "TODO: Target Language",
  "config.aitranslator.save": "TODO: Save",
  "config.aitranslator.close": "TODO: Close",
  "config.aitranslator.model_help": "TODO: Recommended translation models",
  "screen.aitranslator.model_help": "TODO: Recommended Models",
  "config.aitranslator.model_help_body": "TODO: To use the default settings, you need Ollama installed and running locally.\n\n1. Install Ollama (ollama.com) and launch it — it runs quietly in the background.\n2. In a terminal, pull the two models the defaults expect:\nollama pull minicpm-v\nollama pull aya-expanse:8b\n\nThat's it: the default OCR Model, Translation Model, Endpoint and API Key above are already set to match — no further changes needed.\n\nPrefer an online service like ChatGPT (OpenAI) instead? Set the Endpoint to https://api.openai.com/v1/chat/completions, enter a real API key from your OpenAI account, and use a model name such as gpt-4o-mini or gpt-4o in both the OCR Model and Translation Model fields. Keep in mind this is not free: unlike local Ollama models, each translation request consumes tokens billed to your OpenAI account.",
  "config.aitranslator.api_key_tooltip": "TODO: Authentication key sent with each request. With Ollama, any non-empty value works (e.g. \"ollama\").",
  "config.aitranslator.endpoint_tooltip": "TODO: URL of the OpenAI-compatible chat-completions API. Local Ollama default: http://localhost:11434/v1/chat/completions",
  "config.aitranslator.model_tooltip": "TODO: Vision-capable model used to read the screenshot's text (OCR). Must support image input — e.g. minicpm-v, llava, gpt-4o-mini.",
  "config.aitranslator.translation_model_tooltip": "TODO: Optional separate text-only model for the translation step. Leave blank to reuse the OCR Model above.",
  "config.aitranslator.timeout_tooltip": "TODO: How long to wait for a reply before giving up. Range: 10 to 300 seconds.",
  "config.aitranslator.target_lang_tooltip": "TODO: Language the translated text will be produced in.",
  "screen.aitranslator.selection": "TODO: Select area to translate",
  "aitranslator.selection.hint": "TODO: Drag to select text — ESC to cancel"
}
```

