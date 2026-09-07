import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

game_file = Path(r"G:\curseforge\minecraft\Instances\Cisco's Fantasy Medieval RPG [Dragonfyre]\config\ftbquests\quests\chapters\textchampions_of_the_risencolor0be4f3_2.snbt")

text = game_file.read_text(encoding="utf-8")
print(f"=== ВЕРИФИКАЦИЯ КВЕСТА В ИГРОВОМ ФАЙЛЕ {game_file.name} ===")

pattern = r'(\{\s*(?:[^{}]|\{[^{}]*\})*?id:\s*"1F42D7C3A2431C43"(?:[^{}]|\{[^{}]*\})*?\})'
m = re.search(pattern, text, re.DOTALL)
if m:
    print(m.group(1))
else:
    print("Квест не найден!")
