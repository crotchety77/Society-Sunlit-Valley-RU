const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');
const files = fs.readdirSync(reviewDir).filter(f => f.endsWith('.md') && !f.startsWith('README')).sort();

// Let's gather all lines that still contain English letters
const remainingLines = [];

files.forEach(file => {
    const content = fs.readFileSync(path.join(reviewDir, file), 'utf8');
    const lines = content.split('\n');

    lines.forEach((line, idx) => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.')) {
            const parts = line.split('|').map(p => p.trim());
            if (parts.length >= 4) {
                const key = parts[1].replace(/`/g, '');
                const en = parts[2];
                const ru = parts[3];
                const cleaned = (ru || '').replace(/@i/g, '').replace(/§[0-9a-fk-or]/gi, '').trim();
                if (!ru || (/[a-zA-Z]/.test(cleaned) && !key.includes('gnome') && !cleaned.startsWith('Passe une bonne'))) {
                    remainingLines.push({ file, key, en, ru });
                }
            }
        }
    });
});

console.log(`Total remaining lines needing full translation: ${remainingLines.length}`);
fs.writeFileSync(path.join(__dirname, 'all_remaining_lines.json'), JSON.stringify(remainingLines, null, 2), 'utf8');
