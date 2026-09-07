const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');
const files = fs.readdirSync(reviewDir).filter(f => f.endsWith('.md') && !f.startsWith('README')).sort();

const untranslatedByFile = {};

files.forEach(file => {
    const content = fs.readFileSync(path.join(reviewDir, file), 'utf8');
    const lines = content.split('\n');
    untranslatedByFile[file] = {};

    lines.forEach(line => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.')) {
            const parts = line.split('|').map(p => p.trim());
            if (parts.length >= 4) {
                const keyMatch = parts[1].match(/`([^`]+)`/);
                if (keyMatch) {
                    const key = keyMatch[1];
                    const en = parts[2];
                    const ru = parts[3];
                    const cleaned = (ru || '').replace(/@i/g, '').replace(/§[0-9a-fk-or]/gi, '').trim();
                    if (!ru || (/[a-zA-Z]/.test(cleaned) && !key.includes('gnome') && !cleaned.startsWith('Passe une bonne'))) {
                        untranslatedByFile[file][key] = en;
                    }
                }
            }
        }
    });
    console.log(`${file}: ${Object.keys(untranslatedByFile[file]).length} untranslated`);
});

fs.writeFileSync(path.join(__dirname, 'untranslated_lines.json'), JSON.stringify(untranslatedByFile, null, 2), 'utf8');
