const fs = require('fs');
const path = require('path');
const { updateMarkdownFile } = require('./translation_helper');

const finalBankerLines = {
  "dialog.npc.banker.chatter_friendship1.17.line_1": "Соблюдай деловой тон, если ты вообще на такое способен.",
  "dialog.npc.banker.chatter_friendship1.19.line_1": "И это отнюдь не комплимент.",
  "dialog.npc.banker.chatter_friendship2.0.line_1": "И тем не менее, ты только и делаешь, что болтаешь.",
  "dialog.npc.banker.chatter_friendship2.1.line_1": "Я не хочу, чтобы благополучие города зависело от одного уязвимого звена.",
  "dialog.npc.banker.chatter_friendship2.4.line_1": "Так они хотя бы услышат мои слова больше одного раза.",
  "dialog.npc.banker.chatter_friendship2.5.line_1": "Мне пришлось дважды за этот сезон заказывать дополнительный товар.",
  "dialog.npc.banker.chatter_friendship2.6.line_1": "Пожалуйста, хватит лениться — старайся лучше.",
  "dialog.npc.banker.chatter_friendship2.9.line_1": "Разочаровали меня.",
  "dialog.npc.banker.chatter_friendship2.10.line_1": "Не пополняй этот список собой.",
  "dialog.npc.banker.chatter_friendship2.11.line_1": "Должно быть, я всё делаю правильно.",
  "dialog.npc.banker.chatter_friendship2.12.line_1": "Ты похож на человека, который совершенно слеп к подобным вещам.",
  "dialog.npc.banker.chatter_friendship2.12.line_2": "Всё здесь происходит лишь потому, что я это позволяю. Помни об этом.",
  "dialog.npc.banker.chatter_friendship3.3.line_1": "Это крайне неприятно.",
  "dialog.npc.banker.chatter_friendship3.4.line_1": "Я бы не рекомендовала тебе проверять мои границы на прочность.",
  "dialog.npc.banker.chatter_friendship3.5.line_1": "Ужасный человек во всех отношениях, я не одолжила бы ему ни гроша.",
  "dialog.npc.banker.chatter_friendship4.0.line_1": "Как только моя работа здесь будет окончена, я найму управляющего и перейду к более масштабным делам.",
  "dialog.npc.banker.chatter_friendship4.1.line_1": "Хотя бы позаботься о том, чтобы подарки были приличными.",
  "dialog.npc.banker.chatter_friendship4.3.line_1": "Твои показатели в последнее время заметно подросли.",
  "dialog.npc.banker.chatter_friendship4.4.line_1": "Ты, должно быть, уже просто принюхался и не замечаешь запаха.",
  "dialog.npc.banker.chatter_friendship4.5.line_1": "Это должно хоть немного сократить долю ручного труда.",
  "dialog.npc.banker.chatter_friendship4.5.line_2": "Тебе пригодится любая возможная помощь.",
  "dialog.npc.banker.chatter_friendship4.6.line_1": "Пожалуйста, направь эту энергию в более прибыльное русло.",
  "dialog.npc.banker.chatter_friendship4.7.line_1": "Что? К этому времени ты уже должен был усвоить, что меня нельзя так бесцеремонно перебивать.",
  "dialog.npc.banker.chatter_friendship4.9.line_0": "У меня сегодня просто нет времени на пустую болтовню.",
  "dialog.npc.banker.chatter_friendship4.10.line_0": "А, тебе что-то нужно?"
};

updateMarkdownFile('02_banker.md', finalBankerLines);
console.log('Final 25 banker lines updated!');
