const fs = require('fs');
const path = require('path');

const reviewDir = __dirname;
const ruData = {};
const qaErrors = [];

const files = fs.readdirSync(reviewDir).filter(f => f.endsWith('.md') && !f.startsWith('README')).sort();

let totalParsed = 0;
let translatedCount = 0;

files.forEach(file => {
  const content = fs.readFileSync(path.join(reviewDir, file), 'utf8');
  const lines = content.split('\n');
  
  lines.forEach((line, lineIndex) => {
    line = line.trim();
    if (line.startsWith('|') && line.includes('`dialog.npc.')) {
      const parts = line.split('|').map(p => p.trim());
      // parts[0] is empty
      // parts[1] is `key`
      // parts[2] is EN (Оригинал)
      // parts[3] is RU (Перевод)
      if (parts.length >= 4) {
        const keyMatch = parts[1].match(/`([^`]+)`/);
        if (keyMatch) {
          const key = keyMatch[1];
          const ruVal = parts[3];
          totalParsed++;
          
          if (ruVal && ruVal.length > 0) {
            // QA Check: unescaped single %
            const percentMatches = ruVal.match(/(?<!%)%(?!%)/g);
            if (percentMatches) {
              qaErrors.push(`[ОШИБКА %] В файле ${file} (строка ${lineIndex + 1}): одиночный знак % в ключе "${key}". Замените на %%!`);
            }
            ruData[key] = ruVal;
            translatedCount++;
          }
        }
      }
    }
  });
});

console.log('====================================================');
console.log('         СБОРКА ПЕРЕВОДА ДИАЛОГОВ (SOCIETY)');
console.log('====================================================');
console.log(`Всего строк диалогов найдено: ${totalParsed}`);
console.log(`Переведено строк:             ${translatedCount} / ${totalParsed}`);
console.log('----------------------------------------------------');

if (qaErrors.length > 0) {
  console.log('\n[ВНИМАНИЕ] Обнаружены критические ошибки форматирования:');
  qaErrors.forEach(err => console.log(' ❌ ' + err));
  console.log('----------------------------------------------------');
}

// 1. Создаем локальный ru_ru.json в этой же папке
const outRuPath = path.join(reviewDir, 'ru_ru.json');
fs.writeFileSync(outRuPath, JSON.stringify(ruData, null, 2), 'utf8');
console.log(`✅ Итоговый файл успешно сохранён:\n   ${outRuPath}`);

// 2. Если на компьютере установлен модпак, сразу копируем в игру
const modpackPath = 'D:\\ModrinthApp\\profiles\\Society_ Sunlit Valley\\kubejs\\assets\\dialog\\lang\\ru_ru.json';
try {
  const modpackDir = path.dirname(modpackPath);
  if (fs.existsSync(modpackDir)) {
    fs.writeFileSync(modpackPath, JSON.stringify(ruData, null, 2), 'utf8');
    console.log(`\n🚀 [СИНХРОНИЗАЦИЯ] Файл скопирован в модпак:\n   ${modpackPath}`);
    console.log('   (В игре нажмите F3 + T для применения перевода)');
  }
} catch (e) {
  // Игнорируем, если модпака нет на этом ПК
}
console.log('====================================================\n');
