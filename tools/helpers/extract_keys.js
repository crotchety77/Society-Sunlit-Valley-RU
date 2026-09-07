const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');
const files = fs.readdirSync(reviewDir).filter(f => f.endsWith('.md') && !f.startsWith('README')).sort();

const allKeysByFile = {};

files.forEach(file => {
    const content = fs.readFileSync(path.join(reviewDir, file), 'utf8');
    const lines = content.split('\n');
    allKeysByFile[file] = {};

    lines.forEach((line) => {
        line = line.trim();
        if (line.startsWith('|') && line.includes('`dialog.npc.')) {
            const parts = line.split('|').map(p => p.trim());
            if (parts.length >= 4) {
                const keyMatch = parts[1].match(/`([^`]+)`/);
                if (keyMatch) {
                    const key = keyMatch[1];
                    const enVal = parts[2];
                    allKeysByFile[file][key] = enVal;
                }
            }
        }
    });
    console.log(`${file}: ${Object.keys(allKeysByFile[file]).length} keys`);
});

fs.writeFileSync(path.join(__dirname, 'extracted_keys_by_file.json'), JSON.stringify(allKeysByFile, null, 2), 'utf8');
