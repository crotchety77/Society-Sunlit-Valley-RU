// priority: 100
/**
 * ============================================================================
 * 🎯 Cobblemon Real-Time Catch Rate HUD + Preview Mode (Client-Side)
 * ============================================================================
 * Версия: Cobblemon 1.5.2 | Minecraft 1.20.1 Forge | KubeJS 6
 * 
 * Точное математическое воспроизведение:
 * com.cobblemon.mod.common.pokeball.catching.calculators.CobblemonCaptureCalculator
 * 
 * Особенности:
 * - 100% Client-Side: 0 серверных пакетов, 0 команд, 0 TPS-нагрузки.
 * - Строгое разделение: Actual (текущий расчёт) vs Preview (прогноз контекста).
 * - Прямой Java Interop: вызов оригинальных модификаторов покеболов Cobblemon.
 * - Умное кэширование: мгновенная инвалидация при смене цели, руки или окружения.
 * ============================================================================
 */

// ============================================================================
// ⚙️ КОНФИГУРАЦИЯ И НАСТРОЙКИ
// ============================================================================
const HUD_CONFIG = {
    ENABLED: true,
    DEBUG: false,               // Расширенный вывод промежуточных переменных (X, A, B, Modifiers)
    OFFSET_X: 20,              // Смещение от центра экрана по X (+ вправо, - влево)
    OFFSET_Y: 25,              // Смещение от центра экрана по Y (+ вниз, - вверх)
    MAX_RAYCAST_DISTANCE: 16.0, // Дистанция поиска покемона перед игроком (в блоках)
    BG_COLOR: (0xAA000000 | 0),      // Полупрозрачный тёмный фон (ARGB)
    BORDER_COLOR: (0xCC555555 | 0)    // Цвет рамки HUD (ARGB)
};

// ============================================================================
// 📦 JAVA КЛАССЫ (COBBLEMON & MINECRAFT)
// ============================================================================
const $Minecraft = Java.loadClass('net.minecraft.client.Minecraft');
const $PokemonEntity = Java.loadClass('com.cobblemon.mod.common.entity.pokemon.PokemonEntity');
const $PokeBallItem = Java.loadClass('com.cobblemon.mod.common.item.PokeBallItem');
const $PokeBalls = Java.loadClass('com.cobblemon.mod.common.api.pokeball.PokeBalls');
const $HitResultType = Java.loadClass('net.minecraft.world.phys.HitResult$Type');

// Клиентское хранилище покемонов Cobblemon
let $CobblemonClient = null;
try {
    $CobblemonClient = Java.loadClass('com.cobblemon.mod.common.client.CobblemonClient');
} catch (e) {
    // Fallback if not available
}

// Классы статусов покемонов в Cobblemon
const $SleepStatus = Java.loadClass('com.cobblemon.mod.common.pokemon.status.statuses.persistent.SleepStatus');
const $FrozenStatus = Java.loadClass('com.cobblemon.mod.common.pokemon.status.statuses.persistent.FrozenStatus');
const $ParalysisStatus = Java.loadClass('com.cobblemon.mod.common.pokemon.status.statuses.persistent.ParalysisStatus');
const $BurnStatus = Java.loadClass('com.cobblemon.mod.common.pokemon.status.statuses.persistent.BurnStatus');
const $PoisonStatus = Java.loadClass('com.cobblemon.mod.common.pokemon.status.statuses.persistent.PoisonStatus');
const $PoisonBadlyStatus = Java.loadClass('com.cobblemon.mod.common.pokemon.status.statuses.persistent.PoisonBadlyStatus');

// ============================================================================
// 🧠 КЭШИРОВАНИЕ СОСТОЯНИЯ
// ============================================================================
let lastStateKey = null;
let cachedCalculation = null;

/**
 * Стилизация компонента вероятности поимки (100% безопасная для KubeJS / Minecraft)
 */
function styleChanceComponent(comp, chance) {
    if (chance >= 100.0) return comp.aqua().bold();
    if (chance >= 80.0) return comp.green().bold();
    if (chance >= 50.0) return comp.yellow().bold();
    if (chance >= 20.0) return comp.gold().bold();
    return comp.red().bold();
}

/**
 * Трассировка луча (Raycast) для поиска покемона перед игроком
 */
function getTargetedPokemon(mc, maxDistance) {
    let player = mc.player;
    let level = mc.level;
    if (!player || !level) return null;

    // 1. Проверяем стандартный кроссхейр Minecraft
    let hit = mc.hitResult;
    if (hit && hit.type == $HitResultType.ENTITY) {
        let entity = hit.entity;
        if (entity instanceof $PokemonEntity) return entity;
    }

    // 2. Расширенный raycast по направлению взгляда
    let eyePos = player.getEyePosition(1.0);
    let lookVec = player.getViewVector(1.0);
    let reachVec = eyePos.add(lookVec.x * maxDistance, lookVec.y * maxDistance, lookVec.z * maxDistance);
    let searchBox = player.getBoundingBox().expandTowards(lookVec.scale(maxDistance)).inflate(1.5);

    let candidateEntities = level.getEntities(player, searchBox, e => e instanceof $PokemonEntity && e.isAlive());
    if (!candidateEntities || candidateEntities.isEmpty()) return null;

    let closestEntity = null;
    let closestDistSq = maxDistance * maxDistance;

    for (let i = 0; i < candidateEntities.size(); i++) {
        let candidate = candidateEntities.get(i);
        let hitbox = candidate.getBoundingBox().inflate(0.3);
        let clipResult = hitbox.clip(eyePos, reachVec);
        if (clipResult.isPresent()) {
            let distSq = eyePos.distanceToSqr(clipResult.get());
            if (distSq < closestDistSq) {
                closestDistSq = distSq;
                closestEntity = candidate;
            }
        }
    }

    return closestEntity;
}

/**
 * Получение объекта PokeBall строго из ОСНОВНОЙ руки (MainHand)
 */
function getHeldPokeBall(player) {
    if (!player) return null;
    let item = player.getMainHandItem();
    if (!item || item.isEmpty()) return null;

    try {
        let rawItem = item.getItem();
        if (rawItem instanceof $PokeBallItem) {
            return rawItem.getPokeBall();
        }
        let itemId = item.getId();
        if (itemId && itemId.startsWith('cobblemon:') && itemId.endsWith('_ball')) {
            let pokeBall = $PokeBalls.INSTANCE.getPokeBall(itemId);
            if (pokeBall) return pokeBall;
        }
        if (item.hasTag('cobblemon:poke_balls')) {
            let pokeBall = $PokeBalls.INSTANCE.getPokeBall(itemId);
            if (pokeBall) return pokeBall;
        }
    } catch (e) {
        // Ignore invalid/non-Cobblemon item
    }
    return null;
}

/**
 * Получение первого живого (не упавшего в обморок) покемона из команды игрока (Party Lead)
 */
function getPlayerLeadPokemon() {
    if (!$CobblemonClient) return null;
    try {
        let storage = $CobblemonClient.storage;
        if (!storage) return null;
        let myParty = storage.getMyParty();
        if (!myParty || myParty.isEmpty()) return null;

        for (let i = 0; i < 6; i++) {
            let p = myParty.get(i);
            if (p && Number(p.getCurrentHealth()) > 0) {
                return p;
            }
        }
    } catch (e) {
        // Fallback
    }
    return null;
}

/**
 * Общий математический расчёт вероятности захвата по формуле CobblemonCaptureCalculator
 */
function calculateCatchChanceFromModifier(maxHp, currentHp, baseCatchRate, modeMod, statusMod, lowLevelMod, ballMod) {
    if (maxHp <= 0) {
        return { chance: 0.0, A: 0.0, B: 0 };
    }

    let clampedHp = Math.min(Math.max(0, currentHp), maxHp);
    let X = (3.0 * maxHp - 2.0 * clampedHp) * modeMod * baseCatchRate * ballMod;
    let A = (X / (3.0 * maxHp)) * statusMod * lowLevelMod;

    let catchChance = 0.0;
    let B = 0;

    if (A >= 255.0) {
        catchChance = 100.0;
        B = 65536;
    } else if (A <= 0.0) {
        catchChance = 0.0;
        B = 0;
    } else {
        // B = round(65536 / ( (255 / A)^0.1875 )) = round(65536 * (A / 255)^0.1875)
        B = Math.round(65536.0 * Math.pow(A / 255.0, 0.1875));
        let pShake = B / 65537.0;
        catchChance = Math.pow(pShake, 4) * 100.0;
        catchChance = Math.min(100.0, Math.max(0.0, catchChance));
    }

    return { chance: catchChance, A: A, B: B };
}

/**
 * Поиск боевого объекта покемона (ClientBattlePokemon) внутри активного боя Cobblemon
 */
function getBattlePokemonForEntity(targetEntity) {
    if (!$CobblemonClient) return null;
    try {
        let battle = $CobblemonClient.battle;
        if (!battle) return null;

        let targetMon = targetEntity.getPokemon();
        if (!targetMon) return null;
        let targetUuid = targetMon.getUuid();

        let sides = battle.getSides();
        if (!sides) return null;

        for (let s = 0; s < sides.length; s++) {
            let side = sides[s];
            if (!side) continue;
            let activeMons = side.getActiveClientBattlePokemon();
            if (!activeMons) continue;

            let iterator = activeMons.iterator();
            while (iterator.hasNext()) {
                let active = iterator.next();
                if (!active) continue;
                let bp = active.getBattlePokemon();
                if (bp && targetUuid && targetUuid.equals(bp.getUuid())) {
                    return bp;
                }
            }
        }
    } catch (e) {
        // Fallback
    }
    return null;
}

/**
 * Единый слой получения боевого/внебоевого состояния цели (Combat State)
 */
function getTargetCombatState(player, targetEntity) {
    let pokemon = targetEntity.getPokemon();
    if (!pokemon) return null;

    let baseMaxHp = Math.max(1, Number(pokemon.getHp()));
    let battleMon = getBattlePokemonForEntity(targetEntity);

    let currentHp = baseMaxHp;
    let maxHp = baseMaxHp;
    let inBattle = (targetEntity.getBattleId() != null) || (battleMon != null);
    let statusMod = 1.0;
    let statusName = "None";

    if (battleMon) {
        // Данные напрямую из активного боевого интерфейса Cobblemon (BattleOverlay)
        let hpVal = Number(battleMon.getHpValue());
        let maxVal = Number(battleMon.getMaxHp());
        let isFlat = battleMon.isHpFlat();

        if (!isFlat) {
            // Процентный режим (hpValue = 0..100)
            let ratio = Math.min(1.0, Math.max(0.0, hpVal / 100.0));
            currentHp = Math.round(baseMaxHp * ratio);
            maxHp = baseMaxHp;
        } else {
            // Абсолютный режим
            currentHp = Math.round(hpVal);
            maxHp = Math.max(1, Math.round(maxVal));
        }
        if (currentHp <= 0 && hpVal > 0) currentHp = 1;

        // Статус из активного боя
        let pStatus = battleMon.getStatus();
        if (pStatus instanceof $SleepStatus) { statusMod = 2.5; statusName = "Sleep"; }
        else if (pStatus instanceof $FrozenStatus) { statusMod = 2.5; statusName = "Frozen"; }
        else if (pStatus instanceof $ParalysisStatus) { statusMod = 1.5; statusName = "Paralysis"; }
        else if (pStatus instanceof $BurnStatus) { statusMod = 1.5; statusName = "Burn"; }
        else if (pStatus instanceof $PoisonStatus) { statusMod = 1.5; statusName = "Poison"; }
        else if (pStatus instanceof $PoisonBadlyStatus) { statusMod = 1.5; statusName = "Toxic"; }
    } else {
        // Вне боя: используем NBT статы покемона
        currentHp = Math.max(0, Number(pokemon.getCurrentHealth()));
        maxHp = baseMaxHp;
        if (currentHp <= 0 && Number(pokemon.getCurrentHealth()) > 0) currentHp = 1;

        try {
            let statusContainer = pokemon.getStatus();
            let persistentStatus = statusContainer ? statusContainer.getStatus() : null;

            if (persistentStatus instanceof $SleepStatus) { statusMod = 2.5; statusName = "Sleep"; }
            else if (persistentStatus instanceof $FrozenStatus) { statusMod = 2.5; statusName = "Frozen"; }
            else if (persistentStatus instanceof $ParalysisStatus) { statusMod = 1.5; statusName = "Paralysis"; }
            else if (persistentStatus instanceof $BurnStatus) { statusMod = 1.5; statusName = "Burn"; }
            else if (persistentStatus instanceof $PoisonStatus) { statusMod = 1.5; statusName = "Poison"; }
            else if (persistentStatus instanceof $PoisonBadlyStatus) { statusMod = 1.5; statusName = "Toxic"; }
        } catch (e) {
            statusMod = 1.0;
            statusName = "None";
        }
    }

    return {
        pokemon: pokemon,
        inBattle: inBattle,
        currentHp: currentHp,
        maxHp: maxHp,
        statusMod: statusMod,
        statusName: statusName
    };
}

/**
 * Точный расчёт фактического состояния (ACTUAL) по оригинальной формуле Cobblemon 1.5.2
 */
function calculateActualCatchRate(player, pokemonEntity, pokeBall) {
    let combatState = getTargetCombatState(player, pokemonEntity);
    if (!combatState) return null;

    let pokemon = combatState.pokemon;
    let maxHp = combatState.maxHp;
    let currentHp = combatState.currentHp;
    let inBattle = combatState.inBattle;
    let statusMod = combatState.statusMod;
    let statusName = combatState.statusName;

    let modifier = pokeBall.getCatchRateModifier();

    // 1. Проверка на Master Ball / Guaranteed
    if (modifier && modifier.isGuaranteed()) {
        return {
            chance: 100.0,
            isGuaranteed: true,
            ballName: pokeBall.getName().getPath(),
            species: pokemon.getSpecies().getName(),
            level: Number(pokemon.getLevel()),
            hp: currentHp,
            maxHp: maxHp,
            statusName: statusName,
            statusMod: statusMod,
            modeMod: inBattle ? 1.0 : 0.5,
            ballMod: null,
            A: 255.0,
            B: 65536
        };
    }

    // 2. Базовый Catch Rate вида/формы
    let form = pokemon.getForm();
    let baseCatchRate = form ? Number(form.getCatchRate()) : 45;

    // 3. Модификатор режима (В бою = 1.0, В открытом мире = 0.5)
    let modeMod = inBattle ? 1.0 : 0.5;

    // 4. Бонус низкого уровня (Level < 13)
    let level = Number(pokemon.getLevel());
    let lowLevelMod = 1.0;
    if (level < 13) {
        lowLevelMod = Math.max(1.0, Math.floor((36 - 2 * level) / 10));
    }

    // 5. Модификатор покебола через нативный вызов Cobblemon Java Interop
    // Строго по байткоду CobblemonCaptureCalculator: сначала isValid(), затем value()
    let ballMod = 1.0;
    try {
        let isValid = modifier.isValid(player, pokemon);
        if (isValid) {
            ballMod = Number(modifier.value(player, pokemon));
        }
    } catch (e) {
        ballMod = 1.0;
    }

    // 6. Математический расчёт A, B и шанса
    let mathResult = calculateCatchChanceFromModifier(maxHp, currentHp, baseCatchRate, modeMod, statusMod, lowLevelMod, ballMod);

    return {
        chance: mathResult.chance,
        isGuaranteed: false,
        ballName: pokeBall.getName().getPath(),
        species: pokemon.getSpecies().getName(),
        level: level,
        hp: currentHp,
        maxHp: maxHp,
        statusName: statusName,
        statusMod: statusMod,
        modeMod: modeMod,
        ballMod: ballMod,
        baseCatchRate: baseCatchRate,
        lowLevelMod: lowLevelMod,
        A: mathResult.A,
        B: mathResult.B
    };
}

/**
 * Прогнозный расчёт гипотетического боевого контекста (PREVIEW)
 */
function calculatePreviewCatchRate(player, pokemonEntity, pokeBall, actualData) {
    if (!actualData || actualData.isGuaranteed) return null;

    let pokemon = pokemonEntity.getPokemon();
    if (!pokemon) return null;

    let ballId = pokeBall.getName().getPath();
    let inBattle = pokemonEntity.getBattleId() != null;

    let previewBallMod = null;
    let previewContext = null;

    // 1. Quick Ball (5.0x на Turn 1 боя)
    if (ballId === 'quick_ball' && !inBattle) {
        previewBallMod = 5.0;
        previewContext = "Turn 1";
    }
    // 2. Timer Ball (1.3x на Turn 1, до 4.0x на Turn 10+)
    else if (ballId === 'timer_ball' && !inBattle) {
        previewBallMod = 1.3;
        previewContext = "Turn 1";
    }
    // 3. Level Ball (Сравнение уровня с первым живым покемоном группы)
    else if (ballId === 'level_ball' && !inBattle) {
        let leadPokemon = getPlayerLeadPokemon();
        if (leadPokemon) {
            let leadLvl = Number(leadPokemon.getLevel());
            let targetLvl = actualData.level;
            if (leadLvl > targetLvl * 4) {
                previewBallMod = 8.0;
                previewContext = `Lv.${leadLvl} > 4x`;
            } else if (leadLvl > targetLvl * 2) {
                previewBallMod = 4.0;
                previewContext = `Lv.${leadLvl} > 2x`;
            } else if (leadLvl > targetLvl) {
                previewBallMod = 2.0;
                previewContext = `Lv.${leadLvl} > Target`;
            } else {
                previewBallMod = 1.0;
                previewContext = `Lv.${leadLvl} <= Target`;
            }
        } else {
            previewContext = "No Living Mon";
        }
    }
    // 4. Love Ball (Сравнение вида и противоположного пола с первым живым покемоном группы)
    else if (ballId === 'love_ball' && !inBattle) {
        let leadPokemon = getPlayerLeadPokemon();
        if (leadPokemon) {
            let targetGender = String(pokemon.getGender().name());
            let leadGender = String(leadPokemon.getGender().name());
            let targetSpecies = String(pokemon.getSpecies().getName()).toLowerCase();
            let leadSpecies = String(leadPokemon.getSpecies().getName()).toLowerCase();

            let isOppositeGender = (targetGender === 'MALE' && leadGender === 'FEMALE') ||
                                   (targetGender === 'FEMALE' && leadGender === 'MALE');
            let isSameSpecies = (targetSpecies === leadSpecies);

            if (isSameSpecies && isOppositeGender) {
                previewBallMod = 8.0;
                previewContext = "Match";
            } else {
                previewBallMod = 1.0;
                previewContext = "No Match";
            }
        } else {
            previewContext = "No Living Mon";
        }
    }

    if (previewBallMod !== null) {
        let mathResult = calculateCatchChanceFromModifier(
            actualData.maxHp,
            actualData.hp,
            actualData.baseCatchRate,
            actualData.modeMod,
            actualData.statusMod,
            actualData.lowLevelMod,
            previewBallMod
        );

        if (Math.abs(mathResult.chance - actualData.chance) > 0.01) {
            return {
                chance: mathResult.chance,
                ballMod: previewBallMod,
                context: previewContext,
                A: mathResult.A,
                B: mathResult.B
            };
        }
    }

    return null;
}

// ============================================================================
// 🖥️ ОТРИСОВКА HUD (PAINT SCREEN EVENT)
// ============================================================================
let lastErrorLogTime = 0;

ClientEvents.paintScreen(e => {
    try {
        if (!HUD_CONFIG.ENABLED) return;

        let mc = $Minecraft.getInstance();
        let player = mc.player;
        if (!player || mc.options.hideGui) return;

        // 1. Проверяем покебол строго в основной руке
        let pokeBall = getHeldPokeBall(player);
        if (!pokeBall) {
            lastStateKey = null;
            cachedCalculation = null;
            return;
        }

        // 2. Ищем покемона под прицелом
        let target = getTargetedPokemon(mc, HUD_CONFIG.MAX_RAYCAST_DISTANCE);
        if (!target) {
            lastStateKey = null;
            cachedCalculation = null;
            return;
        }

        let pokemon = target.getPokemon();
        if (!pokemon) return;

        // 3. Формируем ключ состояния для кэша
        let lead = getPlayerLeadPokemon();
        let leadKey = 'none';
        if (lead) {
            try {
                leadKey = `${String(lead.getSpecies().getName())}_${lead.getLevel()}_${String(lead.getGender().name())}`;
            } catch (err) {
                leadKey = 'none';
            }
        }

        let timeQuantum = Math.floor(Number(player.tickCount) / 10);
        let targetHealthScaled = Math.round(Number(target.getHealth()) * 10);
        let ballPath = String(pokeBall.getName().getPath());
        let inBattle = target.getBattleId() != null;

        let stateKey = `${target.getId()}_${targetHealthScaled}_${pokemon.getHp()}_${pokemon.getLevel()}_${ballPath}_${inBattle}_${leadKey}_${timeQuantum}`;

        if (stateKey !== lastStateKey || !cachedCalculation) {
            lastStateKey = stateKey;
            let actual = calculateActualCatchRate(player, target, pokeBall);
            let preview = calculatePreviewCatchRate(player, target, pokeBall, actual);
            cachedCalculation = { actual: actual, preview: preview };
        }

        let data = cachedCalculation.actual;
        let previewData = cachedCalculation.preview;
        if (!data) return;

        // 4. Отрисовка интерфейса
        let screenW = e.width;
        let screenH = e.height;

        let centerX = (Math.floor(screenW / 2) + HUD_CONFIG.OFFSET_X) | 0;
        let centerY = (Math.floor(screenH / 2) + HUD_CONFIG.OFFSET_Y) | 0;

        // Форматирование текстов
        let titleText = `${data.species} Lv.${data.level}`;
        let effectiveMaxHp = Math.max(1, data.maxHp);
        let hpPercent = Math.round((data.hp / effectiveMaxHp) * 100);
        let hpText = `HP: ${data.hp}/${data.maxHp} (${hpPercent}%)`;
        let statusText = data.statusName !== 'None' ? `Status: ${data.statusName}` : null;
        let ballText = `Ball: ${data.ballName.replace(/_/g, ' ').toUpperCase()}`;

        // Расчёт размеров плашки
        let hasPreview = (previewData !== null && previewData.chance !== data.chance);
        let boxW = 150;
        let boxH = 52;
        if (statusText) boxH += 10;
        if (hasPreview) boxH += 10;
        if (HUD_CONFIG.DEBUG) boxH += 40;

        let startX = centerX;
        let startY = centerY;

        let x1 = (startX - 5) | 0;
        let y1 = (startY - 5) | 0;
        let x2 = (startX + boxW) | 0;
        let y2 = (startY + boxH) | 0;

        // Отрисовка фона через GuiGraphics
        if (e.graphics) {
            e.graphics.fill(x1 - 1, y1 - 1, x2 + 1, y2 + 1, (HUD_CONFIG.BORDER_COLOR | 0));
            e.graphics.fill(x1, y1, x2, y2, (HUD_CONFIG.BG_COLOR | 0));
        }

        // Отрисовка строк
        let currentY = startY;

        // 1. Имя и Уровень
        e.text(Component.literal(titleText).gold().bold(), (startX | 0), (currentY | 0), (0xFFFFAA00 | 0), true);
        currentY += 10;

        // 2. HP
        let hpColor = (hpPercent > 50 ? 0xFF55FF55 : (hpPercent > 20 ? 0xFFFFAA00 : 0xFFFF5555)) | 0;
        e.text(Component.literal(hpText), (startX | 0), (currentY | 0), hpColor, true);
        currentY += 10;

        // 3. Статус (если есть)
        if (statusText) {
            e.text(Component.literal(statusText).aqua(), (startX | 0), (currentY | 0), (0xFF55FFFF | 0), true);
            currentY += 10;
        }

        // 4. Тип покебола
        e.text(Component.literal(ballText).white(), (startX | 0), (currentY | 0), (0xFFFFFFFF | 0), true);
        currentY += 11;

        // 5. Итоговый процент поимки
        if (data.isGuaranteed) {
            let guaranteedComponent = Component.literal("Catch: ").white()
                .append(Component.literal("100.0% GUARANTEED").aqua().bold());
            e.text(guaranteedComponent, (startX | 0), (currentY | 0), (0xFFFFFFFF | 0), true);
        } else if (hasPreview) {
            // Режим с предпросмотром: Actual vs Preview
            let actualFormatted = data.chance.toFixed(1) + '%';
            let actualComp = Component.literal("Actual: ").gray()
                .append(styleChanceComponent(Component.literal(actualFormatted), data.chance));
            e.text(actualComp, (startX | 0), (currentY | 0), (0xFFAAAAAA | 0), true);
            currentY += 10;

            let previewFormatted = previewData.chance.toFixed(1) + '%';
            let previewComp = Component.literal("Preview: ").yellow()
                .append(styleChanceComponent(Component.literal(previewFormatted), previewData.chance))
                .append(Component.literal(` [${previewData.context}]`).gray());
            e.text(previewComp, (startX | 0), (currentY | 0), (0xFFFFFFFF | 0), true);
        } else {
            // Обычный режим
            let chanceFormatted = data.chance.toFixed(1) + '%';
            let chanceComponent = Component.literal("Catch: ").white()
                .append(styleChanceComponent(Component.literal(chanceFormatted), data.chance));
            e.text(chanceComponent, (startX | 0), (currentY | 0), (0xFFFFFFFF | 0), true);
        }

        // Debug Mode
        if (HUD_CONFIG.DEBUG) {
            currentY += 11;
            let bModStr = data.ballMod !== null ? `${data.ballMod.toFixed(2)}x` : 'N/A';
            e.text(Component.literal(`Mode: ${data.modeMod}x | BallMod: ${bModStr}`).gray(), (startX | 0), (currentY | 0), (0xFFAAAAAA | 0), false);
            currentY += 9;
            e.text(Component.literal(`BaseCR: ${data.baseCatchRate} | StatusMod: ${data.statusMod}x`).gray(), (startX | 0), (currentY | 0), (0xFFAAAAAA | 0), false);
            currentY += 9;
            e.text(Component.literal(`A: ${data.A.toFixed(2)} | B: ${data.B}`).darkGray(), (startX | 0), (currentY | 0), (0xFF888888 | 0), false);
        }
    } catch (err) {
        let now = Date.now();
        if (now - lastErrorLogTime > 3000) {
            lastErrorLogTime = now;
            console.error("[Cobblemon HUD ERROR] in paintScreen: " + err);
        }
    }
});

console.info("[Cobblemon HUD] catch_rate_hud.js with Preview Mode loaded!");

