const fs = require('fs');
const path = require('path');

const modpackPath = 'D:/ModrinthApp/profiles/Society_ Sunlit Valley/kubejs/assets';
const pbEnUsPath = path.join(modpackPath, 'portable_blueprints/lang/en_us.json');
const pbEnUs = JSON.parse(fs.readFileSync(pbEnUsPath, 'utf8'));

const nonWorn = Object.entries(pbEnUs).filter(([k]) => !k.startsWith('portable_blueprints.worn_blueprint.'));
console.log('Non worn keys:', nonWorn);
