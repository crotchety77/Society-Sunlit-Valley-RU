const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');
const extractedData = JSON.parse(fs.readFileSync(path.join(__dirname, 'extracted_keys_by_file.json'), 'utf8'));

// Helper to update markdown table
function updateMd(fileName, dict) {
    const filePath = path.join(reviewDir, fileName);
    let content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');

    let updatedLines = lines.map((line) => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.'')) {
            const parts = line.split('|');
            if (parts.length >= 5) {
                const keyMatch = parts[1].match(/`([^`]+)`/);
                if (keyMatch) {
                    const key = keyMatch[1];
                    if (dict[key] !== undefined && dict[key].length > 0) {
                        parts[3] = ` ${dict[key]} `;
                        return parts.join('|');
                    }
                }
            }
        }
        return line;
    });

    fs.writeFileSync(filePath, updatedLines.join('\n'), 'utf8');
    console.log(`Updated: ${fileName}`);
}

module.exports = { updateMd, extractedData };
