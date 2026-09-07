const fs = require('fs');
const path = require('path');

const modpackPath = 'D:/ModrinthApp/profiles/Society_ Sunlit Valley/kubejs/assets';
const pbEnUs = JSON.parse(fs.readFileSync(path.join(modpackPath, 'portable_blueprints/lang/en_us.json'), 'utf8'));

// Style translations:
// For masculine nouns (дом, сарай, хлев, курятник) vs feminine nouns (теплица)
const styles = {
    basic: { m: 'Базовый', f: 'Базовая', n: 'Базовое' },
    alpine: { m: 'Альпийский', f: 'Альпийская', n: 'Альпийское' },
    arid: { m: 'Пустынный', f: 'Пустынная', n: 'Пустынное' },
    bamboo: { m: 'Бамбуковый', f: 'Бамбуковая', n: 'Бамбуковое' },
    bavarian: { m: 'Баварский', f: 'Баварская', n: 'Баварское' },
    cherry: { m: 'Вишнёвый', f: 'Вишнёвая', n: 'Вишнёвое' },
    entrana: { m: 'Энтрана', f: 'Энтрана', isQuote: true },
    floral: { m: 'Цветочный', f: 'Цветочная', n: 'Цветочное' },
    mason: { m: 'Каменный', f: 'Каменная', n: 'Каменное' },
    prismarine: { m: 'Призмариновый', f: 'Призмариновая', n: 'Призмариновое' },
    rural: { m: 'Деревенский', f: 'Деревенская', n: 'Деревенское' },
    sakura: { m: 'Сакура', f: 'Сакура', isQuote: true },
    siberian: { m: 'Сибирский', f: 'Сибирская', n: 'Сибирское' },
    tudor: { m: 'Тюдоровский', f: 'Тюдоровская', n: 'Тюдоровское' },
    vibrantown: { m: 'Яркоград', f: 'Яркоград', isQuote: true },
    pineconetown: { m: 'Сосновый городок', f: 'Сосновый городок', isQuote: true }
};

// Building type translations:
const buildingTypes = {
    home: { name: 'фермерский дом', gender: 'm' },
    shed: { name: 'сарай', gender: 'm' },
    large_shed: { name: 'большой сарай', gender: 'm' },
    coop: { name: 'курятник', gender: 'm' },
    barn: { name: 'хлев', gender: 'm' },
    deluxe_barn: { name: 'большой хлев', gender: 'm' },
    greenhouse: { name: 'теплица', gender: 'f' },
    carpenter: { name: 'дом плотника', gender: 'm' },
    blacksmith: { name: 'дом кузнеца', gender: 'm' },
    shepherd: { name: 'дом пастуха', gender: 'm' },
    market: { name: 'дом торговца', gender: 'm' },
    fisher: { name: 'дом рыбака', gender: 'm' },
    banker: { name: 'дом банкира', gender: 'm' },
    librarian: { name: 'дом библиотекаря', gender: 'm' },
    witch: { name: 'дом ведьмы', gender: 'm' },
    trader: { name: 'дом странствующего торговца', gender: 'm' }
};

function formatBuildingTitle(setStyle, typeKey) {
    const styleInfo = styles[setStyle];
    const bInfo = buildingTypes[typeKey];
    if (!styleInfo || !bInfo) {
        return null;
    }

    if (styleInfo.isQuote) {
        // e.g. "Хлев «Сакура»" or "Теплица «Тюдор»"
        const capBuilding = bInfo.name.charAt(0).toUpperCase() + bInfo.name.slice(1);
        return `${capBuilding} «${styleInfo.m}»`;
    } else {
        const adj = bInfo.gender === 'f' ? styleInfo.f : styleInfo.m;
        return `${adj} ${bInfo.name}`;
    }
}

const pbRu = {};

for (const [key, val] of Object.entries(pbEnUs)) {
    if (key === 'portable_blueprints.worn_blueprint.blockapedia') {
        pbRu[key] = 'Чертёж: Блокопедия';
        continue;
    }
    if (key === 'portable_blueprints.worn_blueprint.blockapedia.author') {
        pbRu[key] = val.replace('Designed by: ', 'Автор проекта: ');
        continue;
    }
    if (key === 'portable_blueprints.worn_blueprint.blockapedia.dimensions') {
        pbRu[key] = val.replace('Dimensions: ', 'Размеры: ');
        continue;
    }

    if (key.endsWith('.author')) {
        pbRu[key] = val.replace('Designed by: ', 'Автор проекта: ');
    } else if (key.endsWith('.dimensions')) {
        pbRu[key] = val.replace('Dimensions: ', 'Размеры: ');
    } else {
        // e.g. portable_blueprints.worn_blueprint.sakura_large_shed
        const suffix = key.replace('portable_blueprints.worn_blueprint.', '');
        // find matching set and type
        let matched = false;
        for (const setKey of Object.keys(styles)) {
            if (suffix.startsWith(setKey + '_')) {
                const typeKey = suffix.slice(setKey.length + 1);
                const title = formatBuildingTitle(setKey, typeKey);
                if (title) {
                    pbRu[key] = title;
                    matched = true;
                    break;
                }
            }
        }
        if (!matched) {
            console.warn('Unmatched key:', key, val);
            pbRu[key] = val;
        }
    }
}

// Society Trading translations
const stRu = {
    "selector.society_trading.building_shop": "Фермерские постройки",
    "selector.society_trading.town_building_shop": "Деревенские постройки",
    "shop.society_trading.building_shop.banker": "Дом банкира",
    "shop.society_trading.building_shop.barn": "Хлев",
    "shop.society_trading.building_shop.blacksmith": "Дом кузнеца",
    "shop.society_trading.building_shop.carpenter": "Дом плотника",
    "shop.society_trading.building_shop.coop": "Курятник",
    "shop.society_trading.building_shop.deluxe_barn": "Большой хлев",
    "shop.society_trading.building_shop.fisher": "Дом рыбака",
    "shop.society_trading.building_shop.greenhouse": "Теплица",
    "shop.society_trading.building_shop.home": "Фермерский дом",
    "shop.society_trading.building_shop.large_shed": "Большой сарай",
    "shop.society_trading.building_shop.librarian": "Дом библиотекаря",
    "shop.society_trading.building_shop.market": "Дом торговца",
    "shop.society_trading.building_shop.shed": "Сарай",
    "shop.society_trading.building_shop.shepherd": "Дом пастуха",
    "shop.society_trading.building_shop.trader": "Дом странствующего торговца",
    "shop.society_trading.building_shop.witch": "Дом ведьмы"
};

// Create output folders
const localDir = path.join(__dirname, '../building_translations');
if (!fs.existsSync(localDir)) fs.mkdirSync(localDir, { recursive: true });

fs.writeFileSync(path.join(localDir, 'portable_blueprints_ru_ru.json'), JSON.stringify(pbRu, null, 2), 'utf8');
fs.writeFileSync(path.join(localDir, 'society_trading_building_shop_ru_ru.json'), JSON.stringify(stRu, null, 2), 'utf8');

// Copy directly to modpack
const modpackPbDir = path.join(modpackPath, 'portable_blueprints/lang');
const modpackStDir = path.join(modpackPath, 'society_trading/lang');

fs.writeFileSync(path.join(modpackPbDir, 'ru_ru.json'), JSON.stringify(pbRu, null, 2), 'utf8');

// For society_trading, also merge with existing clean translations if any
let existingStRu = {};
try {
    const existingStRuPath = path.join(modpackStDir, 'ru_ru.json');
    if (fs.existsSync(existingStRuPath)) {
        existingStRu = JSON.parse(fs.readFileSync(existingStRuPath, 'utf8'));
    }
} catch (e) {}

const mergedStRu = { ...existingStRu, ...stRu };
fs.writeFileSync(path.join(modpackStDir, 'ru_ru.json'), JSON.stringify(mergedStRu, null, 2), 'utf8');

console.log('Successfully generated and saved all translations!');
console.log('Total portable_blueprints keys:', Object.keys(pbRu).length);
console.log('Total society_trading keys:', Object.keys(mergedStRu).length);
