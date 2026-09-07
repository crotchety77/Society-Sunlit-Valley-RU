#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re

def main():
    with open('tasks/Translate_Mods/completed/translate_cluttered/en_us_all.json', 'r', encoding='utf-8') as f:
        en_us = json.load(f)

    # Загрузим существующий translations/mods/cluttered.json если есть
    try:
        with open('translations/mods/cluttered.json', 'r', encoding='utf-8') as f:
            ru_existing = json.load(f)
    except Exception:
        ru_existing = {}

    # Начнем формировать словарь полных переводов
    translations = {}

    # 1. Non-block keys
    translations["item.cluttered.hand_drill"] = "Ручная дрель"
    translations["cluttered.hand_drill.tooltip"] = "Используется для изменения деталей некоторых блоков.\nПрисядьте (Shift), чтобы вращать блоки.\nТекстура: EyeSeeDee!"
    translations["cluttered.bouncymushroom.tooltip"] = "Он такой прыгучий!"
    translations["cluttered.eye_block.tooltip"] = "Неприлично пялиться..."
    translations["cluttered.garland.tooltip"] = "Можно сдвигать влево и вправо с помощью ручной дрели"
    translations["cluttered.bracket.tooltip"] = "Можно размещать на заборах"
    translations["cluttered.polaroid_camera.tooltip"] = "Попробуйте вставить бумагу!"
    translations["cluttered.storage"] = "Хранилище"
    translations["cluttered.fridge"] = "Холодильник"
    translations["cluttered.box"] = "Картонная коробка"
    translations["creativetab.cluttered_tab"] = "Cluttered: Блоки"
    translations["creativetab.cluttered_furniture_tab"] = "Cluttered: Мебель"

    # Paintings
    translations["painting.cluttered.mimikyu.title"] = "Мимикью"
    translations["painting.cluttered.mimikyu.author"] = "YellowChuJelly"
    translations["painting.cluttered.candle.title"] = "Свеча"
    translations["painting.cluttered.candle.author"] = "Blakes"
    translations["painting.cluttered.cat_short.title"] = "Низкий кот"
    translations["painting.cluttered.cat_short.author"] = "Blakes"
    translations["painting.cluttered.crow_on_a_beach.title"] = "Ворона на пляже"
    translations["painting.cluttered.crow_on_a_beach.author"] = "Blakes"
    translations["painting.cluttered.eggplants_lynnhays.title"] = "Баклажаны"
    translations["painting.cluttered.eggplants_lynnhays.author"] = "Lynnhays"
    translations["painting.cluttered.etienne_carolhoffnagle.title"] = "Этьен"
    translations["painting.cluttered.etienne_carolhoffnagle.author"] = "Carol Hoffnagle"
    translations["painting.cluttered.flower_pots.title"] = "Цветочные горшки"
    translations["painting.cluttered.flower_pots.author"] = "Blakes"
    translations["painting.cluttered.lemons.title"] = "Лимоны"
    translations["painting.cluttered.lemons.author"] = "Blakes"
    translations["painting.cluttered.red_mushroom.title"] = "Красный гриб"
    translations["painting.cluttered.red_mushroom.author"] = "Blakes"
    translations["painting.cluttered.stiefmutterchen_heidedahl.title"] = "Анютины глазки"
    translations["painting.cluttered.stiefmutterchen_heidedahl.author"] = "Heide Dahl"
    translations["painting.cluttered.two_cats.title"] = "Два кота"
    translations["painting.cluttered.two_cats.author"] = "Blakes"
    translations["painting.cluttered.cat_tall.title"] = "Высокий кот"
    translations["painting.cluttered.cat_tall.author"] = "Blakes"
    translations["painting.cluttered.day_sky.title"] = "Дневное небо"
    translations["painting.cluttered.day_sky.author"] = "Blakes"
    translations["painting.cluttered.night_sky.title"] = "Ночное небо"
    translations["painting.cluttered.night_sky.author"] = "Blakes"
    translations["painting.cluttered.frogman_washington.title"] = "Человек-лягушка Вашингтон"
    translations["painting.cluttered.frogman_washington.author"] = "YellowChuJelly"
    translations["painting.cluttered.van_gogh_flamenettle.title"] = "Колеус"
    translations["painting.cluttered.van_gogh_flamenettle.author"] = "Ван Гог"
    translations["painting.cluttered.vase_of_sunflowers.title"] = "Ваза с подсолнухами"
    translations["painting.cluttered.vase_of_sunflowers.author"] = "Blakes"
    translations["painting.cluttered.worm.title"] = "Червячок"
    translations["painting.cluttered.worm.author"] = "YellowChuJelly"
    translations["painting.cluttered.pinned_butterflies.title"] = "Бабочки под стеклом"
    translations["painting.cluttered.pinned_butterflies.author"] = "Blakes"
    translations["painting.cluttered.van_gogh_horse.title"] = "Лошадь"
    translations["painting.cluttered.van_gogh_horse.author"] = "Ван Гог"
    translations["painting.cluttered.gold_sunflower.title"] = "Золотой подсолнух"
    translations["painting.cluttered.gold_sunflower.author"] = "Blakes"
    translations["painting.cluttered.van_gogh_wheatfield.title"] = "Пшеничное поле"
    translations["painting.cluttered.van_gogh_wheatfield.author"] = "Ван Гог"
    translations["painting.cluttered.ridley_fire.title"] = "Плазма Ридли"
    translations["painting.cluttered.ridley_fire.author"] = "YellowChuJelly"
    translations["painting.cluttered.ridley_dimension.title"] = "Измерение Ридли"
    translations["painting.cluttered.ridley_dimension.author"] = "RidleyDimensionFan"

    # Сохраняем промежуточный словарь
    print(f"Base translations loaded: {len(translations)}")

if __name__ == "__main__":
    main()
