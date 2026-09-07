import json
import os
import sys
import subprocess
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

WORKSPACE = Path(r"c:\Users\Foxi8\OneDrive\Рабочий стол\СозданиеПеревода")
GAME_PROFILE = Path(r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\kubejs")

RU_LANG_FILE = WORKSPACE / "translations" / "society" / "ru_ru.json"
EN_LANG_FILE = WORKSPACE / "translations" / "society" / "en_us.json"

GAME_RU_LANG = GAME_PROFILE / "assets" / "society" / "lang" / "ru_ru.json"
GAME_EN_LANG = GAME_PROFILE / "assets" / "society" / "lang" / "en_us.json"

SERVER_SCRIPTS_GLOBAL = WORKSPACE / "game_data" / "server_scripts" / "globalServer.js"
SERVER_SCRIPTS_DEBT = WORKSPACE / "game_data" / "server_scripts" / "handleDebt.js"
STARTUP_SCRIPTS_UTILS = WORKSPACE / "game_data" / "startup_scripts" / "globalTextTranslationUtils.js"

GAME_SCRIPTS_GLOBAL = GAME_PROFILE / "server_scripts" / "globalServer.js"
GAME_SCRIPTS_DEBT = GAME_PROFILE / "server_scripts" / "handleDebt.js"
GAME_STARTUP_UTILS = GAME_PROFILE / "startup_scripts" / "globalTextTranslationUtils.js"

NEW_KEYS_RU = {
    "society.hospital_receipt.title": "Больничная справка #%s",
    "society.hospital_receipt.first_death.title": "Больничная справка #%s",
    "society.hospital_receipt.quote.1": "«Первый раз у нас? Добро пожаловать в клинику Харви! Надеюсь, вы надолго не задержитесь.»",
    "society.hospital_receipt.quote.2_3": "«Лёгкое недомогание. Берегите себя в следующий раз!»",
    "society.hospital_receipt.quote.4_5": "«Обычные производственные травмы. Ничего страшного, у нас всё схвачено!»",
    "society.hospital_receipt.quote.6_7": "«Вам пора заводить карту постоянного клиента! Кофе в приёмной — за наш счёт.»",
    "society.hospital_receipt.quote.8_9": "«За вами уже закреплена персональная койка в приёмном покое. Хотите, подушку принесём?»",
    "society.hospital_receipt.quote.10_11": "«Доктор Харви уже начал писать статью о ваших похождениях. Вы — медицинский феномен!»",
    "society.hospital_receipt.quote.12_15": "«Мы уже перестали удивляться. Просто подписывайте здесь... и здесь... Спасибо, что выбираете нас.»",
    "society.hospital_receipt.quote.16_18": "«Почётный спонсор строительства нового хирургического крыла! Может, назовём вашим именем?»",
    "society.hospital_receipt.quote.19": "«Ваш портрет висит в холле среди основателей клиники. Мы гордимся вами! (И вашими деньгами.)»",
    "society.hospital_receipt.quote.20": "«Мы не знаем, как вы это делаете. Но если вы умрёте ещё раз — мы закрываем больницу и уходим в монастырь.»",
    "society.hospital_receipt.quote.21_plus": "«Стандартная процедура восстановления завершена. Берегите себя и будьте аккуратнее!»",
    "society.hospital_receipt.note.paid": "Клиника доктора Харви (Визит #%s)\n\n%s\n\nОплачено: %s §e●§r",
    "society.hospital_receipt.note.debt": "Клиника доктора Харви (Визит #%s)\n\n%s\n\nДолг за визит: %s §e●§r\n+Непогашенные долги: %s §e●§r",
    "society.hospital_receipt.note.free": "Клиника доктора Харви (Визит #%s)\n\n%s\n\nПервое лечение за наш счёт!\nБерегите себя впредь.",
    "society.skull_cavern.intro.note": "Пещера Черепа опасна: ищите верёвки под рудой и валунами.\nВ 5:50 утра пещера забирает всех, кто остался внутри!\n\nСпасательная верёвка вернёт вас наверх, но до выхода ещё предстоит добежать!",
    "society.hospital_receipt.hud.first_death": "§fКлиника доктора Харви:§r Визит #1 | Первое лечение бесплатно!",
    "society.hospital_receipt.hud.fee_taked": "§r Визит #%s | Списано %s §e●§r",
    "society.hospital_receipt.hud.debt": "§r Визит #%s | Долг: %s §e●§r (Весь долг: %s §e●§r)"
}

NEW_KEYS_EN = {
    "society.hospital_receipt.title": "Medical Certificate #%s",
    "society.hospital_receipt.first_death.title": "Medical Certificate #%s",
    "society.hospital_receipt.quote.1": "\"First time here? Welcome to Harvey's Clinic! Hope you won't stay long.\"",
    "society.hospital_receipt.quote.2_3": "\"Just a mild malaise. Take care next time!\"",
    "society.hospital_receipt.quote.4_5": "\"Typical workplace injuries. Nothing to worry about, we've got it covered!\"",
    "society.hospital_receipt.quote.6_7": "\"Time to get a regular client card! Coffee in the lobby is on the house.\"",
    "society.hospital_receipt.quote.8_9": "\"A personal bed is already reserved for you in the ER. Want a pillow?\"",
    "society.hospital_receipt.quote.10_11": "\"Dr. Harvey has already started writing a paper on your adventures. You're a medical marvel!\"",
    "society.hospital_receipt.quote.12_15": "\"We've stopped being surprised. Just sign here... and here... Thanks for choosing us.\"",
    "society.hospital_receipt.quote.16_18": "\"Honorary sponsor of the new surgical wing! Maybe we'll name it after you?\"",
    "society.hospital_receipt.quote.19": "\"Your portrait hangs in the lobby among clinic founders. We're proud of you! (And your coins.)\"",
    "society.hospital_receipt.quote.20": "\"We don't know how you do it. But if you die one more time, we're closing the hospital and joining a monastery.\"",
    "society.hospital_receipt.quote.21_plus": "\"Standard recovery procedure completed. Take care and stay safe!\"",
    "society.hospital_receipt.note.paid": "Dr. Harvey's Clinic (Visit #%s)\n\n%s\n\nPaid: %s §e●§r",
    "society.hospital_receipt.note.debt": "Dr. Harvey's Clinic (Visit #%s)\n\n%s\n\nVisit debt: %s §e●§r\nUnpaid debts: %s §e●§r",
    "society.hospital_receipt.note.free": "Dr. Harvey's Clinic (Visit #%s)\n\n%s\n\nFirst treatment is on the house!\nTake care next time.",
    "society.hospital_receipt.hud.first_death": "§fDr. Harvey's Clinic:§r Visit #1 | First treatment is on the house!",
    "society.hospital_receipt.hud.fee_taked": "§r Visit #%s | %s §e●§r deducted",
    "society.hospital_receipt.hud.debt": "§r Visit #%s | Debt: %s §e●§r (Total debt: %s §e●§r)"
}

def update_json_file(file_path: Path, new_entries: dict):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.pop("society.hospital_receipt.quote.20_plus", None)
    data.update(new_entries)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Updated {file_path} with {len(new_entries)} keys")

def update_startup_utils(file_path: Path):
    content = '''global.translatableWithFallback = (key, fallback) => {
    if(!fallback) return Text.translatable(key);
    else return Text.of(NBT.stringTag(`{"translate":"${key}", "fallback":"${fallback}"}`));
}

global.getTranslatedEntityName = (entity_id, fallback) => {
    return global.translatableWithFallback(`entity.${entity_id.namespace}.${entity_id.path}`, fallback)
}

global.getTranslatedItemName = (item_id, fallback) => {
    const prefix = Item.of(item_id).block ? "block" : "item";
    return global.translatableWithFallback(`${prefix}.${item_id.namespace}.${item_id.path}`, fallback)
}

global.getTranslatedTextWithColorCode = (colorCode, key) => {
    switch(colorCode) {
        case "0":
            return Text.translatable(key).black();
        case "1":
            return Text.translatable(key).darkBlue();
        case "2":
            return Text.translatable(key).darkGreen();
        case "3":
            return Text.translatable(key).darkAqua();
        case "4":
            return Text.translatable(key).darkRed();
        case "5":
            return Text.translatable(key).darkPurple();
        case "6":
            return Text.translatable(key).gold();
        case "7":
            return Text.translatable(key).gray();
        case "8":
            return Text.translatable(key).darkGray();
        case "9":
            return Text.translatable(key).blue();
        case "a":
            return Text.translatable(key).green();
        case "b":
            return Text.translatable(key).aqua();
        case "c":
            return Text.translatable(key).red();
        case "d":
            return Text.translatable(key).lightPurple();
        case "e":
            return Text.translatable(key).yellow();
        case "f":
            return Text.translatable(key).white();
        default:
            return Text.translatable(key);
    }
}

global.getNotePaperItem = (author, text, title) => {
    return Item.of("candlelight:note_paper_written", {
        author: String(author),
        text: [String(text)],
        title: String(title)
    });
}

global.getEmbersTextAPICommand = (target, design, duration, text) => {
    return `emberstextapi sendcustom ${target} ${design} ${duration} ${text}`
}
'''
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Updated globalTextTranslationUtils.js at {file_path}")

def get_handle_debt_js_content():
    return '''console.info("[SOCIETY] handleDebt.js loaded");

CommonAddedEvents.playerRespawn((e) => {
  const { player, server } = e;
  if (global.enableDeathDebt) {
    const UUID = player.getUuid().toString();
    if (!server.persistentData.hospitalVisits) server.persistentData.hospitalVisits = {};
    server.persistentData.hospitalVisits[UUID] = (server.persistentData.hospitalVisits[UUID] || 0) + 1;
    let visits = server.persistentData.hospitalVisits[UUID];

    if (!player.stages.has("first_death")) {
      player.stages.add("first_death");
      let quoteKey = global.getHospitalQuoteKey(visits);
      let noteText = Text.translatable("society.hospital_receipt.note.free", `${visits}`, Text.translatable(quoteKey)).toJson();
      let noteTitle = `Больничная справка #${visits}`;
      let noteAuthor = global.translatableWithFallback("society.hospital_receipt.author", "Doctor Harvey").getString();
      player.give(
        global.getNotePaperItem(noteAuthor, noteText, noteTitle)
      );
      server.runCommandSilent(
        global.getEmbersTextAPICommand(
          player.username,
          `{anchor:"TOP_LEFT",background:1,color:"#55FF55",size:1,offsetY:36,offsetX:6,typewriter:1,align:"TOP_LEFT"}`,
          220,
          Text.translatable("society.hospital_receipt.hud.first_death").toJson()
        )
      );
      player.tell(Text.translatable("society.hospital_receipt.hud.first_death").green());
      player.tell(Text.translatable(quoteKey).italic().gray());
    } else {
      global.handleFee(server, player, "death");
      if (!player.stages.has("first_aid_guide") && Math.random() <= 0.01)
        player.give("society:first_aid_guide");
    }
    player.potionEffects.add("minecraft:slowness", 1200, 0, false, true);
  }
});
'''

def update_handle_debt_js(file_path: Path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(get_handle_debt_js_content())
    print(f"[OK] Updated handleDebt.js at {file_path}")

def update_global_server_js(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    helper_fn = '''global.getHospitalQuoteKey = (visits) => {
  if (visits <= 1) return "society.hospital_receipt.quote.1";
  if (visits <= 3) return "society.hospital_receipt.quote.2_3";
  if (visits <= 5) return "society.hospital_receipt.quote.4_5";
  if (visits <= 7) return "society.hospital_receipt.quote.6_7";
  if (visits <= 9) return "society.hospital_receipt.quote.8_9";
  if (visits <= 11) return "society.hospital_receipt.quote.10_11";
  if (visits <= 15) return "society.hospital_receipt.quote.12_15";
  if (visits <= 18) return "society.hospital_receipt.quote.16_18";
  if (visits === 19) return "society.hospital_receipt.quote.19";
  if (visits === 20) return "society.hospital_receipt.quote.20";
  return "society.hospital_receipt.quote.21_plus";
};

'''
    if "global.getHospitalQuoteKey" not in code:
        code = helper_fn + code
    else:
        start_fn = code.find("global.getHospitalQuoteKey =")
        end_fn = code.find("};", start_fn) + 2
        code = code[:start_fn] + helper_fn.strip() + code[end_fn:]

    # Replace handleFee
    handle_fee_start = code.find("global.handleFee = (server, player, reason) => {")
    if handle_fee_start != -1:
        end_idx = code.find("global.teleportHome =", handle_fee_start)
        if end_idx != -1:
            new_handle_fee = '''global.handleFee = (server, player, reason) => {
  const UUID = player.getUuid().toString();
  let amountToDeduct = 0;
  let account = global.getPersonalOrCurioAccount(player.level, player);
  let balance = account.getBalance() || 0;
  let maxFee = 0;
  let minimumFee = 512;
  
  if (!server.persistentData.hospitalVisits) server.persistentData.hospitalVisits = {};
  let visits = server.persistentData.hospitalVisits[UUID] || 1;
  let quoteKey = global.getHospitalQuoteKey(visits);
  let noteTitle = `Больничная справка #${visits}`;
  let noteAuthor = global.translatableWithFallback("society.hospital_receipt.author", "Doctor Harvey").getString();
  
  if (reason === "death") {
    maxFee = 4096;
    if (player.stages.has("first_aid_guide")) maxFee = 2048;
    amountToDeduct = Math.min(Math.round(balance * 0.1), maxFee);
  }
  if (reason === "skull_cavern") {
    minimumFee = 1024;
    maxFee = 8192;

    amountToDeduct = Math.min(Math.round(balance * 0.15), maxFee);
  }
  if (amountToDeduct < minimumFee) amountToDeduct = minimumFee;
  if (balance < maxFee && player.stages.has("entered_skull_cavern")) amountToDeduct = maxFee;
  let formattedAmountToDeduct = global.formatPrice(amountToDeduct);

  if (balance < amountToDeduct) {
    let currentDebt = null;
    let foundIndex = -1;
    if (!server.persistentData.debts) server.persistentData.debts = [];
    for (let index = 0; index < server.persistentData.debts.length; index++) {
      if (String(UUID) === String(server.persistentData.debts[index].uuid)) {
        currentDebt = Number(server.persistentData.debts[index].amount);
        server.persistentData.debts[index].amount = currentDebt + amountToDeduct;
        foundIndex = index;
        break;
      }
    }
    if (!currentDebt) {
      server.persistentData.debts.push({ uuid: UUID.toString(), amount: amountToDeduct });
    }
    let previousDebt = currentDebt ? currentDebt : 0;
    let totalDebt = previousDebt + amountToDeduct;
    let formattedPreviousDebt = global.formatPrice(previousDebt);
    let formattedTotalDebt = global.formatPrice(totalDebt);

    let noteText = Text.translatable("society.hospital_receipt.note.debt", `${visits}`, Text.translatable(quoteKey), `${formattedAmountToDeduct}`, `${formattedPreviousDebt}`).toJson();
    player.give(
      global.getNotePaperItem(noteAuthor, noteText, noteTitle)
    );
    server.runCommandSilent(
      global.getEmbersTextAPICommand(
        player.username,
        `{anchor:"TOP_LEFT",background:1,color:"#FF5555",size:1,offsetY:36,offsetX:6,typewriter:1,align:"TOP_LEFT"}`,
        240,
        Text.translatable("society.hospital_receipt.hud.debt", `${visits}`, `${formattedAmountToDeduct}`, `${formattedTotalDebt}`).toJson()
      )
    );
    player.tell(Text.translatable("society.hospital_receipt.hud.debt", `${visits}`, `${formattedAmountToDeduct}`, `${formattedTotalDebt}`).red());
    player.tell(Text.translatable(quoteKey).italic().gray());
  } else {
    account.setBalance(balance - amountToDeduct);
    let noteText = Text.translatable("society.hospital_receipt.note.paid", `${visits}`, Text.translatable(quoteKey), `${formattedAmountToDeduct}`).toJson();
    player.give(
      global.getNotePaperItem(noteAuthor, noteText, noteTitle)
    );
    server.runCommandSilent(
      global.getEmbersTextAPICommand(
        player.username,
        `{anchor:"TOP_LEFT",background:1,color:"#FFAA00",size:1,offsetY:36,offsetX:6,typewriter:1,align:"TOP_LEFT"}`,
        200,
        Text.translatable("society.hospital_receipt.hud.fee_taked", `${visits}`, `${formattedAmountToDeduct}`).toJson()
      )
    );
    player.tell(Text.translatable("society.hospital_receipt.hud.fee_taked", `${visits}`, `${formattedAmountToDeduct}`).gold());
    player.tell(Text.translatable(quoteKey).italic().gray());
  }
};
'''
            code = code[:handle_fee_start] + new_handle_fee + code[end_idx:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"[OK] Successfully updated global.handleFee in {file_path}")

def main():
    print("=== 1. Updating Workspace Translations ===")
    update_json_file(RU_LANG_FILE, NEW_KEYS_RU)
    update_json_file(EN_LANG_FILE, NEW_KEYS_EN)

    print("\n=== 2. Updating Workspace KubeJS Server & Startup Scripts ===")
    update_handle_debt_js(SERVER_SCRIPTS_DEBT)
    update_global_server_js(SERVER_SCRIPTS_GLOBAL)
    update_startup_utils(STARTUP_SCRIPTS_UTILS)

    print("\n=== 3. Updating Game Profile KubeJS Scripts ===")
    update_handle_debt_js(GAME_SCRIPTS_DEBT)
    update_global_server_js(GAME_SCRIPTS_GLOBAL)
    update_startup_utils(GAME_STARTUP_UTILS)

    print("\n=== 4. Running sync_all_to_game.js ===")
    res = subprocess.run(["node", str(WORKSPACE / "sync_all_to_game.js")], cwd=str(WORKSPACE), capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)

    print("\n=== 5. MANDATORY VERIFICATION ASSERTION (Reading directly from Game Profile) ===")
    with open(GAME_RU_LANG, "r", encoding="utf-8") as f:
        game_ru_data = json.load(f)

    for k in NEW_KEYS_RU:
        val = game_ru_data.get(k)
        assert val == NEW_KEYS_RU[k], f"Verification failed for key: {k}! Expected {NEW_KEYS_RU[k]}, got {val}"
        print(f"  [VERIFIED GAME LANG] {k} -> {val}")

    with open(GAME_SCRIPTS_GLOBAL, "r", encoding="utf-8") as f:
        game_script_content = f.read()
    assert "quote.21_plus" in game_script_content, "Verification failed for quote.21_plus in globalServer.js!"
    print("  [VERIFIED GAME SCRIPT] globalServer.js contains 21+ infinite quote logic")

    with open(GAME_SCRIPTS_DEBT, "r", encoding="utf-8") as f:
        game_debt_content = f.read()
    assert "hospitalVisits" in game_debt_content, "Verification failed for hospitalVisits counter in handleDebt.js!"
    print("  [VERIFIED GAME SCRIPT] handleDebt.js contains visits counter")

    with open(GAME_STARTUP_UTILS, "r", encoding="utf-8") as f:
        game_utils_content = f.read()
    assert 'author: String(author)' in game_utils_content, "Verification failed for getNotePaperItem in startup utils!"
    print("  [VERIFIED STARTUP SCRIPT] globalTextTranslationUtils.js contains safe NBT object builder")

    print("\n>>> ALL VERIFICATION CHECKS PASSED DIRECTLY FROM GAME DIRECTORY! <<<")

if __name__ == "__main__":
    main()
