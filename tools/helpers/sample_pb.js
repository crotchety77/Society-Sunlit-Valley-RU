const fs = require('fs');
const path = require('path');

const modpackPath = 'D:/ModrinthApp/profiles/Society_ Sunlit Valley/kubejs/assets';
const pbEnUsPath = path.join(modpackPath, 'portable_blueprints/lang/en_us.json');
const pbEnUs = JSON.parse(fs.readFileSync(pbEnUsPath, 'utf8'));

console.log('Sample keys from portable_blueprints en_us.json:');
Object.entries(pbEnUs).slice(0, 40).forEach(([k, v]) => console.log(`${k} -> ${v}`));
