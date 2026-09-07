const fs = require('fs');
const path = require('path');

const ruJson = JSON.parse(fs.readFileSync(path.join(__dirname, '../dialogs_review/ru_ru.json'), 'utf8'));

// Check for frequency of exact identical values per character
const valuesByChar = {};

for (const [k, v] of Object.entries(ruJson)) {
    const char = k.split('.')[2];
    if (!valuesByChar[char]) valuesByChar[char] = {};
    if (!valuesByChar[char][v]) valuesByChar[char][v] = [];
    valuesByChar[char][v].push(k);
}

for (const [char, valMap] of Object.entries(valuesByChar)) {
    for (const [val, keys] of Object.entries(valMap)) {
        if (keys.length > 3) {
            console.log(`[${char}] repeated ${keys.length} times: "${val}"`);
            console.log(`   Keys:`, keys.slice(0, 5));
        }
    }
}
