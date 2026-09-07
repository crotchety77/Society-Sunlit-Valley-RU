const fs = require('fs');
const path = require('path');

const ruJson = JSON.parse(fs.readFileSync(path.join(__dirname, '../dialogs_review/ru_ru.json'), 'utf8'));

const englishEntries = [];

for (const [k, v] of Object.entries(ruJson)) {
    // Check if contains latin letters (excluding token @i and color codes or SGA runes)
    const cleaned = v.replace(/@i/g, '').replace(/§[0-9a-fk-or]/gi, '').trim();
    if (/[a-zA-Z]/.test(cleaned) && !k.includes('gnome')) {
        englishEntries.push({ key: k, value: v });
    }
}

console.log('Total English entries remaining:', englishEntries.length);
englishEntries.slice(0, 30).forEach(e => console.log(`${e.key} -> ${e.value}`));
