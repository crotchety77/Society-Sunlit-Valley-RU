const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');
const files = fs.readdirSync(reviewDir).filter(f => f.endsWith('.md') && !f.startsWith('README')).sort();

let missing = [];

files.forEach(file => {
    const content = fs.readFileSync(path.join(reviewDir, file), 'utf8');
    const lines = content.split('\n');

    lines.forEach((line, idx) => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.')) {
            const parts = line.split('|').map(p => p.trim());
            if (parts.length >= 4) {
                const key = parts[1];
                const en = parts[2];
                const ru = parts[3];
                if (!ru || ru.length === 0) {
                    missing.push({ file, lineNum: idx + 1, key, en });
                }
            }
        }
    });
});

console.log(`Total missing: ${missing.length}`);
missing.forEach(m => console.log(`${m.file}:${m.lineNum} -> ${m.key}: ${m.en}`));
