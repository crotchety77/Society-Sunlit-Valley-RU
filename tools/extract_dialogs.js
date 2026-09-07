const fs = require('fs');
const path = require('path');

let translationKeys = {};
global.datagenDialog = true;

const generateDialogEntries = (npcId, dialogType, dialogIndex, dialogLines, portraitPath, isChatter, customOptions) => {
  let entries = [];
  let resolvedDialogLines = Array.isArray(dialogLines) ? dialogLines : [dialogLines];
  resolvedDialogLines.forEach((entry, index) => {
    let lineTranslationKey = `dialog.npc.${npcId}.${dialogType}${dialogIndex == -1 ? "" : `.${dialogIndex}`}.line_${index}`;
    translationKeys[lineTranslationKey] = entry;
    let queuedEntry = {
      id: index == 0 ? "start" : index == resolvedDialogLines.length - 1 ? "end" : index,
    };
    if (customOptions && resolvedDialogLines.length - 1 == index) {
      queuedEntry.options = customOptions.map((option, optIndex) => {
        let optionKey = `dialog.npc.${npcId}.${dialogType}.option_${optIndex}`;
        translationKeys[optionKey] = option.text;
        return {
          text: {
            translate: optionKey
          },
          target: option.target || "end",
          command: Array.isArray(option.command) ? option.command : [option.command]
        };
      });
    }

    if (isChatter && resolvedDialogLines.length - 1 == index && !customOptions) {
      if (npcId == "carpenter") {
        translationKeys["dialog.npc.carpenter.purchase_supplies"] = "Purchase supplies";
        translationKeys["dialog.npc.carpenter.invite_villagers"] = "Invite Villagers";
        translationKeys["dialog.npc.carpenter.build_farm"] = "Build Farm buildings";
        translationKeys["dialog.npc.carpenter.build_village"] = "Build Village buildings";
      }
    }
  });
};

global.runNpcDatagen = (npcId, npcDef) => {
  let nameTranslationKey = `dialog.npc.${npcId}.name`;
  let resolvedPortraitPath = npcDef.noPortrait ? null : (npcDef.portraitPath ? npcDef.portraitPath : npcId);
  translationKeys[nameTranslationKey] = npcDef.name || npcId;
  translationKeys[`dialog.npc.${npcId}.chatter.description`] = `Chatting with ${npcDef.name || npcId}`;

  // Chatter
  if (npcDef.chatter) {
    for (let index = 0; index <= 5; index++) {
      let friendshipKey = `friendship${index}`;
      let chatterSet = npcDef.chatter[friendshipKey];
      if (chatterSet && chatterSet.length > 0) {
        chatterSet.forEach((chatter, chatterIndex) => {
          generateDialogEntries(
            npcId,
            `chatter_${friendshipKey}`,
            chatterIndex,
            chatter,
            resolvedPortraitPath,
            true
          );
        });
      }
    }
  }
  // Introduction
  if (npcDef.intro) {
    translationKeys[`dialog.npc.${npcId}.intro.description`] = `${npcDef.name}'s Introduction`;
    generateDialogEntries(npcId, `intro`, 0, npcDef.intro, npcId);
  }
  // Gifts
  if (npcDef.giftResponse) {
    let giftResponseKeys = ["loved", "liked", "neutral", "disliked", "hated"];
    giftResponseKeys.forEach((responseType) => {
      if (npcDef.giftResponse[responseType]) {
        npcDef.giftResponse[responseType].forEach((response, responseIndex) => {
          generateDialogEntries(
            npcId,
            `gift_${responseType}`,
            responseIndex,
            response,
            responseType === "neutral" ? npcId : `${responseType}/${npcId}`
          );
        });
      }
    });
  }
  if (npcDef.unique) {
    npcDef.unique.forEach((dialog) => {
      generateDialogEntries(
        npcId,
        `unique_${dialog.name}`,
        -1,
        dialog.text,
        resolvedPortraitPath,
        false
      );
    });
  }
  if (npcDef.choiceDialogs) {
    npcDef.choiceDialogs.forEach((dialog) => {
      generateDialogEntries(
        npcId,
        `dialog.${dialog.name}`,
        -1,
        dialog.text,
        resolvedPortraitPath,
        false,
        dialog.options
      );
    });
  }
};

const npcsDir = path.join(__dirname, 'server_scripts', 'datagen', 'npcs');
const files = fs.readdirSync(npcsDir);
files.forEach(file => {
  if (file.endsWith('.js')) {
    const code = fs.readFileSync(path.join(npcsDir, file), 'utf8');
    eval(code);
  }
});

const outputPath = path.join(__dirname, 'dialog_en_us.json');
fs.writeFileSync(outputPath, JSON.stringify(translationKeys, null, 2), 'utf8');
console.log(`Extracted ${Object.keys(translationKeys).length} dialog keys to ${outputPath}`);
