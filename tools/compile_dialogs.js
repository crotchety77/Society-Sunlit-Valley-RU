const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../translations/dialogs');
const enJsonPath = path.join(__dirname, '../game_data/raw_lang/dialog_en_us.json');

if (!fs.existsSync(enJsonPath)) {
  console.error('Error: dialog_en_us.json not found!');
  process.exit(1);
}

const enData = JSON.parse(fs.readFileSync(enJsonPath, 'utf8'));
const ruData = {};

const files = fs.readdirSync(reviewDir).filter(f => f.endsWith('.md') && !f.startsWith('README')).sort();

let totalParsed = 0;
let translatedCount = 0;

files.forEach(file => {
  const content = fs.readFileSync(path.join(reviewDir, file), 'utf8');
  const lines = content.split('\n');
  
  lines.forEach(line => {
    line = line.trim();
    if (line.startsWith('|') && line.includes('`dialog.npc.')) {
      const parts = line.split('|').map(p => p.trim());
      // parts[0] is empty, parts[1] is `key`, parts[2] is EN, parts[3] is RU
      if (parts.length >= 4) {
        const keyMatch = parts[1].match(/`([^`]+)`/);
        if (keyMatch) {
          const key = keyMatch[1];
          const ruVal = parts[3];
          totalParsed++;
          if (ruVal && ruVal.length > 0) {
            ruData[key] = ruVal;
            translatedCount++;
          }
        }
      }
    }
  });
});

console.log(`Parsed ${totalParsed} keys from Markdown files.`);
console.log(`Translated keys: ${translatedCount} / ${Object.keys(enData).length}`);

// Output compiled ru_ru.json
const outRuPath = path.join(__dirname, 'dialog_ru_ru.json');
fs.writeFileSync(outRuPath, JSON.stringify(ruData, null, 2), 'utf8');
console.log(`Wrote compiled dialog translations to: ${outRuPath}`);

// Target modpack directory sync check
const modpackPath = 'D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\assets\\dialog\\lang\\ru_ru.json';
try {
  const modpackDir = path.dirname(modpackPath);
  if (fs.existsSync(modpackDir)) {
    fs.writeFileSync(modpackPath, JSON.stringify(ruData, null, 2), 'utf8');
    console.log(`[SYNC SUCCESS] Copied to modpack: ${modpackPath}`);
  } else {
    console.log(`Modpack directory not accessible right now, skipping direct copy.`);
  }
} catch (e) {
  console.log(`Modpack direct sync notice: ${e.message}`);
}
