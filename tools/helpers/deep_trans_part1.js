const fs = require('fs');
const path = require('path');

const untranslated = JSON.parse(fs.readFileSync(path.join(__dirname, 'untranslated_lines.json'), 'utf8'));

// Let's create a comprehensive translation file that contains all remaining strings
const deepTrans = {};

// 1. Goddess
deepTrans["dialog.npc.goddess.name"] = "Селена";
deepTrans["dialog.npc.goddess.chatter.description"] = "Разговор с Селеной";

// 2. Trader remaining
deepTrans["dialog.npc.trader.gift_loved.0.line_0"] = "Какая редкость! Это украсит мою коллекцию заморских чудес, спасибо, @i!";
deepTrans["dialog.npc.trader.gift_liked.0.line_0"] = "Благодарю за подарок! Такой товар всегда в цене.";
deepTrans["dialog.npc.trader.gift_neutral.0.line_0"] = "Спасибо, сойдёт для обмена в пути.";
deepTrans["dialog.npc.trader.gift_disliked.1.line_0"] = "Мне это и даром не нужно.";
deepTrans["dialog.npc.trader.gift_disliked.2.line_0"] = "Ну... спасибо за попытку.";
deepTrans["dialog.npc.trader.gift_disliked.3.line_0"] = "Эм, я не смогу это никому продать.";
deepTrans["dialog.npc.trader.gift_disliked.4.line_0"] = "Не лучший твой выбор, друг мой.";
deepTrans["dialog.npc.trader.gift_hated.1.line_0"] = "Убери этот мусор с моих глаз!";
deepTrans["dialog.npc.trader.gift_hated.2.line_0"] = "Ты пытаешься меня оскорбить этим хламом?";
deepTrans["dialog.npc.trader.gift_hated.3.line_0"] = "Отвратительно. Больше не подходи ко мне с таким.";
deepTrans["dialog.npc.trader.gift_hated.4.line_0"] = "Забери эту мерзость немедленно!";
deepTrans["dialog.npc.trader.chatter_friendship3.0.line_0"] = "Торговля идёт полным ходом, @i!";
deepTrans["dialog.npc.trader.chatter_friendship3.0.line_1"] = "В каждом новом городке я нахожу что-то уникальное.";

// 3. Market remaining
deepTrans["dialog.npc.market.gift_loved.1.line_0"] = "Потрясающий подарок! Я в полном восторге, @i!";
deepTrans["dialog.npc.market.gift_loved.2.line_0"] = "Ты лучший друг, о котором только можно мечтать!";
deepTrans["dialog.npc.market.gift_loved.3.line_0"] = "Ничего себе роскошь! Ради такого стоило переехать в эту долину!";
deepTrans["dialog.npc.market.gift_liked.0.line_0"] = "О, отличная вещь! Спасибо большое, @i.";
deepTrans["dialog.npc.market.gift_liked.1.line_0"] = "Мне очень нравится! Обязательно найду этому применение.";
deepTrans["dialog.npc.market.gift_neutral.0.line_0"] = "О, спасибо.";
deepTrans["dialog.npc.market.gift_neutral.1.line_0"] = "Пригодится на прилавке, благодарю.";
deepTrans["dialog.npc.market.gift_neutral.2.line_0"] = "Спасибо за презент.";
deepTrans["dialog.npc.market.gift_disliked.0.line_0"] = "Э-э... спасибо, наверное?";
deepTrans["dialog.npc.market.gift_disliked.1.line_0"] = "Я не фанат таких вещей, если честно.";
deepTrans["dialog.npc.market.gift_disliked.2.line_0"] = "Ну... ладно.";
deepTrans["dialog.npc.market.gift_hated.0.line_0"] = "Фу, какая гадость. Забери это немедленно.";
deepTrans["dialog.npc.market.gift_hated.1.line_0"] = "Ты надо мной издеваешься? Убери этот мусор с прилавка.";
deepTrans["dialog.npc.market.gift_hated.2.line_0"] = "Отвратительно. Больше так не шути.";

// Write out to deep_trans.json
fs.writeFileSync(path.join(__dirname, 'deep_trans.json'), JSON.stringify(deepTrans, null, 2), 'utf8');
console.log('Saved deep_trans.json');
