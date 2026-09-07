const fs = require('fs');
const path = require('path');

const modpackPath = 'D:/ModrinthApp/profiles/Society_ Sunlit Valley/kubejs/assets';

// Load original building shop strings
const pbJsonPath = path.join(modpackPath, 'portable_blueprints/lang/building_shop_generated.json');
const stJsonPath = path.join(modpackPath, 'society_trading/lang/building_shop_generated.json');

const pbEn = JSON.parse(fs.readFileSync(pbJsonPath, 'utf8'));
const stEn = JSON.parse(fs.readFileSync(stJsonPath, 'utf8'));

console.log('Portable Blueprints generated keys:', Object.keys(pbEn).length);
console.log('Society Trading generated keys:', Object.keys(stEn).length);

// Also check en_us.json in portable_blueprints
const pbEnUsPath = path.join(modpackPath, 'portable_blueprints/lang/en_us.json');
const pbEnUs = JSON.parse(fs.readFileSync(pbEnUsPath, 'utf8'));
console.log('Portable Blueprints en_us keys:', Object.keys(pbEnUs).length);
