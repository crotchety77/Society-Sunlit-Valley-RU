const fs = require('fs');
const path = require('path');

const npcsMeta = {
  carpenter: {
    name: "Эйс (Ace the Carpenter)",
    role: "Плотник и строитель фермы / городка",
    personality: "Добродушный, активный, любит природу, собирательство ягод и трав в диких лесах, честный труженик. Дружит с кузнецом Эйденом и Кэролайн. Обращается к игроку на «ты» (@i).",
    order: "01"
  },
  banker: {
    name: "Леон (Leon the Banker)",
    role: "Банкир и финансист Солнечной Долины",
    personality: "Строгий, практичный, пунктуальный деловой человек. Внимателен к цифрам, процентам и расходам. Постепенно раскрывается как заботящийся о процветании долины наставник.",
    order: "02"
  },
  market: {
    name: "Кэролайн (Caroline the Merchant)",
    role: "Основательница рынка и продавец семян",
    personality: "Энергичная, общительная, душа ярмарки. Знает все фермерские тонкости, сезонные культуры и рецепты. Заботится обо всех жителях долины.",
    order: "03"
  },
  blacksmith: {
    name: "Эйден (Aiden the Blacksmith)",
    role: "Кузнец и мастер по обработке руд",
    personality: "Крепкий, прямолинейный мастер. Любит звон наковальни, качественные инструменты, редкие минералы, жеоды, а также питает тайную слабость к полевым цветам.",
    order: "04"
  },
  shepherd: {
    name: "Мария (Maria the Shepherd)",
    role: "Пастух и животновод",
    personality: "Мягкая, заботливая, обожает всех домашних и диких животных (овец, коров, белок, пингвинов). Знает всё об уходе за скотом и качественной шерсти/сыре.",
    order: "05"
  },
  fisher: {
    name: "Харуна (Haruna the Fisher)",
    role: "Рыбачка Солнечной Долины",
    personality: "Спокойная, загадочная, любит шум волн и океан. Знает повадки редких сезонных рыб, тайны Нептуна и древние легенды водоёмов.",
    order: "06"
  },
  witch: {
    name: "Ведьма (Witch)",
    role: "Обитательница Незера и мастер мистических ритуалов",
    personality: "Эксцентричная, острая на язык, независимая ведьма. Понимает язык духов и животных, создает магические механизмы вроде Авто-ласки (Auto-Petter).",
    order: "07"
  },
  librarian: {
    name: "Библиотекарь (Librarian)",
    role: "Хранитель знаний, книг и свитков",
    personality: "Эрудированный, вдумчивый интеллектуал. Изучает историю долины, подземелий и древних артефактов.",
    order: "08"
  },
  trader: {
    name: "Экзотический торговец (Exotic Trader)",
    role: "Торговец из Пещеры Черепа",
    personality: "Авантюрист и искатель редких сокровищ в глубинах пещер. Готов обменивать подземные реликвии на ценные предметы.",
    order: "09"
  },
  wise_oak: {
    name: "Мудрый Дуб (Wise Oak)",
    role: "Древний древесный дух в дикой природе",
    personality: "Величественный, древний хранитель лесов. Говорит размеренно, глубоко и метафорично о балансе природы.",
    order: "10"
  },
  goddess: {
    name: "Статуя Богини (Ancient Goddess)",
    role: "Храм и статуя благословения",
    personality: "Божественный голос, принимающий подношения и дарующий благословения земли и плодородия.",
    order: "11"
  },
  misc: {
    name: "Разное: Гном и Чертежи (Gnome & Blueprints)",
    role: "Интерфейсные диалоги и пасхалки",
    personality: "Меню выбора построек Эйса и загадочные послания Гнома.",
    order: "12"
  }
};

const outputDir = path.join(__dirname, '../translations/dialogs');
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

let npcsData = {};
global.datagenDialog = true;

global.runNpcDatagen = (npcId, npcDef) => {
  npcsData[npcId] = npcDef;
};

const npcsDir = path.join(__dirname, '../game_data/server_scripts', 'datagen', 'npcs');
const files = fs.readdirSync(npcsDir);
files.forEach(file => {
  if (file.endsWith('.js')) {
    const code = fs.readFileSync(path.join(npcsDir, file), 'utf8');
    eval(code);
  }
});

// Generate Markdown review files for each NPC
for (const [npcId, meta] of Object.entries(npcsMeta)) {
  const npcDef = npcsData[npcId] || (npcId === 'misc' ? { isMisc: true } : null);
  if (!npcDef && npcId !== 'misc') continue;

  let md = [];
  md.push(`# 📜 Диалоги NPC: ${meta.name}`);
  md.push(`\n**Роль:** ${meta.role}`);
  md.push(`**Характер и контекст:** ${meta.personality}`);
  md.push(`\n> [!NOTE]\n> - **Токен \`@i\`**: Обязательно сохраняйте \`@i\` на месте обращения к игроку по имени.\n> - **Символ \`%%\`**: Все проценты должны экранироваться как \`%%\`.\n> - **Колонка «Перевод (RU)»**: Заполняется русским текстом. Можно вносить любые правки формулировок и характера.\n`);

  if (npcId === 'misc') {
    // Handle gnome and blueprints
    ['gnome', 'blueprints'].forEach(id => {
      const def = npcsData[id];
      if (!def) return;
      md.push(`\n## 🔹 ${def.name || id} (\`${id}\`)\n`);
      md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
      md.push(`|---|---|---|---|`);
      md.push(`| \`dialog.npc.${id}.name\` | ${def.name || id} | | Имя |`);
      md.push(`| \`dialog.npc.${id}.chatter.description\` | Chatting with ${def.name || id} | | Описание |`);
      if (def.unique) {
        md.push(`### Уникальные реплики (Unique lines)`);
        md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
        md.push(`|---|---|---|---|`);
        def.unique.forEach(u => {
          let lines = Array.isArray(u.text) ? u.text : [u.text];
          lines.forEach((l, idx) => {
            let key = `dialog.npc.${id}.unique_${u.name}.line_${idx}`;
            md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | |`);
          });
        });
      }
      if (def.choiceDialogs) {
        md.push(`\n### Меню выбора (Choice Dialogs)`);
        md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
        md.push(`|---|---|---|---|`);
        def.choiceDialogs.forEach(c => {
          let lines = Array.isArray(c.text) ? c.text : [c.text];
          lines.forEach((l, idx) => {
            let key = `dialog.npc.${id}.dialog.${c.name}.line_${idx}`;
            md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | |`);
          });
          if (c.options) {
            c.options.forEach((opt, optIdx) => {
              let optKey = `dialog.npc.${id}.dialog.${c.name}.option_${optIdx}`;
              md.push(`| \`${optKey}\` | ${opt.text.replace(/\|/g, '\\|')} | | Кнопка выбора |`);
            });
          }
        });
      }
    });
  } else {
    // 1. Имя и базовые описания
    md.push(`## 🏷️ Системные строки и имя`);
    md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Примечание |`);
    md.push(`|---|---|---|---|`);
    md.push(`| \`dialog.npc.${npcId}.name\` | ${npcDef.name || npcId} | | Имя персонажа |`);
    md.push(`| \`dialog.npc.${npcId}.chatter.description\` | Chatting with ${npcDef.name || npcId} | | Статус диалогового окна |`);

    if (npcId === 'carpenter') {
      md.push(`| \`dialog.npc.carpenter.purchase_supplies\` | Purchase supplies | Купить материалы | Кнопка магазина |`);
      md.push(`| \`dialog.npc.carpenter.invite_villagers\` | Invite Villagers | Пригласить жителей | Кнопка магазина |`);
      md.push(`| \`dialog.npc.carpenter.build_farm\` | Build Farm buildings | Построить ферму | Кнопка магазина |`);
      md.push(`| \`dialog.npc.carpenter.build_village\` | Build Village buildings | Построить город | Кнопка магазина |`);
    }

    if (npcDef.intro) {
      md.push(`\n## 🤝 Знакомство (Первая встреча / Intro)`);
      md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
      md.push(`|---|---|---|---|`);
      md.push(`| \`dialog.npc.${npcId}.intro.description\` | ${npcDef.name}'s Introduction | | Описание окна знакомства |`);
      let introLines = Array.isArray(npcDef.intro) ? npcDef.intro : [npcDef.intro];
      introLines.forEach((l, idx) => {
        let key = `dialog.npc.${npcId}.intro.0.line_${idx}`;
        md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | Реплика ${idx + 1} |`);
      });
    }

    // 3. Повседневные реплики по уровням дружбы (Chatter 0..5)
    if (npcDef.chatter) {
      md.push(`\n## 💬 Повседневный диалог (Chatter по уровням дружбы)`);
      for (let lvl = 0; lvl <= 5; lvl++) {
        let fKey = `friendship${lvl}`;
        let chatterSet = npcDef.chatter[fKey];
        if (chatterSet && chatterSet.length > 0) {
          md.push(`\n### 💖 Уровень дружбы ${lvl} (${fKey}) — ${chatterSet.length} диалогов`);
          md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
          md.push(`|---|---|---|---|`);
          chatterSet.forEach((chat, cIdx) => {
            let lines = Array.isArray(chat) ? chat : [chat];
            lines.forEach((l, lIdx) => {
              let key = `dialog.npc.${npcId}.chatter_${fKey}.${cIdx}.line_${lIdx}`;
              md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | Диалог ${cIdx + 1}, строка ${lIdx + 1} |`);
            });
          });
        }
      }
    }

    // 4. Реакция на подарки (Gift Responses)
    if (npcDef.giftResponse) {
      md.push(`\n## 🎁 Реакция на подарки (Gift Responses)`);
      const giftTypes = [
        { key: "loved", label: "❤️ Любимый подарок (Loved)" },
        { key: "liked", label: "👍 Понравившийся подарок (Liked)" },
        { key: "neutral", label: "😐 Нейтральный подарок (Neutral)" },
        { key: "disliked", label: "👎 Не понравившийся подарок (Disliked)" },
        { key: "hated", label: "😡 Ненавистный подарок (Hated)" }
      ];
      giftTypes.forEach(gt => {
        let respList = npcDef.giftResponse[gt.key];
        if (respList && respList.length > 0) {
          md.push(`\n### ${gt.label}`);
          md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
          md.push(`|---|---|---|---|`);
          respList.forEach((r, rIdx) => {
            let lines = Array.isArray(r) ? r : [r];
            lines.forEach((l, lIdx) => {
              let key = `dialog.npc.${npcId}.gift_${gt.key}.${rIdx}.line_${lIdx}`;
              md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | Вариант ${rIdx + 1} |`);
            });
          });
        }
      });
    }

    // 5. Уникальные диалоги
    if (npcDef.unique && npcDef.unique.length > 0) {
      md.push(`\n## 🌟 Уникальные диалоги (Unique)`);
      md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
      md.push(`|---|---|---|---|`);
      npcDef.unique.forEach(u => {
        let lines = Array.isArray(u.text) ? u.text : [u.text];
        lines.forEach((l, idx) => {
          let key = `dialog.npc.${npcId}.unique_${u.name}.line_${idx}`;
          md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | ${u.name} |`);
        });
      });
    }

    // 6. Диалоги с выбором (Choice)
    if (npcDef.choiceDialogs && npcDef.choiceDialogs.length > 0) {
      md.push(`\n## 🔀 Диалоги с выбором (Choice Dialogs)`);
      md.push(`| ID ключа | Оригинал (EN) | Перевод (RU) | Заметки редактора |`);
      md.push(`|---|---|---|---|`);
      npcDef.choiceDialogs.forEach(c => {
        let lines = Array.isArray(c.text) ? c.text : [c.text];
        lines.forEach((l, idx) => {
          let key = `dialog.npc.${npcId}.dialog.${c.name}.line_${idx}`;
          md.push(`| \`${key}\` | ${l.replace(/\|/g, '\\|')} | | ${c.name} |`);
        });
        if (c.options) {
          c.options.forEach((opt, optIdx) => {
            let optKey = `dialog.npc.${npcId}.dialog.${c.name}.option_${optIdx}`;
            md.push(`| \`${optKey}\` | ${opt.text.replace(/\|/g, '\\|')} | | Кнопка выбора: ${c.name} |`);
          });
        }
      });
    }
  }

  const fileName = `${meta.order}_${npcId}.md`;
  const filePath = path.join(outputDir, fileName);
  fs.writeFileSync(filePath, md.join('\n'), 'utf8');
  console.log(`Generated ${fileName}`);
}
