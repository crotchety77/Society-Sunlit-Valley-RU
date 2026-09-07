const fs = require('fs');
const path = require('path');

const modpackBase = 'D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\assets';
const modpackKubejs = 'D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs';
const localBase = __dirname;

// 1. Run compile.js for Dialogs
console.log('--- 1. Сборка диалогов NPC (1475 строк) ---');
require(path.join(localBase, 'translations/dialogs/compile.js'));

// 2. Sync portable_blueprints
console.log('\n--- 2. Синхронизация построек (portable_blueprints) ---');
const blueprintsSource = path.join(localBase, 'translations/buildings/portable_blueprints_ru_ru.json');
const blueprintsTargetDir = path.join(modpackBase, 'portable_blueprints/lang');
const blueprintsTarget = path.join(blueprintsTargetDir, 'ru_ru.json');

if (fs.existsSync(blueprintsSource)) {
    if (!fs.existsSync(blueprintsTargetDir)) {
        fs.mkdirSync(blueprintsTargetDir, { recursive: true });
    }
    fs.copyFileSync(blueprintsSource, blueprintsTarget);
    const count = Object.keys(JSON.parse(fs.readFileSync(blueprintsSource, 'utf8'))).length;
    console.log(`✅ Скопировано (${count} ключей) -> ${blueprintsTarget}`);
}

// 3. Sync society_trading
console.log('\n--- 3. Синхронизация торговли (society_trading) ---');
const tradingSource = path.join(localBase, 'translations/buildings/society_trading_building_shop_ru_ru.json');
const tradingTargetDir = path.join(modpackBase, 'society_trading/lang');
const tradingTarget = path.join(tradingTargetDir, 'ru_ru.json');

if (fs.existsSync(tradingSource)) {
    if (!fs.existsSync(tradingTargetDir)) {
        fs.mkdirSync(tradingTargetDir, { recursive: true });
    }
    
    let currentTrading = {};
    if (fs.existsSync(tradingTarget)) {
        try {
            currentTrading = JSON.parse(fs.readFileSync(tradingTarget, 'utf8'));
        } catch (e) {}
    }
    const newTrading = JSON.parse(fs.readFileSync(tradingSource, 'utf8'));
    const merged = { ...currentTrading, ...newTrading };
    
    fs.writeFileSync(tradingTarget, JSON.stringify(merged, null, 2), 'utf8');
    console.log(`✅ Синхронизировано (${Object.keys(merged).length} ключей) -> ${tradingTarget}`);
}

// 4. Sync society_tips
console.log('\n--- 4. Синхронизация внутриигровых советов (society_tips) ---');
const tipsSource = path.join(localBase, 'translations/tips/society_tips_ru_ru.json');
const tipsTargetDir = path.join(modpackBase, 'society_tips/lang');
const tipsTarget = path.join(tipsTargetDir, 'ru_ru.json');

if (fs.existsSync(tipsSource)) {
    if (!fs.existsSync(tipsTargetDir)) {
        fs.mkdirSync(tipsTargetDir, { recursive: true });
    }
    fs.copyFileSync(tipsSource, tipsTarget);
    const count = Object.keys(JSON.parse(fs.readFileSync(tipsSource, 'utf8'))).length;
    console.log(`✅ Скопировано (${count} советов) -> ${tipsTarget}`);
}

// 5. Sync custom client scripts (invitation & greenhouse tooltips, JEI categories)
console.log('\n--- 5. Синхронизация скриптов подсказок и JEI KubeJS ---');
const scriptTargetDir = path.join(modpackKubejs, 'client_scripts/tooltips');

function installTooltipScript(filename, label) {
    const src = path.join(localBase, 'kubejs_scripts/client', filename);
    const target = path.join(scriptTargetDir, filename);
    const staleRoot = path.join(modpackKubejs, 'client_scripts', filename);

    if (fs.existsSync(src)) {
        if (!fs.existsSync(scriptTargetDir)) {
            fs.mkdirSync(scriptTargetDir, { recursive: true });
        }
        fs.copyFileSync(src, target);
        console.log(`✅ Установлен скрипт подсказок ${label} -> ${target}`);

        // Защита от дублирования KubeJS: удаляем старый файл из корня client_scripts/
        if (fs.existsSync(staleRoot)) {
            fs.unlinkSync(staleRoot);
            console.log(`🧹 Удалён устаревший дубликат из корня -> ${staleRoot}`);
        }
    }
}

installTooltipScript('invitationTooltips.js', 'Invitation & NPC');
installTooltipScript('unusualFishTooltips.js', 'Unusual Fish');
installTooltipScript('tanukiDecorTooltips.js', 'Tanuki Decor');
installTooltipScript('longwingsTooltips.js', 'Longwings');
installTooltipScript('etceteraTooltips.js', 'Etcetera');
installTooltipScript('buildinggadgets2Tooltips.js', 'Building Gadgets 2');
installTooltipScript('createCentralKitchenTooltips.js', 'Create: Central Kitchen');
installTooltipScript('bountifulTooltips.js', 'Bountiful');

const addTooltipsSrc = path.join(localBase, 'game_data/client_scripts/tooltips/addTooltips.js');
const addTooltipsTarget = path.join(modpackKubejs, 'client_scripts/tooltips/addTooltips.js');
if (fs.existsSync(addTooltipsSrc)) {
    fs.copyFileSync(addTooltipsSrc, addTooltipsTarget);
    console.log(`✅ Синхронизирован основной скрипт подсказок addTooltips.js -> ${addTooltipsTarget}`);
}

const jeiScriptSource = path.join(localBase, 'kubejs_scripts/client/universalGiftsJei.js');
const jeiScriptTarget = path.join(modpackKubejs, 'client_scripts/universalGiftsJei.js');
if (fs.existsSync(jeiScriptSource)) {
    fs.copyFileSync(jeiScriptSource, jeiScriptTarget);
    console.log(`✅ Установлен скрипт JEI -> ${jeiScriptTarget}`);
}

const etceteraJeiSource = path.join(localBase, 'kubejs_scripts/client/etceteraJei.js');
const etceteraJeiTarget = path.join(modpackKubejs, 'client_scripts/etceteraJei.js');
if (fs.existsSync(etceteraJeiSource)) {
    fs.copyFileSync(etceteraJeiSource, etceteraJeiTarget);
    console.log(`✅ Установлен скрипт JEI Etcetera -> ${etceteraJeiTarget}`);
}


const ticketScriptSource = path.join(localBase, 'kubejs_scripts/server/slimeTicket.js');
const ticketScriptTarget = path.join(modpackKubejs, 'server_scripts/entities/slimeTicket.js');
if (fs.existsSync(ticketScriptSource)) {
    fs.copyFileSync(ticketScriptSource, ticketScriptTarget);
    console.log(`✅ Установлен скрипт Билета слайма -> ${ticketScriptTarget}`);
}

const inspectorScriptSource = path.join(localBase, 'tasks/Translate_Mods/translate_splendid_slimes/kubejs_scripts/server/slimeInspectorEnhanced.js');
const inspectorScriptTarget = path.join(modpackKubejs, 'server_scripts/entities/slimeInspectorEnhanced.js');
if (fs.existsSync(inspectorScriptSource)) {
    fs.copyFileSync(inspectorScriptSource, inspectorScriptTarget);
    console.log(`✅ Установлен скрипт расширенного Анализатора слаймов -> ${inspectorScriptTarget}`);
}





// 6. Sync society main lang
console.log('\n--- 6. Синхронизация основного мода Society (society) ---');
const societySource = path.join(localBase, 'translations/society/ru_ru.json');
const societyTargetDir = path.join(modpackBase, 'society/lang');
const societyTarget = path.join(societyTargetDir, 'ru_ru.json');

if (fs.existsSync(societySource)) {
    if (!fs.existsSync(societyTargetDir)) {
        fs.mkdirSync(societyTargetDir, { recursive: true });
    }
    fs.copyFileSync(societySource, societyTarget);
    const count = Object.keys(JSON.parse(fs.readFileSync(societySource, 'utf8'))).length;
    console.log(`✅ Скопировано (${count} ключей) -> ${societyTarget}`);
}

const framesSource = path.join(localBase, 'translations/society/tooltipoverhaul/custom_frames.json');
const framesTargetDir = path.join(modpackBase, 'society/tooltipoverhaul');
const framesTarget = path.join(framesTargetDir, 'custom_frames.json');

if (fs.existsSync(framesSource)) {
    if (!fs.existsSync(framesTargetDir)) {
        fs.mkdirSync(framesTargetDir, { recursive: true });
    }
    fs.copyFileSync(framesSource, framesTarget);
    console.log(`✅ Скопированы кастомные рамки Tooltip Overhaul -> ${framesTarget}`);
}

// 7. Apply mod translations from translations/mods/*.json
console.log('\n--- 7. Синхронизация переводов модов (translations/mods/) ---');
const modsDir = path.join(localBase, 'translations/mods');
if (fs.existsSync(modsDir)) {
    const modFiles = fs.readdirSync(modsDir).filter(file => file.endsWith('.json'));
    modFiles.forEach(file => {
        const namespace = path.basename(file, '.json');
        if (!/^[a-z0-9_.-]+$/.test(namespace)) {
            console.error(`❌ Пропущен недопустимый namespace (должен быть в нижнем регистре [a-z0-9_.-]): ${namespace}`);
            return;
        }
        const srcFile = path.join(modsDir, file);
        const gameDir = path.join(modpackBase, namespace, 'lang');
        const gameJson = path.join(gameDir, 'ru_ru.json');
        
        try {
            const modData = JSON.parse(fs.readFileSync(srcFile, 'utf8'));
            if (!fs.existsSync(gameDir)) {
                fs.mkdirSync(gameDir, { recursive: true });
            }
            let gameData = {};
            if (fs.existsSync(gameJson)) {
                try { gameData = JSON.parse(fs.readFileSync(gameJson, 'utf8')); } catch(e) {}
            }
            const merged = { ...gameData, ...modData };
            fs.writeFileSync(gameJson, JSON.stringify(merged, null, 2), 'utf8');
            console.log(`✅ [${namespace}] Синхронизировано (${Object.keys(modData).length} ключей) -> ${gameJson}`);
        } catch(e) {
            console.error(`❌ Ошибка синхронизации мода ${file}: ${e.message}`);
        }
    });
}


// 8. Sync translate inspector command (/trans)
console.log('\n--- 8. Синхронизация команды инспектора (/trans) ---');
const inspectorSource = path.join(localBase, 'kubejs_scripts/server/translateInspector.js');
const inspectorTarget = path.join(modpackKubejs, 'server_scripts/translateInspector.js');
if (fs.existsSync(inspectorSource)) {
    fs.copyFileSync(inspectorSource, inspectorTarget);
    console.log(`✅ Установлен скрипт команды /trans -> ${inspectorTarget}`);
}

// 9. Sync Puffish Skills (society_skills)
console.log('\n--- 9. Синхронизация навыков Puffish Skills (society_skills) ---');
const skillsSource = path.join(localBase, 'translations/skills/ru_ru.json');
const skillsTargetDir = path.join(modpackBase, 'society_skills/lang');
const skillsTarget = path.join(skillsTargetDir, 'ru_ru.json');

if (fs.existsSync(skillsSource)) {
    if (!fs.existsSync(skillsTargetDir)) {
        fs.mkdirSync(skillsTargetDir, { recursive: true });
    }
    fs.copyFileSync(skillsSource, skillsTarget);
    const count = Object.keys(JSON.parse(fs.readFileSync(skillsSource, 'utf8'))).length;
    console.log(`✅ Скопировано (${count} ключей) -> ${skillsTarget}`);
}

// 10. Sync FTB Quests (ftbquestlocalizer)
console.log('\n--- 10. Синхронизация FTB Quests (ftbquestlocalizer) ---');
const ftbSourceDir = path.join(localBase, 'translations/ftbquests');
const ftbTargetDir = path.join(modpackBase, 'ftbquestlocalizer/lang');

if (fs.existsSync(ftbSourceDir)) {
    if (!fs.existsSync(ftbTargetDir)) {
        fs.mkdirSync(ftbTargetDir, { recursive: true });
    }
    ['ru_ru.json', 'en_us.json'].forEach(file => {
        const src = path.join(ftbSourceDir, file);
        const dst = path.join(ftbTargetDir, file);
        if (fs.existsSync(src)) {
            fs.copyFileSync(src, dst);
            const count = Object.keys(JSON.parse(fs.readFileSync(src, 'utf8'))).length;
            console.log(`✅ Скопировано (${count} ключей, ${file}) -> ${dst}`);
        }
    });
}

console.log('\n====================================================');
console.log('🎉 ВСЕ ПЕРЕВОДЫ И СКРИПТЫ СИНХРОНИЗИРОВАНЫ С ИГРОЙ!');
console.log('====================================================');

