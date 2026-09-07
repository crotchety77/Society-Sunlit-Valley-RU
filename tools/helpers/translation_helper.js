const fs = require('fs');
const path = require('path');

// Helper to update a markdown file table
function updateMarkdownFile(fileName, translations) {
    const filePath = path.join(__dirname, '../dialogs_review', fileName);
    let content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');

    let updatedLines = lines.map((line) => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.')) {
            const parts = line.split('|');
            if (parts.length >= 5) {
                // parts[0] = ""
                // parts[1] = " `key` "
                // parts[2] = " Original (EN) "
                // parts[3] = " Перевод (RU) "
                // parts[4] = " Заметки "
                const keyMatch = parts[1].match(/`([^`]+)`/);
                if (keyMatch) {
                    const key = keyMatch[1];
                    if (translations[key] !== undefined) {
                        parts[3] = ` ${translations[key]} `;
                        return parts.join('|');
                    }
                }
            }
        }
        return line;
    });

    fs.writeFileSync(filePath, updatedLines.join('\n'), 'utf8');
    console.log(`Updated ${fileName}`);
}

module.exports = { updateMarkdownFile };
