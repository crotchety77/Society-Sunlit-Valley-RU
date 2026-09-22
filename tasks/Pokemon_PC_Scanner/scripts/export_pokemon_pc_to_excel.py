"""
Скрипт генерации детального Excel-каталога покемонов из ПК Cobblemon
с автоматической цветовой градацией показателей IV и процентов (K:R).
Вкладки:
1. 'Все покемоны'
2. 'Команда (Party)'
3. 'ПК (PC Boxes)'
4. 'Шайни ✨'
5. 'Топ IV (80%+)'
"""

import os
import glob
import json
import zipfile
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Цвета типов покемонов (HEX) и перевод
TYPE_DATA = {
    'normal':   {'ru': 'Обычный',     'bg': 'A8A878', 'fg': 'FFFFFF'},
    'fire':     {'ru': 'Огненный',    'bg': 'F08030', 'fg': 'FFFFFF'},
    'water':    {'ru': 'Водный',      'bg': '6890F0', 'fg': 'FFFFFF'},
    'grass':    {'ru': 'Травяной',    'bg': '78C850', 'fg': 'FFFFFF'},
    'electric': {'ru': 'Электрический','bg': 'F8D030', 'fg': '000000'},
    'ice':      {'ru': 'Ледяной',     'bg': '98D8D8', 'fg': '000000'},
    'fighting': {'ru': 'Боевой',      'bg': 'C03028', 'fg': 'FFFFFF'},
    'poison':   {'ru': 'Ядовитый',    'bg': 'A040A0', 'fg': 'FFFFFF'},
    'ground':   {'ru': 'Земляной',    'bg': 'E0C068', 'fg': '000000'},
    'flying':   {'ru': 'Летающий',    'bg': 'A890F0', 'fg': 'FFFFFF'},
    'psychic':  {'ru': 'Психический', 'bg': 'F85888', 'fg': 'FFFFFF'},
    'bug':      {'ru': 'Насекомое',   'bg': 'A8B820', 'fg': 'FFFFFF'},
    'rock':     {'ru': 'Каменный',    'bg': 'B8A038', 'fg': 'FFFFFF'},
    'ghost':    {'ru': 'Призрачный',  'bg': '705898', 'fg': 'FFFFFF'},
    'dragon':   {'ru': 'Драконий',    'bg': '7038F8', 'fg': 'FFFFFF'},
    'steel':    {'ru': 'Стальной',    'bg': 'B8B8D0', 'fg': '000000'},
    'dark':     {'ru': 'Тёмный',      'bg': '705848', 'fg': 'FFFFFF'},
    'fairy':    {'ru': 'Волшебный',   'bg': 'EE99AC', 'fg': '000000'},
}

def get_iv_stat_style(val):
    """
    Цветовая градация для показателей IV (0-31):
    - 0-8: Красный
    - 9-16: Оранжевый
    - 17-23: Жёлтый
    - 24-27: Светло-зелёный
    - 28-31: Насыщенный зелёный (31 жирный)
    """
    if val <= 8:
        return {'bg': 'FECACA', 'fg': '991B1B', 'bold': False}  # Красный
    elif val <= 16:
        return {'bg': 'FED7AA', 'fg': '9A3412', 'bold': False}  # Оранжевый
    elif val <= 23:
        return {'bg': 'FEF08A', 'fg': '854D0E', 'bold': False}  # Жёлтый
    elif val <= 27:
        return {'bg': 'BBF7D0', 'fg': '166534', 'bold': False}  # Светло-зелёный
    else:
        return {'bg': '4ADE80', 'fg': '052E16', 'bold': True}   # Зелёный (28-31)

def get_iv_percent_style(pct):
    """
    Цветовая градация для общего IV%:
    - < 50%: Красный
    - 50-64.9%: Оранжевый
    - 65-79.9%: Жёлтый
    - 80-89.9%: Светло-зелёный
    - 90-100%: Насыщенный зелёный
    """
    if pct < 50.0:
        return {'bg': 'FECACA', 'fg': '991B1B', 'bold': False}
    elif pct < 65.0:
        return {'bg': 'FED7AA', 'fg': '9A3412', 'bold': False}
    elif pct < 80.0:
        return {'bg': 'FEF08A', 'fg': '854D0E', 'bold': False}
    elif pct < 90.0:
        return {'bg': 'BBF7D0', 'fg': '166534', 'bold': True}
    else:
        return {'bg': '4ADE80', 'fg': '052E16', 'bold': True}

def load_ru_pokemon_names():
    ru_species = {}
    ru_moves = {}
    ru_natures = {
        'hardy': 'Выносливый', 'docile': 'Послушный', 'brave': 'Храбрый', 'adamant': 'Непреклонный',
        'naughty': 'Озорной', 'bold': 'Смелый', 'relaxed': 'Спокойный', 'impish': 'Шаловливый',
        'lax': 'Беспечный', 'timid': 'Робкий', 'hasty': 'Поспешный', 'serious': 'Серьёзный',
        'jolly': 'Весёлый', 'naive': 'Наивный', 'modest': 'Скромный', 'mild': 'Мягкий',
        'quiet': 'Тихий', 'bashful': 'Застенчивый', 'rash': 'Опрометчивый', 'calm': 'Спокойный',
        'gentle': 'Нежный', 'sassy': 'Дерзкий', 'careful': 'Осторожный', 'quirky': 'Причудливый',
        'lonely': 'Одинокий'
    }

    for jar_path in glob.glob(r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\mods\*.jar'):
        try:
            with zipfile.ZipFile(jar_path, 'r') as z:
                for n in z.namelist():
                    if 'ru_ru.json' in n:
                        try:
                            d = json.loads(z.read(n).decode('utf-8'))
                            for k, v in d.items():
                                if k.startswith('cobblemon.species.') and not k.endswith('.desc'):
                                    sp_id = k.replace('cobblemon.species.', '').lower()
                                    ru_species[sp_id] = v
                                elif k.startswith('cobblemon.move.') and not k.endswith('.desc'):
                                    m_id = k.replace('cobblemon.move.', '').lower()
                                    ru_moves[m_id] = v
                        except:
                            pass
        except:
            pass

    return ru_species, ru_moves, ru_natures

def build_pokemon_excel(pokemon_list, ru_species, ru_moves, ru_natures, output_path):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    header_font = Font(name='Segoe UI', size=11, bold=True, color='FFFFFF')
    header_fill = PatternFill(start_color='0F172A', end_color='0F172A', fill_type='solid')

    zebra_fill = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid')
    white_fill = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')
    shiny_gold_fill = PatternFill(start_color='FEF08A', end_color='FEF08A', fill_type='solid')

    headers = [
        'Расположение', 'Покемон (EN)', 'Русское имя', 'Уровень', 'Шайни ✨', 'Пол',
        'Тип 1', 'Тип 2', 'Характер', 'Способность',
        'IV %', 'HP', 'Атк', 'Защ', 'СпА', 'СпЗ', 'Скор',
        'EV Всего', 'Атаки (Moveset)', 'Надетый предмет'
    ]

    sheets_config = [
        ('Все покемоны', pokemon_list),
        ('Команда (Party)', [p for p in pokemon_list if 'Команда' in p.get('location', '')]),
        ('ПК (PC Boxes)', [p for p in pokemon_list if 'Коробка' in p.get('location', '')]),
        ('Шайни ✨', [p for p in pokemon_list if p.get('shiny')]),
        ('Топ IV (80%+)', [p for p in pokemon_list if p.get('ivs', {}).get('percentage', 0) >= 80])
    ]

    for title, p_list in sheets_config:
        if not p_list and title != 'Все покемоны':
            continue

        ws = wb.create_sheet(title=title)
        ws.views.sheetView[0].showGridLines = True

        ws.append(headers)
        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col_idx)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = thin_border
        ws.row_dimensions[1].height = 28

        for row_idx, p in enumerate(p_list, start=2):
            sp_en = p.get('species', 'Unknown').capitalize()
            sp_ru = ru_species.get(p.get('species', '').lower(), sp_en)
            loc = p.get('location', 'PC')
            lvl = p.get('level', 1)
            shiny_str = '✨ ШАЙНИ' if p.get('shiny') else 'Нет'
            gender = '♂ Самец' if p.get('gender') == 'MALE' else ('♀ Самка' if p.get('gender') == 'FEMALE' else '⚲ Без пола')
            
            types = p.get('types', [])
            t1 = types[0] if len(types) > 0 else 'normal'
            t2 = types[1] if len(types) > 1 else None

            t1_info = TYPE_DATA.get(t1.lower(), {'ru': t1.capitalize(), 'bg': 'E2E8F0', 'fg': '000000'})
            t2_info = TYPE_DATA.get(t2.lower(), {'ru': t2.capitalize(), 'bg': 'E2E8F0', 'fg': '000000'}) if t2 else None

            nat_raw = p.get('nature', 'Unknown').lower()
            nat_ru = ru_natures.get(nat_raw, nat_raw.capitalize())
            ability = p.get('ability', 'Unknown').capitalize()

            ivs = p.get('ivs', {})
            iv_num = ivs.get('percentage', 0)
            iv_pct = f"{iv_num}%"
            hp_iv = ivs.get('hp', 0)
            atk_iv = ivs.get('attack', 0)
            def_iv = ivs.get('defence', 0)
            spa_iv = ivs.get('special_attack', 0)
            spd_iv = ivs.get('special_defence', 0)
            spe_iv = ivs.get('speed', 0)

            evs = p.get('evs', {})
            ev_tot = evs.get('total', 0)

            moves_raw = p.get('moves', [])
            moves_display = ', '.join([ru_moves.get(m.lower().replace(' ', '').replace('-', ''), m.title()) for m in moves_raw])
            held = p.get('held_item', 'None').replace('minecraft:', '').replace('_', ' ').capitalize()

            row_data = [
                loc, sp_en, sp_ru, lvl, shiny_str, gender,
                t1_info['ru'], t2_info['ru'] if t2_info else '-', nat_ru, ability,
                iv_pct, hp_iv, atk_iv, def_iv, spa_iv, spd_iv, spe_iv,
                ev_tot, moves_display, held
            ]

            ws.append(row_data)

            is_even = (row_idx % 2 == 0)
            row_fill = zebra_fill if is_even else white_fill

            for col_idx in range(1, len(headers) + 1):
                c = ws.cell(row=row_idx, column=col_idx)
                c.border = thin_border
                c.font = Font(name='Segoe UI', size=10)
                c.alignment = Alignment(horizontal='center', vertical='center')
                c.fill = row_fill

            ws.cell(row=row_idx, column=1).alignment = Alignment(horizontal='left', vertical='center')
            ws.cell(row=row_idx, column=2).alignment = Alignment(horizontal='left', vertical='center')
            ws.cell(row=row_idx, column=3).alignment = Alignment(horizontal='left', vertical='center')
            ws.cell(row=row_idx, column=19).alignment = Alignment(horizontal='left', vertical='center')

            # Подсветка Шайни
            if p.get('shiny'):
                ws.cell(row=row_idx, column=5).fill = shiny_gold_fill
                ws.cell(row=row_idx, column=5).font = Font(name='Segoe UI', size=10, bold=True, color='854D0E')

            # Подсветка Типов
            c_t1 = ws.cell(row=row_idx, column=7)
            c_t1.fill = PatternFill(start_color=t1_info['bg'], end_color=t1_info['bg'], fill_type='solid')
            c_t1.font = Font(name='Segoe UI', size=10, bold=True, color=t1_info['fg'])

            if t2_info:
                c_t2 = ws.cell(row=row_idx, column=8)
                c_t2.fill = PatternFill(start_color=t2_info['bg'], end_color=t2_info['bg'], fill_type='solid')
                c_t2.font = Font(name='Segoe UI', size=10, bold=True, color=t2_info['fg'])

            # 🎨 ЦВЕТОВАЯ ГРАДАЦИЯ СТОЛБЦОВ K:Q (IV% и отдельные статы)
            # 1. Столбец K (11) - IV %
            pct_style = get_iv_percent_style(iv_num)
            c_pct = ws.cell(row=row_idx, column=11)
            c_pct.fill = PatternFill(start_color=pct_style['bg'], end_color=pct_style['bg'], fill_type='solid')
            c_pct.font = Font(name='Segoe UI', size=10, bold=pct_style['bold'], color=pct_style['fg'])

            # 2. Столбцы L:Q (12-17) - HP, Атк, Защ, СпА, СпЗ, Скор
            iv_stat_values = [hp_iv, atk_iv, def_iv, spa_iv, spd_iv, spe_iv]
            for offset, val in enumerate(iv_stat_values):
                col_i = 12 + offset
                st = get_iv_stat_style(val)
                c_stat = ws.cell(row=row_idx, column=col_i)
                c_stat.fill = PatternFill(start_color=st['bg'], end_color=st['bg'], fill_type='solid')
                c_stat.font = Font(name='Segoe UI', size=10, bold=st['bold'], color=st['fg'])

            # 3. Столбец R (18) - EV Всего (если прокачан на максимум 508-510)
            if ev_tot >= 508:
                c_ev = ws.cell(row=row_idx, column=18)
                c_ev.fill = PatternFill(start_color='E0E7FF', end_color='E0E7FF', fill_type='solid')
                c_ev.font = Font(name='Segoe UI', size=10, bold=True, color='3730A3')

            ws.row_dimensions[row_idx].height = 22

        ws.freeze_panes = 'A2'

        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or '')
                max_len = max(max_len, len(val))
            ws.column_dimensions[col_letter].width = max(max_len + 4, 11)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        wb.save(output_path)
        print(f"Таблица покемонов успешно сохранена: {output_path}")
    except PermissionError:
        alt_path = output_path.replace('.xlsx', '_updated.xlsx')
        wb.save(alt_path)
        print(f"[ВНИМАНИЕ] Файл '{os.path.basename(output_path)}' открыт в Excel. Сохранено в: {alt_path}")

def main():
    json_candidates = [
        r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Pokemon_PC_Scanner\docs\my_cobblemon_pc.json',
        r'G:\curseforge\minecraft\Instances\Society Sunlit Cobblemon\kubejs\my_cobblemon_pc.json',
    ]

    target_json = None
    for p in json_candidates:
        if os.path.exists(p):
            target_json = p
            break

    if not target_json:
        print("Файл my_cobblemon_pc.json пока не найден. Зайдите в игру, откройте ПК и нажмите F9!")
        return

    print(f"Загрузка данных из: {target_json}")
    with open(target_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    p_list = data.get('pokemon', [])
    print(f"Найдено покемонов в JSON: {len(p_list)}")

    ru_species, ru_moves, ru_natures = load_ru_pokemon_names()

    out_xlsx = r'c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода\tasks\Pokemon_PC_Scanner\docs\Cobblemon_PC_Catalog.xlsx'
    build_pokemon_excel(p_list, ru_species, ru_moves, ru_natures, out_xlsx)

if __name__ == '__main__':
    main()
