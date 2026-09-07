const fs = require('fs');
const path = require('path');

const modpackBase = 'D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\assets';
const localBase = path.join(__dirname, '../..');

// Helper function to update and sync namespace lang JSON
function updateNamespaceLang(namespace, updates, localJsonPath = null) {
    if (localJsonPath) {
        let localData = {};
        if (fs.existsSync(localJsonPath)) {
            try { localData = JSON.parse(fs.readFileSync(localJsonPath, 'utf8')); } catch(e) {}
        }
        Object.assign(localData, updates);
        fs.writeFileSync(localJsonPath, JSON.stringify(localData, null, 2), 'utf8');
        console.log(`✅ Обновлен локальный ${path.relative(localBase, localJsonPath)}`);
    }

    const gameDir = path.join(modpackBase, namespace, 'lang');
    if (!fs.existsSync(gameDir)) fs.mkdirSync(gameDir, { recursive: true });
    const gameJson = path.join(gameDir, 'ru_ru.json');
    let gameData = {};
    if (fs.existsSync(gameJson)) {
        try { gameData = JSON.parse(fs.readFileSync(gameJson, 'utf8')); } catch(e) {}
    }
    Object.assign(gameData, updates);
    fs.writeFileSync(gameJson, JSON.stringify(gameData, null, 2), 'utf8');
    console.log(`✅ Синхронизирован ${namespace}/lang/ru_ru.json`);
}

// 1. society
updateNamespaceLang('society', {
    'item.society.face_note': 'Отношения с жителями',
    'tooltip.society.face_note': 'Показывает отношение всех жителей к вам.',
    'item.society.building_supplies': 'Строительные материалы',
    'item.society.greenhouse_building_supplies': 'Тепличные стройматериалы',
    'tooltip.society.chiseled_organic_glass': 'Выращивает первый урожай под собой в любой сезон. Радиус 16 блоков.'
}, path.join(localBase, 'translations/society/ru_ru.json'));

// 2. moreminecarts
updateNamespaceLang('moreminecarts', {
    "block.moreminecarts.chiseled_organic_glass": "Тепличное стекло",
    "block.moreminecarts.chiseled_organic_glass_pane": "Тепличная стеклянная панель",
    "item.moreminecarts.chiseled_organic_glass": "Тепличное стекло",
    "item.moreminecarts.chiseled_organic_glass_pane": "Тепличная стеклянная панель",
    "block.moreminecarts.organic_glass": "Органическое стекло",
    "block.moreminecarts.organic_glass_pane": "Органическая стеклянная панель",
    "item.moreminecarts.organic_glass": "Органическое стекло",
    "item.moreminecarts.organic_glass_pane": "Органическая стеклянная панель",
    "block.moreminecarts.glass_cactus": "Кристаллический кактус",
    "item.moreminecarts.glass_cactus": "Кристаллический кактус",
    "item.moreminecarts.glass_spines": "Стеклянные шипы",
    "block.moreminecarts.chunk_loader": "Топливный прогрузчик чанков"
});

// 3. shippingbin
updateNamespaceLang('shippingbin', {
    "block.shippingbin.basic_shipping_bin": "Базовый ящик для поставок",
    "block.shippingbin.smart_shipping_bin": "Умный ящик для поставок",
    "item.shippingbin.basic_shipping_bin": "Базовый ящик для поставок",
    "item.shippingbin.smart_shipping_bin": "Умный ящик для поставок"
});

// 4. oreganized
updateNamespaceLang('oreganized', {
    "item.oreganized.electrum_upgrade_smithing_template": "Кузнечный шаблон §6электруемового§r улучшения",
    "upgrade.oreganized.electrum_upgrade": "§6Электруемовое улучшение§r",
    "item.oreganized.smithing_template.electrum_upgrade.additions_slot_description": "Добавьте электруемовый слиток",
    "item.oreganized.smithing_template.electrum_upgrade.applies_to": "Алмазное снаряжение",
    "item.oreganized.smithing_template.electrum_upgrade.ingredients": "Электруемовый слиток"
});

// 5. minecraft (netherite -> iridium smithing template)
updateNamespaceLang('minecraft', {
    "item.minecraft.netherite_upgrade_smithing_template": "Кузнечный шаблон §5иридиевого§r улучшения",
    "upgrade.minecraft.netherite_upgrade": "§5Иридиевое улучшение§r",
    "item.minecraft.smithing_template.netherite_upgrade.additions_slot_description": "Добавьте незеритовый слиток",
    "item.minecraft.smithing_template.netherite_upgrade.ingredients": "Незеритовый слиток",
    "item.minecraft.smithing_template.netherite_upgrade.applies_to": "Алмазное снаряжение"
});

// 6. refurbished_furniture
updateNamespaceLang('refurbished_furniture', {
    "block.refurbished_furniture.workbench": "Верстак мебели",
    "item.refurbished_furniture.workbench": "Верстак мебели",
    "container.refurbished_furniture.workbench": "Верстак мебели"
});

// 7. justhammers
updateNamespaceLang('justhammers', {
    "item.justhammers.impact_core": "Большое ядро"
});

// 8. extractinator
updateNamespaceLang('extractinator', {
    "block.extractinator.extractinator": "Раскалыватель жеод",
    "item.extractinator.extractinator": "Раскалыватель жеод",
    "itemGroup.extractinator.main": "Раскалыватель жеод",
    "emi.category.extractinator.extractinator": "Раскалывание жеод"
});

// 9. Update kubejs_scripts/client/invitationTooltips.js with greenhouse glass tooltip if not present
const tooltipScriptPath = path.join(localBase, 'kubejs_scripts/client/invitationTooltips.js');
if (fs.existsSync(tooltipScriptPath)) {
    let tooltipScript = fs.readFileSync(tooltipScriptPath, 'utf8');
    if (!tooltipScript.includes('chiseled_organic_glass')) {
        const extraTooltipCode = `
  // Подсказка для тепличного стекла
  tooltip.add([
    "moreminecarts:chiseled_organic_glass",
    "moreminecarts:chiseled_organic_glass_pane"
  ], Text.of("Выращивает первый урожай под собой в любой сезон. Радиус 16 блоков.").green());
`;
        const lastIndex = tooltipScript.lastIndexOf('});');
        if (lastIndex !== -1) {
            tooltipScript = tooltipScript.substring(0, lastIndex) + extraTooltipCode + tooltipScript.substring(lastIndex);
            fs.writeFileSync(tooltipScriptPath, tooltipScript, 'utf8');
            console.log('✅ Добавлен тултип для тепличного стекла в invitationTooltips.js');
        }
    }
}
