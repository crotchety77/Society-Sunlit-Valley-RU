import json, os, shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RU_SOURCE = os.path.join(BASE_DIR, "translations", "mods", "dramaticdoors.json")
GAME_TARGET = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\dramaticdoors\lang\ru_ru.json"

def main():
    print("--- Применение и синхронизация Dramatic Doors ---")
    with open(RU_SOURCE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Загружено {len(data)} ключей из источника.")
    
    os.makedirs(os.path.dirname(GAME_TARGET), exist_ok=True)
    with open(GAME_TARGET, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Успешно записано в {GAME_TARGET}")
    
    # Run sync_all_to_game
    os.system("node sync_all_to_game.js")

if __name__ == "__main__":
    main()
