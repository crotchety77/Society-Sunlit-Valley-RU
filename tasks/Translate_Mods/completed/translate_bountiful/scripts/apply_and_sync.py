import os
import json
import subprocess

MOD_NAME = "bountiful"
SRC_TRANS = os.path.abspath(f"translations/mods/{MOD_NAME}.json")
GAME_ASSETS_DIR = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\assets\bountiful\lang"
GAME_RU_FILE = os.path.join(GAME_ASSETS_DIR, "ru_ru.json")
CLIENT_SCRIPTS_SRC = os.path.abspath("kubejs_scripts/client/bountifulTooltips.js")
CLIENT_SCRIPTS_DST = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs\client_scripts\bountifulTooltips.js"

def main():
    print(f"--- [1/4] Applying {MOD_NAME} translation ---")
    if not os.path.exists(SRC_TRANS):
        print(f"Error: {SRC_TRANS} does not exist!")
        return

    with open(SRC_TRANS, "r", encoding="utf-8") as f:
        src_data = json.load(f)

    os.makedirs(GAME_ASSETS_DIR, exist_ok=True)
    existing_data = {}
    if os.path.exists(GAME_RU_FILE):
        try:
            with open(GAME_RU_FILE, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except Exception:
            existing_data = {}

    existing_data.update(src_data)

    with open(GAME_RU_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(existing_data)} keys to {GAME_RU_FILE}")

    print("--- [2/4] Syncing tooltip script ---")
    if os.path.exists(CLIENT_SCRIPTS_SRC):
        os.makedirs(os.path.dirname(CLIENT_SCRIPTS_DST), exist_ok=True)
        with open(CLIENT_SCRIPTS_SRC, "r", encoding="utf-8") as f_in:
            content = f_in.read()
        with open(CLIENT_SCRIPTS_DST, "w", encoding="utf-8") as f_out:
            f_out.write(content)
        print(f"Copied tooltips to {CLIENT_SCRIPTS_DST}")

    print("--- [3/4] Running sync_all_to_game.js ---")
    subprocess.run(["node", "sync_all_to_game.js"], check=True)

    print("--- [4/4] Physical verification of game file ---")
    with open(GAME_RU_FILE, "r", encoding="utf-8") as f:
        verified = json.load(f)

    sample_keys = [
        "block.bountiful.bountyboard",
        "bountiful.bounty",
        "bountiful.decree",
        "bountiful.decree.artisan.name",
        "bountiful.decree.farming.name",
        "bountiful.entry.fisherman_obj_catch_ench_book",
        "bountiful.tooltip.rewards"
    ]
    print("\nVerified game values:")
    for k in sample_keys:
        print(f"  {k} -> {verified.get(k, 'MISSING')}")

if __name__ == "__main__":
    main()
