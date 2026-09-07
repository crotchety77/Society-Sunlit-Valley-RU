const fs = require('fs');
const path = require('path');

const reviewDir = path.join(__dirname, '../dialogs_review');

function updateMd(fileName, dict) {
    const filePath = path.join(reviewDir, fileName);
    let content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');

    let updatedLines = lines.map((line) => {
        let trimmed = line.trim();
        if (trimmed.startsWith('|') && trimmed.includes('`dialog.npc.')) {
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

// -------------------------------------------------------------
// MARKET / LEON (03_market.md)
// -------------------------------------------------------------
const marketPerfect = {
    "dialog.npc.market.gift_hated.3.line_0": "Ни один зверь не способен быть столь жесток, как человек — так артистично, так живописно жесток.",
    "dialog.npc.market.gift_hated.4.line_0": "Надеюсь, в фермерстве ты не настолько же бездарен.",
    "dialog.npc.market.gift_hated.5.line_0": "Когда ночью смотришься в зеркало, подумай обо всём, что растрачено на тебя впустую.",
    "dialog.npc.market.gift_hated.6.line_0": "Ты абсолютно бестолков, и мне неприятно твоё общество.",
    "dialog.npc.market.gift_hated.7.line_0": "За кого ты меня вообще принимаешь?",
    "dialog.npc.market.gift_hated.8.line_0": "Чтобы поступать разумно, одного ума недостаточно.",
    "dialog.npc.market.gift_hated.9.line_0": "Я заслуживаю гораздо лучшего отношения к себе.",
    "dialog.npc.market.gift_hated.10.line_0": "Это отвратительно.",
    "dialog.npc.market.gift_hated.11.line_0": "Абсолютная, вопиющая безвкусица.",
    "dialog.npc.market.gift_hated.12.line_0": "Ты ведёшь себя как незрелый ребёнок. Отойди от меня.",

    "dialog.npc.market.unique_five_gift.line_0": "А-а-а, как раз тот, кого я мечтал видеть сегодня! У меня к тебе небольшая просьба.",
    "dialog.npc.market.unique_five_gift.line_1": "Кэролайн заставляет меня читать эту ужасно сухую книгу по агрономии, а мне до смерти лень...",
    "dialog.npc.market.unique_five_gift.line_2": "Но ведь ты фермер! Причём первоклассный, и я знаю это лучше любого в этой долине.",
    "dialog.npc.market.unique_five_gift.line_3": "Та-а-ак что... Не мог бы ты прочесть её за меня и кратко пересказать суть?",
    "dialog.npc.market.unique_five_gift.line_4": "Взамен я уговорю Кэролайн разрешить мне круглый год держать на прилавке семена всех сезонов!",
    "dialog.npc.market.unique_five_gift.line_5": "Мы оба в выигрыше, хотя я знаю, что ты согласился бы в любом случае — ты ведь просто без ума от меня.",
    "dialog.npc.market.unique_five_gift.line_6": "...Ты, знаешь ли, совершенно не умеешь скрывать свои чувства...",

    "dialog.npc.market.unique_five_gift_read.line_0": "Эй, @i, ты выглядишь как человек, прочитавший «Универсальные методы фермерства», я прав?",
    "dialog.npc.market.unique_five_gift_read.line_1": "Прости, я не хотел называть тебя занудой. То есть ты определённо фермерский зануда, тут без сомнений.",
    "dialog.npc.market.unique_five_gift_read.line_2": "Но ближе к делу: можешь быстро пересказать мне самое главное?",
    "dialog.npc.market.unique_five_gift_read.line_3": "Кэролайн заставляет меня читать эту скучнейшую книгу, а я просто не вынесу...",
    "dialog.npc.market.unique_five_gift_read.line_4": "Я заранее отсыплю тебе редких семян искропода — мы оба останемся в плюсе!",
    "dialog.npc.market.unique_five_gift_read.line_5": "Хотя... я знаю, что ты согласился бы в любом случае, ведь ты просто без ума от меня.",
    "dialog.npc.market.unique_five_gift_read.line_6": "...Ты совершенно не умеешь скрывать свои чувства..."
};

updateMd('03_market.md', marketPerfect);

// -------------------------------------------------------------
// TRADER / CARLOS (09_trader.md)
// -------------------------------------------------------------
const traderPerfect = {
    "dialog.npc.trader.unique_five_gift.line_0": "О-о-о, мой дорогой @i! Взгляни, что у меня есть!",
    "dialog.npc.trader.unique_five_gift.line_1": "В знак нашей крепкой дружбы я открываю для тебя секретную линейку заморских нарядов и экипировки!",
    "dialog.npc.trader.unique_five_gift.line_2": "Таких стильных одеяний ты не сыщешь даже в столичных бутиках!",
    "dialog.npc.trader.unique_five_gift.line_3": "Носи с гордостью, мой лучший торговый партнёр!",
    "dialog.npc.trader.unique_five_gift.line_4": "И помни: для тебя у меня всегда самые эксклюзивные предложения!"
};

updateMd('09_trader.md', traderPerfect);
